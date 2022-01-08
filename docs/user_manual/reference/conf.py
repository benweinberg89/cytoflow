# -*- coding: utf-8 -*-

# (c) Massachusetts Institute of Technology 2015-2018
# (c) Brian Teague 2018-2021
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# CytoFlow documentation build configuration file, created by
# sphinx-quickstart on Fri Mar  6 19:42:50 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, glob, pathlib, shutil

# select the 'null' pyface toolkit. an exception is raised if the qt toolkit
# is subsequently imported, but that's better than trying to actually create
# a Qt app if PyQt is accidentally imported.

from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'null'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../..')) # the docs/ directory
sys.path.insert(0, os.path.abspath('../../..')) # the base project directory

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinxext.plot_directive',
    # 'fulltoc'
]

# autodoc options
autodoc_member_order = 'bysource'
autodoc_mock_imports = ['traitsui', 'pyface']

# napoleon options
napoleon_use_param = False

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False
plot_working_directory = pathlib.Path(__file__).parents[3].joinpath('cytoflow', 'tests', 'data').as_posix()

plot_pre_code = "import matplotlib.pyplot as plt; plt.switch_backend('agg')"
# plot_rcparams = {'backend' : "Agg"}
# plot_apply_rcparams = True
# plot_pre_code = 'import matplotlib; matplotlib.use("Agg")'

# intersphinx config
intersphinx_mapping = {'pandas' : ('https://pandas.pydata.org/pandas-docs/stable/', None),
                       'envisage' : ('https://docs.enthought.com/envisage/', None),
                       'traits' : ('https://docs.enthought.com/traits/', None)} 


# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'reference'

# General information about the project.
project = u'Cytoflow'
import time
copyright = u'Massachusetts Institute of Technology 2015-2018, Brian Teague 2018-{}'.format(time.strftime("%Y"))

# Configure the sidebar

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# this is a workaround so we can use versioneer without importing the entire cytoflow module
# import versioneer
# 
# old_cwd = os.getcwd()
# os.chdir(os.path.split(old_cwd)[0])
# 
# # The short X.Y version.
# version = versioneer.get_version()
# # The full version, including alpha/beta/rc tags.
# release = versioneer.get_version()
# 
# os.chdir(old_cwd)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '*.logicle_ext*.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'show_powered_by' : False}

html_sidebars = { '**': ['about.html', 'globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'cytoflow'


def setup(app):
    app.connect('builder-inited', set_builder_config)
#     app.connect('build-finished', copy_embedded_help)

    sys.modules['sys'].IN_SPHINX = True
    
        
def set_builder_config(app):
    app.builder.config.html_copy_source = False
    app.builder.config.html_show_sourcelink = False
    app.builder.config.html_show_copyright = False
    app.builder.config.html_show_sphinx = False
    
    app.builder.copysource = False
    app.builder.add_permalinks = False
    app.builder.embedded = True
    app.builder.download_support = False
    app.builder.search = False
    
    app.config.plot_include_source = False

def copy_embedded_help(app, exc):  # @UnusedVariable
    if app.builder.name != 'embedded_help':
        return
    
    dest_dir = pathlib.Path(__file__).parents[1].joinpath('cytoflowgui', 'help')
    print("Copying {} to {}".format(app.outdir, dest_dir))
    shutil.rmtree(dest_dir, ignore_errors = True)
    shutil.copytree(app.outdir, dest_dir)
    
    img_dir_in = pathlib.Path(app.srcdir).joinpath('images').as_posix()
    img_dir_out = pathlib.Path(dest_dir).joinpath('_images').as_posix()
    
    try:
        filelist = glob.glob(os.path.join(img_dir_in, "*"))
        for f in filelist:
            print(f)
            shutil.copy(f, img_dir_out)
    except FileNotFoundError:
        pass
