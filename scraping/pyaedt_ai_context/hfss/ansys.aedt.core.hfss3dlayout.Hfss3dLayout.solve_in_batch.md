---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.solve_in_batch.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# solve_in_batch 

Hfss3dLayout.solve_in_batch(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup in batch mode.
Note
To use this function, the project must be closed.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, which means that the active project is to be solved. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores to use in the simulation. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks to use in the simulation. Set `num_tasks` to `-1` to apply auto settings and distributed mode. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup, which can be an optimetrics setup or a simple setup. The default is `None`, in which case all setups are solved. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to the initial mesh before solving. The default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solve_in_batch(cores=4, tasks=1)

```
Copy to clipboard
# solve_in_batch 

Hfss3dLayout.solve_in_batch(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup in batch mode.
Note
To use this function, the project must be closed.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, which means that the active project is to be solved. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores to use in the simulation. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks to use in the simulation. Set `num_tasks` to `-1` to apply auto settings and distributed mode. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup, which can be an optimetrics setup or a simple setup. The default is `None`, in which case all setups are solved. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to the initial mesh before solving. The default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solve_in_batch(cores=4, tasks=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.solve_in_batch.rst.txt)

# solve_in_batch 

Hfss3dLayout.solve_in_batch(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup in batch mode.
Note
To use this function, the project must be closed.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, which means that the active project is to be solved. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores to use in the simulation. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks to use in the simulation. Set `num_tasks` to `-1` to apply auto settings and distributed mode. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup, which can be an optimetrics setup or a simple setup. The default is `None`, in which case all setups are solved. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to the initial mesh before solving. The default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solve_in_batch(cores=4, tasks=1)

```
Copy to clipboard