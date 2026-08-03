---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# start_continue_from_previous_setup 

SetupHFSSAuto.start_continue_from_previous_setup(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _map_variables_by_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Start or continue from a previously solved setup. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution in the format `"name : solution_name"`. For example, `"Setup1 : Transient", "MySetup : LastAdaptive"`. 

**map_variables_by_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether variables are mapped by name from the source design. The default is `True`. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the parameters. This parameter is not considered if `map_variables_by_name=True`. If `None`, the default is `appname.available_variations.nominal_values`. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

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
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> setup = m2d.get_setup("Setup1")
>>> setup.start_continue_from_previous_setup(design="IM", solution="Setup1 : Transient")

```
Copy to clipboard
# start_continue_from_previous_setup 

SetupHFSSAuto.start_continue_from_previous_setup(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _map_variables_by_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Start or continue from a previously solved setup. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution in the format `"name : solution_name"`. For example, `"Setup1 : Transient", "MySetup : LastAdaptive"`. 

**map_variables_by_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether variables are mapped by name from the source design. The default is `True`. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the parameters. This parameter is not considered if `map_variables_by_name=True`. If `None`, the default is `appname.available_variations.nominal_values`. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

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
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> setup = m2d.get_setup("Setup1")
>>> setup.start_continue_from_previous_setup(design="IM", solution="Setup1 : Transient")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup.rst.txt)

# start_continue_from_previous_setup 

SetupHFSSAuto.start_continue_from_previous_setup(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _map_variables_by_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'This Project*'_, _force_source_to_solve : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _preserve_partner_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Start or continue from a previously solved setup. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the solution in the format `"name : solution_name"`. For example, `"Setup1 : Transient", "MySetup : LastAdaptive"`. 

**map_variables_by_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether variables are mapped by name from the source design. The default is `True`. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the parameters. This parameter is not considered if `map_variables_by_name=True`. If `None`, the default is `appname.available_variations.nominal_values`. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Name of the project with the design. The default is `"This Project*"`. However, you can supply the full path and name to another project. 

**force_source_to_solve**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

**preserve_partner_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`. 

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
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> setup = m2d.get_setup("Setup1")
>>> setup.start_continue_from_previous_setup(design="IM", solution="Setup1 : Transient")

```
Copy to clipboard