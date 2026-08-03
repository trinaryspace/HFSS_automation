---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.export_config.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# export_config 

Configurations.export_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export current design properties to a JSON or TOML file.
The sections to be exported are defined with `configuration.options` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to json file. If `None`, then the config file will be saved in working directory. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the json file will be overwritten if already existing. If `False` and the version is compatible, the data in the existing file will be updated. Default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Exported config file.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.export_config(r"C:\Temp\hfss_config.json", overwrite=True)

```
Copy to clipboard
# export_config 

Configurations.export_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export current design properties to a JSON or TOML file.
The sections to be exported are defined with `configuration.options` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to json file. If `None`, then the config file will be saved in working directory. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the json file will be overwritten if already existing. If `False` and the version is compatible, the data in the existing file will be updated. Default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Exported config file.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.export_config(r"C:\Temp\hfss_config.json", overwrite=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.export_config.rst.txt)

# export_config 

Configurations.export_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export current design properties to a JSON or TOML file.
The sections to be exported are defined with `configuration.options` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to json file. If `None`, then the config file will be saved in working directory. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the json file will be overwritten if already existing. If `False` and the version is compatible, the data in the existing file will be updated. Default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Exported config file.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.export_config(r"C:\Temp\hfss_config.json", overwrite=True)

```
Copy to clipboard