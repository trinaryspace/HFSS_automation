---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Stackup3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D(_application_ , _frequency =None_) 
    
Main Stackup3D Class. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The stackup frequency, it will be common to all layers in the stackup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)

```
Copy to clipboard
Methods  
| [`Stackup3D.add_dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer")(name[, ...])  | Add a new dielectric layer to the stackup.  |  
| --- | --- |  
| [`Stackup3D.add_ground_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.add_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer")(name[, layer_type, ...])  | Add a new layer to the stackup.  |  
| [`Stackup3D.add_padstack`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack")(name[, material])  | Add a new padstack definition.  |  
| [`Stackup3D.add_signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.resize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize")(percentage_offset)  | Resize the stackup around objects created by a percentage offset.  |  
| [`Stackup3D.resize_around_element`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element")(element[, ...])  | Resize the stackup around parametrized objects and make it parametrize.  |  
Attributes  
| [`Stackup3D.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application")  | Application object.  |  
| --- | --- |  
| [`Stackup3D.dielectric_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length")  | Stackup length.  |  
| [`Stackup3D.dielectric_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width")  | Stackup width.  |  
| [`Stackup3D.dielectric_x_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position")  | Stackup x origin.  |  
| [`Stackup3D.dielectric_y_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position")  | Stackup y origin.  |  
| [`Stackup3D.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics")  | List of dielectrics created.  |  
| [`Stackup3D.duplicated_material_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list")  | List of all duplicated material.  |  
| [`Stackup3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency")  | Frequency variable.  |  
| [`Stackup3D.grounds`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds")  | List of grounds created.  |  
| [`Stackup3D.layer_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names")  | List of all layer names.  |  
| [`Stackup3D.layer_positions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions")  | List of all layer positions.  |  
| [`Stackup3D.objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects")  | List of objects created.  |  
| [`Stackup3D.objects_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer")  | List of definitions created.  |  
| [`Stackup3D.padstacks`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks")  | List of definitions created.  |  
| [`Stackup3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir")  | Shortcut for dir(self).  |  
| [`Stackup3D.signals`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals")  | List of signals created.  |  
| [`Stackup3D.stackup_layers`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers")  | Dictionary of all stackup layers.  |  
| [`Stackup3D.start_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position")  | Variable containing the start position.  |  
| [`Stackup3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness")  | Total stackup thickness.  |  
| [`Stackup3D.z_position_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset")  | Elevation.  |  
# Stackup3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D(_application_ , _frequency =None_) 
    
Main Stackup3D Class. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The stackup frequency, it will be common to all layers in the stackup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)

```
Copy to clipboard
Methods  
| [`Stackup3D.add_dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer")(name[, ...])  | Add a new dielectric layer to the stackup.  |  
| --- | --- |  
| [`Stackup3D.add_ground_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.add_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer")(name[, layer_type, ...])  | Add a new layer to the stackup.  |  
| [`Stackup3D.add_padstack`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack")(name[, material])  | Add a new padstack definition.  |  
| [`Stackup3D.add_signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.resize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize")(percentage_offset)  | Resize the stackup around objects created by a percentage offset.  |  
| [`Stackup3D.resize_around_element`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element")(element[, ...])  | Resize the stackup around parametrized objects and make it parametrize.  |  
Attributes  
| [`Stackup3D.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application")  | Application object.  |  
| --- | --- |  
| [`Stackup3D.dielectric_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length")  | Stackup length.  |  
| [`Stackup3D.dielectric_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width")  | Stackup width.  |  
| [`Stackup3D.dielectric_x_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position")  | Stackup x origin.  |  
| [`Stackup3D.dielectric_y_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position")  | Stackup y origin.  |  
| [`Stackup3D.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics")  | List of dielectrics created.  |  
| [`Stackup3D.duplicated_material_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list")  | List of all duplicated material.  |  
| [`Stackup3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency")  | Frequency variable.  |  
| [`Stackup3D.grounds`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds")  | List of grounds created.  |  
| [`Stackup3D.layer_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names")  | List of all layer names.  |  
| [`Stackup3D.layer_positions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions")  | List of all layer positions.  |  
| [`Stackup3D.objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects")  | List of objects created.  |  
| [`Stackup3D.objects_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer")  | List of definitions created.  |  
| [`Stackup3D.padstacks`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks")  | List of definitions created.  |  
| [`Stackup3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir")  | Shortcut for dir(self).  |  
| [`Stackup3D.signals`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals")  | List of signals created.  |  
| [`Stackup3D.stackup_layers`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers")  | Dictionary of all stackup layers.  |  
| [`Stackup3D.start_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position")  | Variable containing the start position.  |  
| [`Stackup3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness")  | Total stackup thickness.  |  
| [`Stackup3D.z_position_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset")  | Elevation.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.rst.txt)

# Stackup3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D(_application_ , _frequency =None_) 
    
Main Stackup3D Class. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The stackup frequency, it will be common to all layers in the stackup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)

```
Copy to clipboard
Methods  
| [`Stackup3D.add_dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer")(name[, ...])  | Add a new dielectric layer to the stackup.  |  
| --- | --- |  
| [`Stackup3D.add_ground_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_ground_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.add_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer")(name[, layer_type, ...])  | Add a new layer to the stackup.  |  
| [`Stackup3D.add_padstack`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_padstack")(name[, material])  | Add a new padstack definition.  |  
| [`Stackup3D.add_signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer")(name[, material, ...])  | Add a new ground layer to the stackup.  |  
| [`Stackup3D.resize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize")(percentage_offset)  | Resize the stackup around objects created by a percentage offset.  |  
| [`Stackup3D.resize_around_element`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element")(element[, ...])  | Resize the stackup around parametrized objects and make it parametrize.  |  
Attributes  
| [`Stackup3D.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.application")  | Application object.  |  
| --- | --- |  
| [`Stackup3D.dielectric_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_length")  | Stackup length.  |  
| [`Stackup3D.dielectric_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_width")  | Stackup width.  |  
| [`Stackup3D.dielectric_x_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_x_position")  | Stackup x origin.  |  
| [`Stackup3D.dielectric_y_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectric_y_position")  | Stackup y origin.  |  
| [`Stackup3D.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.dielectrics")  | List of dielectrics created.  |  
| [`Stackup3D.duplicated_material_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.duplicated_material_list")  | List of all duplicated material.  |  
| [`Stackup3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.frequency")  | Frequency variable.  |  
| [`Stackup3D.grounds`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.grounds")  | List of grounds created.  |  
| [`Stackup3D.layer_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_names")  | List of all layer names.  |  
| [`Stackup3D.layer_positions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.layer_positions")  | List of all layer positions.  |  
| [`Stackup3D.objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects")  | List of objects created.  |  
| [`Stackup3D.objects_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.objects_by_layer")  | List of definitions created.  |  
| [`Stackup3D.padstacks`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.padstacks")  | List of definitions created.  |  
| [`Stackup3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.public_dir")  | Shortcut for dir(self).  |  
| [`Stackup3D.signals`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.signals")  | List of signals created.  |  
| [`Stackup3D.stackup_layers`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.stackup_layers")  | Dictionary of all stackup layers.  |  
| [`Stackup3D.start_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.start_position")  | Variable containing the start position.  |  
| [`Stackup3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.thickness")  | Total stackup thickness.  |  
| [`Stackup3D.z_position_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.z_position_offset")  | Elevation.  |