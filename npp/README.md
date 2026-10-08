# N++ Programming Language & Web Engine

**N++** is a modern, expressive text-based programming language designed so that writing code and **building web applications** feels just like writing simple English sentences — making web development **1000x cleaner, faster, and better than HTML**.

---

## Highlights

- **Revolutionary Web Engine**: Build complete, responsive websites in plain English. Generates standalone HTML5 + CSS with zero external dependencies.
- **Complete HTML5 Tag Catalog**: Supports all 110+ official HTML5 tags (`h1`-`h6`, `div`, `span`, `form`, `input`, `table`, `video`, `details`, etc.) and arbitrary HTML attributes.
- **Embedded Web Server**: Zero-setup local development server (`npp serve app.npp`) with automatic browser launch.
- **Modern Theme Presets**: Built-in visual themes (`dark`, `modern`, `glassmorphism`, `cyberpunk`) with Google Fonts and responsive layouts.
- **High-Level UI Components**: Instant `navbar`, `hero`, `card`, `grid`, `badge`, `alert`, and `footer` components.
- **Supercharged Standard Library**: File System I/O (`read_file`, `write_file`), HTTP requests (`http_get`, `http_post`), JSON parsing, UUIDs, crypto hashing, and advanced math.
- **Object Member Access & Method Calls**: Clean dot syntax (`page.add(...)`, `item.render()`, `map.key`).
- **Zero Dependencies**: Pure standard Python 3 runtime; runs out-of-the-box on Windows, macOS, and Linux.
- **Editor Support**: TextMate grammar included for VS Code syntax highlighting (`syntaxes/npp.tmLanguage.json`).

---

## Directory Structure

```
npp/
├── BEGINNER_GUIDE.md       # Step-by-step beginner guide with everyday analogies
├── WEB_GUIDE.md            # Comprehensive Web Engine & HTML5 tag documentation
├── INTRO.md                # Quickstart & Plain English cheat sheet
├── README.md               # Main repository documentation
├── SPEC.md                 # Language grammar and technical specification
├── main.py                 # CLI entry point
├── play.bat                # 1-click interactive menu launcher
├── npp.bat                 # Windows CLI wrapper
├── npp/                    # Core language & web engine
│   ├── __init__.py         # Package exports
│   ├── tokens.py           # Token types & keywords
│   ├── lexer.py            # Tokenizer with English phrase recognition
│   ├── ast_nodes.py        # AST nodes with MemberAccess & MethodCall
│   ├── parser.py           # Precedence parser with multiline expressions
│   ├── environment.py      # Lexical scoping & closures
│   ├── builtins.py         # Standard library + 110+ HTML5 tag constructors
│   ├── interpreter.py      # Evaluator with DOM and object method calling
│   ├── errors.py           # Contextual diagnostics with visual carets
│   ├── cli.py              # CLI with run, build, serve, repl, test
│   └── web/                # Web engine package
│       ├── __init__.py     # Web engine exports
│       ├── html_tags.py    # Complete catalog of HTML5 tags & attributes
│       ├── elements.py     # HTMLElement DOM node & tree renderer
│       ├── themes.py       # Modern CSS stylesheet & theme presets
│       ├── components.py   # High-level components (Navbar, Hero, Card, Grid)
│       └── server.py       # Embedded development HTTP server
├── syntaxes/
│   └── npp.tmLanguage.json # VS Code TextMate syntax grammar
├── examples/               # Sample N++ scripts & web apps
│   ├── web_all_html_tags.npp # Complete HTML5 tags & components showcase
│   ├── web_saas_landing.npp  # High-converting SaaS landing page
│   ├── guided_tour.npp       # Interactive step-by-step tour
│   ├── intro_basics.npp      # Beginner basics
│   ├── simple_english.npp    # Plain English weather & grocery cart
│   ├── fizzbuzz.npp          # FizzBuzz algorithm
│   └── fibonacci.npp         # Recursive Fibonacci sequence
└── tests/
    ├── test_suite.py       # Core language unit tests
    └── test_web.py         # Web engine & HTML5 tag unit tests
```

---

## New: Full Beginner Manual

If you want the complete beginner walkthrough for the whole project and each file, see [BEGINNER_FULL_GUIDE.md](BEGINNER_FULL_GUIDE.md).

## Quickstart

### Running an N++ Script
On Windows:
```powershell
.\npp.bat examples\intro_basics.npp
```
Or directly with Python:
```powershell
python main.py examples\intro_basics.npp
```

### Starting the Interactive REPL
```powershell
.\npp.bat repl
```

Inside the REPL:
```
n++> say "Welcome!"
Welcome!

n++> set x to 10
n++> set y to 25
n++> x + y
=> 35

n++> repeat 3 times say "Hi!" end
Hi!
Hi!
Hi!
```

### Running the Test Suite
```powershell
.\npp.bat test
```

---

## Syntax Overview

### Output & Input
```npp
say "Hello world!"
set name to ask "What is your name? "
```

### Variables
```npp
set score to 100
change score to 150

// Or standard programming style:
let x = 10
const PI = 3.14159
```

### Conditionals
```npp
if score is greater than 100 then
    say "Champion!"
otherwise if score is 100 then
    say "Century!"
otherwise
    say "Keep going!"
end
```

### Loops
```npp
repeat 3 times
    say "Cheers!"
end

for each fruit in ["apple", "banana", "orange"]
    say "Fruit: " + fruit
end

set i to 0
while i is less than 5
    i += 1
end
```

### Functions
```npp
to multiply with a, b
    give back a * b
end

say multiply(4, 5)
```
*(Also supports `fn multiply(a, b) { return a * b }`)*
