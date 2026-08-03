---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_image 

FieldPlot.export_image(_full_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_region : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the active plot to an image file.
Note
There are some limitations on HFSS 3D Layout plots. 

full_pathstr or pathlib.Path, optional 
    
Path for saving the image file. PNG and GIF formats are supported. The default is `None` which export file in working_directory. 

widthint, optional 
    
Plot Width. 

heightint, optional 
    
Plot height. 

orientationstr, optional 
    
View of the exported plot. Options are `isometric`, `top`, `bottom`, `right`, `left`, `front`, `back`, and any custom orientation. 

display_wireframebool, optional 
    
Whether the objects has to be put in wireframe mode. Default is `True`. 

selectionsstr or List[str], optional 
    
Objects to fit for the zoom on the exported image. Default is None in which case all the objects in the design will be shown. One important note is that, if the fieldplot extension is larger than the selection extension, the fieldplot extension will be the one considered for the zoom of the exported image. 

show_regionbool, optional 
    
Whether to include the air region in the exported image. Default is `True`. 

show_gridbool, optional 
    
Whether to display the background grid in the exported image. Default is `True`. 

show_axisbool, optional 
    
Whether to display the axis triad in the exported image. Default is `True`. 

show_rulerbool, optional 
    
Whether to display the ruler in the exported image. Default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile
>>> oModule.ExportPlotImageWithViewToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image(full_path="example.png", width="2mm")

```
Copy to clipboard
# export_image 

FieldPlot.export_image(_full_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_region : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the active plot to an image file.
Note
There are some limitations on HFSS 3D Layout plots. 

full_pathstr or pathlib.Path, optional 
    
Path for saving the image file. PNG and GIF formats are supported. The default is `None` which export file in working_directory. 

widthint, optional 
    
Plot Width. 

heightint, optional 
    
Plot height. 

orientationstr, optional 
    
View of the exported plot. Options are `isometric`, `top`, `bottom`, `right`, `left`, `front`, `back`, and any custom orientation. 

display_wireframebool, optional 
    
Whether the objects has to be put in wireframe mode. Default is `True`. 

selectionsstr or List[str], optional 
    
Objects to fit for the zoom on the exported image. Default is None in which case all the objects in the design will be shown. One important note is that, if the fieldplot extension is larger than the selection extension, the fieldplot extension will be the one considered for the zoom of the exported image. 

show_regionbool, optional 
    
Whether to include the air region in the exported image. Default is `True`. 

show_gridbool, optional 
    
Whether to display the background grid in the exported image. Default is `True`. 

show_axisbool, optional 
    
Whether to display the axis triad in the exported image. Default is `True`. 

show_rulerbool, optional 
    
Whether to display the ruler in the exported image. Default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile
>>> oModule.ExportPlotImageWithViewToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image(full_path="example.png", width="2mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image.rst.txt)

# export_image 

FieldPlot.export_image(_full_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _display_wireframe : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _selections : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_region : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_grid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_ruler : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the active plot to an image file.
Note
There are some limitations on HFSS 3D Layout plots. 

full_pathstr or pathlib.Path, optional 
    
Path for saving the image file. PNG and GIF formats are supported. The default is `None` which export file in working_directory. 

widthint, optional 
    
Plot Width. 

heightint, optional 
    
Plot height. 

orientationstr, optional 
    
View of the exported plot. Options are `isometric`, `top`, `bottom`, `right`, `left`, `front`, `back`, and any custom orientation. 

display_wireframebool, optional 
    
Whether the objects has to be put in wireframe mode. Default is `True`. 

selectionsstr or List[str], optional 
    
Objects to fit for the zoom on the exported image. Default is None in which case all the objects in the design will be shown. One important note is that, if the fieldplot extension is larger than the selection extension, the fieldplot extension will be the one considered for the zoom of the exported image. 

show_regionbool, optional 
    
Whether to include the air region in the exported image. Default is `True`. 

show_gridbool, optional 
    
Whether to display the background grid in the exported image. Default is `True`. 

show_axisbool, optional 
    
Whether to display the axis triad in the exported image. Default is `True`. 

show_rulerbool, optional 
    
Whether to display the ruler in the exported image. Default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.ExportPlotImageToFile
>>> oModule.ExportModelImageToFile
>>> oModule.ExportPlotImageWithViewToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image(full_path="example.png", width="2mm")

```
Copy to clipboard