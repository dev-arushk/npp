# npp
By Arush Kulkarni, N++ CODING LANGUAGE 2026 - OPEN THE FOLDER ABOVE 👆
WHEN OPENED, PLEASE READ ALL .MD FILES AS THEY CONTAIN INFO ABOUT USAGE INSTRUCTIONS.
AFTER READING, YOU CAN SAFELY DOWNLOAD THE FILES AND TEST N++ ON YOUR COMPUTER!
HAVE FUN CODING! - ARUSH

UPDATE 2 -

1. 🛠️ Fixed All .bat Files (No More Immediate Quitting)
Why they were crashing:
Windows Console Character Encoding (cp1252 / cp437): When Python printed emojis or Unicode characters (🌟, 🌐, 🚀, 👉, ✅, ❌, —), it threw: UnicodeEncodeError: 'charmap' codec can't encode character... Because Windows closes batch windows when an error occurs, the window vanished instantly!
Unescaped Ampersands (&): In Windows batch scripts, & is a command separator. Titles and menu text like & Quick Launcher and & test scripts caused Windows to try executing them as non-existent commands.
Execution Directory: When .bat files were double-clicked from File Explorer, the working directory could diverge from the project root.
What was fixed:
tutorial_beginner.bat: Added chcp 65001 >nul, PYTHONIOENCODING=utf-8, Python auto-detection (python / py), cd /d "%~dp0", and error protection with pause.
tutorial_web.bat: Upgraded with full UTF-8 encoding protection, Python detection, and clean exit handling.
walkthrough_tour.bat: Upgraded with full UTF-8 encoding protection and clean exit handling.
npp.bat (Interactive Code Tester): Completely redesigned so it never immediately quits:
When double-clicked: Opens an interactive testing hub with options to launch the live REPL, test one-line English code, run beginner basics, run the guided tour, or run all 21 unit tests.
When run with arguments (npp test, npp my_script.npp): Runs the command directly and pauses on errors so you can read the output.
START_HERE.bat & play.bat: Replaced unquoted ampersands, added UTF-8 console support, and added loop-back navigation so menus stay open.
2. 🌟 Lots of Code Updates & New Features

New 1-Line Interactive Web Components (npp/web/components.py & npp/builtins.py):

stat_counter(target, label, icon): Creates an animated numeric counter that counts up smoothly on scroll.
progress_bar(value, label): Creates an animated percentage bar with labels.
modal(id, title, content, close_text): Creates a popup modal window with backdrop click and ESC key dismiss.
accordion(items): Creates an expandable/collapsible FAQ accordion from simple lists.
typewriter(text, tag): Creates an animated self-typing text heading.

New Example Programs (examples/):

examples/calculator.npp: An interactive English math calculator demonstrating functions, input, math operations, and return values.
examples/interactive_dashboard.npp: A realtime planetary analytics dashboard compiling into dashboard.html using the cyberpunk theme, animated metric counters, progress bars, accordions, and cluster provisioner modals.

Expanded Unit Test Suite (tests/):

Added test_interactive_components to verify all new components.
All 21 unit tests pass in 0.012s with 100% health (python main.py test).
3. 📘 New Complete Instruction Manual (MANUAL.md)

A comprehensive beginner-friendly manual has been created at MANUAL.md. It documents every single file in the repository:

Category	Files Covered
Root Launchers	START_HERE.bat, play.bat, npp.bat, tutorial_beginner.bat, tutorial_web.bat, walkthrough_tour.bat
CLI & Entry	main.py
Compiler Engine	npp/tokens.py, npp/lexer.py, npp/ast_nodes.py, npp/parser.py, npp/environment.py, npp/interpreter.py, npp/builtins.py, npp/cli.py, npp/errors.py
Web Engine	npp/web/html_tags.py, npp/web/elements.py, npp/web/themes.py, npp/web/runtime.py, npp/web/components.py, npp/web/server.py
Tutorial Engines	tutorials/interactive_beginner.py, tutorials/interactive_web.py, tutorials/interactive_walkthrough.py
Example Scripts	examples/intro_basics.npp, examples/guided_tour.npp, examples/calculator.npp, examples/interactive_dashboard.npp, examples/web_all_html_tags.npp, examples/web_saas_landing.npp, etc.
Web Output	showcase.html, saas_landing.html, dashboard.html
Automated Tests	tests/test_suite.py, tests/test_web.py (21 unit tests)
Syntax Grammar	syntaxes/npp.tmLanguage.json

HAVE FUN TESTING! - OCTOBER 19 2026
