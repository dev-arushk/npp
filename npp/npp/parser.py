"""
N++ Parser
Constructs an Abstract Syntax Tree (AST) from a stream of tokens.
Supports both English sentence structures and traditional programming syntax.
"""

from typing import List, Tuple, Optional
from .tokens import Token, TokenType
from .ast_nodes import (
    ASTNode, Program, Block, Literal, Identifier, BinaryOp, UnaryOp,
    AskExpr, ListLiteral, MapLiteral, IndexExpr, CallExpr,
    MemberAccess, MethodCall,
    ExpressionStmt, SayStmt, VarDecl, AssignStmt,
    IfStmt, WhileStmt, RepeatStmt, ForEachStmt, FunctionDef,
    ReturnStmt, BreakStmt, ContinueStmt
)
from .errors import NppSyntaxError


class Parser:
    def __init__(self, tokens: List[Token], source: str = "", filename: str = "<input>"):
        self.tokens = tokens
        self.source = source
        self.filename = filename
        self.pos = 0

    # -------------------------------------------------------------------------
    # Helper navigation methods
    # -------------------------------------------------------------------------
    def peek(self, offset: int = 0) -> Token:
        idx = self.pos + offset
        if idx >= len(self.tokens):
            return self.tokens[-1]  # Return EOF token
        return self.tokens[idx]

    def current(self) -> Token:
        return self.peek(0)

    def is_at_end(self) -> bool:
        return self.current().type == TokenType.EOF

    def advance(self) -> Token:
        tok = self.current()
        if not self.is_at_end():
            self.pos += 1
        return tok

    def check(self, *token_types: TokenType) -> bool:
        return self.current().type in token_types

    def match(self, *token_types: TokenType) -> bool:
        if self.check(*token_types):
            self.advance()
            return True
        return False

    def consume(self, token_type: TokenType, error_msg: str) -> Token:
        if self.check(token_type):
            return self.advance()
        tok = self.current()
        raise NppSyntaxError(error_msg, tok.line, tok.column, self.filename)

    def skip_separators(self):
        """Skip optional newlines and semicolons."""
        while self.check(TokenType.NEWLINE, TokenType.SEMICOLON):
            self.advance()

    # -------------------------------------------------------------------------
    # Top-level parsing
    # -------------------------------------------------------------------------
    def parse(self) -> Program:
        statements: List[ASTNode] = []
        self.skip_separators()

        while not self.is_at_end():
            stmt = self.parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self.skip_separators()

        return Program(statements=statements)

    # -------------------------------------------------------------------------
    # Statements
    # -------------------------------------------------------------------------
    def parse_statement(self) -> Optional[ASTNode]:
        self.skip_separators()
        if self.is_at_end():
            return None

        tok = self.current()

        # Output: say / print / display / show
        if self.check(TokenType.SAY):
            return self.parse_say_statement()

        # Variable declarations: set, let, make, const
        if self.check(TokenType.SET, TokenType.CONST):
            return self.parse_var_declaration()

        # Variable reassignment: change <var> to <val>
        if self.check(TokenType.CHANGE):
            return self.parse_change_statement()

        # Conditionals: if
        if self.check(TokenType.IF):
            return self.parse_if_statement()

        # Loops: repeat / loop
        if self.check(TokenType.REPEAT):
            return self.parse_repeat_statement()

        # Loops: while
        if self.check(TokenType.WHILE):
            return self.parse_while_statement()

        # Loops: for / for each
        if self.check(TokenType.FOR):
            return self.parse_for_each_statement()

        # Functions: to / fn / function / def
        if self.check(TokenType.FN) or (self.check(TokenType.TO) and self.peek(1).type == TokenType.IDENTIFIER):
            return self.parse_function_definition()

        # Control keywords
        if self.check(TokenType.RETURN):
            return self.parse_return_statement()

        if self.check(TokenType.BREAK):
            tok = self.advance()
            return BreakStmt(line=tok.line, column=tok.column)

        if self.check(TokenType.CONTINUE):
            tok = self.advance()
            return ContinueStmt(line=tok.line, column=tok.column)

        # Standard assignments or expression statements
        return self.parse_assignment_or_expression()

    def parse_say_statement(self) -> SayStmt:
        start_tok = self.advance()  # 'say'
        expr = self.parse_expression()
        return SayStmt(expression=expr, line=start_tok.line, column=start_tok.column)

    def parse_var_declaration(self) -> VarDecl:
        start_tok = self.advance()  # 'set' / 'let' / 'const'
        is_const = (start_tok.type == TokenType.CONST)

        # Variable name
        name_tok = self.consume(TokenType.IDENTIFIER, "Expected variable name after declaration keyword")

        # Separator: 'to' or '=' or ':' or directly expression
        if self.check(TokenType.TO, TokenType.ASSIGN, TokenType.COLON):
            self.advance()

        init_expr = self.parse_expression()
        return VarDecl(name=name_tok.value, initializer=init_expr, is_const=is_const, line=start_tok.line, column=start_tok.column)

    def parse_change_statement(self) -> AssignStmt:
        start_tok = self.advance()  # 'change'
        name_tok = self.consume(TokenType.IDENTIFIER, "Expected variable name after 'change'")
        if self.check(TokenType.TO, TokenType.ASSIGN):
            self.advance()
        expr = self.parse_expression()
        target = Identifier(name=name_tok.value, line=name_tok.line, column=name_tok.column)
        return AssignStmt(target=target, value=expr, operator="=", line=start_tok.line, column=start_tok.column)

    def parse_if_statement(self) -> IfStmt:
        start_tok = self.advance()  # 'if'
        condition = self.parse_expression()

        # Optional 'then' or ':'
        self.match(TokenType.THEN, TokenType.COLON)

        is_braced = self.match(TokenType.LBRACE)
        then_branch = self.parse_block(is_braced=is_braced, stop_at_elif=True)

        elif_branches: List[Tuple[ASTNode, ASTNode]] = []
        else_branch: Optional[ASTNode] = None

        while self.check(TokenType.ELIF):
            elif_tok = self.advance()  # 'elif' / 'otherwise if'
            elif_cond = self.parse_expression()
            self.match(TokenType.THEN, TokenType.COLON)
            elif_braced = self.match(TokenType.LBRACE)
            elif_body = self.parse_block(is_braced=elif_braced, stop_at_elif=True)
            elif_branches.append((elif_cond, elif_body))

        if self.check(TokenType.OTHERWISE):
            self.advance()  # 'otherwise' / 'else'
            self.match(TokenType.COLON)
            else_braced = self.match(TokenType.LBRACE)
            else_branch = self.parse_block(is_braced=else_braced, stop_at_elif=False)

        if not is_braced:
            self.consume(TokenType.END, "Expected 'end' at the close of 'if' block")

        return IfStmt(
            condition=condition,
            then_branch=then_branch,
            elif_branches=elif_branches,
            else_branch=else_branch,
            line=start_tok.line,
            column=start_tok.column
        )

    def parse_while_statement(self) -> WhileStmt:
        start_tok = self.advance()  # 'while'
        condition = self.parse_expression()
        self.match(TokenType.DO, TokenType.COLON)
        is_braced = self.match(TokenType.LBRACE)
        body = self.parse_block(is_braced=is_braced, stop_at_elif=False)
        if not is_braced:
            self.consume(TokenType.END, "Expected 'end' at the close of 'while' loop")
        return WhileStmt(condition=condition, body=body, line=start_tok.line, column=start_tok.column)

    def parse_repeat_statement(self) -> RepeatStmt:
        start_tok = self.advance()  # 'repeat' / 'loop'
        count = self.parse_expression()
        self.match(TokenType.TIMES, TokenType.DO, TokenType.COLON)
        is_braced = self.match(TokenType.LBRACE)
        body = self.parse_block(is_braced=is_braced, stop_at_elif=False)
        if not is_braced:
            self.consume(TokenType.END, "Expected 'end' at the close of 'repeat' block")
        return RepeatStmt(count=count, body=body, line=start_tok.line, column=start_tok.column)

    def parse_for_each_statement(self) -> ForEachStmt:
        start_tok = self.advance()  # 'for'
        self.match(TokenType.EACH)  # optional 'each'
        var_tok = self.consume(TokenType.IDENTIFIER, "Expected variable name in for-each loop")
        self.consume(TokenType.IN, "Expected 'in' after variable name in for-each loop")
        collection = self.parse_expression()
        self.match(TokenType.DO, TokenType.COLON)
        is_braced = self.match(TokenType.LBRACE)
        body = self.parse_block(is_braced=is_braced, stop_at_elif=False)
        if not is_braced:
            self.consume(TokenType.END, "Expected 'end' at the close of for-each loop")
        return ForEachStmt(variable=var_tok.value, collection=collection, body=body, line=start_tok.line, column=start_tok.column)

    def parse_function_definition(self) -> FunctionDef:
        start_tok = self.advance()  # 'to' or 'fn'
        name_tok = self.consume(TokenType.IDENTIFIER, "Expected function name")

        params: List[str] = []
        # Check if parameters defined with 'with' (e.g. "to greet with name, age")
        if self.match(TokenType.WITH):
            p = self.consume(TokenType.IDENTIFIER, "Expected parameter name after 'with'")
            params.append(p.value)
            while self.match(TokenType.COMMA):
                p = self.consume(TokenType.IDENTIFIER, "Expected parameter name after ','")
                params.append(p.value)
        elif self.match(TokenType.LPAREN):
            if not self.check(TokenType.RPAREN):
                p = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
                params.append(p.value)
                while self.match(TokenType.COMMA):
                    p = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
                    params.append(p.value)
            self.consume(TokenType.RPAREN, "Expected ')' after parameter list")

        self.match(TokenType.COLON)
        is_braced = self.match(TokenType.LBRACE)
        body = self.parse_block(is_braced=is_braced, stop_at_elif=False)
        if not is_braced:
            self.consume(TokenType.END, "Expected 'end' at the close of function")

        return FunctionDef(name=name_tok.value, parameters=params, body=body, line=start_tok.line, column=start_tok.column)

    def parse_return_statement(self) -> ReturnStmt:
        start_tok = self.advance()  # 'return' / 'give back'
        if self.check(TokenType.NEWLINE, TokenType.SEMICOLON, TokenType.END, TokenType.RBRACE, TokenType.EOF):
            return ReturnStmt(value=None, line=start_tok.line, column=start_tok.column)
        value = self.parse_expression()
        return ReturnStmt(value=value, line=start_tok.line, column=start_tok.column)

    def parse_block(self, is_braced: bool, stop_at_elif: bool) -> Block:
        stmts: List[ASTNode] = []
        self.skip_separators()

        while not self.is_at_end():
            if is_braced and self.check(TokenType.RBRACE):
                self.advance()  # consume '}'
                break
            if not is_braced:
                if self.check(TokenType.END):
                    break
                if stop_at_elif and self.check(TokenType.ELIF, TokenType.OTHERWISE):
                    break

            stmt = self.parse_statement()
            if stmt is not None:
                stmts.append(stmt)
            self.skip_separators()

        return Block(statements=stmts)

    def parse_assignment_or_expression(self) -> ASTNode:
        expr = self.parse_expression()

        # Check for assignment operators: =, +=, -=, *=, /=
        if self.check(TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN, TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN):
            op_tok = self.advance()
            val = self.parse_expression()

            if isinstance(expr, (Identifier, IndexExpr)):
                return AssignStmt(target=expr, value=val, operator=op_tok.value, line=op_tok.line, column=op_tok.column)
            else:
                raise NppSyntaxError(f"Invalid assignment target: {type(expr).__name__}", op_tok.line, op_tok.column, self.filename)

        return ExpressionStmt(expression=expr, line=expr.line, column=expr.column)

    # -------------------------------------------------------------------------
    # Expressions & Operator Precedence
    # -------------------------------------------------------------------------
    def parse_expression(self) -> ASTNode:
        return self.parse_logical_or()

    def parse_logical_or(self) -> ASTNode:
        left = self.parse_logical_and()
        while self.match(TokenType.OR):
            op = "or"
            self.skip_separators()
            right = self.parse_logical_and()
            left = BinaryOp(left=left, operator=op, right=right, line=left.line, column=left.column)
        return left

    def parse_logical_and(self) -> ASTNode:
        left = self.parse_equality()
        while self.match(TokenType.AND):
            op = "and"
            self.skip_separators()
            right = self.parse_equality()
            left = BinaryOp(left=left, operator=op, right=right, line=left.line, column=left.column)
        return left

    def parse_equality(self) -> ASTNode:
        left = self.parse_comparison()
        while self.check(TokenType.IS, TokenType.IS_NOT):
            op_tok = self.advance()
            self.skip_separators()
            right = self.parse_comparison()
            left = BinaryOp(left=left, operator=op_tok.value, right=right, line=op_tok.line, column=op_tok.column)
        return left

    def parse_comparison(self) -> ASTNode:
        left = self.parse_term()
        while self.check(TokenType.GREATER, TokenType.LESS, TokenType.GREATER_EQUAL, TokenType.LESS_EQUAL):
            op_tok = self.advance()
            self.skip_separators()
            right = self.parse_term()
            left = BinaryOp(left=left, operator=op_tok.value, right=right, line=op_tok.line, column=op_tok.column)
        return left

    def parse_term(self) -> ASTNode:
        left = self.parse_factor()
        while self.check(TokenType.PLUS, TokenType.MINUS):
            op_tok = self.advance()
            self.skip_separators()
            right = self.parse_factor()
            left = BinaryOp(left=left, operator=op_tok.value, right=right, line=op_tok.line, column=op_tok.column)
        return left

    def parse_factor(self) -> ASTNode:
        left = self.parse_power()
        while self.check(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op_tok = self.advance()
            self.skip_separators()
            right = self.parse_power()
            left = BinaryOp(left=left, operator=op_tok.value, right=right, line=op_tok.line, column=op_tok.column)
        return left

    def parse_power(self) -> ASTNode:
        left = self.parse_unary()
        while self.check(TokenType.CARET):
            op_tok = self.advance()
            self.skip_separators()
            right = self.parse_unary()
            left = BinaryOp(left=left, operator="^", right=right, line=op_tok.line, column=op_tok.column)
        return left

    def parse_unary(self) -> ASTNode:
        if self.check(TokenType.NOT, TokenType.MINUS):
            op_tok = self.advance()
            operand = self.parse_unary()
            return UnaryOp(operator=op_tok.value, operand=operand, line=op_tok.line, column=op_tok.column)
        return self.parse_call_and_index()

    def parse_call_and_index(self) -> ASTNode:
        expr = self.parse_primary()

        while True:
            # Function call: expr(arg1, arg2)
            if self.match(TokenType.LPAREN):
                args: List[ASTNode] = []
                self.skip_separators()
                if not self.check(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    self.skip_separators()
                    while self.match(TokenType.COMMA):
                        self.skip_separators()
                        if self.check(TokenType.RPAREN):
                            break
                        args.append(self.parse_expression())
                        self.skip_separators()
                self.consume(TokenType.RPAREN, "Expected ')' after argument list")
                expr = CallExpr(callee=expr, args=args, line=expr.line, column=expr.column)

            # Indexing: expr[index]
            elif self.match(TokenType.LBRACKET):
                self.skip_separators()
                idx = self.parse_expression()
                self.skip_separators()
                self.consume(TokenType.RBRACKET, "Expected ']' after index")
                expr = IndexExpr(target=expr, index=idx, line=expr.line, column=expr.column)

            # Member access or Method call: expr.member or expr.method(args)
            elif self.match(TokenType.DOT):
                member_tok = self.consume(TokenType.IDENTIFIER, "Expected member name after '.'")
                if self.match(TokenType.LPAREN):
                    args: List[ASTNode] = []
                    self.skip_separators()
                    if not self.check(TokenType.RPAREN):
                        args.append(self.parse_expression())
                        self.skip_separators()
                        while self.match(TokenType.COMMA):
                            self.skip_separators()
                            if self.check(TokenType.RPAREN):
                                break
                            args.append(self.parse_expression())
                            self.skip_separators()
                    self.consume(TokenType.RPAREN, "Expected ')' after method arguments")
                    expr = MethodCall(target=expr, method=member_tok.value, args=args, line=member_tok.line, column=member_tok.column)
                else:
                    expr = MemberAccess(target=expr, member=member_tok.value, line=member_tok.line, column=member_tok.column)

            else:
                break

        return expr

    def parse_primary(self) -> ASTNode:
        tok = self.current()

        # Literals
        if self.match(TokenType.NUMBER, TokenType.STRING, TokenType.BOOLEAN, TokenType.NULL):
            return Literal(value=tok.value, line=tok.line, column=tok.column)

        # ask <prompt> expression
        if self.match(TokenType.ASK):
            prompt = self.parse_expression()
            return AskExpr(prompt=prompt, line=tok.line, column=tok.column)

        # Identifier
        if self.match(TokenType.IDENTIFIER):
            return Identifier(name=tok.value, line=tok.line, column=tok.column)

        # Grouping (expr)
        if self.match(TokenType.LPAREN):
            self.skip_separators()
            expr = self.parse_expression()
            self.skip_separators()
            self.consume(TokenType.RPAREN, "Expected ')' to close grouped expression")
            return expr

        # List Literal [a, b, c]
        if self.match(TokenType.LBRACKET):
            elements: List[ASTNode] = []
            self.skip_separators()
            if not self.check(TokenType.RBRACKET):
                elements.append(self.parse_expression())
                self.skip_separators()
                while self.match(TokenType.COMMA):
                    self.skip_separators()
                    if self.check(TokenType.RBRACKET):
                        break  # Allow trailing comma
                    elements.append(self.parse_expression())
                    self.skip_separators()
            self.consume(TokenType.RBRACKET, "Expected ']' at end of list")
            return ListLiteral(elements=elements, line=tok.line, column=tok.column)

        # Map Literal { "key": val, ... }
        if self.match(TokenType.LBRACE):
            entries: List[Tuple[ASTNode, ASTNode]] = []
            self.skip_separators()
            if not self.check(TokenType.RBRACE):
                k = self.parse_expression()
                self.consume(TokenType.COLON, "Expected ':' after map key")
                self.skip_separators()
                v = self.parse_expression()
                entries.append((k, v))
                self.skip_separators()
                while self.match(TokenType.COMMA):
                    self.skip_separators()
                    if self.check(TokenType.RBRACE):
                        break  # Allow trailing comma
                    k = self.parse_expression()
                    self.consume(TokenType.COLON, "Expected ':' after map key")
                    self.skip_separators()
                    v = self.parse_expression()
                    entries.append((k, v))
                    self.skip_separators()
            self.consume(TokenType.RBRACE, "Expected '}' at end of map literal")
            return MapLiteral(entries=entries, line=tok.line, column=tok.column)

        raise NppSyntaxError(f"Unexpected token {tok.value!r} ({tok.type.name}) in expression", tok.line, tok.column, self.filename)
