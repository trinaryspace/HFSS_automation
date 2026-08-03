---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_cylinder.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_cylinder 

Modeler3D.create_cylinder(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a cylinder. 

Parameters: 
     

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` `Plane` 
    
Axis of rotation of the starting point around the center point. `ansys.aedt.core.constants.Axis` Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point of the cylinder in a list of `(x, y, z)` coordinates. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the cylinder. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cylinder. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a cylinder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cylinder. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateCylinder

```
Copy to clipboard
Examples
This example shows how to create a cylinder in HFSS. The required parameters are `cs_axis`, `position`, `radius`, and `height`. The `cs_axis` parameter provides the direction axis of the cylinder. The `position` parameter provides the origin of the cylinder. The other two parameters provide the radius and height of the cylinder.
The optional parameter `matname` allows you to set the material name of the cylinder. The optional parameter `name` allows to assign a name to the cylinder.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> cylinder_object = aedtapp.modeler.create_cylinder(
...     orientation="Z", origin=[0, 0, 0], radius=2, height=3, name="mycyl", material="vacuum"
... )

```
Copy to clipboard
# create_cylinder 

Modeler3D.create_cylinder(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a cylinder. 

Parameters: 
     

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` `Plane` 
    
Axis of rotation of the starting point around the center point. `ansys.aedt.core.constants.Axis` Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point of the cylinder in a list of `(x, y, z)` coordinates. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the cylinder. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cylinder. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a cylinder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cylinder. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateCylinder

```
Copy to clipboard
Examples
This example shows how to create a cylinder in HFSS. The required parameters are `cs_axis`, `position`, `radius`, and `height`. The `cs_axis` parameter provides the direction axis of the cylinder. The `position` parameter provides the origin of the cylinder. The other two parameters provide the radius and height of the cylinder.
The optional parameter `matname` allows you to set the material name of the cylinder. The optional parameter `name` allows to assign a name to the cylinder.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> cylinder_object = aedtapp.modeler.create_cylinder(
...     orientation="Z", origin=[0, 0, 0], radius=2, height=3, name="mycyl", material="vacuum"
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_cylinder.rst.txt)

# create_cylinder 

Modeler3D.create_cylinder(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a cylinder. 

Parameters: 
     

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` `Plane` 
    
Axis of rotation of the starting point around the center point. `ansys.aedt.core.constants.Axis` Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point of the cylinder in a list of `(x, y, z)` coordinates. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the cylinder. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Height of the cylinder. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a cylinder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cylinder. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateCylinder

```
Copy to clipboard
Examples
This example shows how to create a cylinder in HFSS. The required parameters are `cs_axis`, `position`, `radius`, and `height`. The `cs_axis` parameter provides the direction axis of the cylinder. The `position` parameter provides the origin of the cylinder. The other two parameters provide the radius and height of the cylinder.
The optional parameter `matname` allows you to set the material name of the cylinder. The optional parameter `name` allows to assign a name to the cylinder.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> cylinder_object = aedtapp.modeler.create_cylinder(
...     orientation="Z", origin=[0, 0, 0], radius=2, height=3, name="mycyl", material="vacuum"
... )

```
Copy to clipboard