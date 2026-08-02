---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.set_custom_hpc_options.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_custom_hpc_options 

Hfss3dLayout.set_custom_hpc_options(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set custom HPC options.
This method creates a temporary ACF file based on the local configuration file and modifies it with the specified HPC options. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `None`. 

**gpus**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of gpus. The default is `None`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks. The default is `None`. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Allowed distribution types. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_custom_hpc_options(cores=4, tasks=2)

```
Copy to clipboard
# set_custom_hpc_options 

Hfss3dLayout.set_custom_hpc_options(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set custom HPC options.
This method creates a temporary ACF file based on the local configuration file and modifies it with the specified HPC options. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `None`. 

**gpus**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of gpus. The default is `None`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks. The default is `None`. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Allowed distribution types. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_custom_hpc_options(cores=4, tasks=2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.set_custom_hpc_options.rst.txt)

# set_custom_hpc_options 

Hfss3dLayout.set_custom_hpc_options(_cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _gpus : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _tasks : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _num_variations_to_distribute : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _allowed_distribution_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _use_auto_settings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set custom HPC options.
This method creates a temporary ACF file based on the local configuration file and modifies it with the specified HPC options. 

Parameters: 
     

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `None`. 

**gpus**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of gpus. The default is `None`. 

**tasks**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of tasks. The default is `None`. 

**num_variations_to_distribute**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

**allowed_distribution_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Allowed distribution types. The default is `None`. 

**use_auto_settings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Number of variations to distribute. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_custom_hpc_options(cores=4, tasks=2)

```
Copy to clipboard