---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# quarter_wave_feeding_line 

Patch.quarter_wave_feeding_line(_impedance_to_adapt : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a Trace to feed the patch.
The trace length is the quarter wavelength, and this width is calculated to return the desired impedance. 

Parameters: 
     

**impedance_to_adapt**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance the feeding line must return. By default 50 Ohms. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
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
>>> my_feeding_line = my_patch.quarter_wave_feeding_line()
>>> my_stackup.dielectric_x_position.expression = (
...     my_stackup.dielectric_x_position.expression + " - " + my_feeding_line.length.name
... )
>>> my_stackup.dielectric_length.expression = (
...     my_stackup.dielectric_length.expression + " + " + my_feeding_line.length.name
... )

```
Copy to clipboard
# quarter_wave_feeding_line 

Patch.quarter_wave_feeding_line(_impedance_to_adapt : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a Trace to feed the patch.
The trace length is the quarter wavelength, and this width is calculated to return the desired impedance. 

Parameters: 
     

**impedance_to_adapt**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance the feeding line must return. By default 50 Ohms. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
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
>>> my_feeding_line = my_patch.quarter_wave_feeding_line()
>>> my_stackup.dielectric_x_position.expression = (
...     my_stackup.dielectric_x_position.expression + " - " + my_feeding_line.length.name
... )
>>> my_stackup.dielectric_length.expression = (
...     my_stackup.dielectric_length.expression + " + " + my_feeding_line.length.name
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.quarter_wave_feeding_line.rst.txt)

# quarter_wave_feeding_line 

Patch.quarter_wave_feeding_line(_impedance_to_adapt : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_) → [Trace](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace") 
    
Create a Trace to feed the patch.
The trace length is the quarter wavelength, and this width is calculated to return the desired impedance. 

Parameters: 
     

**impedance_to_adapt**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance the feeding line must return. By default 50 Ohms. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace")
    
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
>>> my_feeding_line = my_patch.quarter_wave_feeding_line()
>>> my_stackup.dielectric_x_position.expression = (
...     my_stackup.dielectric_x_position.expression + " - " + my_feeding_line.length.name
... )
>>> my_stackup.dielectric_length.expression = (
...     my_stackup.dielectric_length.expression + " + " + my_feeding_line.length.name
... )

```
Copy to clipboard