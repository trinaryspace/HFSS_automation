---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# get_messages 

AedtLogger.get_messages(_project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _aedt_messages : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → MessageList 
    
Get the message manager content for a specified project and design.
If the specified project and design names are invalid, they are ignored. 

Parameters: 
     

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project to read messages from. Leave empty string to get Desktop level messages. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to read messages from. Leave empty string to get Desktop level messages. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of messages to read. 0 – info and above, 1 – warning and above, 2 – error and fatal 

**aedt_messages**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Read content of message manager even if logger is disabled. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of messages for the specified project and design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> msgs = hfss.logger.get_messages(level=0)

```
Copy to clipboard
# get_messages 

AedtLogger.get_messages(_project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _aedt_messages : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → MessageList 
    
Get the message manager content for a specified project and design.
If the specified project and design names are invalid, they are ignored. 

Parameters: 
     

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project to read messages from. Leave empty string to get Desktop level messages. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to read messages from. Leave empty string to get Desktop level messages. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of messages to read. 0 – info and above, 1 – warning and above, 2 – error and fatal 

**aedt_messages**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Read content of message manager even if logger is disabled. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of messages for the specified project and design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> msgs = hfss.logger.get_messages(level=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.rst.txt)

# get_messages 

AedtLogger.get_messages(_project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _aedt_messages : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → MessageList 
    
Get the message manager content for a specified project and design.
If the specified project and design names are invalid, they are ignored. 

Parameters: 
     

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project to read messages from. Leave empty string to get Desktop level messages. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to read messages from. Leave empty string to get Desktop level messages. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of messages to read. 0 – info and above, 1 – warning and above, 2 – error and fatal 

**aedt_messages**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Read content of message manager even if logger is disabled. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of messages for the specified project and design.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> msgs = hfss.logger.get_messages(level=0)

```
Copy to clipboard