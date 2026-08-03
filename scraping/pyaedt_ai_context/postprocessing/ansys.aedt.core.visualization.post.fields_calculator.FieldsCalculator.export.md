---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export 

FieldsCalculator.export(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sample_points : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the field quantity at the top of the register to a file, mapping it to a grid of points.
Two options are available for defining the grid points on which to export:
>   * 

Input grid points from file: maps the field quantity to a customized grid of points.
    
> Before using this command, create a file containing the points and units.
>   * 

Calculate grid points: maps the field quantity to a three-dimensional Cartesian grid.
    
> You specify the dimensions and spacing of the grid in the x, y, and z directions, with units. The initial units are taken from the model. Other grid options are Cylindrical, in which case rho, phi and z directions must be specified, or Spherical, in which case r, theta and phi directions must be specified.
> 

If you want to adopt the first option you must provide either the file containing the grid of points or a list of sample points in `sample_points`. In the latter case, a new file is created in the working directory called “temp_points.pts” that will be automatically written with the data points provided and consequently imported. If you want to adopt the second option you must provide the grid type (Cartesian, Cylindrical or Spherical). If `grid_center`, `grid_start` or `grid_stop` are not provided the default values are used. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`
  * `"Time"`
  * `"Phase"`

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the file with sample points or list of the sample points. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the grid to export. The options are:
  * `Cartesian`
  * `Cylindrical`
  * `Spherical`

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

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.export(quantity=1)

```
Copy to clipboard
# export 

FieldsCalculator.export(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sample_points : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the field quantity at the top of the register to a file, mapping it to a grid of points.
Two options are available for defining the grid points on which to export:
>   * 

Input grid points from file: maps the field quantity to a customized grid of points.
    
> Before using this command, create a file containing the points and units.
>   * 

Calculate grid points: maps the field quantity to a three-dimensional Cartesian grid.
    
> You specify the dimensions and spacing of the grid in the x, y, and z directions, with units. The initial units are taken from the model. Other grid options are Cylindrical, in which case rho, phi and z directions must be specified, or Spherical, in which case r, theta and phi directions must be specified.
> 

If you want to adopt the first option you must provide either the file containing the grid of points or a list of sample points in `sample_points`. In the latter case, a new file is created in the working directory called “temp_points.pts” that will be automatically written with the data points provided and consequently imported. If you want to adopt the second option you must provide the grid type (Cartesian, Cylindrical or Spherical). If `grid_center`, `grid_start` or `grid_stop` are not provided the default values are used. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`
  * `"Time"`
  * `"Phase"`

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the file with sample points or list of the sample points. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the grid to export. The options are:
  * `Cartesian`
  * `Cylindrical`
  * `Spherical`

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

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.export(quantity=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export.rst.txt)

# export 

FieldsCalculator.export(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sample_points : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _export_with_sample_points : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _export_in_si_system : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_field_in_reference : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _grid_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_stop : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _grid_step : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AllObjects'_, _objects_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Vol'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the field quantity at the top of the register to a file, mapping it to a grid of points.
Two options are available for defining the grid points on which to export:
>   * 

Input grid points from file: maps the field quantity to a customized grid of points.
    
> Before using this command, create a file containing the points and units.
>   * 

Calculate grid points: maps the field quantity to a three-dimensional Cartesian grid.
    
> You specify the dimensions and spacing of the grid in the x, y, and z directions, with units. The initial units are taken from the model. Other grid options are Cylindrical, in which case rho, phi and z directions must be specified, or Spherical, in which case r, theta and phi directions must be specified.
> 

If you want to adopt the first option you must provide either the file containing the grid of points or a list of sample points in `sample_points`. In the latter case, a new file is created in the working directory called “temp_points.pts” that will be automatically written with the data points provided and consequently imported. If you want to adopt the second option you must provide the grid type (Cartesian, Cylindrical or Spherical). If `grid_center`, `grid_start` or `grid_stop` are not provided the default values are used. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format `"solution : sweep"`. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all variation variables with their values. The default is `None`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of objects to export. The default is `"AllObjects"`. 

**objects_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of objects to export. The default is `"Vol"`. Options are `"Surf"` for surface and `"Vol"` for volume. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string.
If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`
  * `"Time"`
  * `"Phase"`

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**sample_points**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the file with sample points or list of the sample points. 

**export_with_sample_points**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include the sample points in the file to export. The default is `True`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference coordinate system in the file to export. The default is `"Global"`. 

**export_in_si_system**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the provided sample points are defined in the SI system or model units. The default is `True`. 

**export_field_in_reference**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the field in reference coordinate system. The default is `True`. 

**grid_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the grid to export. The options are:
  * `Cartesian`
  * `Cylindrical`
  * `Spherical`

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

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.export(quantity=1)

```
Copy to clipboard