---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.radial_split_2D.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# radial_split_2D 

Modeler2D.radial_split_2D(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Split the stator and rotor for mesh refinement. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the circle. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.radial_split_2D(radius="10mm", name="MyObject")

```
Copy to clipboard
# radial_split_2D 

Modeler2D.radial_split_2D(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Split the stator and rotor for mesh refinement. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the circle. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.radial_split_2D(radius="10mm", name="MyObject")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.radial_split_2D.rst.txt)

# radial_split_2D 

Modeler2D.radial_split_2D(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Split the stator and rotor for mesh refinement. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radius of the circle. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the circle. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.radial_split_2D(radius="10mm", name="MyObject")

```
Copy to clipboard