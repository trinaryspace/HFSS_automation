---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# add_field_from_data 

ModelPlotter.add_field_from_data(_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]]_, _fields_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _surface_mapping_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _show_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add field data to the scenario. 

Parameters: 
     

**coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list [x,y,z] coordinates. 

**fields_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list Fields Value. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if the field has to be plotted log or not. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fields coordinates units. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Color map of field plot. Default rainbow. 

**label_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. 

**surface_mapping_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_field_from_data(coordinates=[1, 2, 3], fields_data=["Box1"])

```
Copy to clipboard
# add_field_from_data 

ModelPlotter.add_field_from_data(_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]]_, _fields_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _surface_mapping_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _show_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add field data to the scenario. 

Parameters: 
     

**coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list [x,y,z] coordinates. 

**fields_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list Fields Value. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if the field has to be plotted log or not. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fields coordinates units. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Color map of field plot. Default rainbow. 

**label_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. 

**surface_mapping_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_field_from_data(coordinates=[1, 2, 3], fields_data=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data.rst.txt)

# add_field_from_data 

ModelPlotter.add_field_from_data(_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]]_, _fields_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _log_scale : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _coordinate_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'meter'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _color_map : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jet'_, _label_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Field'_, _surface_mapping_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _show_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add field data to the scenario. 

Parameters: 
     

**coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list [x,y,z] coordinates. 

**fields_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list Fields Value. 

**log_scale**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if the field has to be plotted log or not. 

**coordinate_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fields coordinates units. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. 

**color_map**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Color map of field plot. Default rainbow. 

**label_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field. 

**surface_mapping_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delauny tolerance value used for interpolating points. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_field_from_data(coordinates=[1, 2, 3], fields_data=["Box1"])

```
Copy to clipboard