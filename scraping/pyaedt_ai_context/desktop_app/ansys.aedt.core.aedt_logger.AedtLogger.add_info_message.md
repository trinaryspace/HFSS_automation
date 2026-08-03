---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_info_message.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_info_message 

AedtLogger.add_info_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 0 “Info” message to the active design level of the message manager tree.
Also add an info message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the info message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the info message gets added to the `"Design"` level.
Examples
Add an info message at the global level.

```
>>> hfss.logger.info("Global warning message", "Global")

```
Copy to clipboard
# add_info_message 

AedtLogger.add_info_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 0 “Info” message to the active design level of the message manager tree.
Also add an info message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the info message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the info message gets added to the `"Design"` level.
Examples
Add an info message at the global level.

```
>>> hfss.logger.info("Global warning message", "Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_info_message.rst.txt)

# add_info_message 

AedtLogger.add_info_message(_message_text : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Add a type 0 “Info” message to the active design level of the message manager tree.
Also add an info message to the logger if the handler is present. 

Parameters: 
     

**message_text**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Text to display as the info message. 

**level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Level to add the info message to. Options are `"Global"`, `"Project"`, and `"Design"`. The default is `None`, in which case the info message gets added to the `"Design"` level.
Examples
Add an info message at the global level.

```
>>> hfss.logger.info("Global warning message", "Global")

```
Copy to clipboard