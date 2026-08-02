---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_differential_port.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_differential_port 

Hfss3dLayout.create_differential_port(_via_signal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _via_reference : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a differential port. 

Parameters: 
     

**via_signal**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Signal pin. 

**via_reference**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Reference pin. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
New Port Name. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed parasitics. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port Object when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_differential_port(via_signal="via1", via_reference=0.1, name="diff_port1")

```
Copy to clipboard
# create_differential_port 

Hfss3dLayout.create_differential_port(_via_signal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _via_reference : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a differential port. 

Parameters: 
     

**via_signal**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Signal pin. 

**via_reference**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Reference pin. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
New Port Name. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed parasitics. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port Object when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_differential_port(via_signal="via1", via_reference=0.1, name="diff_port1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_differential_port.rst.txt)

# create_differential_port 

Hfss3dLayout.create_differential_port(_via_signal : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _via_reference : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a differential port. 

Parameters: 
     

**via_signal**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Signal pin. 

**via_reference**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Reference pin. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
New Port Name. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed parasitics. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port Object when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_differential_port(via_signal="via1", via_reference=0.1, name="diff_port1")

```
Copy to clipboard