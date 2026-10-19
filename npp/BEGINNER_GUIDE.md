# The Complete Beginner's Guide to N++ 🌟

> **Never coded before? Perfect. This guide is made for you.**
> N++ lets you write code that reads like plain English — and it can build
> stunning, fully interactive websites without touching HTML, CSS, or JavaScript.

---

## 🚀 How to Launch N++ (Pick Any Method)

### 🏆 Method 1 — Easiest: Double-Click `START_HERE.bat`

1. Open the N++ folder:
   ```
   C:\Users\kulka\.gemini\antigravity\scratch\npp
   ```
2. Double-click **`START_HERE.bat`**.
3. A friendly menu appears:

   ```
   ===============================================================================
                               WELCOME TO N++!
              The Programming Language That Reads Like Plain English
                        And Builds Webpages Better Than HTML
   ===============================================================================

     [1] Beginner Interactive Tutorial  — Learn N++ step-by-step from scratch
     [2] Web Engine Interactive Tutorial — Learn to build websites 1000x faster
     [3] System Walkthrough Tour        — Explore architecture, tests and files
     [4] Code Tester / REPL Sandbox     — Type English code live and test scripts
     [5] Launch Master Hub (play.bat)   — Access all tools, servers and scripts
     [6] Exit
   ```

4. Press **`1`** → Enter to start the beginner tutorial!

---

### 🧪 Method 2 — Code Tester: Double-Click `npp.bat`

The interactive code tester. Pick from 8 options:

| Option | What it does |
|--------|-------------|
| `[1]`  | **Live REPL** — type English code directly, see results instantly |
| `[2]`  | Run `examples\intro_basics.npp` |
| `[3]`  | Run `examples\guided_tour.npp` |
| `[4]`  | Run all automated tests and see pass/fail report |
| `[5]`  | Build HTML5 Web Showcase (`examples\web_all_html_tags.npp`) |
| `[6]`  | Build SaaS Landing Page (`examples\web_saas_landing.npp`) |
| `[7]`  | Quick-test: type a single line of English code |
| `[8]`  | Run any `.npp` file you choose |

> **Tip:** It never immediately closes when double-clicked — it always returns to the menu so you can see your results.

---

### 🎮 Method 3 — Master Hub: Double-Click `play.bat`

All tools in one place:

| Option | What it does |
|--------|-------------|
| `[1]`  | Beginner Interactive Tutorial |
| `[2]`  | Web Engine Interactive Tutorial |
| `[3]`  | System Walkthrough Tour |
| `[4]`  | Build and preview HTML5 Showcase (`showcase.html`) |
| `[5]`  | Build and preview SaaS Landing Page (`saas_landing.html`) |
| `[6]`  | Build and preview Analytics Dashboard (`dashboard.html`) |
| `[7]`  | Start the embedded local web server on port 8080 |
| `[8]`  | Live REPL — type and run English code |
| `[9]`  | Run all automated unit tests |

---

### 💻 Method 4 — PowerShell / Terminal

```powershell
cd C:\Users\kulka\.gemini\antigravity\scratch\npp

# Run any example
python main.py run examples\intro_basics.npp
python main.py run examples\calculator.npp

# Start the live REPL
python main.py repl

# Run all tests
python main.py test

# Compile an N++ web script to HTML
python main.py build examples\interactive_dashboard.npp
```

---

## 🧠 The Language in Plain English

### 1. Print something to the screen — `say`

```npp
say "Hello, world!"
say "Welcome to N++!"
```

Anything inside `"quotes"` is text (called a **String**). `say` is an alias for `print` — both work.

---

### 2. Remember things — `set ... to ...`

```npp
set score to 100
set player_name to "Hero"
say "Player: " + player_name + " — Score: " + score
```

Update a variable later with `change`:

```npp
change score to 150
say "New score: " + score
```

You can also use `let` or `const` style:

```npp
let x = 42
const TAX = 0.15
```

---

### 3. Ask the user a question — `ask`

```npp
set name to ask "What is your name? "
say "Great to meet you, " + name + "!"
```

---

### 4. Make decisions — `if` / `otherwise`

```npp
set temperature to 28

if temperature is greater than 30 then
    say "It is very hot! Stay hydrated."
otherwise if temperature is less than 15 then
    say "It is chilly! Grab a warm coat."
otherwise
    say "The weather is pleasant."
end
```

