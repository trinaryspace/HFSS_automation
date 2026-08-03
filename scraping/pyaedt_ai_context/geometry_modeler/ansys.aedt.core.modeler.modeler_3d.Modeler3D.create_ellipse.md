---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_ellipse.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_ellipse 

Modeler3D.create_ellipse(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the ellipse. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the ellipse. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Base radius of the ellipse. 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Aspect ratio of the secondary radius to the base radius. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the ellipse is covered. The default is `True`, in which case the result is a 2D sheet object. If `False,` the result is a closed 1D polyline object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ellipse. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples
The following example shows how to create an ellipse in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ellipse = aedtapp.modeler.create_ellipse(orientation='Z', origin=[0,0,0],
...                                          major_radius=2, ratio=2, is_covered=True, name="myell",
...                                          material="vacuum")

```
Copy to clipboard
# create_ellipse 

Modeler3D.create_ellipse(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the ellipse. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the ellipse. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Base radius of the ellipse. 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Aspect ratio of the secondary radius to the base radius. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the ellipse is covered. The default is `True`, in which case the result is a 2D sheet object. If `False,` the result is a closed 1D polyline object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ellipse. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples
The following example shows how to create an ellipse in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ellipse = aedtapp.modeler.create_ellipse(orientation='Z', origin=[0,0,0],
...                                          major_radius=2, ratio=2, is_covered=True, name="myell",
...                                          material="vacuum")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_ellipse.rst.txt)

# create_ellipse 

Modeler3D.create_ellipse(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the ellipse. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the ellipse. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Base radius of the ellipse. 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Aspect ratio of the secondary radius to the base radius. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the ellipse is covered. The default is `True`, in which case the result is a 2D sheet object. If `False,` the result is a closed 1D polyline object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ellipse. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples
The following example shows how to create an ellipse in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ellipse = aedtapp.modeler.create_ellipse(orientation='Z', origin=[0,0,0],
...                                          major_radius=2, ratio=2, is_covered=True, name="myell",
...                                          material="vacuum")

```
Copy to clipboard