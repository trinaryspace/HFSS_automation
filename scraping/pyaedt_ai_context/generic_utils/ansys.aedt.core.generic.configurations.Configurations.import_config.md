---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.import_config.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# import_config 

Configurations.import_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _* args_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import configuration settings from a JSON or TOML file and apply it to the current design.
The sections to be applied are defined with the `configuration.options` class. The import operation result is saved in the `configuration.results` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to json file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Config dictionary.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.import_config(r"C:\Temp\hfss_config.json")

```
Copy to clipboard
# import_config 

Configurations.import_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _* args_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import configuration settings from a JSON or TOML file and apply it to the current design.
The sections to be applied are defined with the `configuration.options` class. The import operation result is saved in the `configuration.results` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to json file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Config dictionary.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.import_config(r"C:\Temp\hfss_config.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.import_config.rst.txt)

# import_config 

Configurations.import_config(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _* args_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import configuration settings from a JSON or TOML file and apply it to the current design.
The sections to be applied are defined with the `configuration.options` class. The import operation result is saved in the `configuration.results` class. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to json file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Config dictionary.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.import_config(r"C:\Temp\hfss_config.json")

```
Copy to clipboard