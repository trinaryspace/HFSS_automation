---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.select_allfaces_fromobjects.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# select_allfaces_fromobjects 

Modeler2D.select_allfaces_fromobjects(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to include in the search for outer faces. 

Returns: 
     

`List`
    
List of outer faces in the given list of objects.
References

```
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.select_allfaces_fromobjects(assignment="Box1")

```
Copy to clipboard
# select_allfaces_fromobjects 

Modeler2D.select_allfaces_fromobjects(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to include in the search for outer faces. 

Returns: 
     

`List`
    
List of outer faces in the given list of objects.
References

```
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.select_allfaces_fromobjects(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.select_allfaces_fromobjects.rst.txt)

# select_allfaces_fromobjects 

Modeler2D.select_allfaces_fromobjects(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to include in the search for outer faces. 

Returns: 
     

`List`
    
List of outer faces in the given list of objects.
References

```
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.select_allfaces_fromobjects(assignment="Box1")

```
Copy to clipboard