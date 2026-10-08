"""
N++ Complete HTML5 Tag and Attribute Catalog
Contains all standard HTML5 tags and global/specific attributes.
"""

from typing import Set, Dict, List

# Complete collection of standard HTML5 tags
HTML5_TAGS: Set[str] = {
    # Document Metadata
    "html", "head", "title", "base", "link", "meta", "style",

    # Sectioning & Structure
    "body", "article", "section", "nav", "aside",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "header", "footer", "address", "main",

    # Grouping Content
    "p", "hr", "pre", "blockquote", "ol", "ul", "menu", "li",
    "dl", "dt", "dd", "figure", "figcaption", "div",

    # Text-level Semantics
    "a", "em", "strong", "small", "s", "cite", "q", "dfn", "abbr",
    "ruby", "rt", "rp", "data", "time", "code", "var", "samp", "kbd",
    "sub", "sup", "i", "b", "u", "mark", "bdi", "bdo", "span", "br", "wbr",

    # Embedded Media & Content
    "picture", "source", "img", "iframe", "embed", "object",
    "video", "audio", "track", "map", "area", "canvas", "svg",

    # Tabular Data
    "table", "caption", "colgroup", "col", "tbody", "thead", "tfoot", "tr", "td", "th",

    # Forms & Input
    "form", "label", "input", "button", "select", "datalist", "optgroup",
    "option", "textarea", "output", "progress", "meter", "fieldset", "legend",

    # Interactive & Dialogs
    "details", "summary", "dialog",

    # Scripting & Templates
    "script", "noscript", "template", "slot"
}

# Tags that do not have closing tags in HTML5
VOID_TAGS: Set[str] = {
    "area", "base", "br", "col", "embed", "hr", "img",
    "input", "link", "meta", "source", "track", "wbr"
}

# Standard HTML Global Attributes
GLOBAL_ATTRIBUTES: Set[str] = {
    "id", "class", "style", "title", "lang", "dir", "hidden",
    "tabindex", "accesskey", "contenteditable", "draggable",
    "spellcheck", "translate", "role", "autofocus", "nonce"
}

# Common tag-specific attributes
TAG_SPECIFIC_ATTRIBUTES: Dict[str, List[str]] = {
    "a": ["href", "target", "download", "rel", "type", "referrerpolicy"],
    "img": ["src", "alt", "width", "height", "loading", "srcset", "sizes", "crossorigin"],
    "link": ["href", "rel", "type", "media", "crossorigin", "sizes"],
    "meta": ["name", "content", "charset", "http-equiv", "property"],
    "script": ["src", "type", "async", "defer", "crossorigin", "integrity"],
    "form": ["action", "method", "enctype", "target", "autocomplete", "novalidate"],
    "input": ["type", "name", "value", "placeholder", "required", "disabled", "readonly",
              "checked", "min", "max", "step", "pattern", "maxlength", "minlength",
              "multiple", "accept", "autocomplete", "size", "src", "width", "height"],
    "button": ["type", "name", "value", "disabled", "form", "formaction"],
    "textarea": ["name", "rows", "cols", "placeholder", "required", "disabled", "readonly", "maxlength"],
    "select": ["name", "disabled", "multiple", "required", "size"],
    "option": ["value", "selected", "disabled", "label"],
    "label": ["for"],
    "video": ["src", "controls", "autoplay", "loop", "muted", "poster", "preload", "width", "height"],
    "audio": ["src", "controls", "autoplay", "loop", "muted", "preload"],
    "source": ["src", "srcset", "type", "media"],
    "iframe": ["src", "width", "height", "name", "allow", "allowfullscreen", "loading", "sandbox"],
    "table": ["border"],
    "td": ["colspan", "rowspan", "headers"],
    "th": ["colspan", "rowspan", "headers", "scope"],
    "details": ["open"],
    "dialog": ["open"],
    "progress": ["value", "max"],
    "meter": ["value", "min", "max", "low", "high", "optimum"],
    "time": ["datetime"]
}
