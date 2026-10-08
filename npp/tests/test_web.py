"""
N++ Web & Standard Library Tests
Validates HTML5 tags generation, components, styling, and standard library extensions.
"""

import unittest
import os
from npp import run_code
from npp.web import (
    HTML5_TAGS, create_element, HTMLElement, Webpage,
    Navbar, Hero, Card, Grid, Badge, Alert
)
from npp.builtins import get_active_webpage, set_active_webpage


class TestNppWeb(unittest.TestCase):

    def setUp(self):
        set_active_webpage(None)

    def test_html5_tags_catalog(self):
        # Verify that all major HTML5 tags are present
        self.assertIn("h1", HTML5_TAGS)
        self.assertIn("div", HTML5_TAGS)
        self.assertIn("p", HTML5_TAGS)
        self.assertIn("table", HTML5_TAGS)
        self.assertIn("form", HTML5_TAGS)
        self.assertIn("input", HTML5_TAGS)
        self.assertIn("video", HTML5_TAGS)
        self.assertIn("canvas", HTML5_TAGS)
        self.assertIn("dialog", HTML5_TAGS)
        self.assertGreater(len(HTML5_TAGS), 100)

    def test_element_with_attributes(self):
        el = create_element("a", "Click Here", {"href": "https://example.com", "target": "_blank"})
        rendered = el.render()
        self.assertIn("<a", rendered)
        self.assertIn('href="https://example.com"', rendered)
        self.assertIn('target="_blank"', rendered)
        self.assertIn("Click Here", rendered)
        self.assertIn("</a>", rendered)

    def test_void_tag_self_closing(self):
        img = create_element("img", attrs={"src": "banner.jpg", "alt": "Banner"})
        rendered = img.render()
        self.assertIn('<img src="banner.jpg" alt="Banner">', rendered)
        self.assertNotIn("</img>", rendered)

    def test_webpage_render(self):
        page = Webpage("Test App", theme="dark")
        page.add(create_element("h1", "Hello N++ Web"))
        html = page.render()
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("<title>Test App</title>", html)
        self.assertIn("Hello N++ Web", html)
        self.assertIn("var(--npp-primary)", html)

    def test_high_level_components(self):
        c = Card("Fast", "Zero configuration needed", icon="⚡", btn_text="Explore", btn_link="#")
        el = c.to_element()
        rendered = el.render()
        self.assertIn("npp-card", rendered)
        self.assertIn("Fast", rendered)
        self.assertIn("Zero configuration needed", rendered)
        self.assertIn("⚡", rendered)

    def test_npp_script_web_generation(self):
        code = """
        set site to webpage("My Cool Website", "glassmorphism")
        hero("Next-Gen Web", "Built with N++")
        set c1 to card("Card One", "Description 1", "🚀")
        set c2 to card("Card Two", "Description 2", "✨")
        site.add(grid(2, [c1, c2]))
        set out to render_html()
        """
        run_code(code)
        page = get_active_webpage()
        self.assertIsNotNone(page)
        html = page.render()
        self.assertIn("Next-Gen Web", html)
        self.assertIn("Card One", html)
        self.assertIn("Card Two", html)

    def test_standard_library_extensions(self):
        code = """
        set id to uuid()
        set h to hash_sha256("test")
        set data to {"title": "N++", "version": 1}
        set json_str to to_json(data)
        set parsed to from_json(json_str)
        set r to random_int(1, 10)
        set s to sum([1, 2, 3, 4])
        """
        run_code(code)

    def test_html_form_tags_in_npp(self):
        code = """
        set page to webpage("Forms", "modern")
        set f to form({"action": "/login", "method": "post"})
        f.add(label("Username:", {"for": "user"}))
        f.add(input({"type": "text", "id": "user", "placeholder": "Your name"}))
        f.add(button("Submit", {"type": "submit"}))
        set html_str to render_html(f)
        """
        run_code(code)


if __name__ == "__main__":
    unittest.main()
