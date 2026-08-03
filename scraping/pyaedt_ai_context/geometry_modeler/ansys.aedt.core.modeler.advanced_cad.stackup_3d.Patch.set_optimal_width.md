---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# set_optimal_width 

Patch.set_optimal_width() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.
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
>>> my_patch.set_optimal_width()

```
Copy to clipboard
# set_optimal_width 

Patch.set_optimal_width() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.
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
>>> my_patch.set_optimal_width()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.set_optimal_width.rst.txt)

# set_optimal_width 

Patch.set_optimal_width() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set the expression of the NamedVariable corresponding to the patch width, to an optimal expression.
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
>>> my_patch.set_optimal_width()

```
Copy to clipboard