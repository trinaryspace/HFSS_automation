---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# AppFilter 

class ansys.aedt.core.aedt_logger.AppFilter(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _extra : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Specifies the destination of the logger.
AEDT exposes three different loggers, which are the global, project, and design loggers. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Logger to write to. Options are `"Global"`, ``"Project"`, and `"Design"`. The default is `"Global"`. 

**extra**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design or project. The default is `""`.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Project", extra="MyProject")

```
Copy to clipboard
Methods  
| [`AppFilter.filter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.filter.html#ansys.aedt.core.aedt_logger.AppFilter.filter "ansys.aedt.core.aedt_logger.AppFilter.filter")(record)  | Filter logs.  |  
| --- | --- |  
# AppFilter 

class ansys.aedt.core.aedt_logger.AppFilter(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _extra : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Specifies the destination of the logger.
AEDT exposes three different loggers, which are the global, project, and design loggers. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Logger to write to. Options are `"Global"`, ``"Project"`, and `"Design"`. The default is `"Global"`. 

**extra**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design or project. The default is `""`.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Project", extra="MyProject")

```
Copy to clipboard
Methods  
| [`AppFilter.filter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.filter.html#ansys.aedt.core.aedt_logger.AppFilter.filter "ansys.aedt.core.aedt_logger.AppFilter.filter")(record)  | Filter logs.  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.rst.txt)

# AppFilter 

class ansys.aedt.core.aedt_logger.AppFilter(_destination : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _extra : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Specifies the destination of the logger.
AEDT exposes three different loggers, which are the global, project, and design loggers. 

Parameters: 
     

**destination**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Logger to write to. Options are `"Global"`, ``"Project"`, and `"Design"`. The default is `"Global"`. 

**extra**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design or project. The default is `""`.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Project", extra="MyProject")

```
Copy to clipboard
Methods  
| [`AppFilter.filter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.filter.html#ansys.aedt.core.aedt_logger.AppFilter.filter "ansys.aedt.core.aedt_logger.AppFilter.filter")(record)  | Filter logs.  |  
| --- | --- |