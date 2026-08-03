---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.mirror_point.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# mirror_point 

static GeometryOperators.mirror_point(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror point about a plane defining by a point on the plane and a normal point. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Point to be mirrored 

**reference**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
The reference point. Point on the plane around which you want to mirror the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Normalized vector used for the mirroring. 

Returns: 
     

`List`
    
List of the reflected point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.mirror_point(start=[0, 0, 0], reference=["Box1"], vector=[1, 0, 0])

```
Copy to clipboard
# mirror_point 

static GeometryOperators.mirror_point(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror point about a plane defining by a point on the plane and a normal point. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Point to be mirrored 

**reference**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
The reference point. Point on the plane around which you want to mirror the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Normalized vector used for the mirroring. 

Returns: 
     

`List`
    
List of the reflected point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.mirror_point(start=[0, 0, 0], reference=["Box1"], vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.mirror_point.rst.txt)

# mirror_point 

static GeometryOperators.mirror_point(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror point about a plane defining by a point on the plane and a normal point. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Point to be mirrored 

**reference**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
The reference point. Point on the plane around which you want to mirror the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Normalized vector used for the mirroring. 

Returns: 
     

`List`
    
List of the reflected point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.mirror_point(start=[0, 0, 0], reference=["Box1"], vector=[1, 0, 0])

```
Copy to clipboard