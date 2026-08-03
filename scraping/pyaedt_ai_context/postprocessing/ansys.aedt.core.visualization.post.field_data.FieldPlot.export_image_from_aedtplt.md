---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_image_from_aedtplt 

FieldPlot.export_image_from_aedtplt(_export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save an image of the active plot using PyVista.
Note
This method only works if the CPython with PyVista module is installed. 

Parameters: 
     

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path where image will be saved. The default is `None` which export file in working_directory. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot mesh. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output min. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output max. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.UpdateAllFieldsPlots
>>> oModule.UpdateQuantityFieldsPlots
>>> oModule.ExportFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image_from_aedtplt(export_path="directory", view="iso")

```
Copy to clipboard
# export_image_from_aedtplt 

FieldPlot.export_image_from_aedtplt(_export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save an image of the active plot using PyVista.
Note
This method only works if the CPython with PyVista module is installed. 

Parameters: 
     

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path where image will be saved. The default is `None` which export file in working_directory. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot mesh. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output min. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output max. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.UpdateAllFieldsPlots
>>> oModule.UpdateQuantityFieldsPlots
>>> oModule.ExportFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image_from_aedtplt(export_path="directory", view="iso")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.export_image_from_aedtplt.rst.txt)

# export_image_from_aedtplt 

FieldPlot.export_image_from_aedtplt(_export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'isometric'_, _plot_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _scale_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _scale_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save an image of the active plot using PyVista.
Note
This method only works if the CPython with PyVista module is installed. 

Parameters: 
     

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path where image will be saved. The default is `None` which export file in working_directory. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, `"yz"`. 

**plot_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot mesh. 

**scale_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output min. 

**scale_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scale output max. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to exported file if successful.
References

```
>>> oModule.UpdateAllFieldsPlots
>>> oModule.UpdateQuantityFieldsPlots
>>> oModule.ExportFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.export_image_from_aedtplt(export_path="directory", view="iso")

```
Copy to clipboard