# N++ Beginner Full Guide and File Manual

This guide is meant to help a complete beginner understand both the language and the project itself. It explains what N++ is, how to run it, what each file does, and how the language fits together.

This is not just a quick cheat sheet. It is a beginner-friendly map of the whole repo.

---

## 1) What N++ is

N++ is a programming language designed to feel like writing plain English instructions.

Instead of writing lots of syntax-heavy code, you can write things like:

```npp
say "Hello!"
set name to ask "What is your name? "
if name is not "" then
    say "Nice to meet you, " + name
end
```

It is meant to be:
- readable
- friendly for beginners
- simple enough to understand in plain English
- powerful enough to build web pages and scripts

The project also includes a web engine so you can build HTML pages in N++ instead of writing raw HTML/CSS/JS for everything.

---

## 2) The fastest way to run N++

From the project root, you can run:

```powershell
python main.py examples\intro_basics.npp
```

Or on Windows, the easiest route is:

```powershell
.\npp.bat examples\intro_basics.npp
```

To open the interactive REPL:

```powershell
.\npp.bat repl
```

Or:

```powershell
python main.py repl
```

---

## 3) Core commands you will use

The CLI is defined in [npp/cli.py](npp/cli.py). The most useful commands are:

```powershell
python main.py run my_script.npp
python main.py build my_script.npp
python main.py serve my_script.npp 8080
python main.py repl
python main.py test
```

In Windows batch form:

```powershell
.\npp.bat my_script.npp
.\npp.bat repl
.\npp.bat test
```

The main patterns are:
- run a script
- build a web page from a script
- serve the page locally in a browser
- test the project
- use the REPL to type code live

---

## 4) How the language works internally

N++ is made of a few main layers.

### 4.1 The lexer
The lexer reads raw text and turns it into tokens.

That happens in [npp/lexer.py](npp/lexer.py) and [npp/tokens.py](npp/tokens.py).

It recognizes things like:
- keywords such as `say`, `set`, `if`, `while`, `repeat`, `for`, `return`
- operators such as `+`, `-`, `==`, `>`, `<`
- English phrases such as `is greater than` and `is less than`
- strings, numbers, lists, blocks, and braces

### 4.2 The parser
The parser takes tokens and builds an abstract syntax tree (AST).

This is done in [npp/parser.py](npp/parser.py) and [npp/ast_nodes.py](npp/ast_nodes.py).

The parser decides:
- what is a statement
- what is a variable declaration
- what is a function definition
- what is a loop or conditional
- what is an expression

### 4.3 The interpreter
The interpreter executes the AST.

This happens in [npp/interpreter.py](npp/interpreter.py).

It handles:
- running statements in order
- evaluating expressions
- updating variables
- checking conditions
- looping
- calling functions
- returning values

### 4.4 The environment
Variable scope and lookup are handled in [npp/environment.py](npp/environment.py).

This keeps track of:
- current variables
- parent scopes
- constants
- function closures

### 4.5 Built-ins and standard library
Most built-in functions live in [npp/builtins.py](npp/builtins.py).

This file gives N++ things like:
- `say`
- `ask`
- `len`
- `range`
- `push`
- `pop`
- `type`
- `random_int`
- `hash_sha256`
- `uuid`
- `upper`, `lower`, `trim`, `split`
- web element constructors such as `div`, `p`, `button`, `form`, and many others

### 4.6 Errors and diagnostics
Errors are reported in [npp/errors.py](npp/errors.py).

They give helpful error messages with line and column numbers.

---

## 5) How the language is written

These are the key syntax patterns that beginners need to know.

### 5.1 Printing to the screen
```npp
say "Hello world!"
```

This is the simplest and most common command.

### 5.2 Variables
```npp
set score to 10
change score to 15
```

Or:

```npp
let name = "Alice"
const PI = 3.14
```

### 5.3 Input
```npp
set name to ask "What is your name? "
```

### 5.4 Conditionals
```npp
if score is greater than 10 then
    say "You win!"
otherwise
    say "Try again!"
end
```

### 5.5 Loops
```npp
repeat 3 times
    say "Hello"
end
```

```npp
set items to ["a", "b", "c"]
for each item in items
    say item
end
```

### 5.6 Functions
```npp
to add with a, b
    give back a + b
end

say add(2, 3)
```

Function definitions are created in the parser and executed by the interpreter.

### 5.7 Lists and maps
```npp
set nums to [1, 2, 3, 4]
set user to {"name": "Ava", "age": 20}

say nums[0]
say user["name"]
```

### 5.8 Concatenation and automatic conversions
N++ tries to be beginner-friendly. If you combine a string and a number, it often converts automatically:

```npp
set age to 21
say "I am " + age + " years old"
```

This prints:

```text
I am 21 years old
```

---

## 6) Beginner learning path

If you are new to programming, use this order:

