---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Patch 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch(_application_ , _frequency_ , _dx_ , _signal_layer_ , _dielectric_layer_ , _dy =None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'patch'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Patch Class in Stackup3D. Create a parametrized patch.
It is preferable to use the add_patch method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Target resonant frequency for the patch antenna. The default is `None`, in which case the patch frequency is that of the layer or of the stackup. 

**dx**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The patch width. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the patch will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the patch and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**dy**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The patch length. By default, it is None and so the length is calculated by prediction formulas. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch x position, by default it is 0. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch y position, by default it is 0. 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name, by default “patch”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the patch. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch length axis, by default “X”.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> stackup = Stackup3D(hfss)
>>> gnd = stackup.add_ground_layer("ground", material="copper", thickness=0.035, fill_material="air")
>>> dielectric = stackup.add_dielectric_layer("dielectric", thickness="0.5" + length_units, material="Duroid (tm)")
>>> signal = stackup.add_signal_layer("signal", material="copper", thickness=0.035, fill_material="air")
>>> patch = signal.add_patch(patch_length=9.57, patch_width=9.25, patch_name="Patch")
>>> stackup.resize_around_element(patch)
>>> pad_length = [3, 3, 3, 3, 3, 3]  # Air bounding box buffer in mm.
>>> region = hfss.modeler.create_region(pad_length, is_percentage=False)
>>> hfss.assign_radiation_boundary_to_objects(region)
>>> patch.create_probe_port(gnd, rel_x_offset=0.485)

```
Copy to clipboard
Methods  
| [`Patch.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
| [`Patch.create_probe_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port")(reference_layer[, ...])  | Create a coaxial probe port for the patch.  |  
| [`Patch.quarter_wave_feeding_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line")([...])  | Create a Trace to feed the patch.  |  
| [`Patch.set_optimal_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width")()  | Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.  |  
Attributes  
| [`Patch.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length")  | Added length calculation.  |  
| --- | --- |  
| [`Patch.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object")  | PyAEDT object 3D.  |  
| [`Patch.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application")  | App object.  |  
| [`Patch.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Patch.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity")  | Effective permittivity.  |  
| [`Patch.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency")  | Model frequency.  |  
| [`Patch.impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance")  | Impedance.  |  
| [`Patch.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name")  | Layer name.  |  
| [`Patch.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number")  | Layer ID.  |  
| [`Patch.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length")  | Length.  |  
| [`Patch.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name")  | Material name.  |  
| [`Patch.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name")  | Object name.  |  
| [`Patch.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity")  | Permittivity.  |  
| [`Patch.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer")  | Object bounding box.  |  
| [`Patch.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x")  | Starting position X.  |  
| [`Patch.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y")  | Starting position Y.  |  
| [`Patch.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir")  | Shortcut for dir(self).  |  
| [`Patch.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system")  | Coordinate system of the object.  |  
| [`Patch.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Patch.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness")  | Substrate thickness.  |  
| [`Patch.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length")  | Wave length.  |  
| [`Patch.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width")  | Width.  |  
# Patch 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch(_application_ , _frequency_ , _dx_ , _signal_layer_ , _dielectric_layer_ , _dy =None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'patch'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Patch Class in Stackup3D. Create a parametrized patch.
It is preferable to use the add_patch method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Target resonant frequency for the patch antenna. The default is `None`, in which case the patch frequency is that of the layer or of the stackup. 

**dx**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The patch width. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the patch will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the patch and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**dy**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The patch length. By default, it is None and so the length is calculated by prediction formulas. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch x position, by default it is 0. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch y position, by default it is 0. 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name, by default “patch”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the patch. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch length axis, by default “X”.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> stackup = Stackup3D(hfss)
>>> gnd = stackup.add_ground_layer("ground", material="copper", thickness=0.035, fill_material="air")
>>> dielectric = stackup.add_dielectric_layer("dielectric", thickness="0.5" + length_units, material="Duroid (tm)")
>>> signal = stackup.add_signal_layer("signal", material="copper", thickness=0.035, fill_material="air")
>>> patch = signal.add_patch(patch_length=9.57, patch_width=9.25, patch_name="Patch")
>>> stackup.resize_around_element(patch)
>>> pad_length = [3, 3, 3, 3, 3, 3]  # Air bounding box buffer in mm.
>>> region = hfss.modeler.create_region(pad_length, is_percentage=False)
>>> hfss.assign_radiation_boundary_to_objects(region)
>>> patch.create_probe_port(gnd, rel_x_offset=0.485)

```
Copy to clipboard
Methods  
| [`Patch.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
| [`Patch.create_probe_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port")(reference_layer[, ...])  | Create a coaxial probe port for the patch.  |  
| [`Patch.quarter_wave_feeding_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line")([...])  | Create a Trace to feed the patch.  |  
| [`Patch.set_optimal_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width")()  | Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.  |  
Attributes  
| [`Patch.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length")  | Added length calculation.  |  
| --- | --- |  
| [`Patch.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object")  | PyAEDT object 3D.  |  
| [`Patch.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application")  | App object.  |  
| [`Patch.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Patch.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity")  | Effective permittivity.  |  
| [`Patch.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency")  | Model frequency.  |  
| [`Patch.impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance")  | Impedance.  |  
| [`Patch.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name")  | Layer name.  |  
| [`Patch.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number")  | Layer ID.  |  
| [`Patch.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length")  | Length.  |  
| [`Patch.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name")  | Material name.  |  
| [`Patch.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name")  | Object name.  |  
| [`Patch.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity")  | Permittivity.  |  
| [`Patch.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer")  | Object bounding box.  |  
| [`Patch.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x")  | Starting position X.  |  
| [`Patch.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y")  | Starting position Y.  |  
| [`Patch.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir")  | Shortcut for dir(self).  |  
| [`Patch.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system")  | Coordinate system of the object.  |  
| [`Patch.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Patch.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness")  | Substrate thickness.  |  
| [`Patch.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length")  | Wave length.  |  
| [`Patch.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width")  | Width.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.rst.txt)

# Patch 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch(_application_ , _frequency_ , _dx_ , _signal_layer_ , _dielectric_layer_ , _dy =None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'patch'_, _reference_system =None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) 
    
Patch Class in Stackup3D. Create a parametrized patch.
It is preferable to use the add_patch method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Target resonant frequency for the patch antenna. The default is `None`, in which case the patch frequency is that of the layer or of the stackup. 

**dx**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The patch width. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the patch will be drawn. 

**dielectric_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The dielectric layer between the patch and the ground layer. Its permittivity and thickness are used in prediction formulas. 

**dy**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
The patch length. By default, it is None and so the length is calculated by prediction formulas. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch x position, by default it is 0. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch y position, by default it is 0. 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name, by default “patch”. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the patch. By default, None. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch length axis, by default “X”.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> stackup = Stackup3D(hfss)
>>> gnd = stackup.add_ground_layer("ground", material="copper", thickness=0.035, fill_material="air")
>>> dielectric = stackup.add_dielectric_layer("dielectric", thickness="0.5" + length_units, material="Duroid (tm)")
>>> signal = stackup.add_signal_layer("signal", material="copper", thickness=0.035, fill_material="air")
>>> patch = signal.add_patch(patch_length=9.57, patch_width=9.25, patch_name="Patch")
>>> stackup.resize_around_element(patch)
>>> pad_length = [3, 3, 3, 3, 3, 3]  # Air bounding box buffer in mm.
>>> region = hfss.modeler.create_region(pad_length, is_percentage=False)
>>> hfss.assign_radiation_boundary_to_objects(region)
>>> patch.create_probe_port(gnd, rel_x_offset=0.485)

```
Copy to clipboard
Methods  
| [`Patch.create_lumped_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_lumped_port")(reference_layer[, ...])  | Create a parametrized lumped port.  |  
| --- | --- |  
| [`Patch.create_probe_port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port")(reference_layer[, ...])  | Create a coaxial probe port for the patch.  |  
| [`Patch.quarter_wave_feeding_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line")([...])  | Create a Trace to feed the patch.  |  
| [`Patch.set_optimal_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width")()  | Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.  |  
Attributes  
| [`Patch.added_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.added_length")  | Added length calculation.  |  
| --- | --- |  
| [`Patch.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.aedt_object")  | PyAEDT object 3D.  |  
| [`Patch.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.application")  | App object.  |  
| [`Patch.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Patch.effective_permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.effective_permittivity")  | Effective permittivity.  |  
| [`Patch.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.frequency")  | Model frequency.  |  
| [`Patch.impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.impedance")  | Impedance.  |  
| [`Patch.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_name")  | Layer name.  |  
| [`Patch.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.layer_number")  | Layer ID.  |  
| [`Patch.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.length")  | Length.  |  
| [`Patch.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.material_name")  | Material name.  |  
| [`Patch.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name")  | Object name.  |  
| [`Patch.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.permittivity")  | Permittivity.  |  
| [`Patch.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.points_on_layer")  | Object bounding box.  |  
| [`Patch.position_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_x")  | Starting position X.  |  
| [`Patch.position_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.position_y")  | Starting position Y.  |  
| [`Patch.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.public_dir")  | Shortcut for dir(self).  |  
| [`Patch.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.reference_system")  | Coordinate system of the object.  |  
| [`Patch.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.signal_layer")  | Signal layer that the object belongs to.  |  
| [`Patch.substrate_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.substrate_thickness")  | Substrate thickness.  |  
| [`Patch.wave_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.wave_length")  | Wave length.  |  
| [`Patch.width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.width")  | Width.  |