"""
N++ Lexical Environment
Manages variable/function scopes, bindings, closures, and const mutability rules.
"""

from typing import Dict, Set, Optional, Any
from .errors import NppRuntimeError


class Environment:
    def __init__(self, parent: Optional["Environment"] = None):
        self.values: Dict[str, Any] = {}
        self.constants: Set[str] = set()
        self.parent: Optional["Environment"] = parent

    def define(self, name: str, value: Any, is_const: bool = False):
        """Define a new variable or constant in the current immediate scope."""
        self.values[name] = value
        if is_const:
            self.constants.add(name)

    def assign(self, name: str, value: Any, line: int = 1, col: int = 1, filename: str = "<input>"):
        """Assign to an existing variable in the current or an enclosing scope."""
        if name in self.values:
            if name in self.constants:
                raise NppRuntimeError(f"Cannot reassign to constant '{name}'", line, col, filename)
            self.values[name] = value
            return

        if self.parent is not None:
            self.parent.assign(name, value, line, col, filename)
            return

        # If not declared anywhere, auto-define in current scope for ultra-easy beginner forgiveness
        self.values[name] = value

    def get(self, name: str, line: int = 1, col: int = 1, filename: str = "<input>") -> Any:
        """Resolve a variable name from the current or enclosing scopes."""
        if name in self.values:
            return self.values[name]

        if self.parent is not None:
            return self.parent.get(name, line, col, filename)

        raise NppRuntimeError(f"Undefined variable or function '{name}'", line, col, filename)

    def has(self, name: str) -> bool:
        if name in self.values:
            return True
        if self.parent:
            return self.parent.has(name)
        return False
