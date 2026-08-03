---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_plane.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_plane 

Modeler3D.create_plane(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _plane_base_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Plane](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane") 
    
Create a plane. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plane. The default is `None`, in which case the default name is assigned. 

**plane_base_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the plane base. The default value is `"0mm"`. 

**plane_normal_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the normal plane. The default value is `"0mm"`. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing the three integer values for the color of the plane. The default value is `"(143 175 143)"`. 

Returns: 
     

`ansys.aedt.core.modeler.cad.primitives.Plane`
    
Planes object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
Create a new plane. >>> from ansys.aedt.core import hfss >>> hfss = Hfss() >>> plane_object = hfss.modeler.primivites.create_plane( … plane_base_y=”-0.8mm”, plane_normal_x=”-0.7mm”, name=”myplane” … )
# create_plane 

Modeler3D.create_plane(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _plane_base_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Plane](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane") 
    
Create a plane. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plane. The default is `None`, in which case the default name is assigned. 

**plane_base_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the plane base. The default value is `"0mm"`. 

**plane_normal_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the normal plane. The default value is `"0mm"`. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing the three integer values for the color of the plane. The default value is `"(143 175 143)"`. 

Returns: 
     

`ansys.aedt.core.modeler.cad.primitives.Plane`
    
Planes object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
Create a new plane. >>> from ansys.aedt.core import hfss >>> hfss = Hfss() >>> plane_object = hfss.modeler.primivites.create_plane( … plane_base_y=”-0.8mm”, plane_normal_x=”-0.7mm”, name=”myplane” … )
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_plane.rst.txt)

# create_plane 

Modeler3D.create_plane(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _plane_base_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_base_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_x : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_y : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _plane_normal_z : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0mm'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Plane](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane") 
    
Create a plane. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plane. The default is `None`, in which case the default name is assigned. 

**plane_base_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the plane base. The default value is `"0mm"`. 

**plane_base_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the plane base. The default value is `"0mm"`. 

**plane_normal_x**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
X coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_y**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Y coordinate of the normal plane. The default value is `"0mm"`. 

**plane_normal_z**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Z coordinate of the normal plane. The default value is `"0mm"`. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing the three integer values for the color of the plane. The default value is `"(143 175 143)"`. 

Returns: 
     

`ansys.aedt.core.modeler.cad.primitives.Plane`
    
Planes object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples
Create a new plane. >>> from ansys.aedt.core import hfss >>> hfss = Hfss() >>> plane_object = hfss.modeler.primivites.create_plane( … plane_base_y=”-0.8mm”, plane_normal_x=”-0.7mm”, name=”myplane” … )