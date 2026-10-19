"""
N++ Comprehensive Test Suite
Validates lexing, parsing, runtime execution, and English sentence syntax.
"""

import unittest
import io
import sys
from npp.lexer import Lexer
from npp.tokens import TokenType
from npp.parser import Parser
from npp.interpreter import Interpreter
from npp import run_code


class TestNppLanguage(unittest.TestCase):

    def run_npp_capture(self, code: str) -> str:
        """Helper to run N++ code and capture standard output."""
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            interp = Interpreter(filename="<test>")
            lexer = Lexer(code, filename="<test>")
            tokens = lexer.tokenize()
            parser = Parser(tokens, source=code, filename="<test>")
            prog = parser.parse()
            interp.interpret(prog)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    def test_lexer_english_phrases(self):
        source = 'if x is greater than 10 or y is less than or equal to 5'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        types = [t.type for t in tokens]
        self.assertIn(TokenType.IF, types)
        self.assertIn(TokenType.GREATER, types)
        self.assertIn(TokenType.OR, types)
        self.assertIn(TokenType.LESS_EQUAL, types)

    def test_say_and_variables(self):
        code = """
        set name to "Antigravity"
        say "Hello " + name
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "Hello Antigravity")

    def test_english_reassignment(self):
        code = """
        set counter to 5
        change counter to 10
        say counter
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "10")

    def test_english_conditionals(self):
        code = """
        set score to 85
        if score is greater than 90 then
            say "Grade: A"
        otherwise if score is greater than 80 then
            say "Grade: B"
        otherwise
            say "Grade: C"
        end
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "Grade: B")

    def test_repeat_loop(self):
        code = """
        set count to 0
        repeat 4 times
            count += 1
        end
        say count
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "4")

    def test_for_each_loop(self):
        code = """
        set fruits to ["apple", "banana", "orange"]
        set total to 0
        for each item in fruits
            total += 1
        end
        say total
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "3")

    def test_while_loop(self):
        code = """
        set n to 1
        while n is less than 5
            n += 1
        end
        say n
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "5")

    def test_english_function_definition(self):
        code = """
        to multiply with a, b
            give back a * b
        end
        say multiply(6, 7)
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "42")

    def test_string_number_automatic_coercion(self):
        code = """
        set age to 21
        say "I am " + age + " years old"
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "I am 21 years old")

    def test_builtins_len_range(self):
        code = """
        set numbers to range(5)
        say len(numbers)
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "5")

    def test_data_structures_maps(self):
        code = """
        set user to {"name": "Alice", "role": "engineer"}
        say user["name"] + " is an " + user["role"]
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "Alice is an engineer")

    def test_closure(self):
        code = """
        to make_adder with n
            to add with x
                give back x + n
            end
            give back add
        end
        set add5 to make_adder(5)
        say add5(10)
        """
        output = self.run_npp_capture(code)
        self.assertEqual(output, "15")


if __name__ == "__main__":
    unittest.main()
