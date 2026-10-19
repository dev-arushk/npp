# 📘 N++ Master Instruction Manual & Beginner Full Guide

Welcome to the **complete file-by-file instruction manual** for N++! This guide explains what **every single file** in the project does, why it exists, and exactly how you can run or edit it — even if you have never written a single line of code in your life.

---

## 📑 Table of Contents

1. [Quick Start (What to Click First)](#1-quick-start-what-to-click-first)
2. [Root Launcher Files (.bat)](#2-root-launcher-files-bat)
3. [The CLI & Entrypoint](#3-the-cli--entrypoint)
4. [The Core Language Compiler (`npp/`)](#4-the-core-language-compiler-npp)
5. [The Web Engine (`npp/web/`)](#5-the-web-engine-nppweb)
6. [Interactive Tutorial Engines (`tutorials/`)](#6-interactive-tutorial-engines-tutorials)
7. [Example Scripts (`examples/`)](#7-example-scripts-examples)
8. [Compiled Webpages (.html)](#8-compiled-webpages-html)
9. [Automated Test Suite (`tests/`)](#9-automated-test-suite-tests)
10. [Editor Syntax Highlighting (`syntaxes/`)](#10-editor-syntax-highlighting-syntaxes)
11. [Documentation Files (.md)](#11-documentation-files-md)
12. [N++ Plain English Cheat Sheet](#12-n-plain-english-cheat-sheet)

---

## 1. Quick Start (What to Click First)

If you are opening this project for the very first time, do this:

👉 **Double-click `START_HERE.bat`!**

That opens a friendly welcome menu with numbered options:
- Press `1` for the Beginner Tutorial
- Press `2` for the Web Engine Tutorial
- Press `3` for the System Walkthrough Tour
- Press `4` to test your own code live
- Press `5` for the Master Hub with web servers and preview tools

Everything runs automatically in pure Python with zero setup, zero npm, and zero external packages.

---

## 2. Root Launcher Files (.bat)

These Windows batch scripts let you launch any part of N++ with a single click from File Explorer. All `.bat` files feature automatic UTF-8 console encoding, Python detection (works with both `python` and `py`), and error protection so windows never vanish unexpectedly.

### `START_HERE.bat`
* **What it is:** The primary welcome portal for newcomers.
* **How to use:** Double-click it. It displays an interactive menu guiding you to tutorials, code testing, or the master hub.
* **Key feature:** Never quits automatically; returns to the menu after each activity.

### `play.bat`
* **What it is:** The Master Control Hub.
* **How to use:** Double-click it to access all 10 tools in one place:
  * Options `[1]-[3]`: Interactive tutorials and tours
  * Options `[4]-[5]`: One-click compilation and browser preview of showcase websites
  * Option `[6]`: Launch the embedded development web server on port 8080
  * Options `[7]-[8]`: Interactive code testing and custom script runner
  * Option `[9]`: Run the full 21-test automated verification suite

### `npp.bat`
* **What it is:** The Interactive Code Tester and command-line runner.
* **How to use:**
  * **Double-click it:** Opens the Code Tester menu where you can start a live REPL, test one-line English commands, or run any sample script.
  * **From command prompt:** Run commands like `npp myfile.npp`, `npp test`, `npp repl`, or `npp build page.npp`.
* **Key feature:** Automatically pauses if an error occurs so you can read diagnostic messages.

### `tutorial_beginner.bat`
* **What it is:** One-click launcher for the 8-lesson beginner programming tutorial.
* **How to use:** Double-click to start learning N++ from scratch through interactive examples.

### `tutorial_web.bat`
* **What it is:** One-click launcher for the 6-lesson modern web engine tutorial.
* **How to use:** Double-click to learn how to generate complete, responsive websites 1000x faster than writing raw HTML and CSS.

### `walkthrough_tour.bat`
* **What it is:** One-click launcher for the 5-station system walkthrough tour.
* **How to use:** Double-click to tour the compiler architecture, run live unit tests, and preview generated showcase web apps.

---

## 3. The CLI & Entrypoint

### `main.py`
* **What it is:** The top-level command-line entrypoint.
* **How it works:** Reconfigures Windows terminal encoding to UTF-8 and delegates to `npp.cli.main()`.
* **Common commands:**
  ```powershell
  python main.py                           # Starts the interactive REPL
  python main.py examples\intro_basics.npp # Runs an N++ script
  python main.py build my_site.npp         # Compiles script to standalone HTML
  python main.py serve my_site.npp 8080    # Compiles and serves live on port 8080
  python main.py test                      # Runs all 21 automated unit tests
  ```

---

## 4. The Core Language Compiler (`npp/`)

The `npp/` directory contains the complete modular compiler and execution engine.

### `npp/__init__.py`
* **What it is:** Package root.
* **Exports:** Version number (`__version__`), `run_code(source)`, `run_file(filepath)`, and `Interpreter`.

### `npp/tokens.py`
* **What it is:** Defines the vocabulary of the language.
* **How it works:** Contains the `TokenType` enumeration covering compound English keywords (`IS_GREATER_THAN`, `GIVE_BACK`, `FOR_EACH`, `REPEAT_TIMES`), literals, symbols, and the `Token` data structure storing line and column numbers.

### `npp/lexer.py`
* **What it is:** The Lexical Scanner.
* **How it works:** Reads raw text characters and converts them into tokens. Intelligently scans compound English phrases like `is at least`, `otherwise if`, `change ... to`, and handles comments (`//` and `/* ... */`).

### `npp/ast_nodes.py`
* **What it is:** The Abstract Syntax Tree (AST) definitions.
* **How it works:** Defines dataclasses for language constructs: `Statement`, `Expression`, `SayStatement`, `SetStatement`, `IfStatement`, `RepeatLoop`, `ForEachLoop`, `FunctionDef`, `BinaryOp`, and `CallExpr`.

### `npp/parser.py`
* **What it is:** The Recursive-Descent Pratt Parser.
* **How it works:** Takes tokens from the lexer and builds the AST hierarchy. Supports operator precedence, nested blocks closed with `end`, dot-notation method calls (`page.add(...)`), array indexing (`items[0]`), and map literals.

### `npp/environment.py`
* **What it is:** Scoping and memory manager.
* **How it works:** Manages nested lexical scopes (global, function, loop), variable resolution, reassignment checks (`change ... to`), and closures.

### `npp/interpreter.py`
* **What it is:** The Tree-Walk Evaluator.
* **How it works:** Walks the AST nodes and executes the program. Handles English conditionals, loops, functions, return signals, arithmetic coercion, and DOM element registration.

### `npp/builtins.py`
* **What it is:** The Standard Library and HTML5 tag catalog.
* **Included features:**
  * **All 110+ official HTML5 tags** registered as callable functions (`div()`, `h1()`, `p()`, `form()`, `table()`, `button()`, `input()`, etc.)
  * **Math:** `sqrt`, `pow`, `abs`, `round`, `floor`, `ceil`, `sin`, `cos`, `random_int`, `sum`, `max`, `min`
  * **String & Array:** `len`, `range`, `lower`, `upper`, `trim`, `split`, `join`, `replace`, `contains`
  * **Data & I/O:** `read_file`, `write_file`, `append_file`, `fetch_get`, `to_json`, `from_json`, `uuid_v4`, `sha256`, `md5`
  * **High-Level Web Components:** `webpage`, `hero`, `navbar`, `card`, `grid`, `container`, `badge`, `alert`, `stat_counter`, `progress_bar`, `modal`, `accordion`, `typewriter`, `export_html`

### `npp/cli.py`
* **What it is:** Command-Line Interface and interactive REPL.
* **How it works:** Manages commands (`build`, `serve`, `run`, `test`, `repl`), multiline REPL input, banner display, and diagnostic error output.

### `npp/errors.py`
* **What it is:** Diagnostic error formatting engine.
* **How it works:** Formats error messages with filename, line numbers, column indicators, and contextual source code excerpts so bugs are easy to pinpoint.

---

## 5. The Web Engine (`npp/web/`)

N++ includes a built-in web compiler that generates production-grade, zero-dependency HTML5.

### `npp/web/__init__.py`
* **What it is:** Web package exports uniting elements, components, themes, and server utilities.

### `npp/web/html_tags.py`
* **What it is:** Catalog of all 110+ official HTML5 tags, self-closing void elements (`<img/>`, `<input/>`, `<hr/>`), and standard global attributes (`id`, `class`, `style`, `data-*`, `aria-*`).

### `npp/web/elements.py`
* **What it is:** The `HTMLElement` tree structure.
* **How it works:** Handles child nesting (`element.add(...)`), attribute formatting, HTML escaping (preventing XSS while keeping emojis intact), and tag serialization.

### `npp/web/themes.py`
* **What it is:** Built-in modern CSS themes.
* **The 4 Themes:**
  1. `dark`: Obsidian dark theme with neon indigo and emerald accents.
  2. `modern`: Clean Swiss typography, slate cards, and subtle borders.
  3. `glassmorphism`: Frosted glass cards (`backdrop-filter: blur`), subtle borders, and smooth gradients.
  4. `cyberpunk`: High-contrast dark theme with neon pink and electric yellow accents.

### `npp/web/runtime.py`
* **What it is:** Client-side JavaScript v2.0 & CSS runtime (zero external dependencies).
* **17 Built-In Interactive Systems:**
  1. Toast notifications (`nppToast()`)
  2. Modal popup system (`data-npp-modal`) with Escape key and overlay click dismissal
  3. Tab switcher (`.npp-tab-button`, `.npp-tab-panel`)
  4. Accordion expand/collapse FAQ system
  5. Animated number counters that count up on scroll (`data-npp-count`)
  6. Live client-side search filtering (`data-npp-filter`)
  7. Animated progress bars (`data-value`)
  8. Typewriter text animation (`data-npp-type`)
  9. Tooltip hover popups (`data-npp-tip`)
  10. Scroll reveal entrance animations (`data-npp-reveal`)
  11. Button ripple click effect
  12. Floating scroll-to-top button
  13. IntersectionObserver lazy image fade-in
  14. Navbar theme switcher dropdown with `localStorage` persistence
  15. One-click copy-to-clipboard buttons (`data-npp-copy`)
  16. Counter buttons (➖/➕) with bounce animation
  17. Animated form submission with toast confirmation

### `npp/web/components.py`
* **What it is:** Pre-styled high-level UI building blocks.
* **Available Components:**
  * `Webpage`: Root document managing `<head>`, `<style>`, and `<body>`.
  * `Navbar`: Sticky top navigation with brand logo, links, and CTA button.
  * `Hero`: High-impact header banner with headline, subtitle, and CTA.
  * `Card`: Elevated content card with icon, badge, image, and action button.
  * `Grid`: Auto-responsive 2, 3, or 4 column grid without manual CSS.
  * `Container`: Centered, max-width layout wrapper.
  * `Badge`: Pill tag for statuses and categories.
  * `Alert`: Highlighted notice banner.
  * `StatCounter`: Live animated numeric metric card.
  * `ProgressBar`: Animated progress meter with percentage display.
  * `Modal`: Dialog popup with header, body, close button, and footer.
  * `Accordion`: Expandable FAQ accordion.
  * `Typewriter`: Self-typing animated text banner.
  * `PageFooter`: Standard page footer.

### `npp/web/server.py`
* **What it is:** Embedded Python development HTTP server.
* **How it works:** Serves the generated directory on port 8080 and automatically opens your default browser.

---

## 6. Interactive Tutorial Engines (`tutorials/`)

### `tutorials/interactive_beginner.py`
* **What it is:** Step-by-step interactive lesson engine for programming basics.
* **Lessons Covered:**
  1. Talking to the screen (`say`)
  2. Remembering values (`set ... to ...`)
  3. Asking questions (`ask`)
  4. Making decisions (`if`, `otherwise`)
  5. Repeating actions (`repeat N times`)
  6. Lists & shopping lists (`for each ... in ...`)
  7. Writing recipes (`to ... with ... give back ...`)
  8. Live mini-playground

### `tutorials/interactive_web.py`
* **What it is:** Interactive guide for building modern websites.
* **Lessons Covered:**
  1. Why N++ Web beats raw HTML
  2. Creating your first webpage in 5 lines
  3. The 4 visual themes
  4. Modern high-level components (`navbar`, `hero`, `card`, `grid`)
  5. Standard HTML5 tags (all 110+ tags)
  6. Interactive website builder (builds a customized site based on your answers!)

### `tutorials/interactive_walkthrough.py`
* **What it is:** 5-station guided architectural tour.
* **Tour Stations:**
  1. Language architecture & core engine
  2. Live automated health verification (runs all unit tests)
  3. Project structure & codebase overview
  4. Showcase web applications walkthrough
  5. VS Code extension & next steps

---

## 7. Example Scripts (`examples/`)

Every `.npp` file in `examples/` can be run directly using `python main.py examples\<filename>.npp` or option `[8]` in `play.bat`!

### `examples/intro_basics.npp`
* **What it demonstrates:** A gentle introduction to N++ English syntax: `say`, `set ... to ...`, `change ... to ...`, `if/otherwise`, `repeat 3 times`, and `for each`.

### `examples/guided_tour.npp`
* **What it demonstrates:** An interactive tour written completely inside N++ using `ask` to pause between steps, take user names, and test logic.

### `examples/simple_english.npp`
* **What it demonstrates:** Everyday plain English syntax examples that read like natural sentences.

### `examples/calculator.npp`
* **What it demonstrates:** Functions (`to add with a, b`), division checks, square roots, powers, and rounding.

### `examples/fibonacci.npp`
* **What it demonstrates:** Algorithms in English: recursive Fibonacci calculation and loop-based number sequences.

### `examples/fizzbuzz.npp`
* **What it demonstrates:** The classic coding interview problem solved in clean English syntax using `is divisible by`.

### `examples/web_all_html_tags.npp`
* **What it demonstrates:** The ultimate HTML5 showcase. Compiles all 110+ HTML5 tags, tables, forms, interactive tabs, modals, progress bars, and filters into `showcase.html`.

### `examples/web_saas_landing.npp`
* **What it demonstrates:** A full modern SaaS startup landing page with glassmorphism theme, metric counters, feature grid, pricing table, and newsletter signup compiling into `saas_landing.html`.

### `examples/interactive_dashboard.npp`
* **What it demonstrates:** A realtime planetary analytics dashboard compiling into `dashboard.html` using the new high-level `stat_counter`, `progress_bar`, `modal`, and `accordion` components.

---

## 8. Compiled Webpages (.html)

These are production-ready, standalone HTML5 files generated by N++ scripts:

* **`showcase.html`**: The complete HTML5 tags showcase featuring all interactive systems.
* **`saas_landing.html`**: A production-grade SaaS landing page for "Pulse AI".
* **`dashboard.html`**: Realtime interactive telemetry dashboard for "Apex.io".
* **`tutorial_page.html`**: Generated during the interactive web tutorial.
* **`components_demo.html`**: High-level component demo page.

---

## 9. Automated Test Suite (`tests/`)

N++ comes with a 100% automated test suite with **21 tests** that run in ~0.015 seconds.

### `tests/test_suite.py` (12 Tests)
Verifies language mechanics: compound phrases, English conditionals, functions, closures, loops, variable reassignment, maps, type coercion, and builtins.

### `tests/test_web.py` (9 Tests)
Verifies web engine mechanics: HTML tag catalog, void self-closing tags, element attributes, high-level components (`Hero`, `Card`, `Grid`, `Navbar`), interactive components (`StatCounter`, `ProgressBar`, `Modal`, `Accordion`, `Typewriter`), and full HTML rendering.

**To run all tests:**
```powershell
python main.py test
```
Or double-click `npp.bat` and press `4`!

---

## 10. Editor Syntax Highlighting (`syntaxes/`)

### `syntaxes/npp.tmLanguage.json`
* **What it is:** A complete TextMate grammar for VS Code.
* **Features:** Highlights English keywords (`say`, `set ... to`, `repeat times`, `give back`), all 110+ HTML5 tag functions, built-in library functions, numbers, and strings with full syntax color coding.

---

## 11. Documentation Files (.md)

* **`MANUAL.md`**: (This file) Complete file-by-file instruction manual.
* **`BEGINNER_GUIDE.md`**: Step-by-step introduction for beginners.
* **`WEB_GUIDE.md`**: In-depth guide to building webpages with N++.
* **`README.md`**: Full language reference manual and feature breakdown.
* **`INTRO.md`**: The design philosophy of N++ and why it was created.
* **`SPEC.md`**: Formal EBNF grammar specification.

---

## 12. N++ Plain English Cheat Sheet

| What You Want to Do | How to Write It in N++ |
|---------------------|------------------------|
| **Print message** | `say "Hello World!"` |
| **Create variable** | `set score to 100` |
| **Change variable** | `change score to 150` |
| **Ask question** | `set name to ask "Your name? "` |
| **Decision** | `if score is greater than 90 then say "Winner!" end` |
| **Otherwise** | `if x is 10 then say "Ten" otherwise say "Other" end` |
| **Repeat loop** | `repeat 5 times say "Cheer!" end` |
| **List loop** | `for each item in ["A", "B", "C"] say item end` |
| **Function** | `to add with a, b give back a + b end` |
| **Create webpage** | `set page to webpage("Title", "dark")` |
| **Hero banner** | `hero("Headline", "Subtitle", "Button", "#link")` |
| **Navbar** | `navbar("Brand", [{"Home": "#"}], "Sign In", "#")` |
| **Card** | `card("Title", "Description", "🚀")` |
| **3-Column Grid** | `grid(3, [card1, card2, card3])` |
| **Stat Counter** | `stat_counter(50000, "Active Users", "⚡")` |
| **Progress Bar** | `progress_bar(95, "Speed Score")` |
| **Modal Popup** | `modal("demo_id", "Title", "Body Text", "Close")` |
| **Accordion FAQ** | `accordion([["Question", "Answer"]])` |
| **Export HTML** | `export_html("index.html", page)` |
