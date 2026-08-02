---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_coax_port.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_coax_port 

Hfss3dLayout.create_coax_port(_via : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _radial_extent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _alignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'lower'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coax port. 

Parameters: 
     

**via**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the via to create the port on. 

**radial_extent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radial coax extension. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer to apply the reference to. 

**alignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port alignment on the layer. 

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
>>> hfss3d.create_coax_port(via="via1", radial_extent=0.1)

```
Copy to clipboard
# create_coax_port 

Hfss3dLayout.create_coax_port(_via : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _radial_extent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _alignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'lower'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coax port. 

Parameters: 
     

**via**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the via to create the port on. 

**radial_extent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radial coax extension. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer to apply the reference to. 

**alignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port alignment on the layer. 

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
>>> hfss3d.create_coax_port(via="via1", radial_extent=0.1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_coax_port.rst.txt)

# create_coax_port 

Hfss3dLayout.create_coax_port(_via : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _radial_extent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _alignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'lower'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coax port. 

Parameters: 
     

**via**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the via to create the port on. 

**radial_extent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Radial coax extension. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer to apply the reference to. 

**alignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port alignment on the layer. 

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
>>> hfss3d.create_coax_port(via="via1", radial_extent=0.1)

```
Copy to clipboard