1. Learn `say`
2. Learn `set` and `change`
3. Learn `ask`
4. Learn `if` and `otherwise`
5. Learn `repeat`
6. Learn `for each`
7. Learn functions
8. Learn lists and maps
9. Try the web features

A good first program is:

```npp
say "My first N++ program!"
set name to ask "What is your name? "
if name is not "" then
    say "Welcome, " + name + "!"
else
    say "You did not type a name."
end
```

---

## 7) Root-level files: what each file does

These are the top-level project files and what they are for.

### [README.md](README.md)
This is the main overview of the language. It explains what N++ is, the feature list, and how to get started.

### [INTRO.md](INTRO.md)
This is the short plain-English beginner intro. This is a good “first read” doc.

### [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
This is the beginner-focused walkthrough. It explains simple ideas like `say`, variables, loops, and functions using everyday analogies.

### [WEB_GUIDE.md](WEB_GUIDE.md)
This expands on the web engine and explains building pages using HTML-like elements and components.

### [SPEC.md](SPEC.md)
This is the technical specification. It describes grammar, tokens, structure, and syntax rules.

### [main.py](main.py)
This is the project entry point. It imports the CLI and starts the app.

### [npp.bat](npp.bat)
This is the Windows wrapper that runs Python with the project script. It is the easiest way to call the tool from a terminal or PowerShell.

### [play.bat](play.bat)
This is the master menu launcher. It opens a menu with tutorials, web previews, the REPL, and tests.

### [START_HERE.bat](START_HERE.bat)
This is the welcome launcher for new users. It gives an easy entry into tutorials and basics.

### [tutorial_beginner.bat](tutorial_beginner.bat)
This is a Windows launcher for the beginner tutorial flow.

### [tutorial_web.bat](tutorial_web.bat)
This runs the web-focused tutorial flow.

### [walkthrough_tour.bat](walkthrough_tour.bat)
This helps you explore the system and repo in a guided walk-through.

### [components_demo.html](components_demo.html)
This is a generated HTML demo of components built with the web engine.

### [showcase.html](showcase.html)
This is the generated showcase page for HTML5 tags and examples.

### [saas_landing.html](saas_landing.html)
This is a generated landing-page sample.

### [tutorial_page.html](tutorial_page.html)
This is a static HTML tutorial page preview.

### [examples](examples)
This folder contains real N++ scripts to study and run.

Examples:
- [examples/intro_basics.npp](examples/intro_basics.npp)
- [examples/simple_english.npp](examples/simple_english.npp)
- [examples/fizzbuzz.npp](examples/fizzbuzz.npp)
- [examples/fibonacci.npp](examples/fibonacci.npp)
- [examples/guided_tour.npp](examples/guided_tour.npp)
- [examples/web_all_html_tags.npp](examples/web_all_html_tags.npp)
- [examples/web_saas_landing.npp](examples/web_saas_landing.npp)

These are the best place to learn by reading real code.

### [syntaxes/npp.tmLanguage.json](syntaxes/npp.tmLanguage.json)
This adds VS Code syntax highlighting support for N++.

### [tests](tests)
Contains project validation tests.

- [tests/test_suite.py](tests/test_suite.py) checks the language itself
- [tests/test_web.py](tests/test_web.py) checks the web engine and HTML creation

### [tutorials](tutorials)
This contains interactive tutorial scripts.

- [tutorials/interactive_beginner.py](tutorials/interactive_beginner.py)
- [tutorials/interactive_walkthrough.py](tutorials/interactive_walkthrough.py)
- [tutorials/interactive_web.py](tutorials/interactive_web.py)

---

## 8) Package files inside [npp](npp)

### [npp/__init__.py](npp/__init__.py)
This exports the language interface and includes the core functions: `run_code` and `run_file`.

### [npp/lexer.py](npp/lexer.py)
Tokenizes the source into words, symbols, strings, and punctuation.

### [npp/tokens.py](npp/tokens.py)
Defines all token types and keyword mappings. This is where the language vocabulary lives.

### [npp/parser.py](npp/parser.py)
Builds the AST. This is where syntax rules are converted into structured program nodes.

### [npp/ast_nodes.py](npp/ast_nodes.py)
Defines the AST nodes: Program, Literal, BinaryOp, IfStmt, FunctionDef, etc.

### [npp/environment.py](npp/environment.py)
Handles variables, scoping, and closures.

### [npp/builtins.py](npp/builtins.py)
This is a massive central file for the N++ standard library. It includes:
- printing and input
- list operations
- math
- strings
- hashing and random values
- web tags like `div`, `section`, `button`, `img`, `table`, etc.

This is one of the most important files in the project.

### [npp/interpreter.py](npp/interpreter.py)
Executes the parsed program and handles runtime behavior.

### [npp/errors.py](npp/errors.py)
Contains the custom exceptions and error formatting logic.

### [npp/cli.py](npp/cli.py)
This is the command-line interface for:
- `run`
- `build`
- `serve`
- `test`
- `repl`

