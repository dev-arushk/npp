"""
N++ Error Diagnostics and Reporting
Formats clear, friendly errors with file/line context and visual caret indicators.
"""

from typing import Optional


class NppError(Exception):
    def __init__(self, message: str, line: int = 1, column: int = 1, filename: str = "<input>"):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
        self.filename = filename

    def format_diagnostic(self, source_code: Optional[str] = None) -> str:
        header = f"\n[N++ Error] in {self.filename} at line {self.line}, column {self.column}:\n  {self.message}"
        if not source_code:
            return header

        lines = source_code.splitlines()
        if 1 <= self.line <= len(lines):
            target_line = lines[self.line - 1]
            gutter = f"  {self.line} | "
            pointer = " " * (len(gutter) + max(0, self.column - 1)) + "^"
            return f"{header}\n\n{gutter}{target_line}\n{pointer}\n"
        return header

    def __str__(self) -> str:
        return f"{self.message} (line {self.line}, col {self.column})"


class NppSyntaxError(NppError):
    pass


class NppRuntimeError(NppError):
    pass


class NppReturnSignal(Exception):
    """Internal control flow exception used to unwind function returns."""
    def __init__(self, value: any):
        self.value = value


class NppBreakSignal(Exception):
    """Internal control flow exception for loop breaks."""
    pass


class NppContinueSignal(Exception):
    """Internal control flow exception for loop continues."""
    pass
