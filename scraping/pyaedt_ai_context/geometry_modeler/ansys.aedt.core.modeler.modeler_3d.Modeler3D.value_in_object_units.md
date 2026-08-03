---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.value_in_object_units.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# value_in_object_units 

Modeler3D.value_in_object_units(_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert one or more strings for numerical lengths to floating point values. 

Parameters: 
     

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
One or more strings for numerical lengths. For example, `"10mm"` or `["10mm", "12mm", "14mm"]`. When a list is given, the entire list is converted. 

Returns: 
     

`List` `of` `floats` 
    
Defined in model units `ansys.aedt.core.modeler.model_units`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.value_in_object_units(value=1)

```
Copy to clipboard
# value_in_object_units 

Modeler3D.value_in_object_units(_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert one or more strings for numerical lengths to floating point values. 

Parameters: 
     

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
One or more strings for numerical lengths. For example, `"10mm"` or `["10mm", "12mm", "14mm"]`. When a list is given, the entire list is converted. 

Returns: 
     

`List` `of` `floats` 
    
Defined in model units `ansys.aedt.core.modeler.model_units`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.value_in_object_units(value=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.value_in_object_units.rst.txt)

# value_in_object_units 

Modeler3D.value_in_object_units(_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert one or more strings for numerical lengths to floating point values. 

Parameters: 
     

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
One or more strings for numerical lengths. For example, `"10mm"` or `["10mm", "12mm", "14mm"]`. When a list is given, the entire list is converted. 

Returns: 
     

`List` `of` `floats` 
    
Defined in model units `ansys.aedt.core.modeler.model_units`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.value_in_object_units(value=1)

```
Copy to clipboard