---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_summary.FieldSummary.add_calculation.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_calculation 

FieldSummary.add_calculation(_entity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _normal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _mesh : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'All'_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AmbientTemp'_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an entry in the field summary calculation requests. 

Parameters: 
     

**entity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Type of entity to perform the calculation on. Options are
    
`"Boundary"`, `"Monitor`”, and `"Object"`. (`"Monitor"` is available in AEDT 2024 R1 and later.) 

**geometry**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Location to perform the calculation on. Options are `"Surface"` and `"Volume"`. 

**geometry_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Objects to perform the calculation on. If a list is provided, the calculation is performed on the combination of those objects. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quantity to compute. 

**normal**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `floats` 
    
Coordinate values for direction relative to normal. The default is `""`, in which case the normal to the face is used. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing which side of the face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and “Default”`. 

**mesh**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface meshes to use. The default is `"All"`. Options are `"All"` and `"Reduced"`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use in the calculation of the heat transfer coefficient. The default is `"AmbientTemp"`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.add_calculation(entity=1, geometry=1, geometry_name=["Box1"], quantity=1)

```
Copy to clipboard
# add_calculation 

FieldSummary.add_calculation(_entity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _normal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _mesh : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'All'_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AmbientTemp'_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an entry in the field summary calculation requests. 

Parameters: 
     

**entity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Type of entity to perform the calculation on. Options are
    
`"Boundary"`, `"Monitor`”, and `"Object"`. (`"Monitor"` is available in AEDT 2024 R1 and later.) 

**geometry**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Location to perform the calculation on. Options are `"Surface"` and `"Volume"`. 

**geometry_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Objects to perform the calculation on. If a list is provided, the calculation is performed on the combination of those objects. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quantity to compute. 

**normal**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `floats` 
    
Coordinate values for direction relative to normal. The default is `""`, in which case the normal to the face is used. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing which side of the face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and “Default”`. 

**mesh**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface meshes to use. The default is `"All"`. Options are `"All"` and `"Reduced"`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use in the calculation of the heat transfer coefficient. The default is `"AmbientTemp"`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.add_calculation(entity=1, geometry=1, geometry_name=["Box1"], quantity=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_summary.FieldSummary.add_calculation.rst.txt)

# add_calculation 

FieldSummary.add_calculation(_entity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _geometry_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _normal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _mesh : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'All'_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AmbientTemp'_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an entry in the field summary calculation requests. 

Parameters: 
     

**entity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Type of entity to perform the calculation on. Options are
    
`"Boundary"`, `"Monitor`”, and `"Object"`. (`"Monitor"` is available in AEDT 2024 R1 and later.) 

**geometry**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Location to perform the calculation on. Options are `"Surface"` and `"Volume"`. 

**geometry_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Objects to perform the calculation on. If a list is provided, the calculation is performed on the combination of those objects. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quantity to compute. 

**normal**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `floats` 
    
Coordinate values for direction relative to normal. The default is `""`, in which case the normal to the face is used. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing which side of the face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and “Default”`. 

**mesh**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface meshes to use. The default is `"All"`. Options are `"All"` and `"Reduced"`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use in the calculation of the heat transfer coefficient. The default is `"AmbientTemp"`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.add_calculation(entity=1, geometry=1, geometry_name=["Box1"], quantity=1)

```
Copy to clipboard