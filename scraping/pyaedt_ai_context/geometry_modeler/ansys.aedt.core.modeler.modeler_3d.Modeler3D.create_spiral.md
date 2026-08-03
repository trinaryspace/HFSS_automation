---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_spiral.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_spiral 

Modeler3D.create_spiral(_internal_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _spacing : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _faces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _thickness : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _elevation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a spiral inductor from a polyline. 

Parameters: 
     

**internal_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal starting point of spiral. Default is 10. 

**spacing**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal pitch between two turns. Default is 1. 

**faces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of faces per turn. Default is 8 as an octagon. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. Default is 10. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral width. Default is 2. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral thickness. Default is 1. 

**elevation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral elevation. Default is`0`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral material. Default is “copper”. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral name. Default is None. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.cad.elements_3d.Polyline` 
    
Polyline object or `False` if it fails.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_spiral(name="MyObject", material="copper")

```
Copy to clipboard
# create_spiral 

Modeler3D.create_spiral(_internal_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _spacing : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _faces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _thickness : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _elevation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a spiral inductor from a polyline. 

Parameters: 
     

**internal_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal starting point of spiral. Default is 10. 

**spacing**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal pitch between two turns. Default is 1. 

**faces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of faces per turn. Default is 8 as an octagon. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. Default is 10. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral width. Default is 2. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral thickness. Default is 1. 

**elevation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral elevation. Default is`0`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral material. Default is “copper”. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral name. Default is None. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.cad.elements_3d.Polyline` 
    
Polyline object or `False` if it fails.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_spiral(name="MyObject", material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_spiral.rst.txt)

# create_spiral 

Modeler3D.create_spiral(_internal_radius : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _spacing : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _faces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _thickness : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _elevation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a spiral inductor from a polyline. 

Parameters: 
     

**internal_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal starting point of spiral. Default is 10. 

**spacing**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Internal pitch between two turns. Default is 1. 

**faces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of faces per turn. Default is 8 as an octagon. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. Default is 10. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral width. Default is 2. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral thickness. Default is 1. 

**elevation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Spiral elevation. Default is`0`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral material. Default is “copper”. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Spiral name. Default is None. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.cad.elements_3d.Polyline` 
    
Polyline object or `False` if it fails.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_spiral(name="MyObject", material="copper")

```
Copy to clipboard