### [npp/web](npp/web)
This folder contains the web engine.

#### [npp/web/__init__.py](npp/web/__init__.py)
Exports all the web engine pieces.

#### [npp/web/html_tags.py](npp/web/html_tags.py)
Contains the full HTML5 tag catalog and attributes.

#### [npp/web/elements.py](npp/web/elements.py)
Defines the HTML element model and rendering logic.

#### [npp/web/components.py](npp/web/components.py)
Defines web component classes like:
- `Webpage`
- `Navbar`
- `Hero`
- `Card`
- `Grid`
- `Container`
- `Badge`
- `Alert`
- `PageFooter`

#### [npp/web/themes.py](npp/web/themes.py)
Defines the built-in visual themes such as dark, modern, glassmorphism, and cyberpunk.

#### [npp/web/server.py](npp/web/server.py)
Starts the local HTTP server with automatic browser launch.

---

## 9) The web engine: how to use it

This is one of the coolest parts of N++.

### Basic web page
```npp
set page to webpage("My App", "dark")
page.add(h1("Hello from N++"))
render_html(page)
```

Or helper style:

```npp
set page to webpage("My App", "dark")
hero("Welcome", "Build amazing experiences")
page.add(card("Feature 1", "Easy to use"))
export_html("index.html", page)
```

### Why this matters
Instead of writing:
- HTML
- CSS
- JavaScript
- page structure
- theme layering

You can build a webpage using simple code and component helpers.

### Example website code
```npp
set page to webpage("My App", "glassmorphism")
page.add(navbar("Nova", [{"About": "#about"}, {"Features": "#features"}], "Get Started", "#"))
page.add(hero("Build Faster with N++", "Plain English web programming.", "Try It Now", "#"))

set c1 to card("Fast", "Write code quickly", "⚡")
set c2 to card("Clear", "Easy to understand", "🧠")
set c3 to card("Modern", "Beautiful UI", "✨")

page.add(grid(3, [c1, c2, c3]))
render_html(page)
```

---

## 10) Best places to learn from the repo

If you are a beginner, these are the best files to read in order:

1. [INTRO.md](INTRO.md)
2. [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
3. [examples/intro_basics.npp](examples/intro_basics.npp)
4. [examples/simple_english.npp](examples/simple_english.npp)
5. [examples/fizzbuzz.npp](examples/fizzbuzz.npp)
6. [WEB_GUIDE.md](WEB_GUIDE.md)
7. [examples/web_saas_landing.npp](examples/web_saas_landing.npp)
8. [SPEC.md](SPEC.md)

That path gives you a practical beginner reading order.

---

## 11) Beginner workflow for making your own project

Use this exact workflow:

1. Open a new file like `my_program.npp`
2. Start with `say` and `set`
3. Add a condition
4. Add a loop
5. Add a function
6. Run it with:

```powershell
python main.py my_program.npp
```

Example:

```npp
say "My first project"
set total to 0
repeat 5 times
    total += 1
end
say "Total: " + total
```

---

## 12) Troubleshooting

### Problem: script will not run
Check that your file exists and that the command path is correct.

Example:

```powershell
python main.py examples\intro_basics.npp
```

### Problem: syntax error
Look at the line and column in the error. The project includes line-aware diagnostics in [npp/errors.py](npp/errors.py).

### Problem: you do not know what file to open
Start with:
- [INTRO.md](INTRO.md)
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
- [examples/intro_basics.npp](examples/intro_basics.npp)

### Problem: you want to build a web page
Read:
- [WEB_GUIDE.md](WEB_GUIDE.md)
- [examples/web_all_html_tags.npp](examples/web_all_html_tags.npp)
- [examples/web_saas_landing.npp](examples/web_saas_landing.npp)

---

## 13) Final beginner summary

N++ is a language that tries to feel close to English while still being a real programming language.

At the project level:
- [main.py](main.py) starts the app
- [npp/cli.py](npp/cli.py) handles commands
- [npp/lexer.py](npp/lexer.py) reads text
- [npp/parser.py](npp/parser.py) builds program structure
- [npp/interpreter.py](npp/interpreter.py) runs it
- [npp/builtins.py](npp/builtins.py) provides the language features
- [npp/web](npp/web) provides the web engine

Think of it like this:
- the docs teach you the language
- the examples show you the language in use
- the parser and interpreter explain how the language actually works
- the web engine turns N++ into HTML output

That is the full beginner picture.

---

## 14) Where to go next

Try these next:

- run [examples/intro_basics.npp](examples/intro_basics.npp)
- open [INTRO.md](INTRO.md)
- open [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
- run the REPL with `python main.py repl`
- try a simple web page using the examples in [examples/web_saas_landing.npp](examples/web_saas_landing.npp)

Once you are comfortable, read [SPEC.md](SPEC.md) and then look directly into [npp](npp) files to see the real implementation.

That is the best path from beginner to confident user.
