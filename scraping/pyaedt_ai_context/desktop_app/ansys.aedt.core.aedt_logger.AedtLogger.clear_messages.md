---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.clear_messages.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# clear_messages 

AedtLogger.clear_messages(_proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 2_) 
    
Clear all messages. 

Parameters: 
     

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of project. The default is `None`, in which case messages are cleared for the current project. If blank, messages are cleared for all projects. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design within the specified project. The default is `None,` in which case the current design is used. If blank, all designs are used. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the messages to clear. Options are:
  * `0` : Clear all info messages.
  * `1` : Clear all info and warning messages.
  * `2` : Clear all info, warning, and error messages.
  * `3` : Clear all messages, which include info, warning, error, and fatal-error messages.

The default is `2.`
Examples
Clear all messages in the current design and project.

```
>>> hfss.clear_messages(level=3)

```
Copy to clipboard
Clear all messages.

```
>>> hfss.clear_messages(proj_name="", des_name="", level=3)

```
Copy to clipboard
# clear_messages 

AedtLogger.clear_messages(_proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 2_) 
    
Clear all messages. 

Parameters: 
     

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of project. The default is `None`, in which case messages are cleared for the current project. If blank, messages are cleared for all projects. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design within the specified project. The default is `None,` in which case the current design is used. If blank, all designs are used. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the messages to clear. Options are:
  * `0` : Clear all info messages.
  * `1` : Clear all info and warning messages.
  * `2` : Clear all info, warning, and error messages.
  * `3` : Clear all messages, which include info, warning, error, and fatal-error messages.

The default is `2.`
Examples
Clear all messages in the current design and project.

```
>>> hfss.clear_messages(level=3)

```
Copy to clipboard
Clear all messages.

```
>>> hfss.clear_messages(proj_name="", des_name="", level=3)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.clear_messages.rst.txt)

# clear_messages 

AedtLogger.clear_messages(_proj_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _des_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 2_) 
    
Clear all messages. 

Parameters: 
     

**proj_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of project. The default is `None`, in which case messages are cleared for the current project. If blank, messages are cleared for all projects. 

**des_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design within the specified project. The default is `None,` in which case the current design is used. If blank, all designs are used. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the messages to clear. Options are:
  * `0` : Clear all info messages.
  * `1` : Clear all info and warning messages.
  * `2` : Clear all info, warning, and error messages.
  * `3` : Clear all messages, which include info, warning, error, and fatal-error messages.

The default is `2.`
Examples
Clear all messages in the current design and project.

```
>>> hfss.clear_messages(level=3)

```
Copy to clipboard
Clear all messages.

```
>>> hfss.clear_messages(proj_name="", des_name="", level=3)

```
Copy to clipboard