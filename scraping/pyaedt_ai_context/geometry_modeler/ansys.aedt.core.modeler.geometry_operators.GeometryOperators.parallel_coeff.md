---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.parallel_coeff.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# parallel_coeff 

static GeometryOperators.parallel_coeff(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ADD DESCRIPTION. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the first segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
_vdot of 4 vertices of 2 segments.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.parallel_coeff(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
# parallel_coeff 

static GeometryOperators.parallel_coeff(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ADD DESCRIPTION. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the first segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
_vdot of 4 vertices of 2 segments.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.parallel_coeff(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.parallel_coeff.rst.txt)

# parallel_coeff 

static GeometryOperators.parallel_coeff(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ADD DESCRIPTION. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the first segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
_vdot of 4 vertices of 2 segments.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.parallel_coeff(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard