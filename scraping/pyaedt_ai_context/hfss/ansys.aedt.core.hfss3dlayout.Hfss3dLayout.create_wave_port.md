---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_wave_port.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_wave_port 

Hfss3dLayout.create_wave_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a single-ended wave port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is `5`. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is `5`. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is `"1mm"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Port object when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_wave_port(assignment="line1", edge_number=0)

```
Copy to clipboard
# create_wave_port 

Hfss3dLayout.create_wave_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a single-ended wave port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is `5`. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is `5`. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is `"1mm"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Port object when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_wave_port(assignment="line1", edge_number=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_wave_port.rst.txt)

# create_wave_port 

Hfss3dLayout.create_wave_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a single-ended wave port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is `5`. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is `5`. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is `"1mm"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Port object when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_wave_port(assignment="line1", edge_number=0)

```
Copy to clipboard