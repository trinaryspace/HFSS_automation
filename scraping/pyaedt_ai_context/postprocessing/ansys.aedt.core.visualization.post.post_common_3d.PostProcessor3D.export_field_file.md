---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.export_field_file.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_field_file 

PostProcessor3D.export_field_file(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _sample_points_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sample_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution: sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None` which export a file named `"<setup_name>.fld"` in working_directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"` - `"Time"` - `"Phase"` If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file with sample points. The default is `None`. 

**sample_points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the sample points. The default is `None`. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.CalculatorWrite
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> # Intrinsics is provided as a string.
>>> fld_file1 = "test_fld_hfss1.fld"
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file1, assignment="Box1", intrinsics="1GHz")
>>> # Intrinsics is provided as dictionary. Phase is automatically assigned to 0deg.
>>> fld_file2 = "test_fld_hfss2.fld"
>>> m3d.post.export_field_file(
...     quantity="Mag_E", output_file=fld_file2, assignment="Box1", intrinsics={"frequency": "1GHz"}
... )
>>> # Intrinsics is provided as dictionary. Phase is provided.
>>> m3d.post.export_field_file(
...     quantity="Mag_E",
...     output_file=fld_file2,
...     assignment="Box1",
...     intrinsics={"frequency": "1GHz", "phase": "30deg"},
... )
>>> # Intrinsics is not provided. It is computed from the setup arguments.
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file2, assignment="Box1")

```
Copy to clipboard
# export_field_file 

PostProcessor3D.export_field_file(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _sample_points_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sample_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution: sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None` which export a file named `"<setup_name>.fld"` in working_directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"` - `"Time"` - `"Phase"` If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file with sample points. The default is `None`. 

**sample_points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the sample points. The default is `None`. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.CalculatorWrite
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> # Intrinsics is provided as a string.
>>> fld_file1 = "test_fld_hfss1.fld"
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file1, assignment="Box1", intrinsics="1GHz")
>>> # Intrinsics is provided as dictionary. Phase is automatically assigned to 0deg.
>>> fld_file2 = "test_fld_hfss2.fld"
>>> m3d.post.export_field_file(
...     quantity="Mag_E", output_file=fld_file2, assignment="Box1", intrinsics={"frequency": "1GHz"}
... )
>>> # Intrinsics is provided as dictionary. Phase is provided.
>>> m3d.post.export_field_file(
...     quantity="Mag_E",
...     output_file=fld_file2,
...     assignment="Box1",
...     intrinsics={"frequency": "1GHz", "phase": "30deg"},
... )
>>> # Intrinsics is not provided. It is computed from the setup arguments.
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file2, assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.export_field_file.rst.txt)

# export_field_file 

PostProcessor3D.export_field_file(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _sample_points_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sample_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Use the field calculator to create a field file based on a solution and variation. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. For example, `"Temp"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution: sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None` which export a file named `"<setup_name>.fld"` in working_directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"` - `"Time"` - `"Phase"` If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file with sample points. The default is `None`. 

**sample_points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the sample points. The default is `None`. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EnterQty
>>> oModule.CopyNamedExprToStack
>>> oModule.CalcOp
>>> oModule.EnterQty
>>> oModule.EnterVol
>>> oModule.CalculatorWrite
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> # Intrinsics is provided as a string.
>>> fld_file1 = "test_fld_hfss1.fld"
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file1, assignment="Box1", intrinsics="1GHz")
>>> # Intrinsics is provided as dictionary. Phase is automatically assigned to 0deg.
>>> fld_file2 = "test_fld_hfss2.fld"
>>> m3d.post.export_field_file(
...     quantity="Mag_E", output_file=fld_file2, assignment="Box1", intrinsics={"frequency": "1GHz"}
... )
>>> # Intrinsics is provided as dictionary. Phase is provided.
>>> m3d.post.export_field_file(
...     quantity="Mag_E",
...     output_file=fld_file2,
...     assignment="Box1",
...     intrinsics={"frequency": "1GHz", "phase": "30deg"},
... )
>>> # Intrinsics is not provided. It is computed from the setup arguments.
>>> m3d.post.export_field_file(quantity="Mag_E", output_file=fld_file2, assignment="Box1")

```
Copy to clipboard