# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'CodeRefinery manuals'
copyright = '2018-2023, The CodeRefinery team'
author = 'The CodeRefinery team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx_togglebutton',
    'sphinx_coderefinery_branding',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv*',
                    'README.md',  # index.md linked to this, for web serving
                    ]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

master_doc = 'index'

html_context = {'display_github': True,
                'github_user': 'coderefinery',
                'github_repo': 'manuals',
                'github_version': 'master/',
               }

import os
if os.environ.get('GITHUB_REF', '') == 'refs/heads/master':
    html_js_files = [
        ('https://plausible.cs.aalto.fi/js/script.js', {"data-domain": "coderefinery.github.io", "defer": "defer"}),
    ]

epub_basename='CodeRefineryManuals'
latex_documents = [
    (master_doc, 'CodeRefineryManuals.tex', project, author, 'manual')
    ]

# https://github.com/sphinx-contrib/emojicodes/pull/22/files
latex_engine = 'xelatex'

myst_enable_extensions = [
    'colon_fence',   # ::: can be used instead of ``` for better rendering
    ]
