---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_spiral_on_face.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_spiral_on_face 

Modeler2D.create_spiral_on_face(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _filling_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.5_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Create a Spiral Polyline inside a face. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
     

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**filling_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

Returns: 
     

`ansys.aedt.core.modeler.cad.elements_3d.Polyline`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_spiral_on_face(assignment="Box1", width="2mm")

```
Copy to clipboard
# create_spiral_on_face 

Modeler2D.create_spiral_on_face(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _filling_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.5_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Create a Spiral Polyline inside a face. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
     

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**filling_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

Returns: 
     

`ansys.aedt.core.modeler.cad.elements_3d.Polyline`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_spiral_on_face(assignment="Box1", width="2mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_spiral_on_face.rst.txt)

# create_spiral_on_face 

Modeler2D.create_spiral_on_face(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _filling_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.5_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Create a Spiral Polyline inside a face. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
     

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**filling_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

Returns: 
     

`ansys.aedt.core.modeler.cad.elements_3d.Polyline`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_spiral_on_face(assignment="Box1", width="2mm")

```
Copy to clipboard