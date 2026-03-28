#!/usr/bin/env python3.8
# coding: latin-1

# (c) Massachusetts Institute of Technology 2015-2018
# (c) Brian Teague 2018-2022
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

"""
cytoflow.views
--------------

This package contains all `cytoflow` views -- classes
implementing `IView` whose ``plot()`` function plots an
experiment.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn defaults.  this is mostly for the Jupyter notebook;
# these settings can be overridden in the GUI
sns.set(context = "paper", style = "whitegrid", 
        rc = {"xtick.bottom": True, "ytick.left": True})

# make sure that non-seaborn plots use constrained layout
plt.rcParams['figure.constrained_layout.use'] = True

# monkey-patch seaborn
def add_legend(self, legend_data=None, title=None, label_order=None,
                   adjust_subtitles=False, **kwargs):
        """Draw a legend, maybe placing it outside axes and resizing the figure.

        Parameters
        ----------
        legend_data : dict
            Dictionary mapping label names (or two-element tuples where the
            second element is a label name) to matplotlib artist handles. The
            default reads from ``self._legend_data``.
        title : string
            Title for the legend. The default reads from ``self._hue_var``.
        label_order : list of labels
            The order that the legend entries should appear in. The default
            reads from ``self.hue_names``.
        adjust_subtitles : bool
            If True, modify entries with invisible artists to left-align
            the labels and set the font size to that of a title.
        kwargs : key, value pairings
            Other keyword arguments are passed to the underlying legend methods
            on the Figure or Axes object.

        Returns
        -------
        self : Grid instance
            Returns self for easy chaining.

        """
        # Find the data for the legend
        if legend_data is None:
            legend_data = self._legend_data
        if label_order is None:
            if self.hue_names is None:
                label_order = list(legend_data.keys())
            else:
                label_order = list(map(sns.utils.to_utf8, self.hue_names))

        blank_handle = mpl.patches.Patch(alpha=0, linewidth=0)
        handles = [legend_data.get(lab, blank_handle) for lab in label_order]
        title = self._hue_var if title is None else title
        title_size = mpl.rcParams["legend.title_fontsize"]

        # Unpack nested labels from a hierarchical legend
        labels = []
        for entry in label_order:
            if isinstance(entry, tuple):
                _, label = entry
            else:
                label = entry
            labels.append(label)

        # Set default legend kwargs
        kwargs.setdefault("scatterpoints", 1)

        kwargs.setdefault("frameon", False)
        kwargs.setdefault("loc", "outside center right")

        # Draw a full-figure legend outside the grid
        figlegend = self._figure.legend(handles, labels, **kwargs)

        self._legend = figlegend
        figlegend.set_title(title, prop={"size": title_size})

        if adjust_subtitles:
            sns.utils.adjust_legend_subtitles(figlegend)

        return self

def tight_layout(self, *args, **kwargs):
    pass

from seaborn.axisgrid import Grid
Grid.tight_layout = tight_layout
Grid.add_legend = add_legend

from .i_view import IView
from .i_selectionview import ISelectionView

from .base_views import Base1DView, Base2DView

from .histogram import HistogramView
from .scatterplot import ScatterplotView
from .densityplot import DensityView
from .stats_1d import Stats1DView
from .stats_2d import Stats2DView
from .bar_chart import BarChartView
from .matrix import MatrixView
from .mst import MSTView
from .kde_1d import Kde1DView
from .kde_2d import Kde2DView
from .histogram_2d import Histogram2DView
from .violin import ViolinPlotView
from .table import TableView
from .long_table import LongTableView
from .radviz import RadvizView
from .parallel_coords import ParallelCoordinatesView
from .export_fcs import ExportFCS
