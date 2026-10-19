"""
N++ Lexer (Tokenizer)
Transforms source text into a stream of tokens, recognizing both English-style
phrases and standard programming symbols.
"""

from typing import List, Optional
from .tokens import Token, TokenType, KEYWORDS
from .errors import NppSyntaxError


class Lexer:
    def __init__(self, source: str, filename: str = "<input>"):
        self.source = source
        self.filename = filename
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens: List[Token] = []

    def peek(self, offset: int = 0) -> str:
        idx = self.pos + offset
        if idx >= len(self.source):
            return "\0"
        return self.source[idx]

    def advance(self) -> str:
        ch = self.peek()
        self.pos += 1
        if ch == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def match(self, expected: str) -> bool:
        if self.peek() == expected:
            self.advance()
            return True
        return False

    def skip_whitespace_inline(self):
        """Skip whitespace on the same line (spaces, tabs, carriage returns)."""
        while self.peek() in (" ", "\t", "\r"):
            self.advance()

    def tokenize(self) -> List[Token]:
        while self.pos < len(self.source):
            ch = self.peek()

            # Ignore horizontal whitespace
            if ch in (" ", "\t", "\r"):
                self.advance()
                continue

            # Newlines (significant statement separators)
            if ch == "\n":
                line, col = self.line, self.col
                self.advance()
                # Suppress consecutive newlines or newlines at the very start
                if self.tokens and self.tokens[-1].type != TokenType.NEWLINE:
                    self.tokens.append(Token(TokenType.NEWLINE, "\n", line, col))
                continue

            # Comments
            # 1) // single line
            if ch == "/" and self.peek(1) == "/":
                self.advance()
                self.advance()
                while self.peek() not in ("\n", "\0"):
                    self.advance()
                continue

            # 2) /* multi line */
            if ch == "/" and self.peek(1) == "*":
                self.advance()
                self.advance()
                start_line, start_col = self.line, self.col
                while not (self.peek() == "*" and self.peek(1) == "/") and self.peek() != "\0":
                    self.advance()
                if self.peek() == "\0":
                    raise NppSyntaxError("Unterminated multi-line comment /* ... */", start_line, start_col, self.filename)
                self.advance() # *
                self.advance() # /
                continue

            # 3) # single line comment
            if ch == "#":
                while self.peek() not in ("\n", "\0"):
                    self.advance()
                continue

            # Numbers (integers and floats)
            if ch.isdigit():
                self.tokens.append(self.lex_number())
                continue

            # Strings
            if ch in ('"', "'"):
                self.tokens.append(self.lex_string(ch))
                continue

            # Identifiers and words
            if ch.isalpha() or ch == "_":
                tok = self.lex_word()
                if tok:
                    self.tokens.append(tok)
                continue

            # Operators and punctuation
            line, col = self.line, self.col
            if ch == "=":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.IS, "==", line, col))
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, "=", line, col))
            elif ch == "!":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.IS_NOT, "!=", line, col))
                else:
                    self.tokens.append(Token(TokenType.NOT, "!", line, col))
            elif ch == "<":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.LESS_EQUAL, "<=", line, col))
                else:
                    self.tokens.append(Token(TokenType.LESS, "<", line, col))
            elif ch == ">":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, ">=", line, col))
                else:
                    self.tokens.append(Token(TokenType.GREATER, ">", line, col))
            elif ch == "+":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.PLUS_ASSIGN, "+=", line, col))
                else:
                    self.tokens.append(Token(TokenType.PLUS, "+", line, col))
            elif ch == "-":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.MINUS_ASSIGN, "-=", line, col))
                else:
                    self.tokens.append(Token(TokenType.MINUS, "-", line, col))
            elif ch == "*":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.STAR_ASSIGN, "*=", line, col))
                else:
                    self.tokens.append(Token(TokenType.STAR, "*", line, col))
            elif ch == "/":
                self.advance()
                if self.match("="):
                    self.tokens.append(Token(TokenType.SLASH_ASSIGN, "/=", line, col))
                else:
                    self.tokens.append(Token(TokenType.SLASH, "/", line, col))
            elif ch == "%":
                self.advance()
                self.tokens.append(Token(TokenType.PERCENT, "%", line, col))
            elif ch == "^":
                self.advance()
                self.tokens.append(Token(TokenType.CARET, "^", line, col))
            elif ch == "&" and self.peek(1) == "&":
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.AND, "&&", line, col))
            elif ch == "|" and self.peek(1) == "|":
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.OR, "||", line, col))
            elif ch == "(":
                self.advance()
                self.tokens.append(Token(TokenType.LPAREN, "(", line, col))
            elif ch == ")":
                self.advance()
                self.tokens.append(Token(TokenType.RPAREN, ")", line, col))
            elif ch == "[":
                self.advance()
                self.tokens.append(Token(TokenType.LBRACKET, "[", line, col))
            elif ch == "]":
                self.advance()
                self.tokens.append(Token(TokenType.RBRACKET, "]", line, col))
            elif ch == "{":
                self.advance()
                self.tokens.append(Token(TokenType.LBRACE, "{", line, col))
            elif ch == "}":
                self.advance()
                self.tokens.append(Token(TokenType.RBRACE, "}", line, col))
            elif ch == ",":
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ",", line, col))
            elif ch == ":":
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ":", line, col))
            elif ch == ";":
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ";", line, col))
            elif ch == ".":
                self.advance()
                self.tokens.append(Token(TokenType.DOT, ".", line, col))
            else:
                bad_char = self.advance()
                raise NppSyntaxError(f"Unexpected character: {bad_char!r}", line, col, self.filename)

        # Append EOF
        # Ensure trailing newline does not clutter
        while self.tokens and self.tokens[-1].type == TokenType.NEWLINE:
            self.tokens.pop()
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return self.tokens

    def lex_number(self) -> Token:
        start_line, start_col = self.line, self.col
        num_str = ""
        is_float = False

        while self.peek().isdigit():
            num_str += self.advance()

        if self.peek() == "." and self.peek(1).isdigit():
            is_float = True
            num_str += self.advance()  # '.'
            while self.peek().isdigit():
                num_str += self.advance()

        val = float(num_str) if is_float else int(num_str)
        return Token(TokenType.NUMBER, val, start_line, start_col)

    def lex_string(self, quote: str) -> Token:
        start_line, start_col = self.line, self.col
        self.advance()  # opening quote
        chars = []

        while self.peek() != quote and self.peek() != "\0":
            ch = self.advance()
            if ch == "\\":
                esc = self.advance()
                if esc == "n":
                    chars.append("\n")
                elif esc == "t":
                    chars.append("\t")
                elif esc == "r":
                    chars.append("\r")
                elif esc == "\\":
                    chars.append("\\")
                elif esc == quote:
                    chars.append(quote)
                else:
                    chars.append(esc)
            else:
                chars.append(ch)

        if self.peek() == "\0":
            raise NppSyntaxError(f"Unterminated string literal starting with {quote}", start_line, start_col, self.filename)

        self.advance()  # closing quote
        return Token(TokenType.STRING, "".join(chars), start_line, start_col)

    def _peek_word(self) -> str:
        """Look ahead without consuming to inspect the next word on this line."""
        saved_pos = self.pos
        saved_col = self.col
        saved_line = self.line

        # Skip horizontal spaces
        while self.peek() in (" ", "\t"):
            self.advance()

        word = ""
        if self.peek().isalpha() or self.peek() == "_":
            while self.peek().isalnum() or self.peek() == "_":
                word += self.advance()

        # Restore state
        self.pos = saved_pos
        self.col = saved_col
        self.line = saved_line
        return word.lower()

    def _consume_word(self, expected: str) -> bool:
        """If the next word matches expected, consume it and return True."""
        saved_pos = self.pos
        saved_col = self.col
        saved_line = self.line

        while self.peek() in (" ", "\t"):
            self.advance()

        word = ""
        while self.peek().isalnum() or self.peek() == "_":
            word += self.advance()

        if word.lower() == expected.lower():
            return True

        # Backtrack
        self.pos = saved_pos
        self.col = saved_col
        self.line = saved_line
        return False

    def lex_word(self) -> Optional[Token]:
        start_line, start_col = self.line, self.col
        word = ""
        while self.peek().isalnum() or self.peek() == "_":
            word += self.advance()

        lower = word.lower()

        # Check for English "note: ..." comments
        if lower == "note":
            # Check if followed by colon
            self.skip_whitespace_inline()
            if self.peek() == ":":
                self.advance()  # consume ':'
                # Skip remainder of line as comment
                while self.peek() not in ("\n", "\0"):
                    self.advance()
                return None

        # Handle English multi-word phrases:
        # "is not" -> IS_NOT
        if lower == "is":
            if self._consume_word("not"):
                return Token(TokenType.IS_NOT, "!=", start_line, start_col)
            if self._consume_word("greater"):
                if self._consume_word("than"):
                    if self._consume_word("or") and self._consume_word("equal") and self._consume_word("to"):
                        return Token(TokenType.GREATER_EQUAL, ">=", start_line, start_col)
                    return Token(TokenType.GREATER, ">", start_line, start_col)
            if self._consume_word("less"):
                if self._consume_word("than"):
                    if self._consume_word("or") and self._consume_word("equal") and self._consume_word("to"):
                        return Token(TokenType.LESS_EQUAL, "<=", start_line, start_col)
                    return Token(TokenType.LESS, "<", start_line, start_col)
            if self._consume_word("at"):
                if self._consume_word("least"):
                    return Token(TokenType.GREATER_EQUAL, ">=", start_line, start_col)
                if self._consume_word("most"):
                    return Token(TokenType.LESS_EQUAL, "<=", start_line, start_col)
            return Token(TokenType.IS, "==", start_line, start_col)

        # "greater than", "greater than or equal to"
        if lower == "greater":
            if self._consume_word("than"):
                if self._consume_word("or") and self._consume_word("equal") and self._consume_word("to"):
                    return Token(TokenType.GREATER_EQUAL, ">=", start_line, start_col)
                return Token(TokenType.GREATER, ">", start_line, start_col)

        # "less than", "less than or equal to"
        if lower == "less":
            if self._consume_word("than"):
                if self._consume_word("or") and self._consume_word("equal") and self._consume_word("to"):
                    return Token(TokenType.LESS_EQUAL, "<=", start_line, start_col)
                return Token(TokenType.LESS, "<", start_line, start_col)

        # "at least", "at most"
        if lower == "at":
            if self._consume_word("least"):
                return Token(TokenType.GREATER_EQUAL, ">=", start_line, start_col)
            if self._consume_word("most"):
                return Token(TokenType.LESS_EQUAL, "<=", start_line, start_col)

        # "otherwise if", "else if" -> ELIF
        if lower in ("otherwise", "else"):
            if self._consume_word("if"):
                return Token(TokenType.ELIF, "elif", start_line, start_col)
            return Token(TokenType.OTHERWISE, "otherwise", start_line, start_col)

        # "give back" -> RETURN
        if lower == "give":
            if self._consume_word("back"):
                return Token(TokenType.RETURN, "return", start_line, start_col)

        # "for each" -> FOR
        if lower == "for":
            if self._consume_word("each"):
                return Token(TokenType.FOR, "for each", start_line, start_col)
            return Token(TokenType.FOR, "for", start_line, start_col)

        # "repeat" or "loop"
        if lower in ("repeat", "loop"):
            return Token(TokenType.REPEAT, "repeat", start_line, start_col)

        # Single keywords
        if lower in KEYWORDS:
            tok_type = KEYWORDS[lower]
            val = word
            if tok_type == TokenType.BOOLEAN:
                val = lower in ("true", "yes")
            elif tok_type == TokenType.NULL:
                val = None
            return Token(tok_type, val, start_line, start_col)

        # Standard identifier
        return Token(TokenType.IDENTIFIER, word, start_line, start_col)