Every decision block ends with **`end`**.

#### Comparison phrases:

| Phrase | Meaning |
|--------|---------|
| `is` | Equal to |
| `is not` | Not equal to |
| `is greater than` | More than |
| `is less than` | Less than |
| `is at least` | Greater than or equal |
| `is at most` | Less than or equal |

---

### 5. Repeat something — `repeat ... times`

```npp
repeat 3 times
    say "Hip Hip Hooray!"
end
```

---

### 6. Loop over a list — `for each`

```npp
set favorites to ["Pizza", "Tacos", "Ice Cream"]

for each food in favorites
    say "I love: " + food
end
```

---

### 7. Define a function — `to ... with ...`

```npp
to calculate_total with price, tax_rate
    give back price + (price * tax_rate)
end

set total to calculate_total(100, 0.15)
say "Total: " + total
```

Use `give back` to return a value from any function.

---

### 8. Working with lists and maps

```npp
// Lists (ordered collections)
set nums to [1, 2, 3, 4]
say nums[0]              // prints 1

push(nums, 5)            // add 5 to the end
say len(nums)            // prints 5

// Maps (key-value pairs, like a dictionary)
set user to {"name": "Ava", "age": 20}
say user["name"]         // prints Ava
```

---

## 📐 Built-in Functions You Can Use

### Math

| Function | What it does | Example |
|----------|-------------|---------|
| `abs(n)` | Absolute value | `abs(-5)` → `5` |
| `round(n, d)` | Round to d decimal places | `round(3.789, 2)` → `3.79` |
| `floor(n)` | Round down | `floor(4.9)` → `4` |
| `ceil(n)` | Round up | `ceil(4.1)` → `5` |
| `sqrt(n)` | Square root | `sqrt(144)` → `12` |
| `min(a, b)` | Smallest value | `min(3, 7)` → `3` |
| `max(a, b)` | Largest value | `max(3, 7)` → `7` |
| `sum(list)` | Total of a list | `sum([1,2,3])` → `6` |
| `average(list)` | Mean of a list | `average([2,4,6])` → `4` |
| `clamp(v, mn, mx)` | Keep value within range | `clamp(150, 0, 100)` → `100` |
| `sin(n)` | Sine | `sin(0)` → `0` |
| `cos(n)` | Cosine | `cos(0)` → `1` |
| `pi()` | Pi constant | `pi()` → `3.14159...` |
| `random()` | Random 0.0–1.0 | `random()` |
| `random_int(a, b)` | Random integer between a and b | `random_int(1, 6)` |
| `random_choice(list)` | Pick a random item | `random_choice(["a","b","c"])` |

---

### Strings

| Function | What it does | Example |
|----------|-------------|---------|
| `upper(s)` | Uppercase | `upper("hello")` → `"HELLO"` |
| `lower(s)` | Lowercase | `lower("HELLO")` → `"hello"` |
| `trim(s)` | Remove extra spaces | `trim("  hi  ")` → `"hi"` |
| `split(s, d)` | Split into a list | `split("a,b,c", ",")` → `["a","b","c"]` |
| `join(list, d)` | Join list into a string | `join(["a","b"], "-")` → `"a-b"` |
| `replace(s, old, new)` | Replace text | `replace("hi world", "world", "N++")` |
| `contains(s, x)` | Check if something is inside | `contains("hello", "ell")` → `true` |
| `len(s)` | Character count | `len("hello")` → `5` |

---

### Lists

| Function | What it does |
|----------|-------------|
| `push(list, item)` | Add item to end |
| `pop(list)` | Remove and return last item |
| `len(list)` | Number of items |
| `range(n)` | Generate `[0, 1, 2, ... n-1]` |
| `range(a, b)` | Generate `[a, a+1, ..., b-1]` |
| `sum(list)` | Add all numbers |
| `min(list)` | Smallest item |
| `max(list)` | Largest item |
| `average(list)` | Mean of all items |
| `random_choice(list)` | Pick a random item |

---

### Types and Conversions

