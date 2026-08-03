---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_field_file_on_grid.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_field_file_on_grid 

PostProcessor3DLayout.export_field_file_on_grid(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Cartesian'_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file on a grid based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the grid to export. The default is `"Cartesian"`. 

**grid_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the center of the grid. The default is `[0, 0, 0]`. This parameter is disabled if `gridtype= "Cartesian"`. 

**grid_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the starting point of the grid. The default is `[0, 0, 0]`. 

**grid_stop**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the stopping point of the grid. The default is `[0, 0, 0]`. 

**grid_step**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the step size of the grid. The default is `[0, 0, 0]`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Field file path when succeeded.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ExportOnGrid

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> var = hfss.available_variations.nominal_values
>>> setup = "Setup1 : LastAdaptive"
>>> path = "Field.fld"
>>> hfss.post.export_field_file_on_grid("E", setup, var, path, "Cartesian", [0, 0, 0], intrinsics="8GHz")

```
Copy to clipboard
# export_field_file_on_grid 

PostProcessor3DLayout.export_field_file_on_grid(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Cartesian'_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file on a grid based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the grid to export. The default is `"Cartesian"`. 

**grid_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the center of the grid. The default is `[0, 0, 0]`. This parameter is disabled if `gridtype= "Cartesian"`. 

**grid_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the starting point of the grid. The default is `[0, 0, 0]`. 

**grid_stop**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the stopping point of the grid. The default is `[0, 0, 0]`. 

**grid_step**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the step size of the grid. The default is `[0, 0, 0]`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Field file path when succeeded.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ExportOnGrid

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> var = hfss.available_variations.nominal_values
>>> setup = "Setup1 : LastAdaptive"
>>> path = "Field.fld"
>>> hfss.post.export_field_file_on_grid("E", setup, var, path, "Cartesian", [0, 0, 0], intrinsics="8GHz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_field_file_on_grid.rst.txt)

# export_field_file_on_grid 

PostProcessor3DLayout.export_field_file_on_grid(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Cartesian'_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file on a grid based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the grid to export. The default is `"Cartesian"`. 

**grid_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the center of the grid. The default is `[0, 0, 0]`. This parameter is disabled if `gridtype= "Cartesian"`. 

**grid_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the starting point of the grid. The default is `[0, 0, 0]`. 

**grid_stop**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the stopping point of the grid. The default is `[0, 0, 0]`. 

**grid_step**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The `[x, y, z]` coordinates for the step size of the grid. The default is `[0, 0, 0]`. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity is a vector. The default is `False`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Field file path when succeeded.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.ExportOnGrid

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> var = hfss.available_variations.nominal_values
>>> setup = "Setup1 : LastAdaptive"
>>> path = "Field.fld"
>>> hfss.post.export_field_file_on_grid("E", setup, var, path, "Cartesian", [0, 0, 0], intrinsics="8GHz")

```
Copy to clipboard