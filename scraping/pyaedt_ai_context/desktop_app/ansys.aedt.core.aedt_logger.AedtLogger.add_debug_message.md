---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_debug_message 

AedtLogger.add_debug_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Parameterized message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default value is `None`, in which case the info message gets added to the `"Design"` level.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_debug_message("Debug info")

```
Copy to clipboard
# add_debug_message 

AedtLogger.add_debug_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Parameterized message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default value is `None`, in which case the info message gets added to the `"Design"` level.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_debug_message("Debug info")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message.rst.txt)

# add_debug_message 

AedtLogger.add_debug_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Parameterized message to the message manager to specify the type and project or design level. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default value is `None`, in which case the info message gets added to the `"Design"` level.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.add_debug_message("Debug info")

```
Copy to clipboard