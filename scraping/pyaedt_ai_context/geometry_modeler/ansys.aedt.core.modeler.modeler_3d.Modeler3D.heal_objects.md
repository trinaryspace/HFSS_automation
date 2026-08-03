---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.heal_objects.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# heal_objects 

Modeler3D.heal_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _auto_heal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerant_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _simplify_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tighten_gaps : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _heal_to_solid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _stop_after_first_stitch_error : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _max_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _explode_and_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _geometry_simplification_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_generated_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _simplify_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _tighten_gaps_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-05_, _remove_silver_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _silver_face_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_edge_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_face_area_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _bounding_box_scale_factor : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _remove_holes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_chamfers : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_blends : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hole_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _chamfer_width_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _blend_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _allowable_surface_area_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _allowable_volume_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Repair invalid geometry entities for the selected objects within the specified tolerance settings. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to analyze. 

**auto_heal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Auto heal option. Default value is `True`. 

**tolerant_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tolerant stitch for manual healing. The default is `True`. 

**simplify_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Simplify geometry for manual healing. The default is `True`. 

**tighten_gaps**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tighten gaps for manual healing. The default is `True`. 

**heal_to_solid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Heal to solid for manual healing. The default is `False`. 

**stop_after_first_stitch_error**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stop after first stitch error for manual healing. The default is `False`. 

**max_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Max stitch tolerance for manual healing. The default is `0.001`. 

**explode_and_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Explode and stitch for manual healing. The default is `True`. 

**geometry_simplification_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Geometry simplification tolerance for manual healing in mm. The default is `1`. 

**maximum_generated_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum generated radius for manual healing in mm. The default is `1`. 

**simplify_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Simplify type for manual healing. The default is `0` which refers to `Curves`. Other available values are `1` for `Surfaces` and `2` for `Both`. 

**tighten_gaps_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tighten gaps width for manual healing in mm. The default is `0.00001`. 

**remove_silver_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove silver faces for manual healing. The default is `True`. 

**remove_small_edges**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small edges faces for manual healing. The default is `True`. 

**remove_small_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small faces for manual healing. The default is `True`. 

**silver_face_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_edge_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_face_area_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm^2. The default is `1`. 

**bounding_box_scale_factor**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Bounding box scaling factor for manual healing. The default is `0`. 

**remove_holes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove holes for manual healing. The default is `True`. 

**remove_chamfers**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove chamfers for manual healing. The default is``True``. 

**remove_blends**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove blends for manual healing. The default is `True`. 

**hole_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Hole radius tolerance for manual healing in mm. The default is `1`. 

**chamfer_width_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Chamfer width tolerance for manual healing in mm. The default is `1`. 

**blend_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Blend radius tolerance for manual healing in mm. The default is `1`. 

**allowable_surface_area_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable surface area for manual healing in mm. The default is `1`. 

**allowable_volume_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable volume change for manual healing in mm. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.heal_objects(assignment="Box1")

