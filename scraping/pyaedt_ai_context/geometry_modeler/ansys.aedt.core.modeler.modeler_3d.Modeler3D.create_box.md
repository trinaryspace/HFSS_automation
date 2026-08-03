---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_box.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_box 

Modeler3D.create_box(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a box. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Anchor point for the box in Cartesian``[x, y, z]`` coordinates. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Length of the box edges in Cartesian``[x, y, z]`` coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the box. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
This example shows how to create a box in HFSS. The required parameters are `position` that provides the origin of the box and `dimensions_list` that provide the box sizes. The optional parameter `matname` allows you to set the material name of the box. The optional parameter `name` allows you to assign a name to the box.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> dimensions = [10, 5, 20]
>>> box_object = hfss.modeler.create_box(origin=origin, sizes=dimensions, name="mybox", material="copper")

```
Copy to clipboard
# create_box 

Modeler3D.create_box(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a box. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Anchor point for the box in Cartesian``[x, y, z]`` coordinates. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Length of the box edges in Cartesian``[x, y, z]`` coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the box. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
This example shows how to create a box in HFSS. The required parameters are `position` that provides the origin of the box and `dimensions_list` that provide the box sizes. The optional parameter `matname` allows you to set the material name of the box. The optional parameter `name` allows you to assign a name to the box.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> dimensions = [10, 5, 20]
>>> box_object = hfss.modeler.create_box(origin=origin, sizes=dimensions, name="mybox", material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_box.rst.txt)

# create_box 

Modeler3D.create_box(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a box. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Anchor point for the box in Cartesian``[x, y, z]`` coordinates. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Length of the box edges in Cartesian``[x, y, z]`` coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the box. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. If the material name supplied is invalid, the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
This example shows how to create a box in HFSS. The required parameters are `position` that provides the origin of the box and `dimensions_list` that provide the box sizes. The optional parameter `matname` allows you to set the material name of the box. The optional parameter `name` allows you to assign a name to the box.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> origin = [0, 0, 0]
>>> dimensions = [10, 5, 20]
>>> box_object = hfss.modeler.create_box(origin=origin, sizes=dimensions, name="mybox", material="copper")

```
Copy to clipboard