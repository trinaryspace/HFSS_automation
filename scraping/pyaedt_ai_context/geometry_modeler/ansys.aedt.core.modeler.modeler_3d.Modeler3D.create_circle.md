---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_circle.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_circle 

Modeler3D.create_circle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a circle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the circle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Radius of the circle. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the circle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if create the new object as model or non-model. The default is `False`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateCircle

```
Copy to clipboard
Examples
The following example shows how to create a circle in HFSS. The required parameters are `cs_plane`, `position`, `radius`, and `num_sides`. The `cs_plane` parameter provides the plane that the circle is designed on. The `position` parameter provides the origin of the circle. The `radius` and `num_sides` parameters provide the radius and number of discrete sides of the circle,
The optional parameter `matname` allows you to set the material name of the circle. The optional parameter `name` allows you to assign a name to the circle.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> circle_object = aedtapp.modeler.create_circle(orientation='Z', origin=[0,0,0],
...                                                   radius=2, num_sides=8, name="mycyl",
...                                                   material="vacuum")

```
Copy to clipboard
# create_circle 

Modeler3D.create_circle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a circle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the circle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Radius of the circle. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the circle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if create the new object as model or non-model. The default is `False`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateCircle

```
Copy to clipboard
Examples
The following example shows how to create a circle in HFSS. The required parameters are `cs_plane`, `position`, `radius`, and `num_sides`. The `cs_plane` parameter provides the plane that the circle is designed on. The `position` parameter provides the origin of the circle. The `radius` and `num_sides` parameters provide the radius and number of discrete sides of the circle,
The optional parameter `matname` allows you to set the material name of the circle. The optional parameter `name` allows you to assign a name to the circle.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> circle_object = aedtapp.modeler.create_circle(orientation='Z', origin=[0,0,0],
...                                                   radius=2, num_sides=8, name="mycyl",
...                                                   material="vacuum")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_circle.rst.txt)

# create_circle 

Modeler3D.create_circle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a circle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the circle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Radius of the circle. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides. The default is `0`, which is correct for a circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the circle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if create the new object as model or non-model. The default is `False`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateCircle

```
Copy to clipboard
Examples
The following example shows how to create a circle in HFSS. The required parameters are `cs_plane`, `position`, `radius`, and `num_sides`. The `cs_plane` parameter provides the plane that the circle is designed on. The `position` parameter provides the origin of the circle. The `radius` and `num_sides` parameters provide the radius and number of discrete sides of the circle,
The optional parameter `matname` allows you to set the material name of the circle. The optional parameter `name` allows you to assign a name to the circle.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> circle_object = aedtapp.modeler.create_circle(orientation='Z', origin=[0,0,0],
...                                                   radius=2, num_sides=8, name="mycyl",
...                                                   material="vacuum")

```
Copy to clipboard