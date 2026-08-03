---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_warning_message 

AedtLogger.add_warning_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 1 “Warning” message to the message manager tree.
Also add a warning message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the warning message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the warning message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the warning message gets added to the `"Design"` level.
Examples
Add a warning message to the AEDT message manager.

```
>>> hfss.logger.warning("Global warning message")

```
Copy to clipboard
# add_warning_message 

AedtLogger.add_warning_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 1 “Warning” message to the message manager tree.
Also add a warning message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the warning message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the warning message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the warning message gets added to the `"Design"` level.
Examples
Add a warning message to the AEDT message manager.

```
>>> hfss.logger.warning("Global warning message")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message.rst.txt)

# add_warning_message 

AedtLogger.add_warning_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 1 “Warning” message to the message manager tree.
Also add a warning message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the warning message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the warning message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the warning message gets added to the `"Design"` level.
Examples
Add a warning message to the AEDT message manager.

```
>>> hfss.logger.warning("Global warning message")

```
Copy to clipboard