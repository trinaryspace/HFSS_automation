---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_edge_port.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_edge_port 

Hfss3dLayout.create_edge_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | 'Line3dLayout'_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _is_circuit_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _is_wave_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_, _reference_primitive : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_edge_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an edge port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout.html#ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout "ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**is_circuit_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a circuit port. The default is `False`. 

**is_wave_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a wave port. The default is `False`. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is 5. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is 5. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is “1mm”. 

**reference_primitive**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference primitive to place negative edge port terminal. The default is `None`. 

**reference_edge_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Edge number of reference primitive. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port objcet port when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_edge_port(assignment="line1", edge_number=0)

```
Copy to clipboard
# create_edge_port 

Hfss3dLayout.create_edge_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | 'Line3dLayout'_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _is_circuit_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _is_wave_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_, _reference_primitive : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_edge_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an edge port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout.html#ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout "ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**is_circuit_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a circuit port. The default is `False`. 

**is_wave_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a wave port. The default is `False`. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is 5. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is 5. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is “1mm”. 

**reference_primitive**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference primitive to place negative edge port terminal. The default is `None`. 

**reference_edge_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Edge number of reference primitive. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port objcet port when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_edge_port(assignment="line1", edge_number=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_edge_port.rst.txt)

# create_edge_port 

Hfss3dLayout.create_edge_port(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | 'Line3dLayout'_, _edge_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _is_circuit_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _is_wave_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _wave_horizontal_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _wave_vertical_extension : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 3_, _wave_launcher : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '1mm'_, _reference_primitive : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_edge_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_) → [BoundaryObject3dLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an edge port. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout.html#ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout "ansys.aedt.core.modeler.pcb.object_3d_layout.Line3dLayout") 
    
Name of the primitive to create the edge port on. 

**edge_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Edge number to create the edge port on. 

**is_circuit_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a circuit port. The default is `False`. 

**is_wave_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the edge port is a wave port. The default is `False`. 

**wave_horizontal_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Horizontal port extension factor. The default is 5. 

**wave_vertical_extension**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Vertical port extension factor. The default is 5. 

**wave_launcher**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
PEC (perfect electrical conductor) launcher size with units. The default is “1mm”. 

**reference_primitive**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference primitive to place negative edge port terminal. The default is `None`. 

**reference_edge_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Edge number of reference primitive. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")
    
Port objcet port when successful, `False` when failed.
References

```
>>> oEditor.CreateEdgePort

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.create_edge_port(assignment="line1", edge_number=0)

```
Copy to clipboard