```
Copy to clipboard
# heal_objects 

Modeler3D.heal_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _auto_heal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerant_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _simplify_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tighten_gaps : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _heal_to_solid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _stop_after_first_stitch_error : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _max_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _explode_and_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _geometry_simplification_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_generated_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _simplify_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _tighten_gaps_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-05_, _remove_silver_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _silver_face_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_edge_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_face_area_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _bounding_box_scale_factor : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _remove_holes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_chamfers : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_blends : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hole_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _chamfer_width_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _blend_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _allowable_surface_area_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _allowable_volume_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Repair invalid geometry entities for the selected objects within the specified tolerance settings. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to analyze. 

**auto_heal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Auto heal option. Default value is `True`. 

**tolerant_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tolerant stitch for manual healing. The default is `True`. 

**simplify_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Simplify geometry for manual healing. The default is `True`. 

**tighten_gaps**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tighten gaps for manual healing. The default is `True`. 

**heal_to_solid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Heal to solid for manual healing. The default is `False`. 

**stop_after_first_stitch_error**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stop after first stitch error for manual healing. The default is `False`. 

**max_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Max stitch tolerance for manual healing. The default is `0.001`. 

**explode_and_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Explode and stitch for manual healing. The default is `True`. 

**geometry_simplification_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Geometry simplification tolerance for manual healing in mm. The default is `1`. 

**maximum_generated_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum generated radius for manual healing in mm. The default is `1`. 

**simplify_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Simplify type for manual healing. The default is `0` which refers to `Curves`. Other available values are `1` for `Surfaces` and `2` for `Both`. 

**tighten_gaps_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tighten gaps width for manual healing in mm. The default is `0.00001`. 

**remove_silver_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove silver faces for manual healing. The default is `True`. 

**remove_small_edges**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small edges faces for manual healing. The default is `True`. 

**remove_small_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small faces for manual healing. The default is `True`. 

**silver_face_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_edge_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_face_area_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm^2. The default is `1`. 

**bounding_box_scale_factor**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Bounding box scaling factor for manual healing. The default is `0`. 

**remove_holes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove holes for manual healing. The default is `True`. 

**remove_chamfers**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove chamfers for manual healing. The default is``True``. 

**remove_blends**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove blends for manual healing. The default is `True`. 

**hole_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Hole radius tolerance for manual healing in mm. The default is `1`. 

**chamfer_width_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Chamfer width tolerance for manual healing in mm. The default is `1`. 

**blend_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Blend radius tolerance for manual healing in mm. The default is `1`. 

**allowable_surface_area_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable surface area for manual healing in mm. The default is `1`. 

**allowable_volume_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable volume change for manual healing in mm. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.heal_objects(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.heal_objects.rst.txt)

# heal_objects 

Modeler3D.heal_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _auto_heal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerant_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _simplify_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tighten_gaps : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _heal_to_solid : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _stop_after_first_stitch_error : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _max_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _explode_and_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _geometry_simplification_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_generated_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _simplify_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _tighten_gaps_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-05_, _remove_silver_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_edges : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_small_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _silver_face_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_edge_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _small_face_area_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _bounding_box_scale_factor : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _remove_holes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_chamfers : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _remove_blends : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hole_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _chamfer_width_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _blend_radius_tolerance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _allowable_surface_area_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _allowable_volume_change : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Repair invalid geometry entities for the selected objects within the specified tolerance settings. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of object names to analyze. 

**auto_heal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Auto heal option. Default value is `True`. 

**tolerant_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tolerant stitch for manual healing. The default is `True`. 

**simplify_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Simplify geometry for manual healing. The default is `True`. 

**tighten_gaps**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Tighten gaps for manual healing. The default is `True`. 

**heal_to_solid**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Heal to solid for manual healing. The default is `False`. 

**stop_after_first_stitch_error**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Stop after first stitch error for manual healing. The default is `False`. 

**max_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Max stitch tolerance for manual healing. The default is `0.001`. 

**explode_and_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Explode and stitch for manual healing. The default is `True`. 

**geometry_simplification_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Geometry simplification tolerance for manual healing in mm. The default is `1`. 

**maximum_generated_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum generated radius for manual healing in mm. The default is `1`. 

**simplify_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Simplify type for manual healing. The default is `0` which refers to `Curves`. Other available values are `1` for `Surfaces` and `2` for `Both`. 

**tighten_gaps_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tighten gaps width for manual healing in mm. The default is `0.00001`. 

**remove_silver_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove silver faces for manual healing. The default is `True`. 

**remove_small_edges**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small edges faces for manual healing. The default is `True`. 

**remove_small_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove small faces for manual healing. The default is `True`. 

**silver_face_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_edge_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm. The default is `1`. 

**small_face_area_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Silver face tolerance for manual healing in mm^2. The default is `1`. 

**bounding_box_scale_factor**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Bounding box scaling factor for manual healing. The default is `0`. 

**remove_holes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove holes for manual healing. The default is `True`. 

**remove_chamfers**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove chamfers for manual healing. The default is``True``. 

**remove_blends**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Remove blends for manual healing. The default is `True`. 

**hole_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Hole radius tolerance for manual healing in mm. The default is `1`. 

**chamfer_width_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Chamfer width tolerance for manual healing in mm. The default is `1`. 

**blend_radius_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Blend radius tolerance for manual healing in mm. The default is `1`. 

**allowable_surface_area_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable surface area for manual healing in mm. The default is `1`. 

**allowable_volume_change**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Allowable volume change for manual healing in mm. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.heal_objects(assignment="Box1")

```
Copy to clipboard