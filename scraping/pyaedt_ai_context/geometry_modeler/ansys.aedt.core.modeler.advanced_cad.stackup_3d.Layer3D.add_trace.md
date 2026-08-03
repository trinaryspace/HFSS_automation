---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_trace 

Layer3D.add_trace(_line_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _line_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_electrical_length : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_impedance : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a trace. 

Parameters: 
     

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line width. It can be the physical width or the line impedance. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line length. It can be the physical length or the electrical length in degrees. 

**is_electrical_length**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line length is an electrical length or a physical length. The default is `False`, which means it is a physical length. 

**is_impedance**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line width is an impedance. The default is `False`, in which case the line width is a geometrical value. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start x position. The default is `0`. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start y position. The default is `0`. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line reference system. The default is `None`, in which case a new coordinate system is created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency value for the line calculation in Hz. The default is `1e9`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=22)
>>> my_stackup.resize_around_element(my_trace)

```
Copy to clipboard
# add_trace 

Layer3D.add_trace(_line_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _line_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_electrical_length : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_impedance : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a trace. 

Parameters: 
     

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line width. It can be the physical width or the line impedance. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line length. It can be the physical length or the electrical length in degrees. 

**is_electrical_length**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line length is an electrical length or a physical length. The default is `False`, which means it is a physical length. 

**is_impedance**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line width is an impedance. The default is `False`, in which case the line width is a geometrical value. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start x position. The default is `0`. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start y position. The default is `0`. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line reference system. The default is `None`, in which case a new coordinate system is created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency value for the line calculation in Hz. The default is `1e9`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=22)
>>> my_stackup.resize_around_element(my_trace)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace.rst.txt)

# add_trace 

Layer3D.add_trace(_line_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _line_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_electrical_length : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_impedance : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a trace. 

Parameters: 
     

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line width. It can be the physical width or the line impedance. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Line length. It can be the physical length or the electrical length in degrees. 

**is_electrical_length**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line length is an electrical length or a physical length. The default is `False`, which means it is a physical length. 

**is_impedance**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the line width is an impedance. The default is `False`, in which case the line width is a geometrical value. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start x position. The default is `0`. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line center start y position. The default is `0`. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line reference system. The default is `None`, in which case a new coordinate system is created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency value for the line calculation in Hz. The default is `1e9`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_trace = top.add_trace(line_width=2.5, line_length=22)
>>> my_stackup.resize_around_element(my_trace)

```
Copy to clipboard