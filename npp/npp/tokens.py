"""
N++ Token Definitions and Types
Supports both English-like keywords and traditional programming tokens.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()
    IDENTIFIER = auto()

    # English Output / Input Keywords
    SAY = auto()          # say, print, display, show
    ASK = auto()          # ask

    # Variables / Declarations
    SET = auto()          # set, let, make
    TO = auto()           # to (in "set x to 10")
    CONST = auto()        # const
    CHANGE = auto()       # change

    # Control Flow
    IF = auto()           # if
    THEN = auto()         # then
    OTHERWISE = auto()    # otherwise, else
    ELIF = auto()         # elif, otherwise if, else if
    END = auto()          # end

    # Loops
    REPEAT = auto()       # repeat, loop
    TIMES = auto()        # times
    WHILE = auto()        # while
    FOR = auto()          # for
    EACH = auto()         # each
    IN = auto()           # in
    DO = auto()           # do
    BREAK = auto()        # break, stop
    CONTINUE = auto()     # continue, next

    # Functions
    FN = auto()           # fn, function, to, def
    WITH = auto()         # with (for parameters: "to greet with name")
    RETURN = auto()       # return, give back

    # Logical / Comparison Keywords & Symbols
    AND = auto()          # and, &&
    OR = auto()           # or, ||
    NOT = auto()          # not, !
    IS = auto()           # is, ==, equals
    IS_NOT = auto()       # is not, !=
    GREATER = auto()      # >, greater than
    LESS = auto()         # <, less than
    GREATER_EQUAL = auto()# >=, greater than or equal to, at least
    LESS_EQUAL = auto()   # <=, less than or equal to, at most

    # Standard Arithmetic Operators
    PLUS = auto()         # +
    MINUS = auto()        # -
    STAR = auto()         # *
    SLASH = auto()        # /
    PERCENT = auto()      # %
    CARET = auto()        # ^

    # Assignment
    ASSIGN = auto()       # =
    PLUS_ASSIGN = auto()  # +=
    MINUS_ASSIGN = auto() # -=
    STAR_ASSIGN = auto()  # *=
    SLASH_ASSIGN = auto() # /=

    # Delimiters & Punctuation
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACKET = auto()     # [
    RBRACKET = auto()     # ]
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    COMMA = auto()        # ,
    COLON = auto()        # :
    SEMICOLON = auto()    # ;
    DOT = auto()          # .
    NEWLINE = auto()      # \n (statement separator)

    # Meta
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value!r}, L{self.line}:C{self.column})"


KEYWORDS = {
    # Output
    "say": TokenType.SAY,
    "print": TokenType.SAY,
    "display": TokenType.SAY,
    "show": TokenType.SAY,
    # Input
    "ask": TokenType.ASK,
    # Variables
    "set": TokenType.SET,
    "let": TokenType.SET,
    "make": TokenType.SET,
    "to": TokenType.TO,
    "const": TokenType.CONST,
    "change": TokenType.CHANGE,
    # Control flow
    "if": TokenType.IF,
    "then": TokenType.THEN,
    "otherwise": TokenType.OTHERWISE,
    "else": TokenType.OTHERWISE,
    "elif": TokenType.ELIF,
    "end": TokenType.END,
    # Loops
    "repeat": TokenType.REPEAT,
    "times": TokenType.TIMES,
    "while": TokenType.WHILE,
    "for": TokenType.FOR,
    "each": TokenType.EACH,
    "in": TokenType.IN,
    "do": TokenType.DO,
    "loop": TokenType.REPEAT,
    "break": TokenType.BREAK,
    "stop": TokenType.BREAK,
    "continue": TokenType.CONTINUE,
    "next": TokenType.CONTINUE,
    # Functions
    "fn": TokenType.FN,
    "function": TokenType.FN,
    "def": TokenType.FN,
    "with": TokenType.WITH,
    "return": TokenType.RETURN,
    # Logic / Comparisons
    "and": TokenType.AND,
    "or": TokenType.OR,
    "not": TokenType.NOT,
    "is": TokenType.IS,
    "equals": TokenType.IS,
    # Booleans / Null
    "true": TokenType.BOOLEAN,
    "yes": TokenType.BOOLEAN,
    "false": TokenType.BOOLEAN,
    "no": TokenType.BOOLEAN,
    "null": TokenType.NULL,
    "nothing": TokenType.NULL,
    "none": TokenType.NULL,
}
