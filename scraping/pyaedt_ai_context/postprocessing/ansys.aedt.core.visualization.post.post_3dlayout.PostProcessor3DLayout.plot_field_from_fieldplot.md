---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.plot_field_from_fieldplot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# plot_field_from_fieldplot 

PostProcessor3DLayout.plot_field_from_fieldplot(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _mesh_plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _plot_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _plot_cad_objs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _dark_mode : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_bounding : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _file_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'case'_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Export a field plot to an image file (JPG or PNG) using Python PyVista.
This method does not support streamlines plot.
Note
The PyVista module rebuilds the mesh and the overlap fields on the mesh. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the field plot to export. 

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path for saving the image file. The default is `""`. 

**mesh_plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create and plot the mesh over the fields. The default is `False`. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. Options are `"jpg"`, `"png"`, `"svg"`, and `"webp"`. The default is `"jpg"`. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the plot. The default is `"Temperature"`. 

**plot_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot folder to update before exporting the field. The default is `None`, in which case all plot folders are updated. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export Image without plotting on UI. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Minimum value. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Maximum value. 

**plot_cad_objs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include objects in the plot. The default is `True`. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot fields in log scale. The default is `True`. 

**dark_mode**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the model in dark mode or not. The default is `False`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes grid or not. The default is `False`. 

**show_bounding**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes bounding box or not. The default is `False`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend. The default is `True`. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot each object separately, which can require more time to export from AEDT. The default is `True`. 

**file_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File format to export the plot to. The default is `"case". Options are ``"aedtplt"` and `"case"`. If the active design is a Q3D design, the file format is automatically set to `"fldplt"`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_field_from_fieldplot(plot_name=1)

```
Copy to clipboard
# plot_field_from_fieldplot 

PostProcessor3DLayout.plot_field_from_fieldplot(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _mesh_plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _plot_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _plot_cad_objs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _dark_mode : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_bounding : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _file_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'case'_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Export a field plot to an image file (JPG or PNG) using Python PyVista.
This method does not support streamlines plot.
Note
The PyVista module rebuilds the mesh and the overlap fields on the mesh. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the field plot to export. 

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path for saving the image file. The default is `""`. 

**mesh_plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create and plot the mesh over the fields. The default is `False`. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. Options are `"jpg"`, `"png"`, `"svg"`, and `"webp"`. The default is `"jpg"`. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the plot. The default is `"Temperature"`. 

**plot_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot folder to update before exporting the field. The default is `None`, in which case all plot folders are updated. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export Image without plotting on UI. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Minimum value. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Maximum value. 

**plot_cad_objs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include objects in the plot. The default is `True`. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot fields in log scale. The default is `True`. 

**dark_mode**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the model in dark mode or not. The default is `False`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes grid or not. The default is `False`. 

**show_bounding**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes bounding box or not. The default is `False`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend. The default is `True`. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot each object separately, which can require more time to export from AEDT. The default is `True`. 

**file_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File format to export the plot to. The default is `"case". Options are ``"aedtplt"` and `"case"`. If the active design is a Q3D design, the file format is automatically set to `"fldplt"`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_field_from_fieldplot(plot_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.plot_field_from_fieldplot.rst.txt)

# plot_field_from_fieldplot 

PostProcessor3DLayout.plot_field_from_fieldplot(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _mesh_plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _plot_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _plot_cad_objs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _dark_mode : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_bounding : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _file_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'case'_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Export a field plot to an image file (JPG or PNG) using Python PyVista.
This method does not support streamlines plot.
Note
The PyVista module rebuilds the mesh and the overlap fields on the mesh. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the field plot to export. 

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path for saving the image file. The default is `""`. 

**mesh_plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create and plot the mesh over the fields. The default is `False`. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. Options are `"jpg"`, `"png"`, `"svg"`, and `"webp"`. The default is `"jpg"`. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the plot. The default is `"Temperature"`. 

**plot_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot folder to update before exporting the field. The default is `None`, in which case all plot folders are updated. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export Image without plotting on UI. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Minimum value. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fix the Scale Maximum value. 

**plot_cad_objs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include objects in the plot. The default is `True`. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot fields in log scale. The default is `True`. 

**dark_mode**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the model in dark mode or not. The default is `False`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes grid or not. The default is `False`. 

**show_bounding**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the axes bounding box or not. The default is `False`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend. The default is `True`. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot each object separately, which can require more time to export from AEDT. The default is `True`. 

**file_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File format to export the plot to. The default is `"case". Options are ``"aedtplt"` and `"case"`. If the active design is a Q3D design, the file format is automatically set to `"fldplt"`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_field_from_fieldplot(plot_name=1)

```
Copy to clipboard