---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.change_region_padding.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# change_region_padding 

Modeler3D.change_region_padding(_padding_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _padding_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _direction : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _region_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region padding settings. 

Parameters: 
     

**padding_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding value (with unit if necessary). A list of padding values must have corresponding elements in `padding_type` and `direction` arguments. 

**padding_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding type. Available options are `"Percentage Offset"`, `"Transverse Percentage Offset"`, `"Absolute Offset"`, `"Absolute Position"`. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction to which apply the padding settings. A direction can be `"+X"`, `"-X"`, “+Y”`, `"-Y"`, `"+Z"` or `"-Z"`. Default is `None`, in which case all the directions are used (in the order written in the previous sentence). 

**region_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.change_region_padding("10mm", padding_type="Absolute Offset", direction="-X")

```
Copy to clipboard
# change_region_padding 

Modeler3D.change_region_padding(_padding_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _padding_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _direction : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _region_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region padding settings. 

Parameters: 
     

**padding_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding value (with unit if necessary). A list of padding values must have corresponding elements in `padding_type` and `direction` arguments. 

**padding_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding type. Available options are `"Percentage Offset"`, `"Transverse Percentage Offset"`, `"Absolute Offset"`, `"Absolute Position"`. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction to which apply the padding settings. A direction can be `"+X"`, `"-X"`, “+Y”`, `"-Y"`, `"+Z"` or `"-Z"`. Default is `None`, in which case all the directions are used (in the order written in the previous sentence). 

**region_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.change_region_padding("10mm", padding_type="Absolute Offset", direction="-X")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.change_region_padding.rst.txt)

# change_region_padding 

Modeler3D.change_region_padding(_padding_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _padding_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _direction : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _region_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region padding settings. 

Parameters: 
     

**padding_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding value (with unit if necessary). A list of padding values must have corresponding elements in `padding_type` and `direction` arguments. 

**padding_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Padding type. Available options are `"Percentage Offset"`, `"Transverse Percentage Offset"`, `"Absolute Offset"`, `"Absolute Position"`. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction to which apply the padding settings. A direction can be `"+X"`, `"-X"`, “+Y”`, `"-Y"`, `"+Z"` or `"-Z"`. Default is `None`, in which case all the directions are used (in the order written in the previous sentence). 

**region_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.change_region_padding("10mm", padding_type="Absolute Offset", direction="-X")

```
Copy to clipboard