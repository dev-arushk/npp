"""
N++ HTML Element and DOM Tree Model
Represents and renders semantic HTML5 nodes with arbitrary attributes and children.
"""

import html
from typing import Any, Dict, List, Optional, Union
from .html_tags import VOID_TAGS


class HTMLElement:
    def __init__(
        self,
        tag: str,
        content: Optional[Union[str, List[Any]]] = None,
        attributes: Optional[Dict[str, Any]] = None,
        is_raw: bool = False
    ):
        self.tag = tag.lower()
        self.attributes: Dict[str, Any] = attributes.copy() if attributes else {}
        self.children: List[Any] = []
        self.is_raw = is_raw

        if content is not None:
            if isinstance(content, list):
                for c in content:
                    self.add(c)
            else:
                self.add(content)

    def add(self, child: Any) -> "HTMLElement":
        """Add a child node, component, string, number, or list of elements."""
        if child is None:
            return self
        if isinstance(child, list):
            for c in child:
                self.add(c)
        elif hasattr(child, "to_element"):
            self.children.append(child.to_element())
        else:
            self.children.append(child)
        return self

    def set_attr(self, name: str, value: Any) -> "HTMLElement":
        """Set an HTML attribute."""
        if value is not None and value is not False:
            self.attributes[name] = value
        elif value is False and name in self.attributes:
            del self.attributes[name]
        return self

    def render(self, indent: int = 0, pretty: bool = True) -> str:
        """Render the element and all nested children to semantic HTML5."""
        pad = "  " * indent if pretty else ""
        newline = "\n" if pretty else ""

        # Format attributes
        attr_strs = []
        for k, v in self.attributes.items():
            # Handle boolean attributes like required, checked, disabled
            if v is True:
                attr_strs.append(k)
            elif v is not None and v is not False:
                # Replace underscores with dashes for data_*, aria_*
                attr_name = k.replace("_", "-") if k.startswith(("data_", "aria_")) else k
                escaped_val = html.escape(str(v), quote=True)
                attr_strs.append(f'{attr_name}="{escaped_val}"')

        attr_part = (" " + " ".join(attr_strs)) if attr_strs else ""

        # Void elements (self-closing without closing tag)
        if self.tag in VOID_TAGS:
            return f"{pad}<{self.tag}{attr_part}>{newline}"

        # If no children
        if not self.children:
            return f"{pad}<{self.tag}{attr_part}></{self.tag}>{newline}"

        # Inline single text child
        if len(self.children) == 1 and not isinstance(self.children[0], HTMLElement) and not hasattr(self.children[0], "to_element"):
            text_val = str(self.children[0])
            if not self.is_raw:
                text_val = html.escape(text_val)
            return f"{pad}<{self.tag}{attr_part}>{text_val}</{self.tag}>{newline}"

        # Multi-child or nested elements
        lines = [f"{pad}<{self.tag}{attr_part}>{newline}"]
        for child in self.children:
            if hasattr(child, "to_element"):
                lines.append(child.to_element().render(indent=indent + 1, pretty=pretty))
            elif isinstance(child, HTMLElement):
                lines.append(child.render(indent=indent + 1, pretty=pretty))
            else:
                child_pad = "  " * (indent + 1) if pretty else ""
                child_str = str(child) if self.is_raw else html.escape(str(child))
                lines.append(f"{child_pad}{child_str}{newline}")

        lines.append(f"{pad}</{self.tag}>{newline}")
        return "".join(lines)

    def __repr__(self) -> str:
        return f"<HTMLElement <{self.tag}> with {len(self.children)} children>"


def create_element(tag: str, content: Any = None, attrs: Optional[Dict[str, Any]] = None) -> HTMLElement:
    """Factory helper to construct an HTMLElement."""
    # If content is a dict and attrs is None, content was passed as attributes dict
    if isinstance(content, dict) and attrs is None:
        attrs = content
        content = None
    return HTMLElement(tag=tag, content=content, attributes=attrs)
