from typing import Any, Dict, List, Optional
from .elements import HTMLElement, create_element
from .themes import generate_stylesheet
from .runtime import INTERACTIVE_RUNTIME_JS, INTERACTIVE_RUNTIME_CSS

# Active document context for N++ web applications
_ACTIVE_WEBPAGE: Optional["Webpage"] = None


def get_active_webpage() -> Optional["Webpage"]:
    global _ACTIVE_WEBPAGE
    return _ACTIVE_WEBPAGE


def set_active_webpage(page: Optional["Webpage"]):
    global _ACTIVE_WEBPAGE
    _ACTIVE_WEBPAGE = page


class Webpage:
    def __init__(self, title: str = "N++ Web Application", theme: str = "dark", lang: str = "en"):
        self.title = title
        self.theme = theme
        self.lang = lang
        self.meta_tags: List[HTMLElement] = [
            create_element("meta", attrs={"charset": "UTF-8"}),
            create_element("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
            create_element("title", content=title)
        ]
        self.custom_styles: List[str] = []
        self.custom_scripts: List[str] = []
        self.children: List[Any] = []

    def add(self, item: Any) -> "Webpage":
        """Add any HTMLElement, Component, or raw element to the page body."""
        if isinstance(item, list):
            for i in item:
                self.add(i)
        elif item is not None:
            self.children.append(item)
        return self

    def add_meta(self, name: str, content: str) -> "Webpage":
        self.meta_tags.append(create_element("meta", attrs={"name": name, "content": content}))
        return self

    def add_style(self, css_text: str) -> "Webpage":
        self.custom_styles.append(css_text)
        return self

    def add_script(self, js_text: str) -> "Webpage":
        self.custom_scripts.append(js_text)
        return self

    def render(self) -> str:
        """Render complete, standalone HTML5 document with embedded styles."""
        theme_css = generate_stylesheet(self.theme)
        all_css = theme_css + "\n" + INTERACTIVE_RUNTIME_CSS + "\n" + "\n".join(self.custom_styles)

        # Build head
        head_el = create_element("head")
        for m in self.meta_tags:
            head_el.add(m)
        head_el.add(HTMLElement("style", content=all_css, is_raw=True))

        # Build body
        body_el = create_element("body")
        for child in self.children:
            if hasattr(child, "to_element"):
                body_el.add(child.to_element())
            elif isinstance(child, HTMLElement):
                body_el.add(child)
            else:
                body_el.add(create_element("div", content=str(child)))

        for s in self.custom_scripts:
            body_el.add(HTMLElement("script", content=s, is_raw=True))

        # Inject the N++ interactive runtime (last so DOM is ready)
        body_el.add(HTMLElement("script", content=INTERACTIVE_RUNTIME_JS, is_raw=True))

        html_el = create_element("html", attrs={"lang": self.lang})
        html_el.add(head_el)
        html_el.add(body_el)

        return "<!DOCTYPE html>\n" + html_el.render(indent=0, pretty=True)


    def export(self, filepath: str):
        """Save the rendered HTML document to a file."""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.render())


# High-Level Components
class Component:
    def to_element(self) -> HTMLElement:
        raise NotImplementedError


class Navbar(Component):
    def __init__(self, brand: str, links: Optional[List[Dict[str, str]]] = None, cta_text: str = None, cta_link: str = None):
        self.brand = brand
        self.links = links or []
        self.cta_text = cta_text
        self.cta_link = cta_link

    def to_element(self) -> HTMLElement:
        nav = create_element("nav", attrs={"class": "npp-navbar"})
        nav.add(create_element("div", content=self.brand, attrs={"class": "npp-brand"}))

        ul = create_element("ul", attrs={"class": "npp-nav-links"})
        for item in self.links:
            if isinstance(item, dict):
                for label, url in item.items():
                    li = create_element("li")
                    li.add(create_element("a", content=label, attrs={"href": url}))
                    ul.add(li)
        nav.add(ul)

        if self.cta_text:
            cta = create_element("a", content=self.cta_text, attrs={
                "href": self.cta_link or "#",
                "class": "npp-button"
            })
            nav.add(cta)

        return nav


