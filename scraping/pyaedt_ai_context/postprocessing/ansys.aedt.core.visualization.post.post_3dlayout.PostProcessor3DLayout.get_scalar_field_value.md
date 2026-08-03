---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.get_scalar_field_value.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_scalar_field_value 

PostProcessor3DLayout.get_scalar_field_value(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scalar_function : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Maximum'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _object_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'volume'_, _adjacent_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Use the field calculator to Compute Scalar of a Field. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**scalar_function**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The name of the scalar function. For example, `"Maximum"`, `"Integrate"`. The default is `"Maximum"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. e.g. `['power_block:=', ['0.6W'], 'power_source:=', ['0.15W']]` The default is `None`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`.
If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. For example, `"Box1"`. The default is `"AllObjects"`. 

**object_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the object - `"volume"`, `"surface"`, `"point"`. The default is `"volume"`. 

**adjacent_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
To query quantity value on adjacent side for object_type = “surface”, pass `True`. The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Scalar field value.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ClcEval
>>> GetTopEntryValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is explicitly provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is automatically computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name)

```
Copy to clipboard
# get_scalar_field_value 

PostProcessor3DLayout.get_scalar_field_value(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scalar_function : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Maximum'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _object_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'volume'_, _adjacent_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Use the field calculator to Compute Scalar of a Field. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**scalar_function**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The name of the scalar function. For example, `"Maximum"`, `"Integrate"`. The default is `"Maximum"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. e.g. `['power_block:=', ['0.6W'], 'power_source:=', ['0.15W']]` The default is `None`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`.
If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. For example, `"Box1"`. The default is `"AllObjects"`. 

**object_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the object - `"volume"`, `"surface"`, `"point"`. The default is `"volume"`. 

**adjacent_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
To query quantity value on adjacent side for object_type = “surface”, pass `True`. The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Scalar field value.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ClcEval
>>> GetTopEntryValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is explicitly provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is automatically computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.get_scalar_field_value.rst.txt)

# get_scalar_field_value 

PostProcessor3DLayout.get_scalar_field_value(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scalar_function : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Maximum'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _object_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'volume'_, _adjacent_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Use the field calculator to Compute Scalar of a Field. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**scalar_function**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The name of the scalar function. For example, `"Maximum"`, `"Integrate"`. The default is `"Maximum"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. e.g. `['power_block:=', ['0.6W'], 'power_source:=', ['0.15W']]` The default is `None`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`.
If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. For example, `"Box1"`. The default is `"AllObjects"`. 

**object_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the object - `"volume"`, `"surface"`, `"point"`. The default is `"volume"`. 

**adjacent_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
To query quantity value on adjacent side for object_type = “surface”, pass `True`. The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Scalar field value.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ClcEval
>>> GetTopEntryValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is explicitly provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is automatically computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_cutplane(cutlist, quantity_name, setup_name)

```
Copy to clipboard