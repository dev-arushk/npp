"""
N++ Command-Line Interface, Interactive REPL, and Web Compiler / Server
"""

import sys
import os
import argparse
from . import __version__, run_code, run_file
from .interpreter import Interpreter
from .lexer import Lexer
from .parser import Parser
from .builtins import npp_format_value, get_active_webpage
from .errors import NppError
from .web import serve_directory


def print_banner():
    print(f"""
    ==================================================
        _   _       _         _             
       | \\ | |  _ _| |_ _   _| |_ _   _ _   
       |  \\| |_| |_   _| |_| |_   _| | | |  
       |_| \\_|___| |_| |___|_| |_|   |_| |  
                                       |___/ 
             N++ Programming Language v{__version__}
       Simple like English sentences, powerful & fast.
       Built-in Web Engine: Better & Easier than HTML.
    ==================================================
    Type 'help' for instructions, or 'exit'/'quit' to leave.
    """)


def print_help():
    print("""
    N++ Quick Commands:
      help            - Show this guide
      clear           - Clear the screen
      exit or quit    - Exit the REPL

    CLI Commands:
      npp run <file.npp>           - Run script
      npp build <file.npp> [out]   - Compile N++ web script to HTML5
      npp serve <file.npp> [port]  - Compile and serve locally in browser
      npp test                     - Run test suite
      npp repl                     - Start interactive sandbox

    Quick Syntax Examples:
      say "Hello World!"
      set name to ask "What is your name? "
      set score to 95
      if score is greater than 90 then say "Great job!" end
      repeat 3 times say "Hip hip hooray!" end
      for each item in [1, 2, 3] say "Item: " + item end

    Webpage Example:
      set page to webpage("My Website", "dark")
      hero("Welcome to N++", "Better than HTML!")
      export_html("index.html")
    """)


def repl():
    print_banner()
    interpreter = Interpreter(filename="<repl>")

    buffer = []
    in_multiline = False

    while True:
        try:
            prompt = "... " if in_multiline else "n++> "
            line = input(prompt)
            stripped = line.strip()

            if not in_multiline:
                if stripped.lower() in ("exit", "quit", "exit()", "quit()"):
                    print("Goodbye!")
                    break
                if stripped.lower() == "help":
                    print_help()
                    continue
                if stripped.lower() == "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                if not stripped:
                    continue

            buffer.append(line)
            full_source = "\n".join(buffer)

            # Check if block keyword is open without 'end'
            words = full_source.split()
            block_openers = ("if", "while", "repeat", "loop", "fn", "function", "to")
            open_count = sum(1 for w in words if w in block_openers)
            close_count = sum(1 for w in words if w in ("end", "}"))

            if open_count > close_count and line.strip() != "":
                in_multiline = True
                continue

            in_multiline = False
            buffer = []

            try:
                lexer = Lexer(full_source, filename="<repl>")
                tokens = lexer.tokenize()
                parser = Parser(tokens, source=full_source, filename="<repl>")
                program = parser.parse()

                val = interpreter.interpret(program)
                if val is not None:
                    print(f"=> {npp_format_value(val)}")

            except NppError as err:
                print(err.format_diagnostic(full_source))
            except Exception as e:
                print(f"Error: {e}")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting N++.")
            break


def build_command(filepath: str, output_path: str = None):
    """Run an N++ web script and save its active webpage to an HTML file."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    print(f"Compiling '{filepath}' to HTML5...")
    run_file(filepath)
    page = get_active_webpage()

    if page is not None:
        if not output_path:
            base, _ = os.path.splitext(filepath)
            output_path = base + ".html"
        page.export(output_path)
        print(f"Success! Webpage compiled to '{output_path}'.")
    else:
        print("Note: Script executed, but no 'webpage' document was registered.")


def serve_command(filepath: str, port: int = 8080):
    """Compile N++ web script and start local web server."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    build_command(filepath)
    file_dir = os.path.dirname(os.path.abspath(filepath)) or "."
    serve_directory(file_dir, port=port, open_browser=True)


def main():
    args = sys.argv[1:]

    if not args:
        repl()
        return

    cmd = args[0]

    if cmd in ("-v", "--version", "version"):
        print(f"N++ version {__version__}")
        return

    if cmd in ("-h", "--help", "help"):
        print_help()
        return

    if cmd == "repl":
        repl()
        return

    if cmd == "test":
        import unittest
        loader = unittest.TestLoader()
        suite_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests")
        suite = loader.discover(suite_dir, pattern="test_*.py")
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        return

    if cmd == "build":
        if len(args) < 2:
            print("Error: Missing file. Usage: npp build <file.npp> [output.html]")
            sys.exit(1)
        src = args[1]
        out = args[2] if len(args) > 2 else None
        build_command(src, out)
        return

    if cmd == "serve":
        if len(args) < 2:
            print("Error: Missing file. Usage: npp serve <file.npp> [port]")
            sys.exit(1)
        src = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        serve_command(src, port)
        return

    if cmd == "run":
        if len(args) < 2:
            print("Error: Missing file to run. Usage: npp run <file.npp>")
            sys.exit(1)
        filepath = args[1]
    else:
        filepath = cmd

    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    run_file(filepath)


if __name__ == "__main__":
    main()
