---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_model_picture.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_model_picture 

PostProcessorIcepak.export_model_picture(_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _field_selections : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the model to a `JPG` file.
Note
This method works only when AEDT is running in the graphical mode. 

Parameters: 
     

**full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to export image of a selection or not. Default is None. 

**field_selections**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Fields plots to add to the image. Default is None. “all” for all field plots. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Picture orientation. Orientation can be one of “top”, “bottom”, “right”, “left”, “front”, “back”, “trimetric”, “dimetric”, “isometric”, or a custom orientation that you added to the Orientation List. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 0 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 0 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(non_graphical=False)
>>> output_file = q3d.post.export_model_picture(full_name=Path(q3d.working_directory) / "images1.jpg")

```
Copy to clipboard
# export_model_picture 

PostProcessorIcepak.export_model_picture(_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _field_selections : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the model to a `JPG` file.
Note
This method works only when AEDT is running in the graphical mode. 

Parameters: 
     

**full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to export image of a selection or not. Default is None. 

**field_selections**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Fields plots to add to the image. Default is None. “all” for all field plots. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Picture orientation. Orientation can be one of “top”, “bottom”, “right”, “left”, “front”, “back”, “trimetric”, “dimetric”, “isometric”, or a custom orientation that you added to the Orientation List. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 0 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 0 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(non_graphical=False)
>>> output_file = q3d.post.export_model_picture(full_name=Path(q3d.working_directory) / "images1.jpg")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_model_picture.rst.txt)

# export_model_picture 

PostProcessorIcepak.export_model_picture(_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_region : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _field_selections : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the model to a `JPG` file.
Note
This method works only when AEDT is running in the graphical mode. 

Parameters: 
     

**full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**show_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the axes. The default is `True`. 

**show_grid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the grid. The default is `True`. 

**show_ruler**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the ruler. The default is `True`. 

**show_region**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the region or not. The default is `Default`. 

**selections**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to export image of a selection or not. Default is None. 

**field_selections**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Fields plots to add to the image. Default is None. “all” for all field plots. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Picture orientation. Orientation can be one of “top”, “bottom”, “right”, “left”, “front”, “back”, “trimetric”, “dimetric”, “isometric”, or a custom orientation that you added to the Orientation List. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 0 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 0 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportModelImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(non_graphical=False)
>>> output_file = q3d.post.export_model_picture(full_name=Path(q3d.working_directory) / "images1.jpg")

```
Copy to clipboard