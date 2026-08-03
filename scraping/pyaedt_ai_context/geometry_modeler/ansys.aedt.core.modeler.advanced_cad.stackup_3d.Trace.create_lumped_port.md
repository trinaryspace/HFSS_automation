---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_lumped_port 

Trace.create_lumped_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _opposite_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _port_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axisdir : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a parametrized lumped port. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer, which is the ground layer in most cases. 

**opposite_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Change the side where the port is created. 

**port_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the lumped port. 

**axisdir**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. `True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=90, is_electrical_length=True)
>>> my_stackup.resize_around_element(my_trace)
>>> my_trace.create_lumped_port(gnd)
>>> my_trace.create_lumped_port(gnd, opposite_side=True)

```
Copy to clipboard
# create_lumped_port 

Trace.create_lumped_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _opposite_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _port_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axisdir : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a parametrized lumped port. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer, which is the ground layer in most cases. 

**opposite_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Change the side where the port is created. 

**port_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the lumped port. 

**axisdir**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. `True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=90, is_electrical_length=True)
>>> my_stackup.resize_around_element(my_trace)
>>> my_trace.create_lumped_port(gnd)
>>> my_trace.create_lumped_port(gnd, opposite_side=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port.rst.txt)

# create_lumped_port 

Trace.create_lumped_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _opposite_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _port_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axisdir : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a parametrized lumped port. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer, which is the ground layer in most cases. 

**opposite_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Change the side where the port is created. 

**port_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the lumped port. 

**axisdir**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. `True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=90, is_electrical_length=True)
>>> my_stackup.resize_around_element(my_trace)
>>> my_trace.create_lumped_port(gnd)
>>> my_trace.create_lumped_port(gnd, opposite_side=True)

```
Copy to clipboard