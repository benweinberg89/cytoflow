#!/usr/bin/env python3.4
# coding: latin-1

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

from traits.api import provides
from traitsui.api import View, Item, EnumEditor, VGroup, TextEditor
from envisage.api import Plugin, contributes_to
from pyface.api import ImageResource

from ..view_plugins import ViewHandler
from ..view_plugins.histogram import HistogramParamsHandler
from ..editors import SubsetListEditor, ColorTextEditor, ExtendableEnumEditor, InstanceHandlerEditor
from ..workflow.operations import ThresholdWorkflowOp, ThresholdSelectionView
from ..subset_controllers import subset_handler_factory

from .i_op_plugin import IOperationPlugin, OP_PLUGIN_EXT
from .op_plugin_base import OpHandler, shared_op_traits_view, PluginHelpMixin


class ThresholdHandler(OpHandler):
    operation_traits_view = \
        View(Item('name',
                  editor = TextEditor(auto_set = False)),
             Item('channel',
                  editor=EnumEditor(name='context_handler.previous_channels'),
                  label = "Channel"),
             Item('threshold',
                  editor = TextEditor(auto_set = False)),
             shared_op_traits_view) 
        
        
class ThresholdViewHandler(ViewHandler):
    view_traits_view = \
        View(VGroup(
             VGroup(Item('channel', 
                         label = "Channel",
                         style = "readonly"),
                    Item('threshold', 
                         label = "Threshold",
                         style = "readonly"),
                    Item('scale'),
                    Item('huefacet',
                         editor=ExtendableEnumEditor(name='context_handler.previous_conditions_names',
                                                     extra_items = {"None" : ""}),
                         label="Color\nFacet"),
                    label = "Threshold Setup View",
                    show_border = False),
             VGroup(Item('subset_list',
                         show_label = False,
                         editor = SubsetListEditor(conditions = "context_handler.previous_conditions",
                                                   editor = InstanceHandlerEditor(view = 'subset_view',
                                                                                  handler_factory = subset_handler_factory),
                                                   mutable = False)),
                    label = "Subset",
                    show_border = False,
                    show_labels = False),
             Item('context.view_warning',
                  resizable = True,
                  visible_when = 'context.view_warning',
                  editor = ColorTextEditor(foreground_color = "#000000",
                                          background_color = "#ffff99")),
             Item('context.view_error',
                  resizable = True,
                  visible_when = 'context.view_error',
                  editor = ColorTextEditor(foreground_color = "#000000",
                                           background_color = "#ff9191"))))
        
    view_params_view = \
        View(Item('plot_params',
                  editor = InstanceHandlerEditor(view = 'view_params_view',
                                                 handler_factory = HistogramParamsHandler),
                  style = 'custom',
                  show_label = False))


@provides(IOperationPlugin)
class ThresholdPlugin(Plugin, PluginHelpMixin):
    
    id = 'edu.mit.synbio.cytoflowgui.op_plugins.threshold'
    operation_id = 'edu.mit.synbio.cytoflow.operations.threshold'
    view_id = 'edu.mit.synbio.cytoflow.views.threshold'

    short_name = "Threshold"
    menu_group = "Gates"
    
    def get_operation(self):
        return ThresholdWorkflowOp()
    
    def get_handler(self, model, context):
        if isinstance(model, ThresholdWorkflowOp):
            return ThresholdHandler(model = model, context = context)
        elif isinstance(model, ThresholdSelectionView):
            return ThresholdViewHandler(model = model, context = context)

    def get_icon(self):
        return ImageResource('threshold')
    
    @contributes_to(OP_PLUGIN_EXT)
    def get_plugin(self):
        return self

