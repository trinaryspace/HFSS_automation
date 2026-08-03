---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.cs_xy_pointing_expression.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# cs_xy_pointing_expression 

static GeometryOperators.cs_xy_pointing_expression(_yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Return x_pointing and y_pointing vectors as expressions from the yaw, pitch, and roll input (as strings). 

Parameters: 
     

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the yaw angle (rotation about Z-axis) 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the pitch angle (rotation about Y-axis) 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the roll angle (rotation about X-axis) 

Returns: 
     

[`x_pointing`, `y_pointing`] `vector` expressions.
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.cs_xy_pointing_expression(yaw=1, pitch=1, roll=1)

```
Copy to clipboard
# cs_xy_pointing_expression 

static GeometryOperators.cs_xy_pointing_expression(_yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Return x_pointing and y_pointing vectors as expressions from the yaw, pitch, and roll input (as strings). 

Parameters: 
     

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the yaw angle (rotation about Z-axis) 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the pitch angle (rotation about Y-axis) 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the roll angle (rotation about X-axis) 

Returns: 
     

[`x_pointing`, `y_pointing`] `vector` expressions.
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.cs_xy_pointing_expression(yaw=1, pitch=1, roll=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.cs_xy_pointing_expression.rst.txt)

# cs_xy_pointing_expression 

static GeometryOperators.cs_xy_pointing_expression(_yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Return x_pointing and y_pointing vectors as expressions from the yaw, pitch, and roll input (as strings). 

Parameters: 
     

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the yaw angle (rotation about Z-axis) 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the pitch angle (rotation about Y-axis) 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String expression for the roll angle (rotation about X-axis) 

Returns: 
     

[`x_pointing`, `y_pointing`] `vector` expressions.
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.cs_xy_pointing_expression(yaw=1, pitch=1, roll=1)

```
Copy to clipboard