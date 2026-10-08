"""
N++ Web Engine
"""

from .html_tags import HTML5_TAGS, VOID_TAGS, GLOBAL_ATTRIBUTES
from .elements import HTMLElement, create_element
from .components import (
    Webpage, Component, Navbar, Hero, Card, Grid, Container,
    Badge, Alert, PageFooter, get_active_webpage, set_active_webpage
)
from .themes import generate_stylesheet, THEMES
from .server import serve_directory