class Hero(Component):
    def __init__(self, title: str, subtitle: str = "", button_text: str = None, button_link: str = None):
        self.title = title
        self.subtitle = subtitle
        self.button_text = button_text
        self.button_link = button_link

    def to_element(self) -> HTMLElement:
        hero = create_element("header", attrs={"class": "npp-hero"})
        hero.add(create_element("h1", content=self.title))
        if self.subtitle:
            hero.add(create_element("p", content=self.subtitle))
        if self.button_text:
            hero.add(create_element("a", content=self.button_text, attrs={
                "href": self.button_link or "#",
                "class": "npp-button"
            }))
        return hero


class Card(Component):
    def __init__(
        self,
        title: str,
        description: str = "",
        icon: str = None,
        image: str = None,
        badge: str = None,
        button_text: str = None,
        button_link: str = None,
        btn_text: str = None,
        btn_link: str = None
    ):
        self.title = title
        self.description = description
        self.icon = icon
        self.image = image
        self.badge = badge
        self.button_text = button_text or btn_text
        self.button_link = button_link or btn_link

    def to_element(self) -> HTMLElement:
        card = create_element("div", attrs={"class": "npp-card"})
        if self.image:
            card.add(create_element("img", attrs={"src": self.image, "alt": self.title, "style": "border-radius: 8px; margin-bottom: 1rem;"}))
        if self.badge:
            card.add(create_element("span", content=self.badge, attrs={"class": "npp-badge", "style": "margin-bottom: 0.75rem;"}))
        if self.icon:
            card.add(create_element("div", content=self.icon, attrs={"style": "font-size: 2rem; margin-bottom: 0.5rem;"}))
        card.add(create_element("h3", content=self.title))
        if self.description:
            card.add(create_element("p", content=self.description))
        if self.button_text:
            card.add(create_element("a", content=self.button_text, attrs={
                "href": self.button_link or "#",
                "class": "npp-button npp-button-secondary"
            }))
        return card


class Grid(Component):
    def __init__(self, columns: int = 3, children: Optional[List[Any]] = None):
        self.columns = columns
        self.children = children or []

    def add(self, item: Any) -> "Grid":
        self.children.append(item)
        return self

    def to_element(self) -> HTMLElement:
        grid_cls = f"npp-grid npp-grid-{self.columns}"
        grid = create_element("div", attrs={"class": grid_cls})
        for child in self.children:
            if hasattr(child, "to_element"):
                grid.add(child.to_element())
            elif isinstance(child, HTMLElement):
                grid.add(child)
            else:
                grid.add(child)
        return grid


class Container(Component):
    def __init__(self, children: Optional[List[Any]] = None):
        self.children = children or []

    def add(self, item: Any) -> "Container":
        self.children.append(item)
        return self

    def to_element(self) -> HTMLElement:
        c = create_element("div", attrs={"class": "npp-container"})
        for child in self.children:
            if hasattr(child, "to_element"):
                c.add(child.to_element())
            elif isinstance(child, HTMLElement):
                c.add(child)
            else:
                c.add(child)
        return c


class Badge(Component):
    def __init__(self, text: str):
        self.text = text

    def to_element(self) -> HTMLElement:
        return create_element("span", content=self.text, attrs={"class": "npp-badge"})


class Alert(Component):
    def __init__(self, message: str):
        self.message = message

    def to_element(self) -> HTMLElement:
        return create_element("div", content=self.message, attrs={"class": "npp-alert"})


class PageFooter(Component):
    def __init__(self, text: str = "Built with N++"):
        self.text = text

    def to_element(self) -> HTMLElement:
        footer = create_element("footer", attrs={"class": "npp-footer"})
        footer.add(create_element("p", content=self.text))
        return footer
