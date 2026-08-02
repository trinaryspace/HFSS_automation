---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_airbox.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_airbox 

Modeler2D.create_airbox(_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _offset_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Absolute'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AirBox_Auto'_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create an airbox that is as big as the bounding extension of the project. 

Parameters: 
     

**offset**
    
Double offset value to apply on the airbox faces versus the bounding box. The default is `0`. 

**offset_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the offset. Options are `"Absolute"` and `"Relative"`. The default is `"Absolute"`. If `"Relative"`, the offset input is between 0 and 100. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the airbox. The default is `"AirBox_Auto"`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the airbox created.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_airbox(name="MyObject", offset="1mm")

```
Copy to clipboard
# create_airbox 

Modeler2D.create_airbox(_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _offset_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Absolute'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AirBox_Auto'_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create an airbox that is as big as the bounding extension of the project. 

Parameters: 
     

**offset**
    
Double offset value to apply on the airbox faces versus the bounding box. The default is `0`. 

**offset_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the offset. Options are `"Absolute"` and `"Relative"`. The default is `"Absolute"`. If `"Relative"`, the offset input is between 0 and 100. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the airbox. The default is `"AirBox_Auto"`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the airbox created.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_airbox(name="MyObject", offset="1mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_airbox.rst.txt)

# create_airbox 

Modeler2D.create_airbox(_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _offset_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Absolute'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'AirBox_Auto'_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create an airbox that is as big as the bounding extension of the project. 

Parameters: 
     

**offset**
    
Double offset value to apply on the airbox faces versus the bounding box. The default is `0`. 

**offset_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the offset. Options are `"Absolute"` and `"Relative"`. The default is `"Absolute"`. If `"Relative"`, the offset input is between 0 and 100. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the airbox. The default is `"AirBox_Auto"`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the airbox created.
References

```
>>> oEditor.CreateBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_airbox(name="MyObject", offset="1mm")

```
Copy to clipboard