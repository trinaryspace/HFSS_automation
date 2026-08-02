---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.update_udp.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# update_udp 

Modeler2D.update_udp(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update an existing geometrical object that was originally created using a user-defined primitive (UDP). 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object to update. 

**operation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the operation used to create the object. 

**parameters**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the UDP parameters to update and their value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> self.aedtapp.modeler.update_udp(
...     assignment="ClawPoleCore",
...     operation="CreateUserDefinedPart",
...     parameters=[["Length", "110mm"], ["DiaGap", "125mm"]],
... )
True

```
Copy to clipboard
# update_udp 

Modeler2D.update_udp(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update an existing geometrical object that was originally created using a user-defined primitive (UDP). 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object to update. 

**operation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the operation used to create the object. 

**parameters**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the UDP parameters to update and their value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> self.aedtapp.modeler.update_udp(
...     assignment="ClawPoleCore",
...     operation="CreateUserDefinedPart",
...     parameters=[["Length", "110mm"], ["DiaGap", "125mm"]],
... )
True

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.update_udp.rst.txt)

# update_udp 

Modeler2D.update_udp(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update an existing geometrical object that was originally created using a user-defined primitive (UDP). 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object to update. 

**operation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the operation used to create the object. 

**parameters**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the UDP parameters to update and their value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> self.aedtapp.modeler.update_udp(
...     assignment="ClawPoleCore",
...     operation="CreateUserDefinedPart",
...     parameters=[["Length", "110mm"], ["DiaGap", "125mm"]],
... )
True

```
Copy to clipboard