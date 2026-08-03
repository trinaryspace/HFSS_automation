---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# resize_around_element 

Stackup3D.resize_around_element(_element : CommonObject_, _percentage_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.25_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Resize the stackup around parametrized objects and make it parametrize. 

Parameters: 
     

**element** :class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id1)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch, 
    
:class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id3)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace Element around which the resizing is done. 

**percentage_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset of resize. Value accepted are greater than 0. O.25 by default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
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
# resize_around_element 

Stackup3D.resize_around_element(_element : CommonObject_, _percentage_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.25_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Resize the stackup around parametrized objects and make it parametrize. 

Parameters: 
     

**element** :class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id1)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch, 
    
:class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id3)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace Element around which the resizing is done. 

**percentage_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset of resize. Value accepted are greater than 0. O.25 by default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
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
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.rst.txt)

# resize_around_element 

Stackup3D.resize_around_element(_element : CommonObject_, _percentage_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.25_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Resize the stackup around parametrized objects and make it parametrize. 

Parameters: 
     

**element** :class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id1)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Patch, 
    
:class:[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.resize_around_element.html#id3)ansys.aedt.core.modeler.advanced_cad.stackup_3d.Trace Element around which the resizing is done. 

**percentage_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset of resize. Value accepted are greater than 0. O.25 by default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
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