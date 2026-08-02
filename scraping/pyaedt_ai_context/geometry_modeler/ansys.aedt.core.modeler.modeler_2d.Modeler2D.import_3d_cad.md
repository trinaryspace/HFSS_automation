---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.import_3d_cad.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# import_3d_cad 

Modeler2D.import_3d_cad(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _healing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _refresh_all_ids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_materials : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _group_by_assembly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_group : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_disjoints_lumped_object : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_free_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _point_coincidence_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _reduce_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reduce_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _reduce_error : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _merge_planar_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _input_file_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a CAD model. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name of the CAD file. 

**healing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to perform healing. The default is `False`, in which case healing is not performed. 

**refresh_all_ids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refresh all IDs after the CAD file is loaded. The default is `True`. Refreshing IDs can take a lot of time in a big project. 

**import_materials**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") `optional` 
    
Either to import material names from the file or not if presents. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") ,optional 
    
Either to import lightweight or not. 

**group_by_assembly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either import by sub-assembly or individual parts. The default is `False`. 

**create_group**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create a new group of imported objects. The default is `True`. 

**separate_disjoints_lumped_object**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to automatically separate disjoint parts. The default is `False`. 

**import_free_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to import free surfaces parts. The default is `False`. 

**point_coincidence_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance on point. Default is `1e-6`. 

**reduce_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reduce the stl file on import or not. Default is `True`. 

**reduce_percentage**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl reduce percentage. Default is `0`. 

**reduce_error**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl error percentage during reduce operation. Default is `0`. 

**merge_planar_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stl automatic planar face merge during import. Default is `True`. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stl import angle in radians for which faces will be considered planar. Default is `2e-2`. 

**input_file_unit: str, optional**
    
Unit for the stl file. The default is `"Auto"`, which means that the unit is automatically detected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Import

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.import_3d_cad(input_file="example.txt")

```
Copy to clipboard
# import_3d_cad 

Modeler2D.import_3d_cad(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _healing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _refresh_all_ids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_materials : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _group_by_assembly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_group : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_disjoints_lumped_object : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_free_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _point_coincidence_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _reduce_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reduce_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _reduce_error : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _merge_planar_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _input_file_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a CAD model. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name of the CAD file. 

**healing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to perform healing. The default is `False`, in which case healing is not performed. 

**refresh_all_ids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refresh all IDs after the CAD file is loaded. The default is `True`. Refreshing IDs can take a lot of time in a big project. 

**import_materials**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") `optional` 
    
Either to import material names from the file or not if presents. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") ,optional 
    
Either to import lightweight or not. 

**group_by_assembly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either import by sub-assembly or individual parts. The default is `False`. 

**create_group**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create a new group of imported objects. The default is `True`. 

**separate_disjoints_lumped_object**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to automatically separate disjoint parts. The default is `False`. 

**import_free_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to import free surfaces parts. The default is `False`. 

**point_coincidence_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance on point. Default is `1e-6`. 

**reduce_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reduce the stl file on import or not. Default is `True`. 

**reduce_percentage**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl reduce percentage. Default is `0`. 

**reduce_error**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl error percentage during reduce operation. Default is `0`. 

**merge_planar_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stl automatic planar face merge during import. Default is `True`. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stl import angle in radians for which faces will be considered planar. Default is `2e-2`. 

**input_file_unit: str, optional**
    
Unit for the stl file. The default is `"Auto"`, which means that the unit is automatically detected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Import

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.import_3d_cad(input_file="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.import_3d_cad.rst.txt)

# import_3d_cad 

Modeler2D.import_3d_cad(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _healing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _refresh_all_ids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_materials : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _group_by_assembly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_group : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_disjoints_lumped_object : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_free_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _point_coincidence_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _reduce_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reduce_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _reduce_error : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _merge_planar_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _input_file_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a CAD model. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name of the CAD file. 

**healing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to perform healing. The default is `False`, in which case healing is not performed. 

**refresh_all_ids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refresh all IDs after the CAD file is loaded. The default is `True`. Refreshing IDs can take a lot of time in a big project. 

**import_materials**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") `optional` 
    
Either to import material names from the file or not if presents. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") ,optional 
    
Either to import lightweight or not. 

**group_by_assembly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either import by sub-assembly or individual parts. The default is `False`. 

**create_group**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create a new group of imported objects. The default is `True`. 

**separate_disjoints_lumped_object**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to automatically separate disjoint parts. The default is `False`. 

**import_free_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to import free surfaces parts. The default is `False`. 

**point_coincidence_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance on point. Default is `1e-6`. 

**reduce_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reduce the stl file on import or not. Default is `True`. 

**reduce_percentage**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl reduce percentage. Default is `0`. 

**reduce_error**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Stl error percentage during reduce operation. Default is `0`. 

**merge_planar_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stl automatic planar face merge during import. Default is `True`. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stl import angle in radians for which faces will be considered planar. Default is `2e-2`. 

**input_file_unit: str, optional**
    
Unit for the stl file. The default is `"Auto"`, which means that the unit is automatically detected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Import

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.import_3d_cad(input_file="example.txt")

```
Copy to clipboard