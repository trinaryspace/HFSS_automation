---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_air_region.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_air_region 

Modeler2D.create_air_region(_x_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _x_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_percentage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an air region. 

Parameters: 
     

**x_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +X direction in modeler units. If str, padding with units in the +X direction. The default is `0`. 

**y_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Y direction in modeler units. If str, padding with units in the +Y direction. The default is `0`. 

**z_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Z direction in modeler units. If str, padding with units in the +Z direction. The default is `0`. 

**x_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -X direction in modeler units. If str, padding with units in the -X direction. The default is `0`. 

**y_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Y direction in modeler units. If str, padding with units in the -Y direction. The default is `0`. 

**z_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Z direction in modeler units. If str, padding with units in the -Z direction. The default is `0`. 

**is_percentage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Region definition in percentage or absolute value. The default is True`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_air_region(x_pos=[1, 2, 3], y_pos=[1, 2, 3])

```
Copy to clipboard
# create_air_region 

Modeler2D.create_air_region(_x_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _x_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_percentage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an air region. 

Parameters: 
     

**x_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +X direction in modeler units. If str, padding with units in the +X direction. The default is `0`. 

**y_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Y direction in modeler units. If str, padding with units in the +Y direction. The default is `0`. 

**z_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Z direction in modeler units. If str, padding with units in the +Z direction. The default is `0`. 

**x_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -X direction in modeler units. If str, padding with units in the -X direction. The default is `0`. 

**y_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Y direction in modeler units. If str, padding with units in the -Y direction. The default is `0`. 

**z_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Z direction in modeler units. If str, padding with units in the -Z direction. The default is `0`. 

**is_percentage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Region definition in percentage or absolute value. The default is True`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_air_region(x_pos=[1, 2, 3], y_pos=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_air_region.rst.txt)

# create_air_region 

Modeler2D.create_air_region(_x_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_pos : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _x_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_neg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_percentage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an air region. 

Parameters: 
     

**x_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +X direction in modeler units. If str, padding with units in the +X direction. The default is `0`. 

**y_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Y direction in modeler units. If str, padding with units in the +Y direction. The default is `0`. 

**z_pos**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the +Z direction in modeler units. If str, padding with units in the +Z direction. The default is `0`. 

**x_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -X direction in modeler units. If str, padding with units in the -X direction. The default is `0`. 

**y_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Y direction in modeler units. If str, padding with units in the -Y direction. The default is `0`. 

**z_neg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
If float, padding in the -Z direction in modeler units. If str, padding with units in the -Z direction. The default is `0`. 

**is_percentage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Region definition in percentage or absolute value. The default is True`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_air_region(x_pos=[1, 2, 3], y_pos=[1, 2, 3])

```
Copy to clipboard