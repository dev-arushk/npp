"""
N++ Modern Responsive CSS Theme Engine
Generates zero-dependency modern stylesheets with dark mode, animations, and typography.
"""

from typing import Dict

BASE_RESET = """
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
html {
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  scroll-behavior: smooth;
}
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}
input, button, textarea, select {
  font: inherit;
}
p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}
"""

THEMES: Dict[str, Dict[str, str]] = {
    "modern": {
        "bg": "#f8fafc",
        "surface": "#ffffff",
        "surface_card": "#ffffff",
        "text": "#0f172a",
        "text_muted": "#64748b",
        "primary": "#4f46e5",
        "primary_hover": "#4338ca",
        "border": "#e2e8f0",
        "shadow": "0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05)",
        "accent": "#06b6d4"
    },
    "dark": {
        "bg": "#090d16",
        "surface": "#111827",
        "surface_card": "#172033",
        "text": "#f8fafc",
        "text_muted": "#94a3b8",
        "primary": "#6366f1",
        "primary_hover": "#4f46e5",
        "border": "#1e293b",
        "shadow": "0 10px 15px -3px rgb(0 0 0 / 0.4), 0 4px 6px -4px rgb(0 0 0 / 0.4)",
        "accent": "#10b981"
    },
    "glassmorphism": {
        "bg": "linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%)",
        "surface": "rgba(255, 255, 255, 0.07)",
        "surface_card": "rgba(255, 255, 255, 0.08)",
        "text": "#ffffff",
        "text_muted": "#cbd5e1",
        "primary": "#a855f7",
        "primary_hover": "#9333ea",
        "border": "rgba(255, 255, 255, 0.15)",
        "shadow": "0 8px 32px 0 rgba(0, 0, 0, 0.37)",
        "accent": "#38bdf8",
        "backdrop": "backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);"
    },
    "cyberpunk": {
        "bg": "#050508",
        "surface": "#0d0e15",
        "surface_card": "#121420",
        "text": "#00ffcc",
        "text_muted": "#8892b0",
        "primary": "#ff0055",
        "primary_hover": "#e6004c",
        "border": "#25283d",
        "shadow": "0 0 20px rgba(255, 0, 85, 0.2)",
        "accent": "#ffe600"
    }
}


