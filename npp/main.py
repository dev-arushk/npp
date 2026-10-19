"""
Main entry point for N++ CLI.
"""

import sys
import os

# Reconfigure Windows console I/O to UTF-8
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure package is on sys.path
sys.path.insert(0, os.path.dirname(__file__))

from npp.cli import main

if __name__ == "__main__":
    main()
