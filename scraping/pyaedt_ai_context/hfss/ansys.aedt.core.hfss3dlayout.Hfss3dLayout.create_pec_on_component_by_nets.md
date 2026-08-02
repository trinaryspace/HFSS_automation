---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_pec_on_component_by_nets.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_pec_on_component_by_nets 

Hfss3dLayout.create_pec_on_component_by_nets(_component : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _nets : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a PEC connection on a component for a list of nets. 

Parameters: 
     

**component**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Component name. 

**nets**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Nets to include. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_pec_on_component_by_nets(component="U1", nets="GND")

```
Copy to clipboard
# create_pec_on_component_by_nets 

Hfss3dLayout.create_pec_on_component_by_nets(_component : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _nets : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a PEC connection on a component for a list of nets. 

Parameters: 
     

**component**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Component name. 

**nets**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Nets to include. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_pec_on_component_by_nets(component="U1", nets="GND")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_pec_on_component_by_nets.rst.txt)

# create_pec_on_component_by_nets 

Hfss3dLayout.create_pec_on_component_by_nets(_component : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _nets : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a PEC connection on a component for a list of nets. 

Parameters: 
     

**component**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Component name. 

**nets**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Nets to include. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_pec_on_component_by_nets(component="U1", nets="GND")

```
Copy to clipboard