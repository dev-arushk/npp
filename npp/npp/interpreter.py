"""
N++ Tree-Walk Interpreter / Evaluator
Executes the parsed AST with scoping, automatic type coercions, and clear runtime errors.
"""

from typing import Any, List, Optional
from .ast_nodes import (
    ASTNode, Program, Block, Literal, Identifier, BinaryOp, UnaryOp,
    AskExpr, ListLiteral, MapLiteral, IndexExpr, CallExpr,
    MemberAccess, MethodCall,
    ExpressionStmt, SayStmt, VarDecl, AssignStmt,
    IfStmt, WhileStmt, RepeatStmt, ForEachStmt, FunctionDef,
    ReturnStmt, BreakStmt, ContinueStmt
)
from .environment import Environment
from .builtins import (
    get_default_builtins, NppCallable, NppFunction, npp_format_value
)
from .errors import (
    NppRuntimeError, NppReturnSignal, NppBreakSignal, NppContinueSignal
)


class Interpreter:
    def __init__(self, filename: str = "<input>", source: str = ""):
        self.filename = filename
        self.source = source
        self.globals = Environment()
        self.current_env = self.globals

        # Populate built-in standard library
        for name, fn in get_default_builtins().items():
            self.globals.define(name, fn, is_const=True)

    def interpret(self, program: Program) -> Any:
        last_val = None
        for stmt in program.statements:
            last_val = self.execute(stmt)
        return last_val

    def execute(self, node: ASTNode) -> Any:
        method_name = f"execute_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_execute)
        return method(node)

    def generic_execute(self, node: ASTNode):
        raise NppRuntimeError(f"No execution handler for AST node: {type(node).__name__}", node.line, node.column, self.filename)

    # -------------------------------------------------------------------------
    # Statement Handlers
    # -------------------------------------------------------------------------
    def execute_SayStmt(self, stmt: SayStmt):
        val = self.evaluate(stmt.expression)
        print(npp_format_value(val))
        return None

    def execute_VarDecl(self, stmt: VarDecl):
        val = self.evaluate(stmt.initializer) if stmt.initializer is not None else None
        self.current_env.define(stmt.name, val, is_const=stmt.is_const)
        return val

    def execute_AssignStmt(self, stmt: AssignStmt):
        val = self.evaluate(stmt.value)

        if isinstance(stmt.target, Identifier):
            var_name = stmt.target.name
            if stmt.operator == "=":
                new_val = val
            else:
                curr_val = self.current_env.get(var_name, stmt.line, stmt.column, self.filename)
                new_val = self._apply_binary_op(stmt.operator[:-1], curr_val, val, stmt.line, stmt.column)

            self.current_env.assign(var_name, new_val, stmt.line, stmt.column, self.filename)
            return new_val

        elif isinstance(stmt.target, IndexExpr):
            coll = self.evaluate(stmt.target.target)
            idx = self.evaluate(stmt.target.index)
            if isinstance(coll, list):
                if not isinstance(idx, int):
                    raise NppRuntimeError(f"List index must be an integer, got {type(idx).__name__}", stmt.line, stmt.column, self.filename)
                if idx < 0 or idx >= len(coll):
                    raise NppRuntimeError(f"List index out of range: {idx} (size {len(coll)})", stmt.line, stmt.column, self.filename)
                coll[idx] = val
                return val
            elif isinstance(coll, dict):
                coll[idx] = val
                return val
            else:
                raise NppRuntimeError(f"Cannot assign by index to {type(coll).__name__}", stmt.line, stmt.column, self.filename)

        raise NppRuntimeError(f"Invalid assignment target", stmt.line, stmt.column, self.filename)

    def execute_IfStmt(self, stmt: IfStmt):
        cond_val = self.evaluate(stmt.condition)
        if self._is_truthy(cond_val):
            return self.execute_block(stmt.then_branch)

        # Check elif branches
        for elif_cond, elif_body in stmt.elif_branches:
            if self._is_truthy(self.evaluate(elif_cond)):
                return self.execute_block(elif_body)

        # Fallback to else
        if stmt.else_branch:
            return self.execute_block(stmt.else_branch)

        return None

    def execute_WhileStmt(self, stmt: WhileStmt):
        result = None
        while self._is_truthy(self.evaluate(stmt.condition)):
            try:
                result = self.execute_block(stmt.body)
            except NppBreakSignal:
                break
            except NppContinueSignal:
                continue
        return result

    def execute_RepeatStmt(self, stmt: RepeatStmt):
        count_val = self.evaluate(stmt.count)
        if not isinstance(count_val, (int, float)):
            raise NppRuntimeError(f"Repeat count must be a number, got {type(count_val).__name__}", stmt.line, stmt.column, self.filename)

        n = int(count_val)
        result = None
        for _ in range(n):
            try:
                result = self.execute_block(stmt.body)
            except NppBreakSignal:
                break
            except NppContinueSignal:
                continue
        return result

    def execute_ForEachStmt(self, stmt: ForEachStmt):
        coll_val = self.evaluate(stmt.collection)
        items = []

        if isinstance(coll_val, list):
            items = coll_val
        elif isinstance(coll_val, dict):
            items = list(coll_val.keys())
        elif isinstance(coll_val, str):
            items = list(coll_val)
        else:
            raise NppRuntimeError(f"Cannot iterate over {type(coll_val).__name__} in for-each loop", stmt.line, stmt.column, self.filename)

        result = None
        for item in items:
            loop_env = Environment(parent=self.current_env)
            loop_env.define(stmt.variable, item)
            prev_env = self.current_env
            self.current_env = loop_env
            try:
                result = self.execute_block(stmt.body, env=loop_env)
            except NppBreakSignal:
                self.current_env = prev_env
                break
            except NppContinueSignal:
                self.current_env = prev_env
                continue
            finally:
                self.current_env = prev_env
        return result

    def execute_FunctionDef(self, stmt: FunctionDef):
        fn = NppFunction(
            name=stmt.name,
            parameters=stmt.parameters,
            body=stmt.body,
            closure_env=self.current_env
        )
        self.current_env.define(stmt.name, fn)
        return fn

    def execute_ReturnStmt(self, stmt: ReturnStmt):
        val = self.evaluate(stmt.value) if stmt.value else None
        raise NppReturnSignal(val)

    def execute_BreakStmt(self, stmt: BreakStmt):
        raise NppBreakSignal()

    def execute_ContinueStmt(self, stmt: ContinueStmt):
        raise NppContinueSignal()

    def execute_ExpressionStmt(self, stmt: ExpressionStmt):
        return self.evaluate(stmt.expression)

    def execute_block(self, block: Block, env: Optional[Environment] = None) -> Any:
        if env is None:
            block_env = Environment(parent=self.current_env)
        else:
            block_env = env

        prev_env = self.current_env
        self.current_env = block_env
        result = None
        try:
            for stmt in block.statements:
                result = self.execute(stmt)
        finally:
            self.current_env = prev_env
        return result

    # -------------------------------------------------------------------------
    # Expression Evaluators
    # -------------------------------------------------------------------------
    def evaluate(self, node: ASTNode) -> Any:
        method_name = f"evaluate_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_evaluate)
        return method(node)

    def generic_evaluate(self, node: ASTNode):
        raise NppRuntimeError(f"No evaluator for AST node: {type(node).__name__}", node.line, node.column, self.filename)

    def evaluate_Literal(self, node: Literal) -> Any:
        return node.value

    def evaluate_Identifier(self, node: Identifier) -> Any:
        return self.current_env.get(node.name, node.line, node.column, self.filename)

    def evaluate_UnaryOp(self, node: UnaryOp) -> Any:
        val = self.evaluate(node.operand)
        if node.operator in ("not", "!"):
            return not self._is_truthy(val)
        elif node.operator == "-":
            if isinstance(val, (int, float)):
                return -val
            raise NppRuntimeError(f"Cannot negate non-numeric value: {type(val).__name__}", node.line, node.column, self.filename)
        raise NppRuntimeError(f"Unknown unary operator: {node.operator}", node.line, node.column, self.filename)

    def evaluate_BinaryOp(self, node: BinaryOp) -> Any:
        # Short-circuit logical operators
        if node.operator == "and":
            left_val = self.evaluate(node.left)
            if not self._is_truthy(left_val):
                return False
            return self._is_truthy(self.evaluate(node.right))

        if node.operator == "or":
            left_val = self.evaluate(node.left)
            if self._is_truthy(left_val):
                return True
            return self._is_truthy(self.evaluate(node.right))

        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        return self._apply_binary_op(node.operator, left, right, node.line, node.column)

    def _apply_binary_op(self, op: str, left: Any, right: Any, line: int, col: int) -> Any:
        if op == "+":
            # If either side is string, seamlessly convert the other to string (natural & easy!)
            if isinstance(left, str) or isinstance(right, str):
                return npp_format_value(left) + npp_format_value(right)
            # List concatenation
            if isinstance(left, list) and isinstance(right, list):
                return left + right
            # Numeric addition
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            raise NppRuntimeError(f"Cannot add {type(left).__name__} and {type(right).__name__}", line, col, self.filename)

        if op == "-":
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left - right
            raise NppRuntimeError(f"Cannot subtract {type(right).__name__} from {type(left).__name__}", line, col, self.filename)

        if op == "*":
            if isinstance(left, str) and isinstance(right, int):
                return left * right
            if isinstance(left, list) and isinstance(right, int):
                return left * right
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left * right
            raise NppRuntimeError(f"Cannot multiply {type(left).__name__} by {type(right).__name__}", line, col, self.filename)

        if op == "/":
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise NppRuntimeError("Division by zero", line, col, self.filename)
                res = left / right
                return int(res) if res.is_integer() else res
            raise NppRuntimeError(f"Cannot divide {type(left).__name__} by {type(right).__name__}", line, col, self.filename)

        if op == "%":
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise NppRuntimeError("Modulo by zero", line, col, self.filename)
                return left % right
            raise NppRuntimeError(f"Cannot perform modulo on {type(left).__name__} and {type(right).__name__}", line, col, self.filename)

        if op == "^":
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left ** right
            raise NppRuntimeError(f"Cannot raise {type(left).__name__} to power of {type(right).__name__}", line, col, self.filename)

        # Equality & Comparisons
        if op in ("==", "is"):
            return left == right
        if op in ("!=", "is not"):
            return left != right
        if op in (">", "greater than"):
            return left > right
        if op in ("<", "less than"):
            return left < right
        if op in (">=", "greater than or equal to", "at least"):
            return left >= right
        if op in ("<=", "less than or equal to", "at most"):
            return left <= right

        raise NppRuntimeError(f"Unknown binary operator: {op}", line, col, self.filename)

    def evaluate_AskExpr(self, node: AskExpr) -> str:
        prompt_str = ""
        if node.prompt:
            prompt_str = npp_format_value(self.evaluate(node.prompt))
        return input(prompt_str)

    def evaluate_ListLiteral(self, node: ListLiteral) -> List[Any]:
        return [self.evaluate(elem) for elem in node.elements]

    def evaluate_MapLiteral(self, node: MapLiteral) -> dict:
        result = {}
        for k_node, v_node in node.entries:
            key = self.evaluate(k_node)
            val = self.evaluate(v_node)
            result[key] = val
        return result

    def evaluate_IndexExpr(self, node: IndexExpr) -> Any:
        target = self.evaluate(node.target)
        idx = self.evaluate(node.index)

        if isinstance(target, (list, str)):
            if not isinstance(idx, int):
                raise NppRuntimeError(f"Index must be an integer, got {type(idx).__name__}", node.line, node.column, self.filename)
            if idx < 0 or idx >= len(target):
                raise NppRuntimeError(f"Index {idx} out of range for length {len(target)}", node.line, node.column, self.filename)
            return target[idx]

        if isinstance(target, dict):
            if idx not in target:
                raise NppRuntimeError(f"Key {idx!r} not found in map", node.line, node.column, self.filename)
            return target[idx]

        raise NppRuntimeError(f"Cannot index into {type(target).__name__}", node.line, node.column, self.filename)

    def evaluate_CallExpr(self, node: CallExpr) -> Any:
        callee = self.evaluate(node.callee)
        args = [self.evaluate(arg) for arg in node.args]

        if not isinstance(callee, NppCallable):
            name = getattr(node.callee, "name", type(callee).__name__)
            raise NppRuntimeError(f"'{name}' is not a callable function", node.line, node.column, self.filename)

        return callee.call(self, args, node.line, node.column)

    def evaluate_MemberAccess(self, node: MemberAccess) -> Any:
        target = self.evaluate(node.target)
        if isinstance(target, dict):
            if node.member in target:
                return target[node.member]
            raise NppRuntimeError(f"Property '{node.member}' not found in map", node.line, node.column, self.filename)
        if hasattr(target, node.member):
            return getattr(target, node.member)
        raise NppRuntimeError(f"Member '{node.member}' not found on {type(target).__name__}", node.line, node.column, self.filename)

    def evaluate_MethodCall(self, node: MethodCall) -> Any:
        target = self.evaluate(node.target)
        args = [self.evaluate(a) for a in node.args]

        if hasattr(target, node.method):
            attr = getattr(target, node.method)
            if callable(attr):
                try:
                    return attr(*args)
                except Exception as e:
                    raise NppRuntimeError(f"Error calling '{node.method}': {e}", node.line, node.column, self.filename)
            return attr

        if isinstance(target, dict) and node.method in target and callable(target[node.method]):
            return target[node.method](*args)

        raise NppRuntimeError(f"Method '{node.method}' not found on {type(target).__name__}", node.line, node.column, self.filename)

    def _is_truthy(self, val: Any) -> bool:
        if val is None or val is False:
            return False
        if val == 0 or val == "" or val == [] or val == {}:
            return False
        return True
