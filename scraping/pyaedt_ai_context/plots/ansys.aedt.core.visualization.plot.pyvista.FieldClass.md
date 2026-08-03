---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.FieldClass.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# FieldClass 

class ansys.aedt.core.visualization.plot.pyvista.FieldClass(_path_ , _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _headers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _show_edge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to manage Field data to be plotted in pyvista. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the field has to be plotted log or not. The default value is `True`. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fields coordinates units. The default value is `"meter"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color map of field plot. The default value is `"rainbow"`. 

**label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. The default value is `"Field"`. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. The default value is `1e-3`. 

**headers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of lines to of the file containing header info that has to be removed. The default value is `2`.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import FieldClass
>>> obj = FieldClass()

```
Copy to clipboard
Attributes  
| [`FieldClass.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir "ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# FieldClass 

class ansys.aedt.core.visualization.plot.pyvista.FieldClass(_path_ , _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _headers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _show_edge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to manage Field data to be plotted in pyvista. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the field has to be plotted log or not. The default value is `True`. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fields coordinates units. The default value is `"meter"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color map of field plot. The default value is `"rainbow"`. 

**label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. The default value is `"Field"`. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. The default value is `1e-3`. 

**headers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of lines to of the file containing header info that has to be removed. The default value is `2`.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import FieldClass
>>> obj = FieldClass()

```
Copy to clipboard
Attributes  
| [`FieldClass.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir "ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.FieldClass.rst.txt)

# FieldClass 

class ansys.aedt.core.visualization.plot.pyvista.FieldClass(_path_ , _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _headers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _show_edge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to manage Field data to be plotted in pyvista. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the field has to be plotted log or not. The default value is `True`. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fields coordinates units. The default value is `"meter"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color map of field plot. The default value is `"rainbow"`. 

**label**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. The default value is `"Field"`. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. The default value is `1e-3`. 

**headers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of lines to of the file containing header info that has to be removed. The default value is `2`.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import FieldClass
>>> obj = FieldClass()

```
Copy to clipboard
Attributes  
| [`FieldClass.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir "ansys.aedt.core.visualization.plot.pyvista.FieldClass.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |