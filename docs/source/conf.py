# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = "Projet orchestration"
copyright = "2026, julie"
author = "julie"
release = "0"


sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../app_api"))
sys.path.insert(0, os.path.abspath("../../app_front"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",  # Pour extraire la doc du code
    "sphinx.ext.napoleon",  # Pour supporter les docstrings style oogle/NumPy
    "sphinx.ext.mathjax",  # Pour latex
    "sphinx.ext.viewcode",  # pour afficher code source
    "myst_parser",  # pour le markdown
]

templates_path = ["_templates"]
exclude_patterns = []

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
