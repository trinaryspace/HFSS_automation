---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_conical_rings.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_conical_rings 

Modeler3D.create_conical_rings(_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _bottom_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _top_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _cone_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ring_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create rings in a conical shape. 

Parameters: 
     

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate system of the axis. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position of the bottom of the cone. 

**bottom_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Bottom radius of the cone. 

**top_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Top radius of the cone. 

**cone_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cone. 

**ring_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ring height. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ring thickness. The default is `None`, in which case a 2D sheet is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cone. The default is `None`, in which case the default name is assigned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] `or` [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
List of 3D object or `False` if it fails.
References

```
>>> oEditor.CreatePolyline
>>> oEditor.SweepAroundAxis
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
This example shows how to create rings along Z axis with a cone shape.

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> cone_object = aedtapp.modeler.create_conical_rings(
...     axis="Z", origin=[0, 0, 0], bottom_radius=2, top_radius=3, cone_height=4, ring_height=0.1
... )

```
Copy to clipboard
# create_conical_rings 

Modeler3D.create_conical_rings(_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _bottom_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _top_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _cone_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ring_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create rings in a conical shape. 

Parameters: 
     

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate system of the axis. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position of the bottom of the cone. 

**bottom_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Bottom radius of the cone. 

**top_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Top radius of the cone. 

**cone_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cone. 

**ring_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ring height. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ring thickness. The default is `None`, in which case a 2D sheet is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cone. The default is `None`, in which case the default name is assigned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] `or` [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
List of 3D object or `False` if it fails.
References

```
>>> oEditor.CreatePolyline
>>> oEditor.SweepAroundAxis
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
This example shows how to create rings along Z axis with a cone shape.

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> cone_object = aedtapp.modeler.create_conical_rings(
...     axis="Z", origin=[0, 0, 0], bottom_radius=2, top_radius=3, cone_height=4, ring_height=0.1
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_conical_rings.rst.txt)

# create_conical_rings 

Modeler3D.create_conical_rings(_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _bottom_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _top_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _cone_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ring_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create rings in a conical shape. 

Parameters: 
     

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate system of the axis. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position of the bottom of the cone. 

**bottom_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Bottom radius of the cone. 

**top_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Top radius of the cone. 

**cone_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cone. 

**ring_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ring height. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ring thickness. The default is `None`, in which case a 2D sheet is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cone. The default is `None`, in which case the default name is assigned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] `or` [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
List of 3D object or `False` if it fails.
References

```
>>> oEditor.CreatePolyline
>>> oEditor.SweepAroundAxis
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
This example shows how to create rings along Z axis with a cone shape.

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> cone_object = aedtapp.modeler.create_conical_rings(
...     axis="Z", origin=[0, 0, 0], bottom_radius=2, top_radius=3, cone_height=4, ring_height=0.1
... )

```
Copy to clipboard