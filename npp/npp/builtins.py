"""
N++ Built-in Standard Library, HTML5 Tags Catalog, Web Components, and System Utilities
"""

import math
import time
import os
import json
import uuid
import hashlib
import urllib.request
import urllib.parse
from typing import Any, Callable, List, Dict, Optional

from .errors import NppRuntimeError, NppReturnSignal
from .ast_nodes import Block
from .web import (
    HTML5_TAGS, HTMLElement, create_element, Webpage,
    Navbar, Hero, Card, Grid, Container, Badge, Alert, PageFooter,
    get_active_webpage, set_active_webpage
)


class NppCallable:
    """Base class for anything callable in N++."""
    def call(self, interpreter, args: List[Any], line: int = 1, col: int = 1) -> Any:
        raise NotImplementedError


class NppBuiltin(NppCallable):
    def __init__(self, name: str, fn: Callable, min_args: int = 0, max_args: Optional[int] = None):
        self.name = name
        self.fn = fn
        self.min_args = min_args
        self.max_args = max_args

    def call(self, interpreter, args: List[Any], line: int = 1, col: int = 1) -> Any:
        if len(args) < self.min_args:
            raise NppRuntimeError(f"Function '{self.name}' expects at least {self.min_args} arguments, got {len(args)}", line, col, interpreter.filename)
        if self.max_args is not None and len(args) > self.max_args:
            raise NppRuntimeError(f"Function '{self.name}' expects at most {self.max_args} arguments, got {len(args)}", line, col, interpreter.filename)
        try:
            return self.fn(*args)
        except Exception as e:
            raise NppRuntimeError(f"Error in '{self.name}': {str(e)}", line, col, interpreter.filename)

    def __repr__(self) -> str:
        return f"<builtin function {self.name}>"


class NppFunction(NppCallable):
    def __init__(self, name: str, parameters: List[str], body: Block, closure_env):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.closure_env = closure_env

    def call(self, interpreter, args: List[Any], line: int = 1, col: int = 1) -> Any:
        from .environment import Environment

        if len(args) != len(self.parameters):
            raise NppRuntimeError(
                f"Function '{self.name}' expects {len(self.parameters)} arguments ({', '.join(self.parameters)}), got {len(args)}",
                line, col, interpreter.filename
            )

        fn_env = Environment(parent=self.closure_env)
        for param_name, arg_val in zip(self.parameters, args):
            fn_env.define(param_name, arg_val)

        prev_env = interpreter.current_env
        interpreter.current_env = fn_env
        return_value = None
        try:
            interpreter.execute_block(self.body, fn_env)
        except NppReturnSignal as ret:
            return_value = ret.value
        finally:
            interpreter.current_env = prev_env

        return return_value

    def __repr__(self) -> str:
        return f"<function {self.name}({', '.join(self.parameters)})>"


def npp_format_value(val: Any) -> str:
    """Format an N++ value to human-friendly string."""
    if val is None:
        return "null"
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, list):
        return "[" + ", ".join(npp_format_value(x) for x in val) + "]"
    if isinstance(val, dict):
        items = [f'"{k}": {npp_format_value(v)}' for k, v in val.items()]
        return "{" + ", ".join(items) + "}"
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        return str(val)
    if isinstance(val, HTMLElement):
        return f"<{val.tag} ...>"
    if isinstance(val, Webpage):
        return f"<Webpage: {val.title}>"
    return str(val)


def _make_tag_function(tag_name: str) -> Callable:
    """Constructs a function that returns an HTMLElement for the given tag."""
    def tag_fn(*args):
        content = None
        attrs = None
        if len(args) == 1:
            if isinstance(args[0], dict):
                attrs = args[0]
            else:
                content = args[0]
        elif len(args) >= 2:
            content = args[0]
            attrs = args[1] if isinstance(args[1], dict) else None

        return create_element(tag_name, content, attrs)
    return tag_fn


