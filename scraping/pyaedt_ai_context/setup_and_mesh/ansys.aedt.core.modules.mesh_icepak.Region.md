---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Region 

class ansys.aedt.core.modules.mesh_icepak.Region(_app_) 
    
Provides Icepak global mesh region properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import Region
>>> obj = Region()

```
Copy to clipboard
Attributes  
| [`Region.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.name.html#ansys.aedt.core.modules.mesh_icepak.Region.name "ansys.aedt.core.modules.mesh_icepak.Region.name")  | Get the subregion name.  |  
| --- | --- |  
| [`Region.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`Region.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`Region.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`Region.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`Region.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`Region.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`Region.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")  | Get the subregion modeler object.  |  
| [`Region.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_types.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_types "ansys.aedt.core.modules.mesh_icepak.Region.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`Region.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_values.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_values "ansys.aedt.core.modules.mesh_icepak.Region.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`Region.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`Region.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`Region.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`Region.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`Region.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`Region.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`Region.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.public_dir.html#ansys.aedt.core.modules.mesh_icepak.Region.public_dir "ansys.aedt.core.modules.mesh_icepak.Region.public_dir")  | Shortcut for dir(self).  |  
# Region 

class ansys.aedt.core.modules.mesh_icepak.Region(_app_) 
    
Provides Icepak global mesh region properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import Region
>>> obj = Region()

```
Copy to clipboard
Attributes  
| [`Region.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.name.html#ansys.aedt.core.modules.mesh_icepak.Region.name "ansys.aedt.core.modules.mesh_icepak.Region.name")  | Get the subregion name.  |  
| --- | --- |  
| [`Region.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`Region.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`Region.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`Region.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`Region.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`Region.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`Region.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")  | Get the subregion modeler object.  |  
| [`Region.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_types.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_types "ansys.aedt.core.modules.mesh_icepak.Region.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`Region.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_values.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_values "ansys.aedt.core.modules.mesh_icepak.Region.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`Region.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`Region.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`Region.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`Region.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`Region.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`Region.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`Region.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.public_dir.html#ansys.aedt.core.modules.mesh_icepak.Region.public_dir "ansys.aedt.core.modules.mesh_icepak.Region.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.rst.txt)

# Region 

class ansys.aedt.core.modules.mesh_icepak.Region(_app_) 
    
Provides Icepak global mesh region properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import Region
>>> obj = Region()

```
Copy to clipboard
Attributes  
| [`Region.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.name.html#ansys.aedt.core.modules.mesh_icepak.Region.name "ansys.aedt.core.modules.mesh_icepak.Region.name")  | Get the subregion name.  |  
| --- | --- |  
| [`Region.negative_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding")  | Get a string with the padding value used in the -X direction.  |  
| [`Region.negative_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_x_padding_type")  | Get a string with the padding type used in the -X direction.  |  
| [`Region.negative_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding")  | Get a string with the padding value used in the -Y direction.  |  
| [`Region.negative_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_y_padding_type")  | Get a string with the padding type used in the -Y direction.  |  
| [`Region.negative_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding")  | Get a string with the padding value used in the -Z direction.  |  
| [`Region.negative_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.negative_z_padding_type")  | Get a string with the padding type used in the -Z direction.  |  
| [`Region.object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")  | Get the subregion modeler object.  |  
| [`Region.padding_types`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_types.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_types "ansys.aedt.core.modules.mesh_icepak.Region.padding_types")  | Get a list of strings containing the padding types used.  |  
| [`Region.padding_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.padding_values.html#ansys.aedt.core.modules.mesh_icepak.Region.padding_values "ansys.aedt.core.modules.mesh_icepak.Region.padding_values")  | Get a list of padding values (string or float) used.  |  
| [`Region.positive_x_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding")  | Get a string with the padding value used in the +X direction.  |  
| [`Region.positive_x_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_x_padding_type")  | Get a string with the padding type used in the +X direction.  |  
| [`Region.positive_y_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding")  | Get a string with the padding value used in the +Y direction.  |  
| [`Region.positive_y_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_y_padding_type")  | Get a string with the padding type used in the +Y direction.  |  
| [`Region.positive_z_padding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding")  | Get a string with the padding value used in the +Z direction.  |  
| [`Region.positive_z_padding_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type.html#ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type "ansys.aedt.core.modules.mesh_icepak.Region.positive_z_padding_type")  | Get a string with the padding type used in the +Z direction.  |  
| [`Region.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.public_dir.html#ansys.aedt.core.modules.mesh_icepak.Region.public_dir "ansys.aedt.core.modules.mesh_icepak.Region.public_dir")  | Shortcut for dir(self).  |