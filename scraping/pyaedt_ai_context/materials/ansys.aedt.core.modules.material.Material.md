---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# Material 

class ansys.aedt.core.modules.material.Material(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages material properties. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> material = app.materials["copper"]

```
Copy to clipboard
Methods  
| [`Material.get_core_loss_coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_core_loss_coefficients.html#ansys.aedt.core.modules.material.Material.get_core_loss_coefficients "ansys.aedt.core.modules.material.Material.get_core_loss_coefficients")(...[, ...])  | Get electrical steel or power ferrite core loss coefficients at a given frequency.  |  
| --- | --- |  
| [`Material.get_curve_coreloss_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_type.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_type "ansys.aedt.core.modules.material.Material.get_curve_coreloss_type")()  | Return the curve core loss type assigned to material.  |  
| [`Material.get_curve_coreloss_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_values.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_values "ansys.aedt.core.modules.material.Material.get_curve_coreloss_values")()  | Return the curve core values type assigned to material.  |  
| [`Material.get_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.get_magnetic_coercivity "ansys.aedt.core.modules.material.Material.get_magnetic_coercivity")()  | Get the magnetic coercivity values.  |  
| [`Material.is_conductor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_conductor.html#ansys.aedt.core.modules.material.Material.is_conductor "ansys.aedt.core.modules.material.Material.is_conductor")([threshold])  | Check if the material is a conductor.  |  
| [`Material.is_dielectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_dielectric.html#ansys.aedt.core.modules.material.Material.is_dielectric "ansys.aedt.core.modules.material.Material.is_dielectric")([threshold])  | Check if the material is dielectric.  |  
| [`Material.set_bp_curve_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss.html#ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss "ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss")(points[, ...])  | Set B-P Type Core Loss.  |  
| [`Material.set_coreloss_at_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency.html#ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency "ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency")(...[, ...])  | Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies.  |  
| [`Material.set_djordjevic_sarkar_model`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model.html#ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model "ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model")([dk, ...])  | Set Djordjevic-Sarkar model.  |  
| [`Material.set_electrical_steel_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss.html#ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss "ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss")([kh, ...])  | Set electrical steel core loss.  |  
| [`Material.set_hysteresis_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss.html#ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss "ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss")([kdc, hci, ...])  | Set Hysteresis Type Core Loss.  |  
| [`Material.set_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.set_magnetic_coercivity "ansys.aedt.core.modules.material.Material.set_magnetic_coercivity")([value, x, ...])  | Set magnetic coercivity for material.  |  
| [`Material.set_power_ferrite_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss.html#ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss "ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss")([cm, x, ...])  | Set Power Ferrite Type Core Loss.  |  
| [`Material.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.update.html#ansys.aedt.core.modules.material.Material.update "ansys.aedt.core.modules.material.Material.update")()  | Update the material in AEDT.  |  
Attributes  
| [`Material.conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.conductivity.html#ansys.aedt.core.modules.material.Material.conductivity "ansys.aedt.core.modules.material.Material.conductivity")  | Conductivity.  |  
| --- | --- |  
| [`Material.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.coordinate_system.html#ansys.aedt.core.modules.material.Material.coordinate_system "ansys.aedt.core.modules.material.Material.coordinate_system")  | Material coordinate system.  |  
| [`Material.dielectric_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.dielectric_loss_tangent.html#ansys.aedt.core.modules.material.Material.dielectric_loss_tangent "ansys.aedt.core.modules.material.Material.dielectric_loss_tangent")  | Dielectric loss tangent.  |  
| [`Material.diffusivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.diffusivity.html#ansys.aedt.core.modules.material.Material.diffusivity "ansys.aedt.core.modules.material.Material.diffusivity")  | Diffusivity.  |  
| [`Material.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_used.html#ansys.aedt.core.modules.material.Material.is_used "ansys.aedt.core.modules.material.Material.is_used")  | Checks if a project material is in use.  |  
| [`Material.magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.magnetic_coercivity "ansys.aedt.core.modules.material.Material.magnetic_coercivity")  | Magnetic coercivity.  |  
| [`Material.magnetic_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_loss_tangent.html#ansys.aedt.core.modules.material.Material.magnetic_loss_tangent "ansys.aedt.core.modules.material.Material.magnetic_loss_tangent")  | Magnetic loss tangent.  |  
| [`Material.mass_density`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.mass_density.html#ansys.aedt.core.modules.material.Material.mass_density "ansys.aedt.core.modules.material.Material.mass_density")  | Mass density.  |  
| [`Material.material_appearance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.material_appearance.html#ansys.aedt.core.modules.material.Material.material_appearance "ansys.aedt.core.modules.material.Material.material_appearance")  | Material appearance specified as a list.  |  
| [`Material.molecular_mass`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.molecular_mass.html#ansys.aedt.core.modules.material.Material.molecular_mass "ansys.aedt.core.modules.material.Material.molecular_mass")  | Molecular mass.  |  
| [`Material.permeability`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permeability.html#ansys.aedt.core.modules.material.Material.permeability "ansys.aedt.core.modules.material.Material.permeability")  | Permeability.  |  
| [`Material.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permittivity.html#ansys.aedt.core.modules.material.Material.permittivity "ansys.aedt.core.modules.material.Material.permittivity")  | Permittivity.  |  
| [`Material.poissons_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.poissons_ratio.html#ansys.aedt.core.modules.material.Material.poissons_ratio "ansys.aedt.core.modules.material.Material.poissons_ratio")  | Poisson's ratio.  |  
| [`Material.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.public_dir.html#ansys.aedt.core.modules.material.Material.public_dir "ansys.aedt.core.modules.material.Material.public_dir")  | Shortcut for dir(self).  |  
| [`Material.specific_heat`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.specific_heat.html#ansys.aedt.core.modules.material.Material.specific_heat "ansys.aedt.core.modules.material.Material.specific_heat")  | Specific heat.  |  
| [`Material.stacking_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_direction.html#ansys.aedt.core.modules.material.Material.stacking_direction "ansys.aedt.core.modules.material.Material.stacking_direction")  | Stacking direction for the lamination can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.stacking_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_factor.html#ansys.aedt.core.modules.material.Material.stacking_factor "ansys.aedt.core.modules.material.Material.stacking_factor")  | Stacking factor for lamination.  |  
| [`Material.stacking_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_type.html#ansys.aedt.core.modules.material.Material.stacking_type "ansys.aedt.core.modules.material.Material.stacking_type")  | Composition of the wire can either be "Solid", "Lamination" or "Litz Wire".  |  
| [`Material.strand_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.strand_number.html#ansys.aedt.core.modules.material.Material.strand_number "ansys.aedt.core.modules.material.Material.strand_number")  | Strand number for litz wire.  |  
| [`Material.thermal_conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_conductivity.html#ansys.aedt.core.modules.material.Material.thermal_conductivity "ansys.aedt.core.modules.material.Material.thermal_conductivity")  | Thermal conductivity.  |  
| [`Material.thermal_expansion_coefficient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient.html#ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient "ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient")  | Thermal expansion coefficient.  |  
| [`Material.twisting_length_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.twisting_length_factor.html#ansys.aedt.core.modules.material.Material.twisting_length_factor "ansys.aedt.core.modules.material.Material.twisting_length_factor")  | Ratio of the twisted-strand length to the bundle length for Litz Wire.  |  
| [`Material.viscosity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.viscosity.html#ansys.aedt.core.modules.material.Material.viscosity "ansys.aedt.core.modules.material.Material.viscosity")  | Viscosity.  |  
| [`Material.wire_diameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_diameter.html#ansys.aedt.core.modules.material.Material.wire_diameter "ansys.aedt.core.modules.material.Material.wire_diameter")  | Diameter of the round litz wire.  |  
| [`Material.wire_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness.html#ansys.aedt.core.modules.material.Material.wire_thickness "ansys.aedt.core.modules.material.Material.wire_thickness")  | Thickness of rectangular litz wire.  |  
| [`Material.wire_thickness_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness_direction.html#ansys.aedt.core.modules.material.Material.wire_thickness_direction "ansys.aedt.core.modules.material.Material.wire_thickness_direction")  | Thickness direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.wire_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_type.html#ansys.aedt.core.modules.material.Material.wire_type "ansys.aedt.core.modules.material.Material.wire_type")  | The type of the wire can either be "Round", "Square" or "Rectangular".  |  
| [`Material.wire_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width.html#ansys.aedt.core.modules.material.Material.wire_width "ansys.aedt.core.modules.material.Material.wire_width")  | Width of the rectangular or square litz wire.  |  
| [`Material.wire_width_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width_direction.html#ansys.aedt.core.modules.material.Material.wire_width_direction "ansys.aedt.core.modules.material.Material.wire_width_direction")  | Width direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.youngs_modulus`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.youngs_modulus.html#ansys.aedt.core.modules.material.Material.youngs_modulus "ansys.aedt.core.modules.material.Material.youngs_modulus")  | Young's modulus.  |  
# Material 

class ansys.aedt.core.modules.material.Material(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages material properties. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> material = app.materials["copper"]

```
Copy to clipboard
Methods  
| [`Material.get_core_loss_coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_core_loss_coefficients.html#ansys.aedt.core.modules.material.Material.get_core_loss_coefficients "ansys.aedt.core.modules.material.Material.get_core_loss_coefficients")(...[, ...])  | Get electrical steel or power ferrite core loss coefficients at a given frequency.  |  
| --- | --- |  
| [`Material.get_curve_coreloss_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_type.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_type "ansys.aedt.core.modules.material.Material.get_curve_coreloss_type")()  | Return the curve core loss type assigned to material.  |  
| [`Material.get_curve_coreloss_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_values.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_values "ansys.aedt.core.modules.material.Material.get_curve_coreloss_values")()  | Return the curve core values type assigned to material.  |  
| [`Material.get_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.get_magnetic_coercivity "ansys.aedt.core.modules.material.Material.get_magnetic_coercivity")()  | Get the magnetic coercivity values.  |  
| [`Material.is_conductor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_conductor.html#ansys.aedt.core.modules.material.Material.is_conductor "ansys.aedt.core.modules.material.Material.is_conductor")([threshold])  | Check if the material is a conductor.  |  
| [`Material.is_dielectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_dielectric.html#ansys.aedt.core.modules.material.Material.is_dielectric "ansys.aedt.core.modules.material.Material.is_dielectric")([threshold])  | Check if the material is dielectric.  |  
| [`Material.set_bp_curve_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss.html#ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss "ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss")(points[, ...])  | Set B-P Type Core Loss.  |  
| [`Material.set_coreloss_at_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency.html#ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency "ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency")(...[, ...])  | Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies.  |  
| [`Material.set_djordjevic_sarkar_model`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model.html#ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model "ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model")([dk, ...])  | Set Djordjevic-Sarkar model.  |  
| [`Material.set_electrical_steel_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss.html#ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss "ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss")([kh, ...])  | Set electrical steel core loss.  |  
| [`Material.set_hysteresis_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss.html#ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss "ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss")([kdc, hci, ...])  | Set Hysteresis Type Core Loss.  |  
| [`Material.set_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.set_magnetic_coercivity "ansys.aedt.core.modules.material.Material.set_magnetic_coercivity")([value, x, ...])  | Set magnetic coercivity for material.  |  
| [`Material.set_power_ferrite_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss.html#ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss "ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss")([cm, x, ...])  | Set Power Ferrite Type Core Loss.  |  
| [`Material.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.update.html#ansys.aedt.core.modules.material.Material.update "ansys.aedt.core.modules.material.Material.update")()  | Update the material in AEDT.  |  
Attributes  
| [`Material.conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.conductivity.html#ansys.aedt.core.modules.material.Material.conductivity "ansys.aedt.core.modules.material.Material.conductivity")  | Conductivity.  |  
| --- | --- |  
| [`Material.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.coordinate_system.html#ansys.aedt.core.modules.material.Material.coordinate_system "ansys.aedt.core.modules.material.Material.coordinate_system")  | Material coordinate system.  |  
| [`Material.dielectric_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.dielectric_loss_tangent.html#ansys.aedt.core.modules.material.Material.dielectric_loss_tangent "ansys.aedt.core.modules.material.Material.dielectric_loss_tangent")  | Dielectric loss tangent.  |  
| [`Material.diffusivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.diffusivity.html#ansys.aedt.core.modules.material.Material.diffusivity "ansys.aedt.core.modules.material.Material.diffusivity")  | Diffusivity.  |  
| [`Material.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_used.html#ansys.aedt.core.modules.material.Material.is_used "ansys.aedt.core.modules.material.Material.is_used")  | Checks if a project material is in use.  |  
| [`Material.magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.magnetic_coercivity "ansys.aedt.core.modules.material.Material.magnetic_coercivity")  | Magnetic coercivity.  |  
| [`Material.magnetic_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_loss_tangent.html#ansys.aedt.core.modules.material.Material.magnetic_loss_tangent "ansys.aedt.core.modules.material.Material.magnetic_loss_tangent")  | Magnetic loss tangent.  |  
| [`Material.mass_density`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.mass_density.html#ansys.aedt.core.modules.material.Material.mass_density "ansys.aedt.core.modules.material.Material.mass_density")  | Mass density.  |  
| [`Material.material_appearance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.material_appearance.html#ansys.aedt.core.modules.material.Material.material_appearance "ansys.aedt.core.modules.material.Material.material_appearance")  | Material appearance specified as a list.  |  
| [`Material.molecular_mass`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.molecular_mass.html#ansys.aedt.core.modules.material.Material.molecular_mass "ansys.aedt.core.modules.material.Material.molecular_mass")  | Molecular mass.  |  
| [`Material.permeability`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permeability.html#ansys.aedt.core.modules.material.Material.permeability "ansys.aedt.core.modules.material.Material.permeability")  | Permeability.  |  
| [`Material.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permittivity.html#ansys.aedt.core.modules.material.Material.permittivity "ansys.aedt.core.modules.material.Material.permittivity")  | Permittivity.  |  
| [`Material.poissons_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.poissons_ratio.html#ansys.aedt.core.modules.material.Material.poissons_ratio "ansys.aedt.core.modules.material.Material.poissons_ratio")  | Poisson's ratio.  |  
| [`Material.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.public_dir.html#ansys.aedt.core.modules.material.Material.public_dir "ansys.aedt.core.modules.material.Material.public_dir")  | Shortcut for dir(self).  |  
| [`Material.specific_heat`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.specific_heat.html#ansys.aedt.core.modules.material.Material.specific_heat "ansys.aedt.core.modules.material.Material.specific_heat")  | Specific heat.  |  
| [`Material.stacking_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_direction.html#ansys.aedt.core.modules.material.Material.stacking_direction "ansys.aedt.core.modules.material.Material.stacking_direction")  | Stacking direction for the lamination can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.stacking_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_factor.html#ansys.aedt.core.modules.material.Material.stacking_factor "ansys.aedt.core.modules.material.Material.stacking_factor")  | Stacking factor for lamination.  |  
| [`Material.stacking_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_type.html#ansys.aedt.core.modules.material.Material.stacking_type "ansys.aedt.core.modules.material.Material.stacking_type")  | Composition of the wire can either be "Solid", "Lamination" or "Litz Wire".  |  
| [`Material.strand_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.strand_number.html#ansys.aedt.core.modules.material.Material.strand_number "ansys.aedt.core.modules.material.Material.strand_number")  | Strand number for litz wire.  |  
| [`Material.thermal_conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_conductivity.html#ansys.aedt.core.modules.material.Material.thermal_conductivity "ansys.aedt.core.modules.material.Material.thermal_conductivity")  | Thermal conductivity.  |  
| [`Material.thermal_expansion_coefficient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient.html#ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient "ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient")  | Thermal expansion coefficient.  |  
| [`Material.twisting_length_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.twisting_length_factor.html#ansys.aedt.core.modules.material.Material.twisting_length_factor "ansys.aedt.core.modules.material.Material.twisting_length_factor")  | Ratio of the twisted-strand length to the bundle length for Litz Wire.  |  
| [`Material.viscosity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.viscosity.html#ansys.aedt.core.modules.material.Material.viscosity "ansys.aedt.core.modules.material.Material.viscosity")  | Viscosity.  |  
| [`Material.wire_diameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_diameter.html#ansys.aedt.core.modules.material.Material.wire_diameter "ansys.aedt.core.modules.material.Material.wire_diameter")  | Diameter of the round litz wire.  |  
| [`Material.wire_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness.html#ansys.aedt.core.modules.material.Material.wire_thickness "ansys.aedt.core.modules.material.Material.wire_thickness")  | Thickness of rectangular litz wire.  |  
| [`Material.wire_thickness_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness_direction.html#ansys.aedt.core.modules.material.Material.wire_thickness_direction "ansys.aedt.core.modules.material.Material.wire_thickness_direction")  | Thickness direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.wire_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_type.html#ansys.aedt.core.modules.material.Material.wire_type "ansys.aedt.core.modules.material.Material.wire_type")  | The type of the wire can either be "Round", "Square" or "Rectangular".  |  
| [`Material.wire_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width.html#ansys.aedt.core.modules.material.Material.wire_width "ansys.aedt.core.modules.material.Material.wire_width")  | Width of the rectangular or square litz wire.  |  
| [`Material.wire_width_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width_direction.html#ansys.aedt.core.modules.material.Material.wire_width_direction "ansys.aedt.core.modules.material.Material.wire_width_direction")  | Width direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.youngs_modulus`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.youngs_modulus.html#ansys.aedt.core.modules.material.Material.youngs_modulus "ansys.aedt.core.modules.material.Material.youngs_modulus")  | Young's modulus.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.rst.txt)

# Material 

class ansys.aedt.core.modules.material.Material(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages material properties. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> material = app.materials["copper"]

```
Copy to clipboard
Methods  
| [`Material.get_core_loss_coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_core_loss_coefficients.html#ansys.aedt.core.modules.material.Material.get_core_loss_coefficients "ansys.aedt.core.modules.material.Material.get_core_loss_coefficients")(...[, ...])  | Get electrical steel or power ferrite core loss coefficients at a given frequency.  |  
| --- | --- |  
| [`Material.get_curve_coreloss_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_type.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_type "ansys.aedt.core.modules.material.Material.get_curve_coreloss_type")()  | Return the curve core loss type assigned to material.  |  
| [`Material.get_curve_coreloss_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_curve_coreloss_values.html#ansys.aedt.core.modules.material.Material.get_curve_coreloss_values "ansys.aedt.core.modules.material.Material.get_curve_coreloss_values")()  | Return the curve core values type assigned to material.  |  
| [`Material.get_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.get_magnetic_coercivity "ansys.aedt.core.modules.material.Material.get_magnetic_coercivity")()  | Get the magnetic coercivity values.  |  
| [`Material.is_conductor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_conductor.html#ansys.aedt.core.modules.material.Material.is_conductor "ansys.aedt.core.modules.material.Material.is_conductor")([threshold])  | Check if the material is a conductor.  |  
| [`Material.is_dielectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_dielectric.html#ansys.aedt.core.modules.material.Material.is_dielectric "ansys.aedt.core.modules.material.Material.is_dielectric")([threshold])  | Check if the material is dielectric.  |  
| [`Material.set_bp_curve_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss.html#ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss "ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss")(points[, ...])  | Set B-P Type Core Loss.  |  
| [`Material.set_coreloss_at_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency.html#ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency "ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency")(...[, ...])  | Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies.  |  
| [`Material.set_djordjevic_sarkar_model`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model.html#ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model "ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model")([dk, ...])  | Set Djordjevic-Sarkar model.  |  
| [`Material.set_electrical_steel_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss.html#ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss "ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss")([kh, ...])  | Set electrical steel core loss.  |  
| [`Material.set_hysteresis_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss.html#ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss "ansys.aedt.core.modules.material.Material.set_hysteresis_coreloss")([kdc, hci, ...])  | Set Hysteresis Type Core Loss.  |  
| [`Material.set_magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.set_magnetic_coercivity "ansys.aedt.core.modules.material.Material.set_magnetic_coercivity")([value, x, ...])  | Set magnetic coercivity for material.  |  
| [`Material.set_power_ferrite_coreloss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss.html#ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss "ansys.aedt.core.modules.material.Material.set_power_ferrite_coreloss")([cm, x, ...])  | Set Power Ferrite Type Core Loss.  |  
| [`Material.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.update.html#ansys.aedt.core.modules.material.Material.update "ansys.aedt.core.modules.material.Material.update")()  | Update the material in AEDT.  |  
Attributes  
| [`Material.conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.conductivity.html#ansys.aedt.core.modules.material.Material.conductivity "ansys.aedt.core.modules.material.Material.conductivity")  | Conductivity.  |  
| --- | --- |  
| [`Material.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.coordinate_system.html#ansys.aedt.core.modules.material.Material.coordinate_system "ansys.aedt.core.modules.material.Material.coordinate_system")  | Material coordinate system.  |  
| [`Material.dielectric_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.dielectric_loss_tangent.html#ansys.aedt.core.modules.material.Material.dielectric_loss_tangent "ansys.aedt.core.modules.material.Material.dielectric_loss_tangent")  | Dielectric loss tangent.  |  
| [`Material.diffusivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.diffusivity.html#ansys.aedt.core.modules.material.Material.diffusivity "ansys.aedt.core.modules.material.Material.diffusivity")  | Diffusivity.  |  
| [`Material.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_used.html#ansys.aedt.core.modules.material.Material.is_used "ansys.aedt.core.modules.material.Material.is_used")  | Checks if a project material is in use.  |  
| [`Material.magnetic_coercivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_coercivity.html#ansys.aedt.core.modules.material.Material.magnetic_coercivity "ansys.aedt.core.modules.material.Material.magnetic_coercivity")  | Magnetic coercivity.  |  
| [`Material.magnetic_loss_tangent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.magnetic_loss_tangent.html#ansys.aedt.core.modules.material.Material.magnetic_loss_tangent "ansys.aedt.core.modules.material.Material.magnetic_loss_tangent")  | Magnetic loss tangent.  |  
| [`Material.mass_density`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.mass_density.html#ansys.aedt.core.modules.material.Material.mass_density "ansys.aedt.core.modules.material.Material.mass_density")  | Mass density.  |  
| [`Material.material_appearance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.material_appearance.html#ansys.aedt.core.modules.material.Material.material_appearance "ansys.aedt.core.modules.material.Material.material_appearance")  | Material appearance specified as a list.  |  
| [`Material.molecular_mass`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.molecular_mass.html#ansys.aedt.core.modules.material.Material.molecular_mass "ansys.aedt.core.modules.material.Material.molecular_mass")  | Molecular mass.  |  
| [`Material.permeability`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permeability.html#ansys.aedt.core.modules.material.Material.permeability "ansys.aedt.core.modules.material.Material.permeability")  | Permeability.  |  
| [`Material.permittivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.permittivity.html#ansys.aedt.core.modules.material.Material.permittivity "ansys.aedt.core.modules.material.Material.permittivity")  | Permittivity.  |  
| [`Material.poissons_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.poissons_ratio.html#ansys.aedt.core.modules.material.Material.poissons_ratio "ansys.aedt.core.modules.material.Material.poissons_ratio")  | Poisson's ratio.  |  
| [`Material.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.public_dir.html#ansys.aedt.core.modules.material.Material.public_dir "ansys.aedt.core.modules.material.Material.public_dir")  | Shortcut for dir(self).  |  
| [`Material.specific_heat`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.specific_heat.html#ansys.aedt.core.modules.material.Material.specific_heat "ansys.aedt.core.modules.material.Material.specific_heat")  | Specific heat.  |  
| [`Material.stacking_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_direction.html#ansys.aedt.core.modules.material.Material.stacking_direction "ansys.aedt.core.modules.material.Material.stacking_direction")  | Stacking direction for the lamination can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.stacking_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_factor.html#ansys.aedt.core.modules.material.Material.stacking_factor "ansys.aedt.core.modules.material.Material.stacking_factor")  | Stacking factor for lamination.  |  
| [`Material.stacking_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.stacking_type.html#ansys.aedt.core.modules.material.Material.stacking_type "ansys.aedt.core.modules.material.Material.stacking_type")  | Composition of the wire can either be "Solid", "Lamination" or "Litz Wire".  |  
| [`Material.strand_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.strand_number.html#ansys.aedt.core.modules.material.Material.strand_number "ansys.aedt.core.modules.material.Material.strand_number")  | Strand number for litz wire.  |  
| [`Material.thermal_conductivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_conductivity.html#ansys.aedt.core.modules.material.Material.thermal_conductivity "ansys.aedt.core.modules.material.Material.thermal_conductivity")  | Thermal conductivity.  |  
| [`Material.thermal_expansion_coefficient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient.html#ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient "ansys.aedt.core.modules.material.Material.thermal_expansion_coefficient")  | Thermal expansion coefficient.  |  
| [`Material.twisting_length_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.twisting_length_factor.html#ansys.aedt.core.modules.material.Material.twisting_length_factor "ansys.aedt.core.modules.material.Material.twisting_length_factor")  | Ratio of the twisted-strand length to the bundle length for Litz Wire.  |  
| [`Material.viscosity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.viscosity.html#ansys.aedt.core.modules.material.Material.viscosity "ansys.aedt.core.modules.material.Material.viscosity")  | Viscosity.  |  
| [`Material.wire_diameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_diameter.html#ansys.aedt.core.modules.material.Material.wire_diameter "ansys.aedt.core.modules.material.Material.wire_diameter")  | Diameter of the round litz wire.  |  
| [`Material.wire_thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness.html#ansys.aedt.core.modules.material.Material.wire_thickness "ansys.aedt.core.modules.material.Material.wire_thickness")  | Thickness of rectangular litz wire.  |  
| [`Material.wire_thickness_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_thickness_direction.html#ansys.aedt.core.modules.material.Material.wire_thickness_direction "ansys.aedt.core.modules.material.Material.wire_thickness_direction")  | Thickness direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.wire_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_type.html#ansys.aedt.core.modules.material.Material.wire_type "ansys.aedt.core.modules.material.Material.wire_type")  | The type of the wire can either be "Round", "Square" or "Rectangular".  |  
| [`Material.wire_width`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width.html#ansys.aedt.core.modules.material.Material.wire_width "ansys.aedt.core.modules.material.Material.wire_width")  | Width of the rectangular or square litz wire.  |  
| [`Material.wire_width_direction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.wire_width_direction.html#ansys.aedt.core.modules.material.Material.wire_width_direction "ansys.aedt.core.modules.material.Material.wire_width_direction")  | Width direction of the wire can either be "V(1)", "V(2)" or "V(3)".  |  
| [`Material.youngs_modulus`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.youngs_modulus.html#ansys.aedt.core.modules.material.Material.youngs_modulus "ansys.aedt.core.modules.material.Material.youngs_modulus")  | Young's modulus.  |