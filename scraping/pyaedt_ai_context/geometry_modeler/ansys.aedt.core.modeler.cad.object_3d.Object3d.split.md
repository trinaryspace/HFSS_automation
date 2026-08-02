---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.split.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# split 

Object3d.split(_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sides : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Both'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Split the active object. 

Parameters: 
     

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the cut. Choices for the coordinate plane are `"XY"`, `"YZ"`, and `"ZX"`. 

**sides**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Which side to keep. Options are `"Both"`, `"PositiveOnly"`, and `"NegativeOnly"`. The default is `"Both"`, in which case all objects are kept after the split. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of split objects.
References

```
>>> oEditor.Split

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.split(plane="XY")

```
Copy to clipboard
# split 

Object3d.split(_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sides : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Both'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Split the active object. 

Parameters: 
     

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the cut. Choices for the coordinate plane are `"XY"`, `"YZ"`, and `"ZX"`. 

**sides**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Which side to keep. Options are `"Both"`, `"PositiveOnly"`, and `"NegativeOnly"`. The default is `"Both"`, in which case all objects are kept after the split. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of split objects.
References

```
>>> oEditor.Split

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.split(plane="XY")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.split.rst.txt)

# split 

Object3d.split(_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sides : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Both'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Split the active object. 

Parameters: 
     

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the cut. Choices for the coordinate plane are `"XY"`, `"YZ"`, and `"ZX"`. 

**sides**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Which side to keep. Options are `"Both"`, `"PositiveOnly"`, and `"NegativeOnly"`. The default is `"Both"`, in which case all objects are kept after the split. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of split objects.
References

```
>>> oEditor.Split

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.split(plane="XY")

```
Copy to clipboard