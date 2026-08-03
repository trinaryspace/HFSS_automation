---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.validate.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# validate 

Configurations.validate(_config : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate a configuration file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**config**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Configuration as a JSON file or dictionary. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the configuration file is valid, `False` otherwise. If the validation fails, a warning is also written to the logger.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.validate(r"C:\Temp\hfss_config.json")

```
Copy to clipboard
# validate 

Configurations.validate(_config : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate a configuration file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**config**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Configuration as a JSON file or dictionary. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the configuration file is valid, `False` otherwise. If the validation fails, a warning is also written to the logger.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.validate(r"C:\Temp\hfss_config.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.configurations.Configurations.validate.rst.txt)

# validate 

Configurations.validate(_config : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate a configuration file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**config**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Configuration as a JSON file or dictionary. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the configuration file is valid, `False` otherwise. If the validation fails, a warning is also written to the logger.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.configurations.validate(r"C:\Temp\hfss_config.json")

```
Copy to clipboard