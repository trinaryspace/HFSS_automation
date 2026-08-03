---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_patch 

Layer3D.add_patch(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _patch_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _patch_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) → [Patch](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch") 
    
Create a parametric patch. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Frequency value for the patch calculation in Hz. 

**patch_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Patch width. 

**patch_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch length. The default is `None`. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start x position. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start y position. The default is `0.` 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch")
    
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

```
Copy to clipboard
# add_patch 

Layer3D.add_patch(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _patch_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _patch_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) → [Patch](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch") 
    
Create a parametric patch. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Frequency value for the patch calculation in Hz. 

**patch_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Patch width. 

**patch_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch length. The default is `None`. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start x position. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start y position. The default is `0.` 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch")
    
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

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch.rst.txt)

# add_patch 

Layer3D.add_patch(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _patch_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _patch_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _patch_position_x : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_position_y : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _patch_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_) → [Patch](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch") 
    
Create a parametric patch. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Frequency value for the patch calculation in Hz. 

**patch_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Patch width. 

**patch_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch length. The default is `None`. 

**patch_position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start x position. 

**patch_position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Patch start y position. The default is `0.` 

**patch_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Patch name. The default is `None`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Line orientation axis. The default is `"X"`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch")
    
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

```
Copy to clipboard