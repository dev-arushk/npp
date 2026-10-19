# N++ Web Engine Guide: The Evolution of HTML 🌐

> **Build responsive, modern, interactive web applications in plain English. No messy closing tags, zero CSS framework dependencies, 17 built-in interactive systems, and 100% standard HTML5 output.**

---

## ⚡ Why N++ is 1000x Better than HTML

| Feature | Old-Fashioned HTML + CSS | N++ Web Engine |
|:---|:---|:---|
| **Syntax** | Verbose `<tag attr="..."></tag>` with unclosed tag bugs | Clean, natural English function and block syntax |
| **Styling** | Requires Tailwind, Bootstrap, or separate 1,000-line CSS files | 4 built-in modern themes (`dark`, `modern`, `glassmorphism`, `cyberpunk`) |
| **Interactivity** | Requires heavy frameworks (React, Vue) or npm bundlers | 17 built-in interactive systems with zero external JS dependencies |
| **Components** | Hundreds of divs needed for modals, accordions, and tabs | 1-line native components: `stat_counter()`, `modal()`, `accordion()`, `progress_bar()` |
| **Responsive Grid** | Complex CSS Flex/Grid setup | Simple `grid(3, [card1, card2, card3])` |
| **Local Server** | Requires Node.js, `npm install`, Vite, or live-server | Built-in zero-dependency server: `python main.py serve app.npp` |

---

## 🚀 Quick Example: Building an Interactive Web App in 10 Lines

```npp
// 1. Create a page with the modern glassmorphism theme
set page to webpage("Apex Dashboard", "glassmorphism")

// 2. Add an instant responsive navigation bar with live theme switcher
navbar("Apex.io", [{"Features": "#features"}, {"Metrics": "#metrics"}], "Deploy Cluster ⚡", "#deploy")

// 3. Add a Hero Banner with Typewriter effect
hero("Autonomous Edge Cloud", "Stream telemetry across 40 regions in realtime.", "Explore Nodes", "#metrics")

// 4. Add 1-line interactive components!
set c1 to stat_counter(99999, "Requests / Sec", "⚡")
set c2 to stat_counter(40, "Edge Clusters", "🌐")
set c3 to progress_bar(96, "Overall Health SLA")

page.add(grid(3, [c1, c2, c3]))

// 5. Add an expandable FAQ accordion
set faq to accordion([
    ["How is this generated?", "Compiled in 0.01 seconds from pure N++ English code!"],
    ["Does it have dependencies?", "Zero! Pure HTML5, CSS, and standalone JS runtime."]
])
page.add(faq)

// 6. Export to production HTML!
export_html("index.html", page)
```

To view it:
* Double-click **`play.bat`** and pick option **`[6]`** to build and preview, or option **`[7]`** for the local dev server!

---

## 🧩 High-Level Interactive Components

N++ provides native high-level components that compile into responsive, animated UI elements:

### 1. `stat_counter(target, label, icon)`
Creates an animated numeric metric card. When scrolled into view, the number smoothly counts up from 0 to the target:
```npp
set metric to stat_counter(25000, "Active Developers", "🚀")
```

### 2. `progress_bar(value, label)`
Creates an animated progress meter displaying the label and percentage:
```npp
set pb to progress_bar(95, "Server Uptime SLA")
```

### 3. `modal(modal_id, title, content, close_text)`
Creates a popup modal dialog that automatically wires up open/close triggers, background overlay dismissal, and the ESC key:
```npp
modal("demo-modal", "Welcome to N++", "Building websites has never been this easy!", "Got It!")
```
To trigger the modal from any button:
```npp
button("Open Modal", {"class": "npp-button", "data-npp-modal": "demo-modal"})
```

### 4. `accordion(items)`
Creates an expandable/collapsible FAQ accordion from a list of `[title, body]` pairs:
```npp
set faqs to accordion([
    ["What is N++?", "A programming language that reads like English."],
    ["Can I build websites?", "Yes! Faster and cleaner than raw HTML."]
])
page.add(faqs)
```

### 5. `typewriter(text, tag)`
Creates an animated heading that types itself out automatically on screen:
```npp
set title to typewriter("Planetary Scale Realtime Intelligence", "h1")
page.add(title)
```

