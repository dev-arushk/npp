"""
N++ Abstract Syntax Tree (AST) Nodes
"""

from dataclasses import dataclass
from typing import List, Tuple, Optional, Any


@dataclass
class ASTNode:
    line: int = 1
    column: int = 1


@dataclass
class Program(ASTNode):
    statements: List[ASTNode] = None


# Expressions
@dataclass
class Literal(ASTNode):
    value: Any = None


@dataclass
class Identifier(ASTNode):
    name: str = ""


@dataclass
class BinaryOp(ASTNode):
    left: ASTNode = None
    operator: str = ""
    right: ASTNode = None


@dataclass
class UnaryOp(ASTNode):
    operator: str = ""
    operand: ASTNode = None


@dataclass
class AskExpr(ASTNode):
    prompt: ASTNode = None


@dataclass
class ListLiteral(ASTNode):
    elements: List[ASTNode] = None


@dataclass
class MapLiteral(ASTNode):
    entries: List[Tuple[ASTNode, ASTNode]] = None


@dataclass
class IndexExpr(ASTNode):
    target: ASTNode = None
    index: ASTNode = None


@dataclass
class CallExpr(ASTNode):
    callee: ASTNode = None
    args: List[ASTNode] = None


@dataclass
class MemberAccess(ASTNode):
    target: ASTNode = None
    member: str = ""


@dataclass
class MethodCall(ASTNode):
    target: ASTNode = None
    method: str = ""
    args: List[ASTNode] = None


# Statements
@dataclass
class Block(ASTNode):
    statements: List[ASTNode] = None


@dataclass
class ExpressionStmt(ASTNode):
    expression: ASTNode = None


@dataclass
class SayStmt(ASTNode):
    expression: ASTNode = None


@dataclass
class VarDecl(ASTNode):
    name: str = ""
    initializer: ASTNode = None
    is_const: bool = False


@dataclass
class AssignStmt(ASTNode):
    target: ASTNode = None  # Identifier or IndexExpr
    value: ASTNode = None
    operator: str = "="


@dataclass
class IfStmt(ASTNode):
    condition: ASTNode = None
    then_branch: ASTNode = None
    elif_branches: List[Tuple[ASTNode, ASTNode]] = None  # [(cond, block), ...]
    else_branch: Optional[ASTNode] = None


@dataclass
class WhileStmt(ASTNode):
    condition: ASTNode = None
    body: ASTNode = None


@dataclass
class RepeatStmt(ASTNode):
    count: ASTNode = None
    body: ASTNode = None


@dataclass
class ForEachStmt(ASTNode):
    variable: str = ""
    collection: ASTNode = None
    body: ASTNode = None


@dataclass
class FunctionDef(ASTNode):
    name: str = ""
    parameters: List[str] = None
    body: ASTNode = None


@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode] = None


@dataclass
class BreakStmt(ASTNode):
    pass


@dataclass
class ContinueStmt(ASTNode):
    pass