| Function | What it does |
|----------|-------------|
| `type(x)` | Returns `"number"`, `"string"`, `"list"`, `"map"`, etc. |
| `str(x)` / `text(x)` | Convert to string |
| `num(x)` / `number(x)` | Convert to number |
| `bool(x)` | Convert to true/false |

---

### File and System

| Function | What it does |
|----------|-------------|
| `read_file(path)` | Read a text file |
| `write_file(path, text)` | Write to a file (overwrites) |
| `append_file(path, text)` | Add text to a file |
| `file_exists(path)` | Returns true if file exists |
| `list_files(dir)` | List files in a directory |
| `sleep(seconds)` | Pause for N seconds |
| `clock()` / `time()` | Current Unix timestamp |
| `uuid()` | Generate a unique ID |
| `hash_sha256(text)` | Hash a string securely |
| `hash_md5(text)` | Hash a string (fast) |

---

### Data

| Function | What it does |
|----------|-------------|
| `to_json(obj)` | Convert to JSON string |
| `from_json(text)` | Parse JSON string into a map/list |
| `http_get(url)` | Fetch text from a URL |
| `fetch(url)` | Same as http_get |
| `http_post(url, data)` | POST JSON data to a URL |

---

## 🌐 Building Interactive Websites with N++

N++ includes a **full web engine** that outputs standalone HTML files — no CDN, no external CSS, no framework. Everything is embedded.

### The 4 available themes:
- `"dark"` — Sleek dark background, vibrant colors
- `"modern"` — Clean white professional look
- `"glassmorphism"` — Frosted glass visual style
- `"cyberpunk"` — Neon, electric, futuristic

### Your first website (5 lines):

```npp
set page to webpage("My First Site", "dark")
navbar("MyBrand", [{"Home": "#"}, {"About": "#"}], "Sign Up", "#")
hero("Hello from N++!", "Built with plain English code.", "Get Started", "#")
page_footer("Made with N++ in 5 lines")
export_html("my_site.html", page)
```

Run it with:
```powershell
python main.py build examples\web_saas_landing.npp
```

Then open `my_site.html` in your browser!

---

### All Built-in Web Components

#### Page structure

| Function | What it creates |
|----------|----------------|
| `webpage(title, theme)` | Creates a new web document |
| `export_html(file, page)` | Saves the page as a standalone HTML file |
| `render_html(page)` | Returns the HTML as a string |

#### Layout and Navigation

| Function | What it creates |
|----------|----------------|
| `navbar(brand, links, cta_text, cta_link)` | Sticky navigation bar |
| `hero(title, subtitle, btn_text, btn_link)` | Full-width animated banner |
| `grid(columns, [items])` | Multi-column responsive grid |
| `container([items])` | Centered content wrapper |
| `page_footer(text)` | Site footer |

#### Content

| Function | What it creates |
|----------|----------------|
| `card(title, desc, icon, image, badge, btn_text, btn_link)` | Feature card |
| `badge(text)` | Small highlight pill |
| `alert(message)` | Notification/info box |

#### Interactive Components (NEW in v2.0)

| Function | What it creates |
|----------|----------------|
| `stat_counter(target, label, icon)` | Animated number that counts up on scroll |
| `progress_bar(value, label)` | Animated fill bar showing a percentage |
| `modal(id, title, content, close_text)` | Popup dialog overlay |
| `accordion(items)` | Expandable question/answer list |
| `typewriter(text, tag)` | Text that types itself on screen |

---

### Interactive Website Example

```npp
set page to webpage("My Dashboard", "cyberpunk")

navbar("Analytics Hub", [{"Home": "#"}, {"Reports": "#"}], "Export", "#")
hero("Live Analytics", "Real-time insights powered by N++", "View Now", "#")

// Animated stat counters
set users_count to stat_counter(48200, "Active Users", "👥")
set revenue_count to stat_counter(1240000, "Revenue Generated", "💰")
set uptime_count to stat_counter(99.98, "Uptime Percent", "⚡")
page.add(grid(3, [users_count, revenue_count, uptime_count]))

// Animated progress bars
set speed_bar to progress_bar(98, "Performance Score")
set security_bar to progress_bar(95, "Security Score")
page.add(container([speed_bar, security_bar]))

// Accordion FAQ
set faq to accordion([
    ["How do I start?", "Double-click START_HERE.bat to launch the interactive menu."],
    ["Can I build real websites?", "Yes! N++ outputs standalone HTML you can host anywhere."],
    ["Is it free?", "Completely free and open. Zero external dependencies."]
])
page.add(faq)

// Typing headline
page.add(typewriter("Welcome to the Future of Coding", "h2"))

// Popup dialog
modal("info_modal", "About N++", "A language that reads like English and compiles to beautiful HTML.")

page_footer("Powered by N++ — zero HTML needed")
export_html("dashboard.html", page)
```

