---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_coaxial.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_coaxial 

Modeler3D.create_coaxial(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _inner_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _outer_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2_, _diel_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.8_, _length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10_, _mat_inner : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_outer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_diel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'teflon_based'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d', 'Object3d'] 
    
Create a coaxial. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or value of the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**inner_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inner coax radius. The default is `1`. 

**outer_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Outer coax radius. The default is `2`. 

**diel_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Dielectric coax radius. The default is `1.8`. 

**length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coaxial length. The default is `10`. 

**mat_inner**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the inner coaxial. The default is `"copper"`. 

**mat_outer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the outer coaxial. The default is `"copper"`. 

**mat_diel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the dielectric. The default is `"teflon_based"`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Contains the inner, outer, and dielectric coax as [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") objects.
References

```
>>> oEditor.CreateCylinder
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a Coaxial Along X Axis waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> coax = app.modeler.create_coaxial(
...     position, Axis.X, inner_radius=0.5, outer_radius=0.8, diel_radius=0.78, length=50
... )

```
Copy to clipboard
# create_coaxial 

Modeler3D.create_coaxial(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _inner_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _outer_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2_, _diel_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.8_, _length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10_, _mat_inner : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_outer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_diel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'teflon_based'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d', 'Object3d'] 
    
Create a coaxial. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or value of the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**inner_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inner coax radius. The default is `1`. 

**outer_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Outer coax radius. The default is `2`. 

**diel_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Dielectric coax radius. The default is `1.8`. 

**length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coaxial length. The default is `10`. 

**mat_inner**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the inner coaxial. The default is `"copper"`. 

**mat_outer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the outer coaxial. The default is `"copper"`. 

**mat_diel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the dielectric. The default is `"teflon_based"`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Contains the inner, outer, and dielectric coax as [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") objects.
References

```
>>> oEditor.CreateCylinder
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a Coaxial Along X Axis waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> coax = app.modeler.create_coaxial(
...     position, Axis.X, inner_radius=0.5, outer_radius=0.8, diel_radius=0.78, length=50
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_coaxial.rst.txt)

# create_coaxial 

Modeler3D.create_coaxial(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _inner_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _outer_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2_, _diel_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.8_, _length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10_, _mat_inner : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_outer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _mat_diel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'teflon_based'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d', 'Object3d'] 
    
Create a coaxial. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or value of the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**inner_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inner coax radius. The default is `1`. 

**outer_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Outer coax radius. The default is `2`. 

**diel_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Dielectric coax radius. The default is `1.8`. 

**length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coaxial length. The default is `10`. 

**mat_inner**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the inner coaxial. The default is `"copper"`. 

**mat_outer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the outer coaxial. The default is `"copper"`. 

**mat_diel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material for the dielectric. The default is `"teflon_based"`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Contains the inner, outer, and dielectric coax as [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") objects.
References

```
>>> oEditor.CreateCylinder
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a Coaxial Along X Axis waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> coax = app.modeler.create_coaxial(
...     position, Axis.X, inner_radius=0.5, outer_radius=0.8, diel_radius=0.78, length=50
... )

```
Copy to clipboard