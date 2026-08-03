---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_parametrize_material 

Layer3D.duplicate_parametrize_material(_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cloned_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _list_of_properties : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = ('permittivity', 'permeability', 'conductivity', 'dielectric_loss_tangent', 'magnetic_loss_tangent')_) → DuplicatedParametrizedMaterial 
    
Duplicate a material and parametrize all properties. 

Parameters: 
     

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of origin material 

**cloned_material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of destination material. The default is `None`. 

**list_of_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties to parametrize. The default is `("permittivity", "permeability", "conductivity", "dielectric_loss_tan", "magnetic_loss_tan")`. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Layer3D
>>> obj = Layer3D()
>>> obj.duplicate_parametrize_material(material_name=1)

```
Copy to clipboard
# duplicate_parametrize_material 

Layer3D.duplicate_parametrize_material(_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cloned_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _list_of_properties : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = ('permittivity', 'permeability', 'conductivity', 'dielectric_loss_tangent', 'magnetic_loss_tangent')_) → DuplicatedParametrizedMaterial 
    
Duplicate a material and parametrize all properties. 

Parameters: 
     

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of origin material 

**cloned_material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of destination material. The default is `None`. 

**list_of_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties to parametrize. The default is `("permittivity", "permeability", "conductivity", "dielectric_loss_tan", "magnetic_loss_tan")`. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Layer3D
>>> obj = Layer3D()
>>> obj.duplicate_parametrize_material(material_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material.rst.txt)

# duplicate_parametrize_material 

Layer3D.duplicate_parametrize_material(_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cloned_material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _list_of_properties : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = ('permittivity', 'permeability', 'conductivity', 'dielectric_loss_tangent', 'magnetic_loss_tangent')_) → DuplicatedParametrizedMaterial 
    
Duplicate a material and parametrize all properties. 

Parameters: 
     

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of origin material 

**cloned_material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of destination material. The default is `None`. 

**list_of_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties to parametrize. The default is `("permittivity", "permeability", "conductivity", "dielectric_loss_tan", "magnetic_loss_tan")`. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Layer3D
>>> obj = Layer3D()
>>> obj.duplicate_parametrize_material(material_name=1)

```
Copy to clipboard