---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_error_message.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_error_message 

AedtLogger.add_error_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 2 “Error” message to the message manager tree.
Also add an error message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the error message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the error message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the error message gets added to the `"Design"` level.
Examples
Add an error message to the AEDT message manager.

```
>>> hfss.logger.project_logger.error("Project Error Message", "Project")

```
Copy to clipboard
# add_error_message 

AedtLogger.add_error_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 2 “Error” message to the message manager tree.
Also add an error message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the error message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the error message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the error message gets added to the `"Design"` level.
Examples
Add an error message to the AEDT message manager.

```
>>> hfss.logger.project_logger.error("Project Error Message", "Project")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_error_message.rst.txt)

# add_error_message 

AedtLogger.add_error_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 2 “Error” message to the message manager tree.
Also add an error message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the error message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the error message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the error message gets added to the `"Design"` level.
Examples
Add an error message to the AEDT message manager.

```
>>> hfss.logger.project_logger.error("Project Error Message", "Project")

```
Copy to clipboard