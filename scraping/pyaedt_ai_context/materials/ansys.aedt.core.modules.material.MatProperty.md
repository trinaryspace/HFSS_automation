---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# MatProperty 

class ansys.aedt.core.modules.material.MatProperty(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _val =None_, _thermalmodifier =None_, _spatialmodifier =None_) 
    
Manages simple, anisotropic, tensor, and non-linear properties. 

Parameters: 
     

**material**[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material property. 

**val**
    
The default is `None`. 

**thermalmodifier**
    
The default is `None`. 

**spatialmodifier**
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> matproperty = app.materials["copper"].conductivity

```
Copy to clipboard
Methods  
| [`MatProperty.add_spatial_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset")(dataset)  | Add a spatial modifier to a material property using an existing dataset.  |  
| --- | --- |  
| [`MatProperty.add_spatial_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form")(formula)  | Add a spatial modifier to a material property using a free-form formula.  |  
| [`MatProperty.add_thermal_modifier_closed_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form")([...])  | Add a thermal modifier to a material property using a closed-form formula.  |  
| [`MatProperty.add_thermal_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset")(dataset)  | Add a thermal modifier to a material property using an existing dataset.  |  
| [`MatProperty.add_thermal_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form")(formula)  | Add a thermal modifier to a material property using a free-form formula.  |  
| [`MatProperty.set_non_linear`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.set_non_linear.html#ansys.aedt.core.modules.material.MatProperty.set_non_linear "ansys.aedt.core.modules.material.MatProperty.set_non_linear")([x_unit, y_unit])  | Enable non-linear material.  |  
Attributes  
| [`MatProperty.data_set`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.data_set.html#ansys.aedt.core.modules.material.MatProperty.data_set "ansys.aedt.core.modules.material.MatProperty.data_set")  | Dataset.  |  
| --- | --- |  
| [`MatProperty.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.evaluated_value.html#ansys.aedt.core.modules.material.MatProperty.evaluated_value "ansys.aedt.core.modules.material.MatProperty.evaluated_value")  | Evaluated value.  |  
| [`MatProperty.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.public_dir.html#ansys.aedt.core.modules.material.MatProperty.public_dir "ansys.aedt.core.modules.material.MatProperty.public_dir")  | Shortcut for dir(self).  |  
| [`MatProperty.spatialmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.spatialmodifier.html#ansys.aedt.core.modules.material.MatProperty.spatialmodifier "ansys.aedt.core.modules.material.MatProperty.spatialmodifier")  | Spatial modifier.  |  
| [`MatProperty.thermalmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.thermalmodifier.html#ansys.aedt.core.modules.material.MatProperty.thermalmodifier "ansys.aedt.core.modules.material.MatProperty.thermalmodifier")  | Thermal modifier.  |  
| [`MatProperty.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.type.html#ansys.aedt.core.modules.material.MatProperty.type "ansys.aedt.core.modules.material.MatProperty.type")  | Type of the material property.  |  
| [`MatProperty.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.unit.html#ansys.aedt.core.modules.material.MatProperty.unit "ansys.aedt.core.modules.material.MatProperty.unit")  | Units for a material property value.  |  
| [`MatProperty.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.value.html#ansys.aedt.core.modules.material.MatProperty.value "ansys.aedt.core.modules.material.MatProperty.value")  | Value for a material property.  |  
# MatProperty 

class ansys.aedt.core.modules.material.MatProperty(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _val =None_, _thermalmodifier =None_, _spatialmodifier =None_) 
    
Manages simple, anisotropic, tensor, and non-linear properties. 

Parameters: 
     

**material**[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material property. 

**val**
    
The default is `None`. 

**thermalmodifier**
    
The default is `None`. 

**spatialmodifier**
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> matproperty = app.materials["copper"].conductivity

```
Copy to clipboard
Methods  
| [`MatProperty.add_spatial_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset")(dataset)  | Add a spatial modifier to a material property using an existing dataset.  |  
| --- | --- |  
| [`MatProperty.add_spatial_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form")(formula)  | Add a spatial modifier to a material property using a free-form formula.  |  
| [`MatProperty.add_thermal_modifier_closed_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form")([...])  | Add a thermal modifier to a material property using a closed-form formula.  |  
| [`MatProperty.add_thermal_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset")(dataset)  | Add a thermal modifier to a material property using an existing dataset.  |  
| [`MatProperty.add_thermal_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form")(formula)  | Add a thermal modifier to a material property using a free-form formula.  |  
| [`MatProperty.set_non_linear`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.set_non_linear.html#ansys.aedt.core.modules.material.MatProperty.set_non_linear "ansys.aedt.core.modules.material.MatProperty.set_non_linear")([x_unit, y_unit])  | Enable non-linear material.  |  
Attributes  
| [`MatProperty.data_set`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.data_set.html#ansys.aedt.core.modules.material.MatProperty.data_set "ansys.aedt.core.modules.material.MatProperty.data_set")  | Dataset.  |  
| --- | --- |  
| [`MatProperty.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.evaluated_value.html#ansys.aedt.core.modules.material.MatProperty.evaluated_value "ansys.aedt.core.modules.material.MatProperty.evaluated_value")  | Evaluated value.  |  
| [`MatProperty.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.public_dir.html#ansys.aedt.core.modules.material.MatProperty.public_dir "ansys.aedt.core.modules.material.MatProperty.public_dir")  | Shortcut for dir(self).  |  
| [`MatProperty.spatialmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.spatialmodifier.html#ansys.aedt.core.modules.material.MatProperty.spatialmodifier "ansys.aedt.core.modules.material.MatProperty.spatialmodifier")  | Spatial modifier.  |  
| [`MatProperty.thermalmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.thermalmodifier.html#ansys.aedt.core.modules.material.MatProperty.thermalmodifier "ansys.aedt.core.modules.material.MatProperty.thermalmodifier")  | Thermal modifier.  |  
| [`MatProperty.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.type.html#ansys.aedt.core.modules.material.MatProperty.type "ansys.aedt.core.modules.material.MatProperty.type")  | Type of the material property.  |  
| [`MatProperty.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.unit.html#ansys.aedt.core.modules.material.MatProperty.unit "ansys.aedt.core.modules.material.MatProperty.unit")  | Units for a material property value.  |  
| [`MatProperty.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.value.html#ansys.aedt.core.modules.material.MatProperty.value "ansys.aedt.core.modules.material.MatProperty.value")  | Value for a material property.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.rst.txt)

# MatProperty 

class ansys.aedt.core.modules.material.MatProperty(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _val =None_, _thermalmodifier =None_, _spatialmodifier =None_) 
    
Manages simple, anisotropic, tensor, and non-linear properties. 

Parameters: 
     

**material**[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material property. 

**val**
    
The default is `None`. 

**thermalmodifier**
    
The default is `None`. 

**spatialmodifier**
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> matproperty = app.materials["copper"].conductivity

```
Copy to clipboard
Methods  
| [`MatProperty.add_spatial_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_dataset")(dataset)  | Add a spatial modifier to a material property using an existing dataset.  |  
| --- | --- |  
| [`MatProperty.add_spatial_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form")(formula)  | Add a spatial modifier to a material property using a free-form formula.  |  
| [`MatProperty.add_thermal_modifier_closed_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form")([...])  | Add a thermal modifier to a material property using a closed-form formula.  |  
| [`MatProperty.add_thermal_modifier_dataset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset")(dataset)  | Add a thermal modifier to a material property using an existing dataset.  |  
| [`MatProperty.add_thermal_modifier_free_form`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form.html#ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form "ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_free_form")(formula)  | Add a thermal modifier to a material property using a free-form formula.  |  
| [`MatProperty.set_non_linear`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.set_non_linear.html#ansys.aedt.core.modules.material.MatProperty.set_non_linear "ansys.aedt.core.modules.material.MatProperty.set_non_linear")([x_unit, y_unit])  | Enable non-linear material.  |  
Attributes  
| [`MatProperty.data_set`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.data_set.html#ansys.aedt.core.modules.material.MatProperty.data_set "ansys.aedt.core.modules.material.MatProperty.data_set")  | Dataset.  |  
| --- | --- |  
| [`MatProperty.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.evaluated_value.html#ansys.aedt.core.modules.material.MatProperty.evaluated_value "ansys.aedt.core.modules.material.MatProperty.evaluated_value")  | Evaluated value.  |  
| [`MatProperty.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.public_dir.html#ansys.aedt.core.modules.material.MatProperty.public_dir "ansys.aedt.core.modules.material.MatProperty.public_dir")  | Shortcut for dir(self).  |  
| [`MatProperty.spatialmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.spatialmodifier.html#ansys.aedt.core.modules.material.MatProperty.spatialmodifier "ansys.aedt.core.modules.material.MatProperty.spatialmodifier")  | Spatial modifier.  |  
| [`MatProperty.thermalmodifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.thermalmodifier.html#ansys.aedt.core.modules.material.MatProperty.thermalmodifier "ansys.aedt.core.modules.material.MatProperty.thermalmodifier")  | Thermal modifier.  |  
| [`MatProperty.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.type.html#ansys.aedt.core.modules.material.MatProperty.type "ansys.aedt.core.modules.material.MatProperty.type")  | Type of the material property.  |  
| [`MatProperty.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.unit.html#ansys.aedt.core.modules.material.MatProperty.unit "ansys.aedt.core.modules.material.MatProperty.unit")  | Units for a material property value.  |  
| [`MatProperty.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.value.html#ansys.aedt.core.modules.material.MatProperty.value "ansys.aedt.core.modules.material.MatProperty.value")  | Value for a material property.  |