def generate_stylesheet(theme_name: str = "dark") -> str:
    palette = THEMES.get(theme_name.lower(), THEMES["dark"])
    backdrop = palette.get("backdrop", "")
    bg = palette["bg"]
    bg_prop = f"background: {bg};" if "gradient" in bg else f"background-color: {bg};"

    return f"""
{BASE_RESET}

/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

:root {{
  --npp-bg: {palette['bg']};
  --npp-surface: {palette['surface']};
  --npp-surface-card: {palette['surface_card']};
  --npp-text: {palette['text']};
  --npp-text-muted: {palette['text_muted']};
  --npp-primary: {palette['primary']};
  --npp-primary-hover: {palette['primary_hover']};
  --npp-border: {palette['border']};
  --npp-shadow: {palette['shadow']};
  --npp-accent: {palette['accent']};
}}

body {{
  {bg_prop}
  color: var(--npp-text);
  font-family: 'Inter', sans-serif;
  padding: 0;
  margin: 0;
}}

/* Typography */
h1, h2, h3, h4, h5, h6 {{
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  line-height: 1.25;
  color: var(--npp-text);
  margin-bottom: 0.75rem;
}}
h1 {{ font-size: 2.5rem; }}
h2 {{ font-size: 2rem; }}
h3 {{ font-size: 1.5rem; }}
p {{ margin-bottom: 1rem; color: var(--npp-text); }}
a {{ color: var(--npp-primary); text-decoration: none; transition: color 0.2s; }}
a:hover {{ color: var(--npp-accent); text-decoration: underline; }}

/* Code blocks */
code, pre, kbd {{
  font-family: 'Fira Code', monospace;
  background: rgba(0,0,0,0.25);
  border-radius: 6px;
}}
code {{ padding: 0.2em 0.4em; font-size: 0.9em; }}
pre {{ padding: 1rem; overflow-x: auto; margin-bottom: 1rem; }}

/* Container & Layout */
.npp-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
  width: 100%;
}}

.npp-grid {{
  display: grid;
  gap: 1.5rem;
}}
.npp-grid-2 {{ grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }}
.npp-grid-3 {{ grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }}
.npp-grid-4 {{ grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }}

.npp-flex {{
  display: flex;
  gap: 1rem;
  align-items: center;
}}

/* High-level Components */
.npp-navbar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: var(--npp-surface);
  border-bottom: 1px solid var(--npp-border);
  {backdrop}
  position: sticky;
  top: 0;
  z-index: 100;
}}
.npp-brand {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--npp-text);
}}
.npp-nav-links {{
  display: flex;
  gap: 1.5rem;
  list-style: none;
}}

.npp-hero {{
  text-align: center;
  padding: 5rem 1.5rem 4rem;
  background: radial-gradient(circle at 50% 20%, rgba(99, 102, 241, 0.15), transparent 70%);
}}
.npp-hero h1 {{
  font-size: 3.5rem;
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
}}
.npp-hero p {{
  font-size: 1.25rem;
  color: var(--npp-text-muted);
  max-width: 650px;
  margin: 0 auto 2rem;
}}

.npp-card {{
  background: var(--npp-surface-card);
  border: 1px solid var(--npp-border);
  border-radius: 14px;
  padding: 1.75rem;
  box-shadow: var(--npp-shadow);
  {backdrop}
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}}
.npp-card:hover {{
  transform: translateY(-4px);
  border-color: var(--npp-primary);
}}
.npp-card h3 {{
  margin-bottom: 0.5rem;
}}
.npp-card p {{
  color: var(--npp-text-muted);
  margin-bottom: 1rem;
}}

.npp-button, button, input[type="submit"] {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: var(--npp-primary);
  color: #ffffff;
  padding: 0.7rem 1.4rem;
  border-radius: 8px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
  text-decoration: none !important;
}}
.npp-button:hover, button:hover {{
  background: var(--npp-primary-hover);
  transform: translateY(-1px);
}}
.npp-button-secondary {{
  background: transparent;
  color: var(--npp-text);
  border: 1px solid var(--npp-border);
}}
.npp-button-secondary:hover {{
  background: var(--npp-surface);
  color: var(--npp-accent);
}}

.npp-badge {{
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  background: rgba(99, 102, 241, 0.15);
  color: var(--npp-primary);
  border: 1px solid rgba(99, 102, 241, 0.3);
}}

.npp-alert {{
  padding: 1rem 1.25rem;
  border-radius: 10px;
  margin-bottom: 1rem;
  border: 1px solid var(--npp-border);
  background: var(--npp-surface);
}}

/* Form elements */
input[type="text"], input[type="email"], input[type="password"], input[type="number"], select, textarea {{
  width: 100%;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border: 1px solid var(--npp-border);
  background: var(--npp-surface);
  color: var(--npp-text);
  margin-bottom: 1rem;
  outline: none;
  transition: border-color 0.2s;
}}
input:focus, select:focus, textarea:focus {{
  border-color: var(--npp-primary);
}}

/* Tables */
table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  border-radius: 8px;
  overflow: hidden;
}}
th, td {{
  padding: 0.85rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--npp-border);
}}
th {{
  background: var(--npp-surface);
  font-weight: 600;
}}
tr:hover {{
  background: rgba(255,255,255,0.02);
}}

/* Footer */
footer, .npp-footer {{
  margin-top: auto;
  padding: 2.5rem 1.5rem;
  border-top: 1px solid var(--npp-border);
  text-align: center;
  color: var(--npp-text-muted);
  background: var(--npp-surface);
}}
"""