def get_default_builtins() -> Dict[str, NppBuiltin]:
    builtins = {}

    # -------------------------------------------------------------------------
    # Core I/O
    # -------------------------------------------------------------------------
    def _print(*args):
        text = " ".join(npp_format_value(a) for a in args)
        print(text)
        return None
    builtins["print"] = NppBuiltin("print", _print, min_args=0, max_args=None)
    builtins["println"] = NppBuiltin("println", _print, min_args=0, max_args=None)
    builtins["say"] = NppBuiltin("say", _print, min_args=0, max_args=None)

    def _input(prompt=""):
        return input(npp_format_value(prompt))
    builtins["input"] = NppBuiltin("input", _input, min_args=0, max_args=1)
    builtins["ask"] = NppBuiltin("ask", _input, min_args=0, max_args=1)

    # -------------------------------------------------------------------------
    # Collections & Iterables
    # -------------------------------------------------------------------------
    def _len(item):
        if isinstance(item, (list, dict, str)):
            return len(item)
        if hasattr(item, "children"):
            return len(item.children)
        raise ValueError(f"Cannot get length of {type(item).__name__}")
    builtins["len"] = NppBuiltin("len", _len, min_args=1, max_args=1)
    builtins["length"] = NppBuiltin("length", _len, min_args=1, max_args=1)

    def _range(start, end=None, step=1):
        if end is None:
            return list(range(int(start)))
        return list(range(int(start), int(end), int(step)))
    builtins["range"] = NppBuiltin("range", _range, min_args=1, max_args=3)

    def _push(lst, item):
        if isinstance(lst, list):
            lst.append(item)
            return lst
        raise ValueError(f"push() expects a list, got {type(lst).__name__}")
    builtins["push"] = NppBuiltin("push", _push, min_args=2, max_args=2)
    builtins["append"] = NppBuiltin("append", _push, min_args=2, max_args=2)

    def _pop(lst):
        if isinstance(lst, list):
            if not lst:
                raise ValueError("pop() on empty list")
            return lst.pop()
        raise ValueError(f"pop() expects a list, got {type(lst).__name__}")
    builtins["pop"] = NppBuiltin("pop", _pop, min_args=1, max_args=1)

    builtins["keys"] = NppBuiltin("keys", lambda d: list(d.keys()) if isinstance(d, dict) else [], min_args=1, max_args=1)
    builtins["values"] = NppBuiltin("values", lambda d: list(d.values()) if isinstance(d, dict) else [], min_args=1, max_args=1)

    # -------------------------------------------------------------------------
    # Type checks and Coercions
    # -------------------------------------------------------------------------
    def _type(val):
        if val is None:
            return "null"
        if isinstance(val, bool):
            return "boolean"
        if isinstance(val, (int, float)):
            return "number"
        if isinstance(val, str):
            return "string"
        if isinstance(val, list):
            return "list"
        if isinstance(val, dict):
            return "map"
        if isinstance(val, (HTMLElement, Webpage)):
            return "web_element"
        if isinstance(val, NppCallable):
            return "function"
        return "unknown"
    builtins["type"] = NppBuiltin("type", _type, min_args=1, max_args=1)

    builtins["str"] = NppBuiltin("str", lambda v: npp_format_value(v), min_args=1, max_args=1)
    builtins["text"] = NppBuiltin("text", lambda v: npp_format_value(v), min_args=1, max_args=1)

    def _num(v):
        if isinstance(v, (int, float)):
            return v
        if isinstance(v, str):
            s = v.strip()
            return float(s) if "." in s else int(s)
        if isinstance(v, bool):
            return 1 if v else 0
        raise ValueError(f"Cannot convert {v!r} to number")
    builtins["num"] = NppBuiltin("num", _num, min_args=1, max_args=1)
    builtins["number"] = NppBuiltin("number", _num, min_args=1, max_args=1)
    builtins["bool"] = NppBuiltin("bool", lambda v: bool(v), min_args=1, max_args=1)

    # -------------------------------------------------------------------------
    # Mathematics & Statistics
    # -------------------------------------------------------------------------
    builtins["abs"] = NppBuiltin("abs", lambda v: abs(v), min_args=1, max_args=1)
    builtins["round"] = NppBuiltin("round", lambda v, d=0: round(v, d), min_args=1, max_args=2)
    builtins["floor"] = NppBuiltin("floor", lambda v: math.floor(v), min_args=1, max_args=1)
    builtins["ceil"] = NppBuiltin("ceil", lambda v: math.ceil(v), min_args=1, max_args=1)
    builtins["sqrt"] = NppBuiltin("sqrt", lambda v: math.sqrt(v), min_args=1, max_args=1)
    builtins["sin"] = NppBuiltin("sin", lambda v: math.sin(v), min_args=1, max_args=1)
    builtins["cos"] = NppBuiltin("cos", lambda v: math.cos(v), min_args=1, max_args=1)
    builtins["tan"] = NppBuiltin("tan", lambda v: math.tan(v), min_args=1, max_args=1)
    builtins["pi"] = NppBuiltin("pi", lambda: math.pi, min_args=0, max_args=0)
    builtins["min"] = NppBuiltin("min", lambda *args: min(args[0]) if len(args) == 1 and isinstance(args[0], list) else min(args), min_args=1, max_args=None)
    builtins["max"] = NppBuiltin("max", lambda *args: max(args[0]) if len(args) == 1 and isinstance(args[0], list) else max(args), min_args=1, max_args=None)
    builtins["sum"] = NppBuiltin("sum", lambda lst: sum(lst) if isinstance(lst, list) else lst, min_args=1, max_args=1)
    builtins["average"] = NppBuiltin("average", lambda lst: (sum(lst) / len(lst)) if isinstance(lst, list) and lst else 0, min_args=1, max_args=1)
    builtins["clamp"] = NppBuiltin("clamp", lambda v, mn, mx: max(mn, min(v, mx)), min_args=3, max_args=3)

    # -------------------------------------------------------------------------
    # Strings
    # -------------------------------------------------------------------------
    builtins["upper"] = NppBuiltin("upper", lambda s: str(s).upper(), min_args=1, max_args=1)
    builtins["lower"] = NppBuiltin("lower", lambda s: str(s).lower(), min_args=1, max_args=1)
    builtins["split"] = NppBuiltin("split", lambda s, d=" ": str(s).split(d), min_args=1, max_args=2)
    builtins["join"] = NppBuiltin("join", lambda lst, d="": d.join(npp_format_value(x) for x in lst), min_args=1, max_args=2)
    builtins["replace"] = NppBuiltin("replace", lambda s, old, new: str(s).replace(str(old), str(new)), min_args=3, max_args=3)
    builtins["trim"] = NppBuiltin("trim", lambda s: str(s).strip(), min_args=1, max_args=1)
    builtins["contains"] = NppBuiltin("contains", lambda coll, item: item in coll, min_args=2, max_args=2)

    # -------------------------------------------------------------------------
    # Crypto, UUID, & Randomness
    # -------------------------------------------------------------------------
    import random
    builtins["uuid"] = NppBuiltin("uuid", lambda: str(uuid.uuid4()), min_args=0, max_args=0)
    builtins["random"] = NppBuiltin("random", lambda: random.random(), min_args=0, max_args=0)
    builtins["random_int"] = NppBuiltin("random_int", lambda a, b: random.randint(int(a), int(b)), min_args=2, max_args=2)
    builtins["random_choice"] = NppBuiltin("random_choice", lambda lst: random.choice(lst) if lst else None, min_args=1, max_args=1)
    builtins["hash_sha256"] = NppBuiltin("hash_sha256", lambda s: hashlib.sha256(str(s).encode("utf-8")).hexdigest(), min_args=1, max_args=1)
    builtins["hash_md5"] = NppBuiltin("hash_md5", lambda s: hashlib.md5(str(s).encode("utf-8")).hexdigest(), min_args=1, max_args=1)

    # -------------------------------------------------------------------------
    # File System Operations
    # -------------------------------------------------------------------------
    def _read_file(path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    builtins["read_file"] = NppBuiltin("read_file", _read_file, min_args=1, max_args=1)

    def _write_file(path: str, content: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(content))
        return True
    builtins["write_file"] = NppBuiltin("write_file", _write_file, min_args=2, max_args=2)

    def _append_file(path: str, content: str):
        with open(path, "a", encoding="utf-8") as f:
            f.write(str(content))
        return True
    builtins["append_file"] = NppBuiltin("append_file", _append_file, min_args=2, max_args=2)
    builtins["file_exists"] = NppBuiltin("file_exists", lambda p: os.path.exists(p), min_args=1, max_args=1)
    builtins["list_files"] = NppBuiltin("list_files", lambda d=".": os.listdir(d), min_args=0, max_args=1)

    # -------------------------------------------------------------------------
    # JSON Serialization
    # -------------------------------------------------------------------------
    builtins["to_json"] = NppBuiltin("to_json", lambda obj, indent=2: json.dumps(obj, indent=indent), min_args=1, max_args=2)
    builtins["from_json"] = NppBuiltin("from_json", lambda s: json.loads(s), min_args=1, max_args=1)

    # -------------------------------------------------------------------------
    # HTTP Networking
    # -------------------------------------------------------------------------
    def _http_get(url: str) -> str:
        req = urllib.request.Request(url, headers={"User-Agent": "N++ Web Agent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8")
    builtins["http_get"] = NppBuiltin("http_get", _http_get, min_args=1, max_args=1)
    builtins["fetch"] = NppBuiltin("fetch", _http_get, min_args=1, max_args=1)

    def _http_post(url: str, data: Any) -> str:
        payload = json.dumps(data).encode("utf-8") if isinstance(data, (dict, list)) else str(data).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json", "User-Agent": "N++ Web Agent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8")
    builtins["http_post"] = NppBuiltin("http_post", _http_post, min_args=2, max_args=2)

    # -------------------------------------------------------------------------
    # System / Time
    # -------------------------------------------------------------------------
    builtins["clock"] = NppBuiltin("clock", lambda: time.time(), min_args=0, max_args=0)
    builtins["time"] = NppBuiltin("time", lambda: time.time(), min_args=0, max_args=0)
    builtins["sleep"] = NppBuiltin("sleep", lambda s: time.sleep(s), min_args=1, max_args=1)

    # -------------------------------------------------------------------------
    # WEB & HTML5 ENGINE: EVERY STANDARD HTML5 TAG
    # -------------------------------------------------------------------------
    # Universal tag builder
    def _generic_tag(name: str, content: Any = None, attrs: Optional[Dict[str, Any]] = None):
        return create_element(name, content, attrs)
    builtins["tag"] = NppBuiltin("tag", _generic_tag, min_args=1, max_args=3)

    # Register all official HTML5 tags as callable built-ins!
    for t in HTML5_TAGS:
        builtins[t] = NppBuiltin(t, _make_tag_function(t), min_args=0, max_args=2)

    # Webpage creator & document manager
    def _webpage(title="N++ Application", theme="dark"):
        page = Webpage(title=title, theme=theme)
        set_active_webpage(page)
        return page
    builtins["webpage"] = NppBuiltin("webpage", _webpage, min_args=0, max_args=2)
    builtins["new_webpage"] = NppBuiltin("new_webpage", _webpage, min_args=0, max_args=2)

    def _get_active():
        return get_active_webpage()
    builtins["active_page"] = NppBuiltin("active_page", _get_active, min_args=0, max_args=0)

    # High-level components
    def _card(title: str, description: str = "", icon: str = None, image: str = None, badge: str = None, btn_text: str = None, btn_link: str = None):
        return Card(title, description, icon, image, badge, btn_text, btn_link)
    builtins["card"] = NppBuiltin("card", _card, min_args=1, max_args=7)

    def _hero(title: str, subtitle: str = "", btn_text: str = None, btn_link: str = None):
        h = Hero(title, subtitle, btn_text, btn_link)
        active = get_active_webpage()
        if active is not None:
            active.add(h)
        return h
    builtins["hero"] = NppBuiltin("hero", _hero, min_args=1, max_args=4)

    def _navbar(brand: str, links: List[Dict[str, str]] = None, cta_text: str = None, cta_link: str = None):
        n = Navbar(brand, links, cta_text, cta_link)
        active = get_active_webpage()
        if active is not None:
            active.add(n)
        return n
    builtins["navbar"] = NppBuiltin("navbar", _navbar, min_args=1, max_args=4)

    def _grid(columns: int = 3, items: List[Any] = None):
        return Grid(columns=int(columns), children=items or [])
    builtins["grid"] = NppBuiltin("grid", _grid, min_args=0, max_args=2)

    def _container(items: List[Any] = None):
        return Container(children=items or [])
    builtins["container"] = NppBuiltin("container", _container, min_args=0, max_args=1)

    def _badge(text: str):
        return Badge(text)
    builtins["badge"] = NppBuiltin("badge", _badge, min_args=1, max_args=1)

    def _alert(message: str):
        return Alert(message)
    builtins["alert"] = NppBuiltin("alert", _alert, min_args=1, max_args=1)

    def _page_footer(text: str = "Built with N++"):
        f = PageFooter(text)
        active = get_active_webpage()
        if active is not None:
            active.add(f)
        return f
    builtins["page_footer"] = NppBuiltin("page_footer", _page_footer, min_args=0, max_args=1)

    # HTML Exporting & Rendering
    def _render_html(target: Any = None) -> str:
        if target is None:
            target = get_active_webpage()
        if isinstance(target, Webpage):
            return target.render()
        if isinstance(target, HTMLElement):
            return target.render()
        if hasattr(target, "to_element"):
            return target.to_element().render()
        return str(target)
    builtins["render_html"] = NppBuiltin("render_html", _render_html, min_args=0, max_args=1)

    def _export_html(filepath: str, target: Any = None):
        if target is None:
            target = get_active_webpage()
        if target is None:
            raise ValueError("No active webpage or target provided to export_html()")
        content = _render_html(target)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Exported HTML to '{filepath}'")
        return filepath
    builtins["export_html"] = NppBuiltin("export_html", _export_html, min_args=1, max_args=2)

    return builtins
