---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# FieldPlot 

class ansys.aedt.core.visualization.post.field_data.FieldPlot(_postprocessor_ , _objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _surfaces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _lines : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cutplanes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _seeding_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LayerNetsExtFace'_) 
    
Provides for creating and editing field plots. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot or the name of the object. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()

```
Copy to clipboard
Methods  
| [`FieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.create.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.create "ansys.aedt.core.visualization.post.field_data.FieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`FieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.delete.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.delete "ansys.aedt.core.visualization.post.field_data.FieldPlot.delete")()  | Delete the field plot.  |  
| [`FieldPlot.export_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image")([full_path, width, ...])  | Export the active plot to an image file.  |  
| [`FieldPlot.export_image_from_aedtplt`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt")([...])  | Save an image of the active plot using PyVista.  |  
| [`FieldPlot.get_points_value`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value "ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value")(points[, ...])  | Get points data from field plot.  |  
| [`FieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update "ansys.aedt.core.visualization.post.field_data.FieldPlot.update")()  | Update the field plot.  |  
| [`FieldPlot.update_field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings")()  | Modify the field plot settings.  |  
Attributes  
| [`FieldPlot.field_line_trace_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings")  | Settings for the field line traces in the plot.  |  
| --- | --- |  
| [`FieldPlot.field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings")  | Field Plot Settings.  |  
| [`FieldPlot.filter_boxes`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes "ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes")  | Volumes on which filter the plot.  |  
| [`FieldPlot.folder_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings")  | Get the folder settings.  |  
| [`FieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| [`FieldPlot.plotGeomInfo`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo")  | Plot geometry information.  |  
| [`FieldPlot.plotsettings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings")  | Plot settings.  |  
| [`FieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir "ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir")  | Shortcut for dir(self).  |  
| [`FieldPlot.surfacePlotInstruction`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction")  | Surface plot settings.  |  
| [`FieldPlot.surfacePlotInstructionLineTraces`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces")  | Surface plot settings for field line traces.  |  
# FieldPlot 

class ansys.aedt.core.visualization.post.field_data.FieldPlot(_postprocessor_ , _objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _surfaces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _lines : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cutplanes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _seeding_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LayerNetsExtFace'_) 
    
Provides for creating and editing field plots. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot or the name of the object. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()

```
Copy to clipboard
Methods  
| [`FieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.create.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.create "ansys.aedt.core.visualization.post.field_data.FieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`FieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.delete.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.delete "ansys.aedt.core.visualization.post.field_data.FieldPlot.delete")()  | Delete the field plot.  |  
| [`FieldPlot.export_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image")([full_path, width, ...])  | Export the active plot to an image file.  |  
| [`FieldPlot.export_image_from_aedtplt`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt")([...])  | Save an image of the active plot using PyVista.  |  
| [`FieldPlot.get_points_value`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value "ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value")(points[, ...])  | Get points data from field plot.  |  
| [`FieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update "ansys.aedt.core.visualization.post.field_data.FieldPlot.update")()  | Update the field plot.  |  
| [`FieldPlot.update_field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings")()  | Modify the field plot settings.  |  
Attributes  
| [`FieldPlot.field_line_trace_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings")  | Settings for the field line traces in the plot.  |  
| --- | --- |  
| [`FieldPlot.field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings")  | Field Plot Settings.  |  
| [`FieldPlot.filter_boxes`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes "ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes")  | Volumes on which filter the plot.  |  
| [`FieldPlot.folder_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings")  | Get the folder settings.  |  
| [`FieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| [`FieldPlot.plotGeomInfo`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo")  | Plot geometry information.  |  
| [`FieldPlot.plotsettings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings")  | Plot settings.  |  
| [`FieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir "ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir")  | Shortcut for dir(self).  |  
| [`FieldPlot.surfacePlotInstruction`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction")  | Surface plot settings.  |  
| [`FieldPlot.surfacePlotInstructionLineTraces`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces")  | Surface plot settings for field line traces.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.rst.txt)

# FieldPlot 

class ansys.aedt.core.visualization.post.field_data.FieldPlot(_postprocessor_ , _objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _surfaces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _lines : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cutplanes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _seeding_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _layer_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LayerNetsExtFace'_) 
    
Provides for creating and editing field plots. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot or the name of the object. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()

```
Copy to clipboard
Methods  
| [`FieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.create.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.create "ansys.aedt.core.visualization.post.field_data.FieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`FieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.delete.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.delete "ansys.aedt.core.visualization.post.field_data.FieldPlot.delete")()  | Delete the field plot.  |  
| [`FieldPlot.export_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image")([full_path, width, ...])  | Export the active plot to an image file.  |  
| [`FieldPlot.export_image_from_aedtplt`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt "ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt")([...])  | Save an image of the active plot using PyVista.  |  
| [`FieldPlot.get_points_value`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value "ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value")(points[, ...])  | Get points data from field plot.  |  
| [`FieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update "ansys.aedt.core.visualization.post.field_data.FieldPlot.update")()  | Update the field plot.  |  
| [`FieldPlot.update_field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.update_field_plot_settings")()  | Modify the field plot settings.  |  
Attributes  
| [`FieldPlot.field_line_trace_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_line_trace_plot_settings")  | Settings for the field line traces in the plot.  |  
| --- | --- |  
| [`FieldPlot.field_plot_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.field_plot_settings")  | Field Plot Settings.  |  
| [`FieldPlot.filter_boxes`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes "ansys.aedt.core.visualization.post.field_data.FieldPlot.filter_boxes")  | Volumes on which filter the plot.  |  
| [`FieldPlot.folder_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings "ansys.aedt.core.visualization.post.field_data.FieldPlot.folder_settings")  | Get the folder settings.  |  
| [`FieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.field_data.FieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| [`FieldPlot.plotGeomInfo`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotGeomInfo")  | Plot geometry information.  |  
| [`FieldPlot.plotsettings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings "ansys.aedt.core.visualization.post.field_data.FieldPlot.plotsettings")  | Plot settings.  |  
| [`FieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir "ansys.aedt.core.visualization.post.field_data.FieldPlot.public_dir")  | Shortcut for dir(self).  |  
| [`FieldPlot.surfacePlotInstruction`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstruction")  | Surface plot settings.  |  
| [`FieldPlot.surfacePlotInstructionLineTraces`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces.html#ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces "ansys.aedt.core.visualization.post.field_data.FieldPlot.surfacePlotInstructionLineTraces")  | Surface plot settings for field line traces.  |