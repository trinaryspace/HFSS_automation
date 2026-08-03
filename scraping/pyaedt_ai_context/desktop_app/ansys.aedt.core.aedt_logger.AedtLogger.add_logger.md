---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_logger.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_logger 

AedtLogger.add_logger(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 10_) → [Logger](https://docs.python.org/3.11/library/logging.html#logging.Logger "\(in Python v3.11\)") 
    
Add a logger for either the active project or active design. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Logger to write to. Options are `"Project"` and `"Design"`. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level enum. The default is `logging.DEBUG`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> project_logger = hfss.logger.add_logger("Project")

```
Copy to clipboard
# add_logger 

AedtLogger.add_logger(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 10_) → [Logger](https://docs.python.org/3.11/library/logging.html#logging.Logger "\(in Python v3.11\)") 
    
Add a logger for either the active project or active design. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Logger to write to. Options are `"Project"` and `"Design"`. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level enum. The default is `logging.DEBUG`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> project_logger = hfss.logger.add_logger("Project")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_logger.rst.txt)

# add_logger 

AedtLogger.add_logger(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 10_) → [Logger](https://docs.python.org/3.11/library/logging.html#logging.Logger "\(in Python v3.11\)") 
    
Add a logger for either the active project or active design. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Logger to write to. Options are `"Project"` and `"Design"`. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level enum. The default is `logging.DEBUG`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> project_logger = hfss.logger.add_logger("Project")

```
Copy to clipboard