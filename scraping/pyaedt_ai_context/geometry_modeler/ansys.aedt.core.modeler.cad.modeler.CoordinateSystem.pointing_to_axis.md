---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# pointing_to_axis 

static CoordinateSystem.pointing_to_axis(_x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system. 

Parameters: 
     

**x_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the X axis. 

**y_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the Y pointing axis. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(Xx, Xy, Xz), (Yx, Yy, Yz), (Zx, Zy, Zz)` of the three axes (normalized).
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.pointing_to_axis(x_pointing=[1, 0, 0], y_pointing=[0, 1, 0])

```
Copy to clipboard
# pointing_to_axis 

static CoordinateSystem.pointing_to_axis(_x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system. 

Parameters: 
     

**x_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the X axis. 

**y_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the Y pointing axis. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(Xx, Xy, Xz), (Yx, Yy, Yz), (Zx, Zy, Zz)` of the three axes (normalized).
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.pointing_to_axis(x_pointing=[1, 0, 0], y_pointing=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis.rst.txt)

# pointing_to_axis 

static CoordinateSystem.pointing_to_axis(_x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system. 

Parameters: 
     

**x_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the X axis. 

**y_pointing**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
`(x, y, z)` coordinates for the Y pointing axis. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(Xx, Xy, Xz), (Yx, Yy, Yz), (Zx, Zy, Zz)` of the three axes (normalized).
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.pointing_to_axis(x_pointing=[1, 0, 0], y_pointing=[0, 1, 0])

```
Copy to clipboard