### 6. Standard Layout Components:
* **`navbar(brand, links, cta_text, cta_link)`**: Responsive sticky navigation bar with auto-injected theme switcher.
* **`hero(title, subtitle, button_text, button_link)`**: High-impact top banner with gradient accents.
* **`card(title, description, icon, image, badge, btn_text, btn_link)`**: Elevated content card.
* **`grid(columns, items)`**: Responsive 1, 2, 3, or 4 column grid.
* **`container(items)`**: Centered layout wrapper.
* **`badge(text)`**: Pill tag for statuses and tags.
* **`alert(message)`**: Highlighted notification banner.
* **`page_footer(text)`**: Standard responsive footer.

---

## ⚡ The 17 Built-in Interactive Systems (Runtime v2.0)

Every webpage exported by N++ automatically embeds the **N++ Interactive Web Runtime v2.0**. This gives your websites rich client-side interactivity with **zero npm packages and zero external script tags**:

1. **Toast Notification System**: Call `nppToast("Success!", "success")` anytime.
2. **Modal System**: Open modals via `data-npp-modal="modal_id"` with auto-close on backdrop click or ESC key.
3. **Tab Switcher**: Seamless tab switching with `.npp-tab-button` and `.npp-tab-panel`.
4. **Accordion FAQ System**: Expand and collapse panels smoothly with animated chevron arrows.
5. **Scroll Animated Stat Counters**: Any element with `data-npp-count="1000"` counts up automatically when visible.
6. **Live Search Filtering**: Add `data-npp-filter=".card-item"` to any input to filter items in real-time.
7. **Animated Progress Bars**: Bars with `data-value="85"` smoothly animate their width.
8. **Typewriter Animation**: Any element with `data-npp-type="..."` types out its text character-by-character.
9. **Hover Tooltips**: Add `data-npp-tip="Help text"` to any element for instant tooltips.
10. **Scroll Reveal Animations**: Elements with `data-npp-reveal="true"` fade and slide in on scroll.
11. **Button Ripple Effect**: Modern Material-style ripple wave on every `.npp-button` click.
12. **Floating Scroll-To-Top Button**: Appears automatically after scrolling down 300px.
13. **Lazy Image Loading**: Progressive fade-in for images with `.npp-lazy` using IntersectionObserver.
14. **Live Theme Switcher Dropdown**: Auto-injected into navbars; saves preference to `localStorage`.
15. **One-Click Copy to Clipboard**: Buttons with `data-npp-copy="target-id"` copy text and show visual feedback.
16. **Interactive Counter Buttons**: ➖/➕ buttons with bounce feedback.
17. **Animated Form Submission**: Automatically catches form submits, prevents page reloads, and displays confirmation toasts.

---

## 🎨 Built-in Visual Themes

Change your site's entire visual design with a single parameter:
```npp
set page to webpage("My App", "cyberpunk")
```

Available presets:
1. `"dark"`: Obsidian background with neon indigo and emerald accents (Default).
2. `"modern"`: Crisp Swiss typography with slate cards and clean borders.
3. `"glassmorphism"`: Frosted glass cards (`backdrop-filter: blur(16px)`) with subtle borders and smooth gradients.
4. `"cyberpunk"`: High-contrast dark theme with electric yellow, neon pink, and cyan accents.

---

## 📋 Comprehensive HTML5 Tag Catalog (110+ Official Tags)

N++ provides native callable functions for **every official HTML5 tag**, accepting optional content and attributes:

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

### 5. Complete Forms & Inputs
Supports all input types and attributes (`type`, `placeholder`, `required`, `value`, `name`, `id`, `disabled`, `readonly`):
* `form(...)`, `label(...)`, `input(...)`, `textarea(...)`, `select(...)`, `option(...)`, `button(...)`
* `progress(...)`, `meter(...)`, `fieldset(...)`, `legend(...)`

### 6. Embedded Media
* `img(...)`, `video(...)`, `audio(...)`, `source(...)`, `iframe(...)`, `picture(...)`, `canvas(...)`, `svg(...)`

---

## 🌟 Ready-to-Preview Showcase Websites

N++ comes with three complete web applications you can explore right now:
1. **`showcase.html`** (compiled from `examples/web_all_html_tags.npp`): Full showcase of all 110+ HTML5 tags, tables, forms, tabs, and modals.
2. **`saas_landing.html`** (compiled from `examples/web_saas_landing.npp`): High-converting SaaS startup landing page with glassmorphism theme and pricing table.
3. **`dashboard.html`** (compiled from `examples/interactive_dashboard.npp`): Realtime cyberpunk analytics dashboard with live counters, progress bars, and cluster deployment modals.

To open any of them, double-click **`play.bat`** and choose options `[4]`, `[5]`, or `[6]`!
