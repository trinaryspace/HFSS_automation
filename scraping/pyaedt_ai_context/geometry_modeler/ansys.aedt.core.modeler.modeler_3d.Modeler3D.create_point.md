---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_point.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_point 

Modeler3D.create_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Point](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point") 
    
Create a point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates. Note, The list can be empty or contain less than 3 elements. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point. The default is `None`, in which case the default name is assigned. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing 3 int values such as “(value1 value2 value3)”. Default value is `"(143 175 143)"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point")
    
Point object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> point_object = hfss.modeler.primivites.create_point([0, 0, 0], name="mypoint")

```
Copy to clipboard
# create_point 

Modeler3D.create_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Point](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point") 
    
Create a point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates. Note, The list can be empty or contain less than 3 elements. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point. The default is `None`, in which case the default name is assigned. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing 3 int values such as “(value1 value2 value3)”. Default value is `"(143 175 143)"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point")
    
Point object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> point_object = hfss.modeler.primivites.create_point([0, 0, 0], name="mypoint")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_point.rst.txt)

# create_point 

Modeler3D.create_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '(143 175 143)'_) → [Point](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point") 
    
Create a point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates. Note, The list can be empty or contain less than 3 elements. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point. The default is `None`, in which case the default name is assigned. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String exposing 3 int values such as “(value1 value2 value3)”. Default value is `"(143 175 143)"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point")
    
Point object.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> point_object = hfss.modeler.primivites.create_point([0, 0, 0], name="mypoint")

```
Copy to clipboard