# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import sphinx_bootstrap_theme

sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pytest-kafka-consumer'
copyright = '2024, James Twose'
author = 'James Twose'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "numpydoc",
    "sphinx.ext.inheritance_diagram",
    "nbsphinx",
    "nbsphinx_link",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"

html_theme_options = {
    "source_link_position": "footer",
    "bootswatch_theme": "simplex",
    "navbar_title": "pytest-kafka-consumer",
    "navbar_sidebarrel": False,
    "bootstrap_version": "4",
    "nosidebar": True,
    "body_max_width": "100%"
}


# Add the custom css we wrote to the build
def setup(app):
    app.add_js_file("copybutton.js")
    app.add_css_file("custom.css")


# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False