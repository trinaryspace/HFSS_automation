---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SubRegion 

class ansys.aedt.core.modules.mesh_icepak.SubRegion(_app_ , _parts_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides Icepak mesh subregions properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import SubRegion
>>> obj = SubRegion()

```
Copy to clipboard
Methods  
| [`SubRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.create.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.create "ansys.aedt.core.modules.mesh_icepak.SubRegion.create")(padding_values, ...)  | Create subregion object.  |  
| --- | --- |  
| [`SubRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.delete "ansys.aedt.core.modules.mesh_icepak.SubRegion.delete")()  | Delete the subregion object.  |  
Attributes  
| [`SubRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.name.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.name "ansys.aedt.core.modules.mesh_icepak.SubRegion.name")  | Get the subregion name.  |  
| --- | --- |  
| [`SubRegion.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`SubRegion.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`SubRegion.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`SubRegion.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`SubRegion.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`SubRegion.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`SubRegion.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.object.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.object "ansys.aedt.core.modules.mesh_icepak.SubRegion.object")  | Get the subregion modeler object.  |  
| [`SubRegion.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`SubRegion.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`SubRegion.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.parts.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.parts "ansys.aedt.core.modules.mesh_icepak.SubRegion.parts")  | Parts included in the subregion.  |  
| [`SubRegion.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`SubRegion.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`SubRegion.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`SubRegion.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`SubRegion.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`SubRegion.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`SubRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir")  | Shortcut for dir(self).  |  
# SubRegion 

class ansys.aedt.core.modules.mesh_icepak.SubRegion(_app_ , _parts_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides Icepak mesh subregions properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import SubRegion
>>> obj = SubRegion()

```
Copy to clipboard
Methods  
| [`SubRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.create.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.create "ansys.aedt.core.modules.mesh_icepak.SubRegion.create")(padding_values, ...)  | Create subregion object.  |  
| --- | --- |  
| [`SubRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.delete "ansys.aedt.core.modules.mesh_icepak.SubRegion.delete")()  | Delete the subregion object.  |  
Attributes  
| [`SubRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.name.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.name "ansys.aedt.core.modules.mesh_icepak.SubRegion.name")  | Get the subregion name.  |  
| --- | --- |  
| [`SubRegion.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`SubRegion.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`SubRegion.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`SubRegion.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`SubRegion.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`SubRegion.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`SubRegion.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.object.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.object "ansys.aedt.core.modules.mesh_icepak.SubRegion.object")  | Get the subregion modeler object.  |  
| [`SubRegion.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`SubRegion.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`SubRegion.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.parts.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.parts "ansys.aedt.core.modules.mesh_icepak.SubRegion.parts")  | Parts included in the subregion.  |  
| [`SubRegion.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`SubRegion.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`SubRegion.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`SubRegion.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`SubRegion.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`SubRegion.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`SubRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.rst.txt)

# SubRegion 

class ansys.aedt.core.modules.mesh_icepak.SubRegion(_app_ , _parts_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides Icepak mesh subregions properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import SubRegion
>>> obj = SubRegion()

```
Copy to clipboard
Methods  
| [`SubRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.create.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.create "ansys.aedt.core.modules.mesh_icepak.SubRegion.create")(padding_values, ...)  | Create subregion object.  |  
| --- | --- |  
| [`SubRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.delete "ansys.aedt.core.modules.mesh_icepak.SubRegion.delete")()  | Delete the subregion object.  |  
Attributes  
| [`SubRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.name.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.name "ansys.aedt.core.modules.mesh_icepak.SubRegion.name")  | Get the subregion name.  |  
| --- | --- |  
| [`SubRegion.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`SubRegion.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`SubRegion.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`SubRegion.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`SubRegion.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`SubRegion.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`SubRegion.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.object.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.object "ansys.aedt.core.modules.mesh_icepak.SubRegion.object")  | Get the subregion modeler object.  |  
| [`SubRegion.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`SubRegion.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values "ansys.aedt.core.modules.mesh_icepak.SubRegion.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`SubRegion.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.parts.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.parts "ansys.aedt.core.modules.mesh_icepak.SubRegion.parts")  | Parts included in the subregion.  |  
| [`SubRegion.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`SubRegion.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`SubRegion.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`SubRegion.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`SubRegion.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`SubRegion.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.SubRegion.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`SubRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.SubRegion.public_dir")  | Shortcut for dir(self).  |