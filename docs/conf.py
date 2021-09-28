# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import django

if os.getenv("READTHEDOCS", default=True) == True:
    sys.path.insert(0, os.path.abspath(".."))
    os.environ["DJANGO_READ_DOT_ENV_FILE"] = "True"
    os.environ["USE_DOCKER"] = "no"
else:
    sys.path.insert(0, os.path.abspath("/app"))
os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ["CELERY_BROKER_URL"] = os.getenv("REDIS_URL", "redis://redis:6379")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

# -- Project information -----------------------------------------------------

project = "DRF Boilerplate"
copyright = """2021, Shubham"""
author = "Shubham"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.png"

html_theme_options = {
    "theme_dev_mode": False,
    "path_to_docs": "docs",
    "repository_url": "https://github.com/executablebooks/sphinx-book-theme",
    "repository_branch": "gh-pages",  # For testing

    # "use_edit_page_button": True,
    # "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "launch_buttons": {
        "jupyterhub_url": "https://{your-binderhub-url}"
    },
    # "logo_only": True,
    # For testing
    # "use_fullscreen_button": False,
    # "home_page_in_toc": True,
    # "single_page": True,
    # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
    "extra_navbar": "<a href='https://example.com'>Your Website</a>",
    "show_navbar_depth": 2,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The master toctree document.
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = ['.rst', '.md']
