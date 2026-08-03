---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.analyze.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# analyze 

SetupParam.analyze(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _solve_in_batch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Solve the active design. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `1`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `1`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphic processing units to use. The default is `0`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set `True` to use automatic settings for HPC. The option is only considered for setups that support automatic settings. 

**solve_in_batch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to solve the project in batch or not. If `True` the project will be saved, closed, solved and repened. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to initial mesh before solving or not. Default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.Analyze

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.analyze(cores=[1, 2, 3], tasks=[1, 2, 3])

```
Copy to clipboard
# analyze 

SetupParam.analyze(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _solve_in_batch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Solve the active design. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `1`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `1`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphic processing units to use. The default is `0`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set `True` to use automatic settings for HPC. The option is only considered for setups that support automatic settings. 

**solve_in_batch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to solve the project in batch or not. If `True` the project will be saved, closed, solved and repened. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to initial mesh before solving or not. Default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.Analyze

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.analyze(cores=[1, 2, 3], tasks=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.analyze.rst.txt)

# analyze 

SetupParam.analyze(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _solve_in_batch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _machine : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'localhost'_, _run_in_thread : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Solve the active design. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `1`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `1`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphic processing units to use. The default is `0`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set `True` to use automatic settings for HPC. The option is only considered for setups that support automatic settings. 

**solve_in_batch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to solve the project in batch or not. If `True` the project will be saved, closed, solved and repened. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the machine if remote. The default is `"localhost"`. 

**run_in_thread**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to submit the batch command as a thread. The default is `False`. 

**revert_to_initial_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to revert to initial mesh before solving or not. Default is `False`. 

**blocking**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to block script while analysis is completed or not. It works from AEDT 2023 R2. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.Analyze

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.analyze(cores=[1, 2, 3], tasks=[1, 2, 3])

```
Copy to clipboard