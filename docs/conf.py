# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'plurk.py'
copyright = '2023, James Chien'
author = 'James Chien'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autoapi_dirs = ['../src']
autoapi_type = 'python'
autoapi_template_dir = '_templates/autoapi'
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'imported-members',
]
autodoc_typehints = 'signature'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'plurk.py',

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    # 'base_url': 'https://project.github.io/project',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/shc261392/plurk.py',
    'repo_name': 'plurk.py',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}
