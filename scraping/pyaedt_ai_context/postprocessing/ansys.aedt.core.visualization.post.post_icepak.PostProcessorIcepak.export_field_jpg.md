---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_field_jpg.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_field_jpg 

PostProcessorIcepak.export_field_jpg(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a field plot and coordinate system to a JPG file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name to save the JPG file to. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the folder plot. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the orientation to apply. The default is `"isometric"`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Width. The default is `1920`. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Height. The default is `1080`. 

**display_wireframe**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Display wireframe. The default is `True`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of objects to include in the plot.
    
Supported in 3D Field Plots only starting from 23R1. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. Supported in 3D Field Plots only starting from 23R1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_field_jpg(file_name=r"example.jpg", plot_name=1, folder_name="directory")

```
Copy to clipboard
# export_field_jpg 

PostProcessorIcepak.export_field_jpg(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a field plot and coordinate system to a JPG file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name to save the JPG file to. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the folder plot. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the orientation to apply. The default is `"isometric"`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Width. The default is `1920`. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Height. The default is `1080`. 

**display_wireframe**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Display wireframe. The default is `True`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of objects to include in the plot.
    
Supported in 3D Field Plots only starting from 23R1. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. Supported in 3D Field Plots only starting from 23R1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_field_jpg(file_name=r"example.jpg", plot_name=1, folder_name="directory")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_field_jpg.rst.txt)

# export_field_jpg 

PostProcessorIcepak.export_field_jpg(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a field plot and coordinate system to a JPG file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name to save the JPG file to. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the folder plot. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the orientation to apply. The default is `"isometric"`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Width. The default is `1920`. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Plot Height. The default is `1080`. 

**display_wireframe**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Display wireframe. The default is `True`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of objects to include in the plot.
    
Supported in 3D Field Plots only starting from 23R1. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. Supported in 3D Field Plots only starting from 23R1. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. Supported in 3D Field Plots only starting from 23R1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_field_jpg(file_name=r"example.jpg", plot_name=1, folder_name="directory")

```
Copy to clipboard