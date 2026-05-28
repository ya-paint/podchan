import sys
import os

# -- Path setup -----------------------------------------------------
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -------------------------------------------
project = 'podchan'
author = 'podchan'
copyright = '2026, podchan'
language = 'ja'

# -- General configuration -----------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output ---------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']