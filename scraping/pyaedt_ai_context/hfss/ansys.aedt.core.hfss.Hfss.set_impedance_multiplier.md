---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_impedance_multiplier.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_impedance_multiplier 

Hfss.set_impedance_multiplier(_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set impedance multiplier. 

Parameters: 
     

**multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Impedance Multiplier. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ChangeImpedanceMult

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> hfss.set_impedance_multiplier(2.0)

```
Copy to clipboard
# set_impedance_multiplier 

Hfss.set_impedance_multiplier(_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set impedance multiplier. 

Parameters: 
     

**multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Impedance Multiplier. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ChangeImpedanceMult

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> hfss.set_impedance_multiplier(2.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_impedance_multiplier.rst.txt)

# set_impedance_multiplier 

Hfss.set_impedance_multiplier(_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set impedance multiplier. 

Parameters: 
     

**multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Impedance Multiplier. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ChangeImpedanceMult

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> hfss.set_impedance_multiplier(2.0)

```
Copy to clipboard