---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.calculate_radius_2D.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# calculate_radius_2D 

Modeler2D.calculate_radius_2D(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _inner : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the extremity of an object in the radial direction. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
name of the object from which to calculate the radius. 

**inner**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Radius value.
Note
If `inner=True`, then the maximum is returned; otherwise, the minimum is returned.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.calculate_radius_2D(assignment="Box1")

```
Copy to clipboard
# calculate_radius_2D 

Modeler2D.calculate_radius_2D(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _inner : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the extremity of an object in the radial direction. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
name of the object from which to calculate the radius. 

**inner**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Radius value.
Note
If `inner=True`, then the maximum is returned; otherwise, the minimum is returned.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.calculate_radius_2D(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.calculate_radius_2D.rst.txt)

# calculate_radius_2D 

Modeler2D.calculate_radius_2D(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _inner : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the extremity of an object in the radial direction. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
name of the object from which to calculate the radius. 

**inner**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Radius value.
Note
If `inner=True`, then the maximum is returned; otherwise, the minimum is returned.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.calculate_radius_2D(assignment="Box1")

```
Copy to clipboard