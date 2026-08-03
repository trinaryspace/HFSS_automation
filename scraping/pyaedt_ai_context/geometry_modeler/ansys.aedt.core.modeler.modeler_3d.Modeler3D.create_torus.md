---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_torus.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_torus 

Modeler3D.create_torus(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minor_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a torus. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point for the torus in a list of `[x, y, z]` coordinates. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Major radius of the torus. 

**minor_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minor radius of the torus. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis of revolution. The default is `None`, in which case the Z axis is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the torus. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateTorus

```
Copy to clipboard
Examples
Create a torus named `"mytorus"` about the Z axis with a major radius of 1 , minor radius of 0.5, and a material of `"copper"`. The optional parameter `matname` allows you to set the material name of the sphere. The optional parameter `name` allows you to give a name to the sphere.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> torus = hfss.modeler.create_torus(origin=origin,major_radius=1,minor_radius=0.5,
...                                   axis="Z",name="mytorus",material="copper")

```
Copy to clipboard
# create_torus 

Modeler3D.create_torus(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minor_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a torus. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point for the torus in a list of `[x, y, z]` coordinates. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Major radius of the torus. 

**minor_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minor radius of the torus. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis of revolution. The default is `None`, in which case the Z axis is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the torus. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateTorus

```
Copy to clipboard
Examples
Create a torus named `"mytorus"` about the Z axis with a major radius of 1 , minor radius of 0.5, and a material of `"copper"`. The optional parameter `matname` allows you to set the material name of the sphere. The optional parameter `name` allows you to give a name to the sphere.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> torus = hfss.modeler.create_torus(origin=origin,major_radius=1,minor_radius=0.5,
...                                   axis="Z",name="mytorus",material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_torus.rst.txt)

# create_torus 

Modeler3D.create_torus(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minor_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a torus. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Center point for the torus in a list of `[x, y, z]` coordinates. 

**major_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Major radius of the torus. 

**minor_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minor radius of the torus. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis of revolution. The default is `None`, in which case the Z axis is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the torus. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateTorus

```
Copy to clipboard
Examples
Create a torus named `"mytorus"` about the Z axis with a major radius of 1 , minor radius of 0.5, and a material of `"copper"`. The optional parameter `matname` allows you to set the material name of the sphere. The optional parameter `name` allows you to give a name to the sphere.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> torus = hfss.modeler.create_torus(origin=origin,major_radius=1,minor_radius=0.5,
...                                   axis="Z",name="mytorus",material="copper")

```
Copy to clipboard