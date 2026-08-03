---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# simplify_objects 

Modeler3D.simplify_objects(_assignment_ , _simplify_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Polygon Fit'_, _extrusion_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _clean_up : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _allow_splitting : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_bodies : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _clone_body : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _generate_primitive_history : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _interior_points_on_arc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _length_threshold_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 25_, _create_group_for_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Simplify command to converts complex objects into simpler primitives which are easy to mesh and solve. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to simplify. 

**simplify_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Simplify type. The default is `"Polygon Fit"`. Options are `"Bounding Box"`, `"Polygon Fit"`, and [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id1)”Primitive Fit”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id3). 

**extrusion_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Extrusion axis. The default is `"Auto"`. Options are `"Auto"`, `"X"`, `"Y"`, and `"Z"`. 

**clean_up**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clean up. The default is `True`. 

**allow_splitting**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to allow splitting. The default is `True`. 

**separate_bodies**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to separate bodies. The default is `True`. 

**clone_body**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the body. The default is `True`. 

**generate_primitive_history**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate primitive history. The default is `False`. If `True`, the history for the selected objects is purged. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id5)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id7) 

**interior_points_on_arc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Number points on curve. The default is `5`. 

**length_threshold_percentage**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length threshold percentage. The default is `25`. 

**create_group_for_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Create group for new objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.simplify_objects(assignment="Box1")

```
Copy to clipboard
# simplify_objects 

Modeler3D.simplify_objects(_assignment_ , _simplify_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Polygon Fit'_, _extrusion_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _clean_up : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _allow_splitting : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_bodies : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _clone_body : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _generate_primitive_history : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _interior_points_on_arc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _length_threshold_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 25_, _create_group_for_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Simplify command to converts complex objects into simpler primitives which are easy to mesh and solve. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to simplify. 

**simplify_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Simplify type. The default is `"Polygon Fit"`. Options are `"Bounding Box"`, `"Polygon Fit"`, and [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id1)”Primitive Fit”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id3). 

**extrusion_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Extrusion axis. The default is `"Auto"`. Options are `"Auto"`, `"X"`, `"Y"`, and `"Z"`. 

**clean_up**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clean up. The default is `True`. 

**allow_splitting**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to allow splitting. The default is `True`. 

**separate_bodies**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to separate bodies. The default is `True`. 

**clone_body**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the body. The default is `True`. 

**generate_primitive_history**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate primitive history. The default is `False`. If `True`, the history for the selected objects is purged. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id5)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id7) 

**interior_points_on_arc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Number points on curve. The default is `5`. 

**length_threshold_percentage**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length threshold percentage. The default is `25`. 

**create_group_for_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Create group for new objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.simplify_objects(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.rst.txt)

# simplify_objects 

Modeler3D.simplify_objects(_assignment_ , _simplify_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Polygon Fit'_, _extrusion_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _clean_up : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _allow_splitting : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _separate_bodies : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _clone_body : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _generate_primitive_history : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _interior_points_on_arc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _length_threshold_percentage : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 25_, _create_group_for_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Simplify command to converts complex objects into simpler primitives which are easy to mesh and solve. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to simplify. 

**simplify_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Simplify type. The default is `"Polygon Fit"`. Options are `"Bounding Box"`, `"Polygon Fit"`, and [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id1)”Primitive Fit”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id3). 

**extrusion_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Extrusion axis. The default is `"Auto"`. Options are `"Auto"`, `"X"`, `"Y"`, and `"Z"`. 

**clean_up**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clean up. The default is `True`. 

**allow_splitting**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to allow splitting. The default is `True`. 

**separate_bodies**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to separate bodies. The default is `True`. 

**clone_body**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the body. The default is `True`. 

**generate_primitive_history**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate primitive history. The default is `False`. If `True`, the history for the selected objects is purged. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id5)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.simplify_objects.html#id7) 

**interior_points_on_arc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Number points on curve. The default is `5`. 

**length_threshold_percentage**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length threshold percentage. The default is `25`. 

**create_group_for_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Create group for new objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.simplify_objects(assignment="Box1")

```
Copy to clipboard