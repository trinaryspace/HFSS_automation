---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# fillet 

VertexPrimitive.fillet(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _setback : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a fillet to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius of the fillet. The default is `0.1`. 

**setback**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Setback value for the file. The default is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Fillet

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import ModifiablePrimitive
>>> obj = ModifiablePrimitive()
>>> obj.fillet(radius="10mm", setback=1.0)

```
Copy to clipboard
# fillet 

VertexPrimitive.fillet(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _setback : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a fillet to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius of the fillet. The default is `0.1`. 

**setback**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Setback value for the file. The default is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Fillet

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import ModifiablePrimitive
>>> obj = ModifiablePrimitive()
>>> obj.fillet(radius="10mm", setback=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet.rst.txt)

# fillet 

VertexPrimitive.fillet(_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _setback : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a fillet to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radius of the fillet. The default is `0.1`. 

**setback**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Setback value for the file. The default is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Fillet

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import ModifiablePrimitive
>>> obj = ModifiablePrimitive()
>>> obj.fillet(radius="10mm", setback=1.0)

```
Copy to clipboard