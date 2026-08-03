---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyhedron.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_polyhedron 

Modeler3D.create_polyhedron(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 0.0, 0.0)_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 1.0, 0.0)_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a regular polyhedron. 

Parameters: 
     

**orientation**`optional` 
    
Axis of rotation of the starting point around the center point. The default is `None`, in which case the Z axis is used. 

**center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position. The default is `(0.0, 0.0, 0.0)`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the starting position. The default is `(0.0, 0.0, 0.0)`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Height of the polyhedron. The default is `1.0`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides of the polyhedron. The default is `12`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyhedron. The default is `None`, in which the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRegularPolyhedron

```
Copy to clipboard
Examples
The following examples shows how to create a regular polyhedron in HFSS. The required parameters are cs_axis that provides the direction axis of the polyhedron, center_position that provides the center of the polyhedron, start_position of the polyhedron, height of the polyhedron and num_sides to determine the number of sides. The parameter matname is optional and allows to set the material name of the polyhedron. The parameter name is optional and allows to give a name to the polyhedron. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ret_obj = aedtapp.modeler.create_polyhedron(orientation='X',center=[0, 0, 0],
...                                             origin=[0,5,0],height=0.5,num_sides=8,
...                                             name="mybox",material="copper")

```
Copy to clipboard
# create_polyhedron 

Modeler3D.create_polyhedron(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 0.0, 0.0)_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 1.0, 0.0)_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a regular polyhedron. 

Parameters: 
     

**orientation**`optional` 
    
Axis of rotation of the starting point around the center point. The default is `None`, in which case the Z axis is used. 

**center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position. The default is `(0.0, 0.0, 0.0)`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the starting position. The default is `(0.0, 0.0, 0.0)`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Height of the polyhedron. The default is `1.0`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides of the polyhedron. The default is `12`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyhedron. The default is `None`, in which the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRegularPolyhedron

```
Copy to clipboard
Examples
The following examples shows how to create a regular polyhedron in HFSS. The required parameters are cs_axis that provides the direction axis of the polyhedron, center_position that provides the center of the polyhedron, start_position of the polyhedron, height of the polyhedron and num_sides to determine the number of sides. The parameter matname is optional and allows to set the material name of the polyhedron. The parameter name is optional and allows to give a name to the polyhedron. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ret_obj = aedtapp.modeler.create_polyhedron(orientation='X',center=[0, 0, 0],
...                                             origin=[0,5,0],height=0.5,num_sides=8,
...                                             name="mybox",material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyhedron.rst.txt)

# create_polyhedron 

Modeler3D.create_polyhedron(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 0.0, 0.0)_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = (0.0, 1.0, 0.0)_, _height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a regular polyhedron. 

Parameters: 
     

**orientation**`optional` 
    
Axis of rotation of the starting point around the center point. The default is `None`, in which case the Z axis is used. 

**center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the center position. The default is `(0.0, 0.0, 0.0)`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the starting position. The default is `(0.0, 0.0, 0.0)`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Height of the polyhedron. The default is `1.0`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of sides of the polyhedron. The default is `12`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyhedron. The default is `None`, in which the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which the default material is assigned. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRegularPolyhedron

```
Copy to clipboard
Examples
The following examples shows how to create a regular polyhedron in HFSS. The required parameters are cs_axis that provides the direction axis of the polyhedron, center_position that provides the center of the polyhedron, start_position of the polyhedron, height of the polyhedron and num_sides to determine the number of sides. The parameter matname is optional and allows to set the material name of the polyhedron. The parameter name is optional and allows to give a name to the polyhedron. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> ret_obj = aedtapp.modeler.create_polyhedron(orientation='X',center=[0, 0, 0],
...                                             origin=[0,5,0],height=0.5,num_sides=8,
...                                             name="mybox",material="copper")

```
Copy to clipboard