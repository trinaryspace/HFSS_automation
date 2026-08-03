---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Trace 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace(_application_ , _frequency_ , _line_width_ , _line_impedance_ , _signal_layer_ , _dielectric_layer_ , _line_electrical_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _line_length =None_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'line'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Trace Class in Stackup3D. Create a parametrized trace.
It is preferable to use the add_trace method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line frequency, it is used in prediction formulas. If it is None, the line frequency will be that of the layer or of the stackup. 

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line width. If it is None, it will calculate it from characteristic impedance of the line. 

**line_impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The characteristic impedance of the line. If a line width is entered by the user, the characteristic impedance will be calculated from it. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the line and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**line_electrical_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The ratio between the line length and the wavelength in degree. By default 90 which is corresponding to the quarter of the wavelength. If it is None, it will be directly calculated from the line length entered by the user. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The line length. By default, it is None and so the length is calculated by prediction formulas according to the electrical length. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line x position, by default it is 0. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line y position, by default it is 0. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name, by default “line”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the line. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line length axis, by default “X”.
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
Methods  
| [`Trace.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
Attributes  
| [`Trace.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length")  | Added Length.  |  
| --- | --- |  
| [`Trace.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object")  | PyAEDT object 3D.  |  
| [`Trace.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application")  | App object.  |  
| [`Trace.charac_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance")  | Characteristic Impedance.  |  
| [`Trace.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Trace.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity")  | Effective Permittivity.  |  
| [`Trace.effective_permittivity_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w")  | Effective Permittivity when dielectric thickness is upper than width.  |  
| [`Trace.effective_permittivity_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h")  | Effective Permittivity when width is upper than dielectric thickness.  |  
| [`Trace.electrical_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length")  | Electrical Length.  |  
| [`Trace.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency")  | Frequency.  |  
| [`Trace.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name")  | Layer name.  |  
| [`Trace.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number")  | Layer ID.  |  
| [`Trace.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length")  | Length.  |  
| [`Trace.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name")  | Material name.  |  
| [`Trace.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name")  | Object name.  |  
| [`Trace.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity")  | Permittivity.  |  
| [`Trace.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer")  | Object bounding box.  |  
| [`Trace.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x")  | Starting Position X.  |  
| [`Trace.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y")  | Starting Position Y.  |  
| [`Trace.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir")  | Shortcut for dir(self).  |  
| [`Trace.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system")  | Coordinate system of the object.  |  
| [`Trace.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Trace.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness")  | Substrate Thickness.  |  
| [`Trace.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length")  | Wave Length.  |  
| [`Trace.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width")  | Width.  |  
| [`Trace.width_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w")  | Width when the substrat thickness is two times upper than the width.  |  
| [`Trace.width_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h")  | Width when the width is two times upper than substrat thickness.  |  
# Trace 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace(_application_ , _frequency_ , _line_width_ , _line_impedance_ , _signal_layer_ , _dielectric_layer_ , _line_electrical_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _line_length =None_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'line'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Trace Class in Stackup3D. Create a parametrized trace.
It is preferable to use the add_trace method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line frequency, it is used in prediction formulas. If it is None, the line frequency will be that of the layer or of the stackup. 

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line width. If it is None, it will calculate it from characteristic impedance of the line. 

**line_impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The characteristic impedance of the line. If a line width is entered by the user, the characteristic impedance will be calculated from it. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the line and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**line_electrical_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The ratio between the line length and the wavelength in degree. By default 90 which is corresponding to the quarter of the wavelength. If it is None, it will be directly calculated from the line length entered by the user. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The line length. By default, it is None and so the length is calculated by prediction formulas according to the electrical length. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line x position, by default it is 0. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line y position, by default it is 0. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name, by default “line”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the line. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line length axis, by default “X”.
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
Methods  
| [`Trace.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
Attributes  
| [`Trace.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length")  | Added Length.  |  
| --- | --- |  
| [`Trace.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object")  | PyAEDT object 3D.  |  
| [`Trace.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application")  | App object.  |  
| [`Trace.charac_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance")  | Characteristic Impedance.  |  
| [`Trace.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Trace.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity")  | Effective Permittivity.  |  
| [`Trace.effective_permittivity_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w")  | Effective Permittivity when dielectric thickness is upper than width.  |  
| [`Trace.effective_permittivity_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h")  | Effective Permittivity when width is upper than dielectric thickness.  |  
| [`Trace.electrical_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length")  | Electrical Length.  |  
| [`Trace.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency")  | Frequency.  |  
| [`Trace.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name")  | Layer name.  |  
| [`Trace.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number")  | Layer ID.  |  
| [`Trace.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length")  | Length.  |  
| [`Trace.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name")  | Material name.  |  
| [`Trace.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name")  | Object name.  |  
| [`Trace.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity")  | Permittivity.  |  
| [`Trace.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer")  | Object bounding box.  |  
| [`Trace.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x")  | Starting Position X.  |  
| [`Trace.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y")  | Starting Position Y.  |  
| [`Trace.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir")  | Shortcut for dir(self).  |  
| [`Trace.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system")  | Coordinate system of the object.  |  
| [`Trace.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Trace.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness")  | Substrate Thickness.  |  
| [`Trace.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length")  | Wave Length.  |  
| [`Trace.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width")  | Width.  |  
| [`Trace.width_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w")  | Width when the substrat thickness is two times upper than the width.  |  
| [`Trace.width_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h")  | Width when the width is two times upper than substrat thickness.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.rst.txt)

# Trace 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace(_application_ , _frequency_ , _line_width_ , _line_impedance_ , _signal_layer_ , _dielectric_layer_ , _line_electrical_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _line_length =None_, _line_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _line_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'line'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Trace Class in Stackup3D. Create a parametrized trace.
It is preferable to use the add_trace method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line frequency, it is used in prediction formulas. If it is None, the line frequency will be that of the layer or of the stackup. 

**line_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
The line width. If it is None, it will calculate it from characteristic impedance of the line. 

**line_impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The characteristic impedance of the line. If a line width is entered by the user, the characteristic impedance will be calculated from it. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the line and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**line_electrical_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The ratio between the line length and the wavelength in degree. By default 90 which is corresponding to the quarter of the wavelength. If it is None, it will be directly calculated from the line length entered by the user. 

**line_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The line length. By default, it is None and so the length is calculated by prediction formulas according to the electrical length. 

**line_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line x position, by default it is 0. 

**line_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Line y position, by default it is 0. 

**line_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line name, by default “line”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the line. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line length axis, by default “X”.
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
Methods  
| [`Trace.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
Attributes  
| [`Trace.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.added_length")  | Added Length.  |  
| --- | --- |  
| [`Trace.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.aedt_object")  | PyAEDT object 3D.  |  
| [`Trace.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.application")  | App object.  |  
| [`Trace.charac_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.charac_impedance")  | Characteristic Impedance.  |  
| [`Trace.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Trace.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity")  | Effective Permittivity.  |  
| [`Trace.effective_permittivity_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_h_w")  | Effective Permittivity when dielectric thickness is upper than width.  |  
| [`Trace.effective_permittivity_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.effective_permittivity_w_h")  | Effective Permittivity when width is upper than dielectric thickness.  |  
| [`Trace.electrical_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.electrical_length")  | Electrical Length.  |  
| [`Trace.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.frequency")  | Frequency.  |  
| [`Trace.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_name")  | Layer name.  |  
| [`Trace.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.layer_number")  | Layer ID.  |  
| [`Trace.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.length")  | Length.  |  
| [`Trace.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.material_name")  | Material name.  |  
| [`Trace.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.name")  | Object name.  |  
| [`Trace.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.permittivity")  | Permittivity.  |  
| [`Trace.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.points_on_layer")  | Object bounding box.  |  
| [`Trace.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_x")  | Starting Position X.  |  
| [`Trace.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.position_y")  | Starting Position Y.  |  
| [`Trace.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.public_dir")  | Shortcut for dir(self).  |  
| [`Trace.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.reference_system")  | Coordinate system of the object.  |  
| [`Trace.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Trace.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.substrate_thickness")  | Substrate Thickness.  |  
| [`Trace.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.wave_length")  | Wave Length.  |  
| [`Trace.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width")  | Width.  |  
| [`Trace.width_h_w`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_h_w")  | Width when the substrat thickness is two times upper than the width.  |  
| [`Trace.width_w_h`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.width_w_h")  | Width when the width is two times upper than substrat thickness.  |