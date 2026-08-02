---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.explicitly_subtract.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# explicitly_subtract 

Modeler2D.explicitly_subtract(_tool_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _blank_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Explicitly subtract all elements in a SolveInside list and a SolveSurface list. 

Parameters: 
     

**tool_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of dielectrics. 

**blank_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of metals. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Subtract
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.explicitly_subtract(tool_parts=["Box1"], blank_parts=["Box1"])

```
Copy to clipboard
# explicitly_subtract 

Modeler2D.explicitly_subtract(_tool_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _blank_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Explicitly subtract all elements in a SolveInside list and a SolveSurface list. 

Parameters: 
     

**tool_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of dielectrics. 

**blank_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of metals. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Subtract
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.explicitly_subtract(tool_parts=["Box1"], blank_parts=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.explicitly_subtract.rst.txt)

# explicitly_subtract 

Modeler2D.explicitly_subtract(_tool_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _blank_parts : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Explicitly subtract all elements in a SolveInside list and a SolveSurface list. 

Parameters: 
     

**tool_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of dielectrics. 

**blank_parts**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of metals. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Subtract
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.explicitly_subtract(tool_parts=["Box1"], blank_parts=["Box1"])

```
Copy to clipboard