Open the result in any browser — it's fully interactive with no server needed.

---

### Every HTML5 Tag is Also Available

N++ maps every standard HTML5 tag as a direct function:

```npp
set page to webpage("Raw HTML Power", "modern")
page.add(h1("Big Headline"))
page.add(p("A paragraph of text."))
page.add(div([
    h2("Subheading"),
    p("More content here"),
    ul([
        li("Item one"),
        li("Item two"),
        li("Item three")
    ])
]))
page.add(button("Click me"))
page.add(img({"src": "photo.jpg", "alt": "A photo"}))
export_html("page.html", page)
```

Available HTML5 tags include: `div`, `p`, `h1`–`h6`, `span`, `ul`, `ol`, `li`,
`table`, `tr`, `td`, `th`, `form`, `input`, `button`, `a`, `img`, `video`, `audio`,
`section`, `article`, `header`, `footer`, `nav`, `aside`, `main`, `canvas`,
`svg`, `iframe`, `details`, `summary`, and 80+ more.

---

## 📁 Example Scripts to Explore

All examples are in the `examples/` folder:

| File | What it demonstrates |
|------|---------------------|
| `intro_basics.npp` | Variables, printing, loops, if/else |
| `simple_english.npp` | Core syntax in natural English |
| `fizzbuzz.npp` | Classic FizzBuzz logic |
| `fibonacci.npp` | Recursive functions and sequences |
| `guided_tour.npp` | Step-by-step walkthrough |
| `calculator.npp` | Functions, math, user input |
| `interactive_dashboard.npp` | Full analytics dashboard website |
| `web_all_html_tags.npp` | Every HTML5 tag demonstrated |
| `web_saas_landing.npp` | Complete SaaS landing page |

To run any of them:
```powershell
python main.py run examples\calculator.npp
python main.py build examples\interactive_dashboard.npp
```

Or use `npp.bat` option `[8]` to pick any file interactively.

---

## 🧪 Running the Test Suite

N++ has an automated test suite. To run it:

```powershell
python main.py test
```

Or via `npp.bat` → option `[4]`.

All 12 core language tests + 9 web engine tests run and should all pass.

---

## 🗂️ File Overview (What Does What)

| File | Purpose |
|------|---------|
| `START_HERE.bat` | Entry menu for new users |
| `npp.bat` | Code tester + REPL launcher |
| `play.bat` | Master hub for all tools |
| `tutorial_beginner.bat` | Launches the beginner tutorial |
| `tutorial_web.bat` | Launches the web engine tutorial |
| `walkthrough_tour.bat` | Guided system exploration tour |
| `main.py` | CLI entry point |
| `BEGINNER_GUIDE.md` | This file! |
| `BEGINNER_FULL_GUIDE.md` | Deep-dive guide (every file explained) |
| `WEB_GUIDE.md` | Full web engine reference |
| `MANUAL.md` | Exhaustive technical manual |
| `README.md` | Technical reference |
| `SPEC.md` | Language grammar specification |
| `npp/` | Core language engine |
| `npp/web/` | Web compiler and components |
| `examples/` | Ready-to-run N++ programs |
| `tutorials/` | Interactive Python-based tutorials |
| `tests/` | Automated test suite |

---

## 📚 Where to Go Next

1. **Run your first script:** Double-click `START_HERE.bat` → press `1`
2. **Experiment live:** Double-click `npp.bat` → press `1` for the REPL
3. **Build a website:** Double-click `play.bat` → press `5` or `6`
4. **Read the web guide:** Open `WEB_GUIDE.md`
5. **Study examples:** Browse the `examples/` folder
6. **See every component:** Open `components_demo.html` in your browser
7. **Deep dive:** Read `BEGINNER_FULL_GUIDE.md` for a file-by-file breakdown
