---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Padstack 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack(_app_ , _stackup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_) 
    
Provides the `Padstack` class member of Stackup3D.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()

```
Copy to clipboard
Methods  
| [`Padstack.add_via`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via")([position_x, position_y, ...])  | Insert a new via on this padstack.  |  
| --- | --- |  
| [`Padstack.set_all_antipad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value")(value)  | Set all antipads in all layers to a specified value.  |  
| [`Padstack.set_all_pad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value")(value)  | Set all pads in all layers to a specified value.  |  
| [`Padstack.set_start_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer")(layer)  | Set the start layer to a specified value.  |  
| [`Padstack.set_stop_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer")(layer)  | Set the stop layer to a specified value.  |  
Attributes  
| [`Padstack.num_sides`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides")  | Number of sides on the circle, which is `0` for a true circle.  |  
| --- | --- |  
| [`Padstack.padstacks_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer")  | Get the padstack definitions by layers.  |  
| [`Padstack.plating_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio")  | Plating ratio between 0 and 1.  |  
| [`Padstack.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir")  | Shortcut for dir(self).  |  
# Padstack 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack(_app_ , _stackup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_) 
    
Provides the `Padstack` class member of Stackup3D.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()

```
Copy to clipboard
Methods  
| [`Padstack.add_via`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via")([position_x, position_y, ...])  | Insert a new via on this padstack.  |  
| --- | --- |  
| [`Padstack.set_all_antipad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value")(value)  | Set all antipads in all layers to a specified value.  |  
| [`Padstack.set_all_pad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value")(value)  | Set all pads in all layers to a specified value.  |  
| [`Padstack.set_start_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer")(layer)  | Set the start layer to a specified value.  |  
| [`Padstack.set_stop_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer")(layer)  | Set the stop layer to a specified value.  |  
Attributes  
| [`Padstack.num_sides`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides")  | Number of sides on the circle, which is `0` for a true circle.  |  
| --- | --- |  
| [`Padstack.padstacks_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer")  | Get the padstack definitions by layers.  |  
| [`Padstack.plating_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio")  | Plating ratio between 0 and 1.  |  
| [`Padstack.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.rst.txt)

# Padstack 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack(_app_ , _stackup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_) 
    
Provides the `Padstack` class member of Stackup3D.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()

```
Copy to clipboard
Methods  
| [`Padstack.add_via`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via")([position_x, position_y, ...])  | Insert a new via on this padstack.  |  
| --- | --- |  
| [`Padstack.set_all_antipad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_antipad_value")(value)  | Set all antipads in all layers to a specified value.  |  
| [`Padstack.set_all_pad_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_all_pad_value")(value)  | Set all pads in all layers to a specified value.  |  
| [`Padstack.set_start_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_start_layer")(layer)  | Set the start layer to a specified value.  |  
| [`Padstack.set_stop_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.set_stop_layer")(layer)  | Set the stop layer to a specified value.  |  
Attributes  
| [`Padstack.num_sides`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.num_sides")  | Number of sides on the circle, which is `0` for a true circle.  |  
| --- | --- |  
| [`Padstack.padstacks_by_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.padstacks_by_layer")  | Get the padstack definitions by layers.  |  
| [`Padstack.plating_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.plating_ratio")  | Plating ratio between 0 and 1.  |  
| [`Padstack.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.public_dir")  | Shortcut for dir(self).  |