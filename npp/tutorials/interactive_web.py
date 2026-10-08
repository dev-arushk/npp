"""
Interactive Web Engine Tutorial for N++
Walks the user through building modern responsive web apps 1000x faster than HTML.
"""

import sys
import os
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from npp import run_code
from npp.web import get_active_webpage, set_active_webpage


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(prompt="Press ENTER to continue to the next step..."):
    print("\n" + "-" * 75)
    input(f"  👉 {prompt}")
    print("-" * 75)


def header(title, step_num, total=6):
    clear()
    print("=" * 75)
    print(f"   🌐 N++ INTERACTIVE WEB ENGINE TUTORIAL — LESSON {step_num} OF {total}")
    print(f"      {title.upper()}")
    print("=" * 75)
    print()


def run_demo(code_str):
    print("  [N++ Code]")
    for line in code_str.strip().splitlines():
        print(f"    | {line}")
    print("\n  [Execution Result]")
    print("  " + "-" * 45)
    run_code(code_str)
    print("  " + "-" * 45)


def lesson_1():
    header("Why N++ Web Beats Raw HTML", 1)
    print("""
  In traditional web design:
    * You have to type verbose HTML: <div><span><p></p></span></div>
    * A missing closing tag breaks your whole page.
    * You need 500 lines of CSS just to make cards look decent.
    * You need npm, vite, webpack, or Node.js just to view it properly.

  In N++ Web Engine:
    ✓ Pure, clean English syntax.
    ✓ Zero unclosed tag errors.
    ✓ Built-in responsive design & Google Fonts (Inter, Outfit, Fira Code).
    ✓ Zero dependencies: compiles to standalone, production-ready HTML5!
    """)
    pause()


def lesson_2():
    header("Creating Your First Webpage in 5 Lines", 2)
    print("""
  Let's see how simple it is to build a full web page:
    """)
    code = """
set page to webpage("My First N++ Site", "dark")
hero("Welcome to the Future", "Web development made 1000x easier.")
page_footer("Built with N++ Web Engine")
export_html("tutorial_page.html", page)
    """
    run_demo(code)
    print("\n  Notice that a complete standalone HTML5 file ('tutorial_page.html') was created!")
    pause()


def lesson_3():
    header("The 4 Built-in Visual Themes", 3)
    print("""
  You can change the entire mood and visual design of your website
  by changing just ONE word in your code:

    1. 'dark': Obsidian black background with neon indigo/emerald accents.
    2. 'modern': Crisp, clean Swiss typography with slate cards.
    3. 'glassmorphism': Frosted glass cards (backdrop-filter: blur) over gradient.
    4. 'cyberpunk': High-contrast dark cyberpunk with neon pink & yellow accents.

  Example:
      set page to webpage("Cyberpunk Portal", "cyberpunk")
    """)
    pause()


def lesson_4():
    header("High-Level Modern UI Components", 4)
    print("""
  N++ gives you ready-to-use, responsive building blocks:
    * navbar: Sticky top navigation with brand and links.
    * hero: Large gradient banner with headline and CTA button.
    * card: Beautiful card with shadows, badges, and icons.
    * grid: Auto-responsive 2, 3, or 4 column layout (no CSS needed!).
    * badge: Pill tag for categories and statuses.
    * alert: Highlighted notification banner.
    """)
    code = """
set page to webpage("Component Demo", "modern")
navbar("TechCorp", [{"Products": "#"}, {"About": "#"}], "Sign In", "#")
set c1 to card("Fast", "Zero build config needed.", "⚡")
set c2 to card("Clean", "Pure English syntax.", "✨")
set c3 to card("Responsive", "Mobile friendly by default.", "📱")
page.add(grid(3, [c1, c2, c3]))
export_html("components_demo.html", page)
    """
    run_demo(code)
    pause()


def lesson_5():
    header("Every Standard HTML5 Tag (110+ Tags)", 5)
    print("""
  Need standard HTML5 tags? N++ includes ALL 110+ of them with full attributes:
    * Forms: form, label, input, button, select, option, textarea
    * Tables: table, thead, tbody, tr, th, td
    * Media: img, video, audio, canvas, svg
    * Interactive: details, summary, dialog, progress, meter
    """)
    code = """
set page to webpage("Form Demo", "dark")
set f to form({"action": "/submit", "method": "post"})
f.add(label("Email Address:", {"for": "email"}))
f.add(input({"type": "email", "id": "email", "placeholder": "user@example.com", "required": true}))
f.add(button("Subscribe", {"type": "submit", "class": "npp-button"}))
page.add(f)
export_html("form_demo.html", page)
    """
    run_demo(code)
    pause()


def lesson_6():
    header("Interactive Web Builder: Create YOUR Page Now!", 6)
    print("""
  Let's build a real customized website right now based on YOUR choices!
    """)
    title = input("  1. Enter your website title (e.g. My Awesome Studio): ").strip() or "My Awesome Studio"
    
    print("\n  Choose a theme:")
    print("    [1] dark (Default)")
    print("    [2] modern (Clean & Crisp)")
    print("    [3] glassmorphism (Frosted Glass)")
    print("    [4] cyberpunk (Neon Future)")
    t_choice = input("  Pick theme (1-4): ").strip()
    theme_map = {"1": "dark", "2": "modern", "3": "glassmorphism", "4": "cyberpunk"}
    chosen_theme = theme_map.get(t_choice, "dark")

    headline = input("\n  2. Enter your main hero headline: ").strip() or "Created with N++ Web Engine"
    subhead = input("  3. Enter a short subtitle: ").strip() or "Web development that is 1000x better than HTML."

    print("\n  Building your webpage...")
    custom_code = f"""
set my_site to webpage("{title}", "{chosen_theme}")
navbar("{title}", [{{"Home": "#"}}, {{"Features": "#"}}, {{"Contact": "#"}}], "Explore", "#")
hero("{headline}", "{subhead}", "Get Started", "#")

set c1 to card("Modern Layout", "Built automatically with N++ responsive CSS.", "🎨")
set c2 to card("Zero Dependencies", "Pure standalone HTML5 with Google Fonts.", "🚀")
set c3 to card("Instant Launch", "Works anywhere in any web browser.", "⚡")

my_site.add(grid(3, [c1, c2, c3]))
page_footer("Created interactively with N++ Web Engine")
export_html("my_custom_site.html", my_site)
"""
    run_code(custom_code)

    file_path = os.path.abspath("my_custom_site.html")
    print(f"\n  🎉 SUCCESS! Your page was created at: {file_path}")
    open_choice = input("  Would you like to open it in your browser right now? (Y/n): ").strip().lower()
    if open_choice != "n":
        webbrowser.open("file://" + file_path)
        print("  Opened in your default web browser!")

    clear()
    print("=" * 75)
    print("   🏆 CONGRATULATIONS! YOU HAVE MASTERED N++ WEB ENGINE!")
    print("=" * 75)
    print("""
  You now know how to:
    ✓ Create web pages with 'webpage(title, theme)'
    ✓ Use built-in visual themes ('dark', 'glassmorphism', 'modern', 'cyberpunk')
    ✓ Use high-level components ('navbar', 'hero', 'card', 'grid', 'page_footer')
    ✓ Use all 110+ official HTML5 tags & attributes
    ✓ Export to production HTML with 'export_html()'
    ✓ Serve locally with 'python main.py serve file.npp'

  Check 'play.bat' anytime for instant launchers and the local dev server!
    """)
    input("  Press ENTER to return...")


def main():
    lesson_1()
    lesson_2()
    lesson_3()
    lesson_4()
    lesson_5()
    lesson_6()


if __name__ == "__main__":
    main()
