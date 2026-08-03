---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# change_cs_mode 

CoordinateSystem.change_cs_mode(_mode_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the mode of the coordinate system. 

Parameters: 
     

**mode_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the mode. Options are:
  * `0` - Axis/Position
  * `1` - Euler Angle ZXZ
  * `2` - Euler Angle ZYZ

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.change_cs_mode(mode_type=1)

```
Copy to clipboard
# change_cs_mode 

CoordinateSystem.change_cs_mode(_mode_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the mode of the coordinate system. 

Parameters: 
     

**mode_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the mode. Options are:
  * `0` - Axis/Position
  * `1` - Euler Angle ZXZ
  * `2` - Euler Angle ZYZ

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.change_cs_mode(mode_type=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode.rst.txt)

# change_cs_mode 

CoordinateSystem.change_cs_mode(_mode_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the mode of the coordinate system. 

Parameters: 
     

**mode_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the mode. Options are:
  * `0` - Axis/Position
  * `1` - Euler Angle ZXZ
  * `2` - Euler Angle ZYZ

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.change_cs_mode(mode_type=1)

```
Copy to clipboard