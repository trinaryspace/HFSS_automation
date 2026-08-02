---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.analyze_setup.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# analyze_setup 

Hfss.analyze_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup, which can be an optimetric setup or a simple setup. The default is `None`, in which case all setups are solved. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `None` which will use default hpc options of AEDT. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `None`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphics processing units. The default is `None`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either use or not auto settings in task/cores. It is not supported by all Setup. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. For this to take effect `use_auto_settings` must be set to `True`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of strings. Each string represents a distribution type. The default value `None` does nothing. An empty list `[]` disables all types. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze_setup(name="Setup1")

```
Copy to clipboard
# analyze_setup 

Hfss.analyze_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup, which can be an optimetric setup or a simple setup. The default is `None`, in which case all setups are solved. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `None` which will use default hpc options of AEDT. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `None`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphics processing units. The default is `None`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either use or not auto settings in task/cores. It is not supported by all Setup. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. For this to take effect `use_auto_settings` must be set to `True`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of strings. Each string represents a distribution type. The default value `None` does nothing. An empty list `[]` disables all types. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze_setup(name="Setup1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.analyze_setup.rst.txt)

# analyze_setup 

Hfss.analyze_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _acf_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _revert_to_initial_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _blocking : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Analyze a design setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup, which can be an optimetric setup or a simple setup. The default is `None`, in which case all setups are solved. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation cores. The default is `None` which will use default hpc options of AEDT. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation tasks. The default is `None`. 

**gpus**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of simulation graphics processing units. The default is `None`. 

**acf_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the custom ACF file. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either use or not auto settings in task/cores. It is not supported by all Setup. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. For this to take effect `use_auto_settings` must be set to `True`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of strings. Each string represents a distribution type. The default value `None` does nothing. An empty list `[]` disables all types. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze_setup(name="Setup1")

```
Copy to clipboard