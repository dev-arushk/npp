"""
Main entry point for N++ CLI.
"""

import sys
import os

# Ensure package is on sys.path
sys.path.insert(0, os.path.dirname(__file__))

from npp.cli import main

if __name__ == "__main__":
    main()
