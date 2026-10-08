"""
N++ Programming Language Engine
"""

from typing import Any
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .errors import NppError

__version__ = "1.0.0"


def run_code(source: str, filename: str = "<input>", interpreter: Interpreter = None) -> Any:
    """Run an N++ code string through the lexer, parser, and interpreter."""
    try:
        lexer = Lexer(source, filename=filename)
        tokens = lexer.tokenize()

        parser = Parser(tokens, source=source, filename=filename)
        program = parser.parse()

        if interpreter is None:
            interpreter = Interpreter(filename=filename, source=source)
        else:
            interpreter.filename = filename
            interpreter.source = source

        return interpreter.interpret(program)

    except NppError as err:
        print(err.format_diagnostic(source))
        return None
    except Exception as exc:
        print(f"\n[Unexpected Internal Error] {exc}")
        return None


def run_file(filepath: str) -> Any:
    """Read and run an N++ script file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
    except Exception as e:
        print(f"Error opening file '{filepath}': {e}")
        return None

    return run_code(source, filename=filepath)
