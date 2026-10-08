"""
Interactive System Walkthrough Tour for N++
Walks the user through the engine architecture, tests, and showcase artifacts.
"""

import sys
import os
import unittest
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from npp import __version__


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(prompt="Press ENTER to continue to the next station..."):
    print("\n" + "-" * 75)
    input(f"  👉 {prompt}")
    print("-" * 75)


def header(title, step_num, total=5):
    clear()
    print("=" * 75)
    print(f"   🚀 N++ SYSTEM WALKTHROUGH TOUR — STATION {step_num} OF {total}")
    print(f"      {title.upper()}")
    print("=" * 75)
    print()


def station_1():
    header("Language Architecture & Core Engine", 1)
    print(f"""
  Welcome to the N++ Language Engine v{__version__}!
  
  N++ is built with a zero-dependency, modular compiler architecture:
    1. Lexer (npp/lexer.py):
       Tokenizes source code and identifies compound English keywords
       like 'is greater than', 'give back', 'for each', 'repeat times'.
    
    2. Parser (npp/parser.py):
       Recursive-descent & Pratt precedence parser constructing the
       Abstract Syntax Tree (AST), supporting multiline expressions and dot syntax.
    
    3. Lexical Scoping (npp/environment.py):
       Handles lexical scoping, const immutability, and nested closures.
    
    4. Evaluator (npp/interpreter.py):
       Tree-walk interpreter executing statements, expressions, and DOM elements.
    
    5. Web Engine (npp/web/):
       Generates semantic HTML5 with modern theme styles and zero external CSS.
    """)
    pause()


def station_2():
    header("Live Automated Health Verification (20 Tests)", 2)
    print("""
  Let's run the automated unit test suite right now to verify that all
  20 core language and web engine tests pass with 100% health:
    """)
    suite_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests")
    loader = unittest.TestLoader()
    suite = loader.discover(suite_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n  ✅ ALL TESTS PASSED! The engine is in pristine condition.")
    else:
        print("\n  ❌ Some tests failed. Please review the output above.")
    pause()


def station_3():
    header("Project Structure & Codebase Overview", 3)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"  Root Directory: {root_dir}\n")

    print("  Key Files and Documentation:")
    print("    * START_HERE.bat          - Primary 1-click launcher for beginners")
    print("    * play.bat                - The Master Hub (all tools & servers)")
    print("    * tutorial_beginner.bat   - Interactive beginner tutorial")
    print("    * tutorial_web.bat        - Interactive web engine tutorial")
    print("    * walkthrough_tour.bat    - This interactive walkthrough tour")
    print("    * BEGINNER_GUIDE.md       - Step-by-step beginner guide")
    print("    * WEB_GUIDE.md            - Web engine & HTML5 tag documentation")
    print("    * README.md               - Full language reference manual")
    print("    * SPEC.md                 - Formal EBNF grammar specification")
    pause()


def station_4():
    header("Showcase Web Applications (Better than HTML)", 4)
    print("""
  We generated two stunning, production-ready HTML5 web applications:
  
    1. showcase.html (From examples/web_all_html_tags.npp):
       Demonstrates all categories of HTML5 tags (headings, tables, forms,
       inputs, media, interactive elements, and modern components).

    2. saas_landing.html (From examples/web_saas_landing.npp):
       A high-converting SaaS startup landing page with glassmorphism design,
       hero banner, feature grid, 3-tier pricing table, and newsletter form.
    """)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(root_dir, "showcase.html")
    p2 = os.path.join(root_dir, "saas_landing.html")

    choice = input("  Would you like to open them in your browser now? (1: Showcase, 2: SaaS, 3: Both, 4: Skip): ").strip()
    if choice == "1":
        webbrowser.open("file://" + p1)
    elif choice == "2":
        webbrowser.open("file://" + p2)
    elif choice == "3":
        webbrowser.open("file://" + p1)
        webbrowser.open("file://" + p2)
    pause()


def station_5():
    header("VS Code Extension & Next Steps", 5)
    print("""
  Syntax Highlighting:
    A complete VS Code TextMate grammar is included at:
      syntaxes/npp.tmLanguage.json
    This highlights all English keywords, HTML5 tags, built-in functions,
    operators, and strings inside VS Code!

  Summary of What You Can Do Next:
    1. Run 'START_HERE.bat' or 'play.bat' whenever you want to code or learn.
    2. Try editing or creating your own '.npp' scripts in the 'examples/' folder.
    3. Run 'python main.py serve my_site.npp' to start a local live web server!
    """)
    input("  Press ENTER to conclude the walkthrough tour...")


def main():
    station_1()
    station_2()
    station_3()
    station_4()
    station_5()


if __name__ == "__main__":
    main()
