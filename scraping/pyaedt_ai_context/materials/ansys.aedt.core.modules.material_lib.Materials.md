---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# Materials 

class ansys.aedt.core.modules.material_lib.Materials(_app_) 
    
Contains the AEDT materials database and all methods for creating and editing materials. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Inherited parent object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> materials = app.materials

```
Copy to clipboard
Methods  
| [`Materials.add_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material.html#ansys.aedt.core.modules.material_lib.Materials.add_material "ansys.aedt.core.modules.material_lib.Materials.add_material")(name[, properties])  | Add a material with default values.  |  
| --- | --- |  
| [`Materials.add_material_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material_sweep.html#ansys.aedt.core.modules.material_lib.Materials.add_material_sweep "ansys.aedt.core.modules.material_lib.Materials.add_material_sweep")(assignment, name)  | Create a sweep material made of an array of materials.  |  
| [`Materials.add_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.add_surface_material "ansys.aedt.core.modules.material_lib.Materials.add_surface_material")(name[, ...])  | Add a surface material.  |  
| [`Materials.check_thermal_modifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier.html#ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier "ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier")(material)  | Check a material to see if it has any thermal modifiers.  |  
| [`Materials.duplicate_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_material")(material[, ...])  | Duplicate a material.  |  
| [`Materials.duplicate_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material")(material)  | Duplicate a surface material.  |  
| [`Materials.exists_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.exists_material.html#ansys.aedt.core.modules.material_lib.Materials.exists_material "ansys.aedt.core.modules.material_lib.Materials.exists_material")(material)  | Check if a material exists in AEDT or PyAEDT Definitions.  |  
| [`Materials.export_materials_to_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file.html#ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file "ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file")(output_file)  | Export all materials to a JSON or TOML file.  |  
| [`Materials.get_used_project_material_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names.html#ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names "ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names")()  | Get list of material names in current project.  |  
| [`Materials.import_materials_from_excel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel")(input_file)  | Import and create materials from a csv or excel file.  |  
| [`Materials.import_materials_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file")([...])  | Import and create materials from a JSON or AMAT file.  |  
| [`Materials.import_materials_from_workbench`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench")(...)  | Import and create materials from Workbench Engineering Data XML file.  |  
| [`Materials.remove_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.remove_material.html#ansys.aedt.core.modules.material_lib.Materials.remove_material "ansys.aedt.core.modules.material_lib.Materials.remove_material")(material[, library])  | Remove a material.  |  
Attributes  
| [`Materials.conductors`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.conductors.html#ansys.aedt.core.modules.material_lib.Materials.conductors "ansys.aedt.core.modules.material_lib.Materials.conductors")  | Conductors in the material database.  |  
| --- | --- |  
| [`Materials.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.dielectrics.html#ansys.aedt.core.modules.material_lib.Materials.dielectrics "ansys.aedt.core.modules.material_lib.Materials.dielectrics")  | Dielectrics in the material database.  |  
| [`Materials.gases`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.gases.html#ansys.aedt.core.modules.material_lib.Materials.gases "ansys.aedt.core.modules.material_lib.Materials.gases")  | Return the gas materials.  |  
| [`Materials.liquids`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.liquids.html#ansys.aedt.core.modules.material_lib.Materials.liquids "ansys.aedt.core.modules.material_lib.Materials.liquids")  | Return the liquids materials.  |  
| [`Materials.mat_names_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt")  | List material names.  |  
| [`Materials.mat_names_aedt_lower`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower")  | List material names with lower case.  |  
| [`Materials.material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.material_keys.html#ansys.aedt.core.modules.material_lib.Materials.material_keys "ansys.aedt.core.modules.material_lib.Materials.material_keys")  | Material dictionary available in current project.  |  
| [`Materials.odefinition_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.odefinition_manager.html#ansys.aedt.core.modules.material_lib.Materials.odefinition_manager "ansys.aedt.core.modules.material_lib.Materials.odefinition_manager")  | Definition Manager from AEDT.  |  
| [`Materials.omaterial_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.omaterial_manager.html#ansys.aedt.core.modules.material_lib.Materials.omaterial_manager "ansys.aedt.core.modules.material_lib.Materials.omaterial_manager")  | Material Manager from AEDT.  |  
| [`Materials.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.public_dir.html#ansys.aedt.core.modules.material_lib.Materials.public_dir "ansys.aedt.core.modules.material_lib.Materials.public_dir")  | Shortcut for dir(self).  |  
| [`Materials.surface_material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.surface_material_keys.html#ansys.aedt.core.modules.material_lib.Materials.surface_material_keys "ansys.aedt.core.modules.material_lib.Materials.surface_material_keys")  | Dictionary of Surface Material in the project.  |  
# Materials 

class ansys.aedt.core.modules.material_lib.Materials(_app_) 
    
Contains the AEDT materials database and all methods for creating and editing materials. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Inherited parent object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> materials = app.materials

```
Copy to clipboard
Methods  
| [`Materials.add_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material.html#ansys.aedt.core.modules.material_lib.Materials.add_material "ansys.aedt.core.modules.material_lib.Materials.add_material")(name[, properties])  | Add a material with default values.  |  
| --- | --- |  
| [`Materials.add_material_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material_sweep.html#ansys.aedt.core.modules.material_lib.Materials.add_material_sweep "ansys.aedt.core.modules.material_lib.Materials.add_material_sweep")(assignment, name)  | Create a sweep material made of an array of materials.  |  
| [`Materials.add_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.add_surface_material "ansys.aedt.core.modules.material_lib.Materials.add_surface_material")(name[, ...])  | Add a surface material.  |  
| [`Materials.check_thermal_modifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier.html#ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier "ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier")(material)  | Check a material to see if it has any thermal modifiers.  |  
| [`Materials.duplicate_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_material")(material[, ...])  | Duplicate a material.  |  
| [`Materials.duplicate_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material")(material)  | Duplicate a surface material.  |  
| [`Materials.exists_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.exists_material.html#ansys.aedt.core.modules.material_lib.Materials.exists_material "ansys.aedt.core.modules.material_lib.Materials.exists_material")(material)  | Check if a material exists in AEDT or PyAEDT Definitions.  |  
| [`Materials.export_materials_to_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file.html#ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file "ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file")(output_file)  | Export all materials to a JSON or TOML file.  |  
| [`Materials.get_used_project_material_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names.html#ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names "ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names")()  | Get list of material names in current project.  |  
| [`Materials.import_materials_from_excel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel")(input_file)  | Import and create materials from a csv or excel file.  |  
| [`Materials.import_materials_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file")([...])  | Import and create materials from a JSON or AMAT file.  |  
| [`Materials.import_materials_from_workbench`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench")(...)  | Import and create materials from Workbench Engineering Data XML file.  |  
| [`Materials.remove_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.remove_material.html#ansys.aedt.core.modules.material_lib.Materials.remove_material "ansys.aedt.core.modules.material_lib.Materials.remove_material")(material[, library])  | Remove a material.  |  
Attributes  
| [`Materials.conductors`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.conductors.html#ansys.aedt.core.modules.material_lib.Materials.conductors "ansys.aedt.core.modules.material_lib.Materials.conductors")  | Conductors in the material database.  |  
| --- | --- |  
| [`Materials.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.dielectrics.html#ansys.aedt.core.modules.material_lib.Materials.dielectrics "ansys.aedt.core.modules.material_lib.Materials.dielectrics")  | Dielectrics in the material database.  |  
| [`Materials.gases`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.gases.html#ansys.aedt.core.modules.material_lib.Materials.gases "ansys.aedt.core.modules.material_lib.Materials.gases")  | Return the gas materials.  |  
| [`Materials.liquids`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.liquids.html#ansys.aedt.core.modules.material_lib.Materials.liquids "ansys.aedt.core.modules.material_lib.Materials.liquids")  | Return the liquids materials.  |  
| [`Materials.mat_names_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt")  | List material names.  |  
| [`Materials.mat_names_aedt_lower`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower")  | List material names with lower case.  |  
| [`Materials.material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.material_keys.html#ansys.aedt.core.modules.material_lib.Materials.material_keys "ansys.aedt.core.modules.material_lib.Materials.material_keys")  | Material dictionary available in current project.  |  
| [`Materials.odefinition_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.odefinition_manager.html#ansys.aedt.core.modules.material_lib.Materials.odefinition_manager "ansys.aedt.core.modules.material_lib.Materials.odefinition_manager")  | Definition Manager from AEDT.  |  
| [`Materials.omaterial_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.omaterial_manager.html#ansys.aedt.core.modules.material_lib.Materials.omaterial_manager "ansys.aedt.core.modules.material_lib.Materials.omaterial_manager")  | Material Manager from AEDT.  |  
| [`Materials.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.public_dir.html#ansys.aedt.core.modules.material_lib.Materials.public_dir "ansys.aedt.core.modules.material_lib.Materials.public_dir")  | Shortcut for dir(self).  |  
| [`Materials.surface_material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.surface_material_keys.html#ansys.aedt.core.modules.material_lib.Materials.surface_material_keys "ansys.aedt.core.modules.material_lib.Materials.surface_material_keys")  | Dictionary of Surface Material in the project.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.rst.txt)

# Materials 

class ansys.aedt.core.modules.material_lib.Materials(_app_) 
    
Contains the AEDT materials database and all methods for creating and editing materials. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Inherited parent object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> materials = app.materials

```
Copy to clipboard
Methods  
| [`Materials.add_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material.html#ansys.aedt.core.modules.material_lib.Materials.add_material "ansys.aedt.core.modules.material_lib.Materials.add_material")(name[, properties])  | Add a material with default values.  |  
| --- | --- |  
| [`Materials.add_material_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material_sweep.html#ansys.aedt.core.modules.material_lib.Materials.add_material_sweep "ansys.aedt.core.modules.material_lib.Materials.add_material_sweep")(assignment, name)  | Create a sweep material made of an array of materials.  |  
| [`Materials.add_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.add_surface_material "ansys.aedt.core.modules.material_lib.Materials.add_surface_material")(name[, ...])  | Add a surface material.  |  
| [`Materials.check_thermal_modifier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier.html#ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier "ansys.aedt.core.modules.material_lib.Materials.check_thermal_modifier")(material)  | Check a material to see if it has any thermal modifiers.  |  
| [`Materials.duplicate_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_material")(material[, ...])  | Duplicate a material.  |  
| [`Materials.duplicate_surface_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material.html#ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material "ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material")(material)  | Duplicate a surface material.  |  
| [`Materials.exists_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.exists_material.html#ansys.aedt.core.modules.material_lib.Materials.exists_material "ansys.aedt.core.modules.material_lib.Materials.exists_material")(material)  | Check if a material exists in AEDT or PyAEDT Definitions.  |  
| [`Materials.export_materials_to_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file.html#ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file "ansys.aedt.core.modules.material_lib.Materials.export_materials_to_file")(output_file)  | Export all materials to a JSON or TOML file.  |  
| [`Materials.get_used_project_material_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names.html#ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names "ansys.aedt.core.modules.material_lib.Materials.get_used_project_material_names")()  | Get list of material names in current project.  |  
| [`Materials.import_materials_from_excel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_excel")(input_file)  | Import and create materials from a csv or excel file.  |  
| [`Materials.import_materials_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_file")([...])  | Import and create materials from a JSON or AMAT file.  |  
| [`Materials.import_materials_from_workbench`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench.html#ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench "ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench")(...)  | Import and create materials from Workbench Engineering Data XML file.  |  
| [`Materials.remove_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.remove_material.html#ansys.aedt.core.modules.material_lib.Materials.remove_material "ansys.aedt.core.modules.material_lib.Materials.remove_material")(material[, library])  | Remove a material.  |  
Attributes  
| [`Materials.conductors`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.conductors.html#ansys.aedt.core.modules.material_lib.Materials.conductors "ansys.aedt.core.modules.material_lib.Materials.conductors")  | Conductors in the material database.  |  
| --- | --- |  
| [`Materials.dielectrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.dielectrics.html#ansys.aedt.core.modules.material_lib.Materials.dielectrics "ansys.aedt.core.modules.material_lib.Materials.dielectrics")  | Dielectrics in the material database.  |  
| [`Materials.gases`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.gases.html#ansys.aedt.core.modules.material_lib.Materials.gases "ansys.aedt.core.modules.material_lib.Materials.gases")  | Return the gas materials.  |  
| [`Materials.liquids`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.liquids.html#ansys.aedt.core.modules.material_lib.Materials.liquids "ansys.aedt.core.modules.material_lib.Materials.liquids")  | Return the liquids materials.  |  
| [`Materials.mat_names_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt")  | List material names.  |  
| [`Materials.mat_names_aedt_lower`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower.html#ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower "ansys.aedt.core.modules.material_lib.Materials.mat_names_aedt_lower")  | List material names with lower case.  |  
| [`Materials.material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.material_keys.html#ansys.aedt.core.modules.material_lib.Materials.material_keys "ansys.aedt.core.modules.material_lib.Materials.material_keys")  | Material dictionary available in current project.  |  
| [`Materials.odefinition_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.odefinition_manager.html#ansys.aedt.core.modules.material_lib.Materials.odefinition_manager "ansys.aedt.core.modules.material_lib.Materials.odefinition_manager")  | Definition Manager from AEDT.  |  
| [`Materials.omaterial_manager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.omaterial_manager.html#ansys.aedt.core.modules.material_lib.Materials.omaterial_manager "ansys.aedt.core.modules.material_lib.Materials.omaterial_manager")  | Material Manager from AEDT.  |  
| [`Materials.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.public_dir.html#ansys.aedt.core.modules.material_lib.Materials.public_dir "ansys.aedt.core.modules.material_lib.Materials.public_dir")  | Shortcut for dir(self).  |  
| [`Materials.surface_material_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.surface_material_keys.html#ansys.aedt.core.modules.material_lib.Materials.surface_material_keys "ansys.aedt.core.modules.material_lib.Materials.surface_material_keys")  | Dictionary of Surface Material in the project.  |