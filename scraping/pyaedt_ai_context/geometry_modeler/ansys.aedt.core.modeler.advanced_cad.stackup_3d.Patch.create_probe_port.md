---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_probe_port 

Patch.create_probe_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _rel_x_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _rel_y_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _r : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Probe'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a coaxial probe port for the patch. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer (ground). 

**rel_x_offset** float, 
    
Relative x-offset for probe feed. Provide a value between 0.0 and 1.0. Offset in the x-direction relative to the center of the patch. 0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**rel_y_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `value` `between` 0 `and` 1 
    
0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**d**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `probe` `diameter` 
    
Default: 0.01 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` [`name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name") `of` `probe` port. 
    
Default value “Probe” 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_patch = top.add_patch(frequency=None, patch_width=51, patch_name="MLPatch")
>>> my_stackup.resize_around_element(my_patch)
>>> my_patch.create_probe_port(gnd)

```
Copy to clipboard
# create_probe_port 

Patch.create_probe_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _rel_x_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _rel_y_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _r : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Probe'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a coaxial probe port for the patch. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer (ground). 

**rel_x_offset** float, 
    
Relative x-offset for probe feed. Provide a value between 0.0 and 1.0. Offset in the x-direction relative to the center of the patch. 0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**rel_y_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `value` `between` 0 `and` 1 
    
0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**d**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `probe` `diameter` 
    
Default: 0.01 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` [`name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name") `of` `probe` port. 
    
Default value “Probe” 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_patch = top.add_patch(frequency=None, patch_width=51, patch_name="MLPatch")
>>> my_stackup.resize_around_element(my_patch)
>>> my_patch.create_probe_port(gnd)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.create_probe_port.rst.txt)

# create_probe_port 

Patch.create_probe_port(_reference_layer : [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")_, _rel_x_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _rel_y_offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _r : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Probe'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a coaxial probe port for the patch. 

Parameters: 
     

**reference_layer** class:ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D 
    
Reference layer (ground). 

**rel_x_offset** float, 
    
Relative x-offset for probe feed. Provide a value between 0.0 and 1.0. Offset in the x-direction relative to the center of the patch. 0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**rel_y_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `value` `between` 0 `and` 1 
    
0 places the probe at the center of the patch. 1 places the probe at the edge of the patch. Default: 0 

**d**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `probe` `diameter` 
    
Default: 0.01 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` [`name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.name") `of` `probe` port. 
    
Default value “Probe” 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_patch = top.add_patch(frequency=None, patch_width=51, patch_name="MLPatch")
>>> my_stackup.resize_around_element(my_patch)
>>> my_patch.create_probe_port(gnd)

```
Copy to clipboard