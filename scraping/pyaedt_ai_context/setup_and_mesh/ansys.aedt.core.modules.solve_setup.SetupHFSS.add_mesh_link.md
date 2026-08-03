---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_mesh_link 

SetupHFSS.add_mesh_link(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _apply_mesh_operations : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _adapt_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import mesh from a source design solution to the target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source design from which the mesh is imported. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source design solution in the format `"name : solution_name"`. If `None`, the default value is taken from the nominal adaptive solution. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the “mapping” variables from the source design. If `None`, the default is appname.available_variations.nominal_values. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**apply_mesh_operations**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Apply mesh operations in target design on the imported mesh. Default value is `True`. 

**adapt_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Perform port adapt/seeding in target solve setup. Default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(design="target_design")
>>> target_setup = m3d.create_setup(name="target_setup")
The target design is duplicated and made it active.
The duplicated design will be the source design from which the mesh is imported.
>>> m3d.duplicate_design(name="target_design", save_after_duplicate=True)
>>> m3d.rename_design(name="source_design")
>>> m3d.create_setup(name="source_setup")
Activate the target design.
>>> m3d.set_active_design("target_design")
The mesh link is assigned to the target design.
>>> target_setup.add_mesh_link("source_design")
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
# add_mesh_link 

SetupHFSS.add_mesh_link(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _apply_mesh_operations : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _adapt_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import mesh from a source design solution to the target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source design from which the mesh is imported. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source design solution in the format `"name : solution_name"`. If `None`, the default value is taken from the nominal adaptive solution. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the “mapping” variables from the source design. If `None`, the default is appname.available_variations.nominal_values. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**apply_mesh_operations**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Apply mesh operations in target design on the imported mesh. Default value is `True`. 

**adapt_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Perform port adapt/seeding in target solve setup. Default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(design="target_design")
>>> target_setup = m3d.create_setup(name="target_setup")
The target design is duplicated and made it active.
The duplicated design will be the source design from which the mesh is imported.
>>> m3d.duplicate_design(name="target_design", save_after_duplicate=True)
>>> m3d.rename_design(name="source_design")
>>> m3d.create_setup(name="source_setup")
Activate the target design.
>>> m3d.set_active_design("target_design")
The mesh link is assigned to the target design.
>>> target_setup.add_mesh_link("source_design")
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link.rst.txt)

# add_mesh_link 

SetupHFSS.add_mesh_link(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _apply_mesh_operations : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _adapt_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import mesh from a source design solution to the target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source design from which the mesh is imported. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source design solution in the format `"name : solution_name"`. If `None`, the default value is taken from the nominal adaptive solution. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the “mapping” variables from the source design. If `None`, the default is appname.available_variations.nominal_values. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Default value is `True`. 

**apply_mesh_operations**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Apply mesh operations in target design on the imported mesh. Default value is `True`. 

**adapt_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Perform port adapt/seeding in target solve setup. Default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(design="target_design")
>>> target_setup = m3d.create_setup(name="target_setup")
The target design is duplicated and made it active.
The duplicated design will be the source design from which the mesh is imported.
>>> m3d.duplicate_design(name="target_design", save_after_duplicate=True)
>>> m3d.rename_design(name="source_design")
>>> m3d.create_setup(name="source_setup")
Activate the target design.
>>> m3d.set_active_design("target_design")
The mesh link is assigned to the target design.
>>> target_setup.add_mesh_link("source_design")
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard