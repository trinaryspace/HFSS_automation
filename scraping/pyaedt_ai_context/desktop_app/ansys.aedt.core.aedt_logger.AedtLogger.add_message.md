---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_message.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_message 

AedtLogger.add_message(_message_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Type of the message. Options are: * `0` : Info * `1` : Warning * `2` : Error * `3` : Debug 

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the message gets added to the `"Design"` level. 

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_message(0, "Custom info message")

```
Copy to clipboard
# add_message 

AedtLogger.add_message(_message_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Type of the message. Options are: * `0` : Info * `1` : Warning * `2` : Error * `3` : Debug 

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the message gets added to the `"Design"` level. 

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_message(0, "Custom info message")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_message.rst.txt)

# add_message 

AedtLogger.add_message(_message_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Type of the message. Options are: * `0` : Info * `1` : Warning * `2` : Error * `3` : Debug 

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the message gets added to the `"Design"` level. 

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the project. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_message(0, "Custom info message")

```
Copy to clipboard