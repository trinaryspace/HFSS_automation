---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.convert_to_selections.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# convert_to_selections 

Modeler3D.convert_to_selections(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _return_list : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Convert modeler objects.
This method converts modeler object or IDs to the corresponding output according to the following scheme:  
| `assignment`  | Return value  |  
| --- | --- |  
> 

`int` object name (str)
    
> `Object3D` object name (str) `FacePrimitive` int, face ID `EdgePrimitive` int, edge ID `str` return the same `str`
  * If `object_id` is a list, a list is returned according

to the table. If `object_id` is a single value, a list of `length == 1` is returned (default).
  * If the second argument, `return_list`, is set to False (default), a

string is returned with elements separated by a comma (,)”. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more object IDs whose name will be returned. A list can contain both strings (object names) and integers (object IDs). 

**return_list**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `option` 
    
Whether to return a list of the selections. The default is `False`, in which case a string of the selections is returned. If `True`, a list of the selections is returned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the objects corresponding to the one or more object IDs passed as arguments.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.convert_to_selections(assignment="Box1")

```
Copy to clipboard
# convert_to_selections 

Modeler3D.convert_to_selections(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _return_list : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Convert modeler objects.
This method converts modeler object or IDs to the corresponding output according to the following scheme:  
| `assignment`  | Return value  |  
| --- | --- |  
> 

`int` object name (str)
    
> `Object3D` object name (str) `FacePrimitive` int, face ID `EdgePrimitive` int, edge ID `str` return the same `str`
  * If `object_id` is a list, a list is returned according

to the table. If `object_id` is a single value, a list of `length == 1` is returned (default).
  * If the second argument, `return_list`, is set to False (default), a

string is returned with elements separated by a comma (,)”. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more object IDs whose name will be returned. A list can contain both strings (object names) and integers (object IDs). 

**return_list**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `option` 
    
Whether to return a list of the selections. The default is `False`, in which case a string of the selections is returned. If `True`, a list of the selections is returned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the objects corresponding to the one or more object IDs passed as arguments.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.convert_to_selections(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.convert_to_selections.rst.txt)

# convert_to_selections 

Modeler3D.convert_to_selections(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _return_list : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Convert modeler objects.
This method converts modeler object or IDs to the corresponding output according to the following scheme:  
| `assignment`  | Return value  |  
| --- | --- |  
> 

`int` object name (str)
    
> `Object3D` object name (str) `FacePrimitive` int, face ID `EdgePrimitive` int, edge ID `str` return the same `str`
  * If `object_id` is a list, a list is returned according

to the table. If `object_id` is a single value, a list of `length == 1` is returned (default).
  * If the second argument, `return_list`, is set to False (default), a

string is returned with elements separated by a comma (,)”. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more object IDs whose name will be returned. A list can contain both strings (object names) and integers (object IDs). 

**return_list**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `option` 
    
Whether to return a list of the selections. The default is `False`, in which case a string of the selections is returned. If `True`, a list of the selections is returned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the objects corresponding to the one or more object IDs passed as arguments.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.convert_to_selections(assignment="Box1")

```
Copy to clipboard