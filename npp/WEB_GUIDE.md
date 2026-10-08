# N++ Web Engine Guide: The Evolution of HTML 🌐

> **Build responsive, modern web applications in plain English. No messy closing tags, zero CSS framework dependencies, and 100% standard HTML5 output.**

---

## ⚡ Why N++ is 1000x Better than HTML

| Feature | Old-Fashioned HTML + CSS | N++ Web Engine |
|:---|:---|:---|
| **Syntax** | Verbose `<tag attr="..."></tag>` with unclosed tag bugs | Clean, natural English function and block syntax |
| **Styling** | Requires Tailwind, Bootstrap, or separate 1,000-line CSS files | Built-in modern themes (`dark`, `modern`, `glassmorphism`, `cyberpunk`) |
| **Logic + Layout** | Split across `.html`, `.css`, and `.js` files | Single unified language for backend logic, loops, and layout |
| **Responsive Grid** | Complex CSS Flex/Grid setup | Simple `grid(3, [card1, card2, card3])` |
| **Local Server** | Requires Node.js, `npm install`, Vite, or live-server | Built-in zero-dependency server: `npp serve app.npp` |

---

## 🚀 Quick Example: Building a Website in 10 Lines

```npp
// 1. Create a page with the modern dark theme
set page to webpage("My App", "dark")

// 2. Add an instant responsive navigation bar
navbar("Nova", [{"About": "#about"}, {"Features": "#features"}], "Get Started", "#")

// 3. Add a Hero Banner
hero("Build Faster with N++", "The plain English language that replaces HTML.", "Try It Now", "#")

// 4. Add a Responsive 3-Column Card Grid
set c1 to card("All HTML5 Tags", "Every official tag and attribute supported.", "🌐")
set c2 to card("Zero Setup", "No npm, no external css required.", "⚡")
set c3 to card("Instant Server", "Embedded server with auto-browser launch.", "🚀")

page.add(grid(3, [c1, c2, c3]))

// 5. Export to a standalone HTML5 file
export_html("index.html", page)
```

To compile and preview in your browser:
```powershell
.\npp.bat examples\web_saas_landing.npp
```
Or start the live server:
```powershell
python main.py serve examples\web_saas_landing.npp 8080
```

---

## 📋 Comprehensive HTML5 Tag Support (110+ Official Tags)

N++ provides native constructors for **every official HTML5 tag**, accepting both text content and full attribute maps:

### 1. Document Structure & Layout
* `header(...)`, `footer(...)`, `nav(...)`, `main(...)`, `section(...)`, `article(...)`, `aside(...)`, `div(...)`, `span(...)`
* `hr()`, `br()`

### 2. Headings & Typography
* `h1(...)`, `h2(...)`, `h3(...)`, `h4(...)`, `h5(...)`, `h6(...)`
* `p(...)`, `blockquote(...)`, `pre(...)`, `code(...)`, `kbd(...)`, `samp(...)`
* `strong(...)`, `em(...)`, `mark(...)`, `small(...)`, `sub(...)`, `sup(...)`, `i(...)`, `b(...)`, `u(...)`

### 3. Links & Navigation
```npp
set my_link to a("Visit GitHub", {"href": "https://github.com", "target": "_blank", "rel": "noopener"})
```

### 4. Tables
* `table(...)`, `thead(...)`, `tbody(...)`, `tfoot(...)`, `tr(...)`, `th(...)`, `td(...)`
```npp
set t to table()
set row to tr()
row.add(th("Product"))
row.add(th("Price"))
t.add(row)
```

### 5. Complete Forms & Inputs
Supports all input types and attributes (`type`, `placeholder`, `required`, `value`, `name`, `id`, `disabled`, `readonly`):
* `form(...)`, `label(...)`, `input(...)`, `textarea(...)`, `select(...)`, `option(...)`, `button(...)`
* `progress(...)`, `meter(...)`, `fieldset(...)`, `legend(...)`
```npp
set f to form({"action": "/login", "method": "post"})
f.add(label("Email:", {"for": "user_email"}))
f.add(input({"type": "email", "id": "user_email", "name": "email", "placeholder": "you@example.com", "required": true}))
f.add(button("Sign In", {"type": "submit", "class": "npp-button"}))
```

### 6. Embedded Media
* `img(...)`, `video(...)`, `audio(...)`, `source(...)`, `iframe(...)`, `picture(...)`, `canvas(...)`, `svg(...)`
```npp
set banner to img({"src": "https://picsum.photos/800/400", "alt": "Scenic View", "width": 800})
```

### 7. Interactive Elements
* `details(...)`, `summary(...)`, `dialog(...)`
```npp
set faq to details()
faq.add(summary("How does N++ work?"))
faq.add(p("It runs with a Python tree-walk engine and outputs pure semantic HTML5!"))
```

---

## 🎨 Built-in Visual Themes

Change your site's entire aesthetic with a single parameter:
```npp
set page to webpage("My App", "glassmorphism")
```

Available theme presets:
1. `"dark"`: Obsidian background with indigo/neon accents and slate borders (Default).
2. `"modern"`: Crisp clean white/gray background with vibrant violet primary buttons.
3. `"glassmorphism"`: Deep midnight gradient with frosted glass cards (`backdrop-filter: blur(16px)`).
4. `"cyberpunk"`: High-contrast dark theme with neon yellow, cyan, and hot pink accents.

---

## 🧩 High-Level Components

* `navbar(brand, links, cta_text, cta_link)`: Sticky responsive navigation bar.
* `hero(title, subtitle, button_text, button_link)`: Large top banner with gradients.
* `card(title, description, icon, image, badge, btn_text, btn_link)`: Styled container card.
* `grid(columns, items)`: Auto-responsive CSS grid (1 to 4 columns).
* `container(items)`: Centered layout wrapper with maximum width and padding.
* `badge(text)`: Pill tag for status and categories.
* `alert(message)`: Highlighted notification banner.
* `page_footer(text)`: Responsive footer.
