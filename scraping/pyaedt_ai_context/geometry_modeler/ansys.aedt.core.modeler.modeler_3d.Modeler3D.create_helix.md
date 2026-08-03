---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_helix.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_helix 

Modeler3D.create_helix(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_hand : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _radius_increment : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _thread : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a helix from a polyline. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the polyline used as the base for the helix. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**x_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along x axis from the polyline. 

**y_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along y axis from the polyline. 

**z_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along z axis from the polyline. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. The default value is `1`. 

**right_hand**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the helix turning direction is right hand. The default value is `True`. 

**radius_increment**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius change per turn. The default value is `0.0`. 

**thread**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateHelix

```
Copy to clipboard
Examples
The following example shows how to create a polyline and then create an helix from the polyline. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> udp1 = [0, 0, 0]
>>> udp2 = [5, 0, 0]
>>> udp3 = [10, 5, 0]
>>> udp4 = [15, 3, 0]
>>> polyline = aedtapp.modeler.create_polyline([udp1, udp2, udp3, udp4],cover_surface=False,
...                                            name="helix_polyline")
>>> helix_right_turn = aedtapp.modeler.create_helix(assignment=polyline.name,origin=[0, 0, 0],
...                                                 x_start_dir=0,y_start_dir=1.0,z_start_dir=1.0,
...                                                 turns=1,right_hand=True,radius_increment=0.0,thread=1.0)

```
Copy to clipboard
# create_helix 

Modeler3D.create_helix(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_hand : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _radius_increment : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _thread : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a helix from a polyline. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the polyline used as the base for the helix. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**x_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along x axis from the polyline. 

**y_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along y axis from the polyline. 

**z_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along z axis from the polyline. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. The default value is `1`. 

**right_hand**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the helix turning direction is right hand. The default value is `True`. 

**radius_increment**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius change per turn. The default value is `0.0`. 

**thread**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateHelix

```
Copy to clipboard
Examples
The following example shows how to create a polyline and then create an helix from the polyline. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> udp1 = [0, 0, 0]
>>> udp2 = [5, 0, 0]
>>> udp3 = [10, 5, 0]
>>> udp4 = [15, 3, 0]
>>> polyline = aedtapp.modeler.create_polyline([udp1, udp2, udp3, udp4],cover_surface=False,
...                                            name="helix_polyline")
>>> helix_right_turn = aedtapp.modeler.create_helix(assignment=polyline.name,origin=[0, 0, 0],
...                                                 x_start_dir=0,y_start_dir=1.0,z_start_dir=1.0,
...                                                 turns=1,right_hand=True,radius_increment=0.0,thread=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_helix.rst.txt)

# create_helix 

Modeler3D.create_helix(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z_start_dir : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _turns : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_hand : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _radius_increment : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _thread : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a helix from a polyline. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the polyline used as the base for the helix. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the center point of the circle. 

**x_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along x axis from the polyline. 

**y_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along y axis from the polyline. 

**z_start_dir**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Distance along z axis from the polyline. 

**turns**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of turns. The default value is `1`. 

**right_hand**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the helix turning direction is right hand. The default value is `True`. 

**radius_increment**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius change per turn. The default value is `0.0`. 

**thread**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateHelix

```
Copy to clipboard
Examples
The following example shows how to create a polyline and then create an helix from the polyline. This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> udp1 = [0, 0, 0]
>>> udp2 = [5, 0, 0]
>>> udp3 = [10, 5, 0]
>>> udp4 = [15, 3, 0]
>>> polyline = aedtapp.modeler.create_polyline([udp1, udp2, udp3, udp4],cover_surface=False,
...                                            name="helix_polyline")
>>> helix_right_turn = aedtapp.modeler.create_helix(assignment=polyline.name,origin=[0, 0, 0],
...                                                 x_start_dir=0,y_start_dir=1.0,z_start_dir=1.0,
...                                                 turns=1,right_hand=True,radius_increment=0.0,thread=1.0)

```
Copy to clipboard