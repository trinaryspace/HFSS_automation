---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# insert_monitor_object_from_dict 

Monitor.insert_monitor_object_from_dict(_monitor_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _mode : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a monitor. 

Parameters: 
     

**monitor_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing monitor object information. 

**mode**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Integer to select the information to handle. To identify the faces, vertices, surfaces, and object to which to assign the monitor to, you can use: - ids and names, mode=0, required dict keys: “Name”, “Type”, “ID”, “Quantity”. - positions, mode=1, required dict keys: “Name”, “Type”, “Geometry Assignment”, “Location”, “Quantity”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the monitor object.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.insert_monitor_object_from_dict(monitor_dict={"Name": "Value"})

```
Copy to clipboard
# insert_monitor_object_from_dict 

Monitor.insert_monitor_object_from_dict(_monitor_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _mode : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a monitor. 

Parameters: 
     

**monitor_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing monitor object information. 

**mode**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Integer to select the information to handle. To identify the faces, vertices, surfaces, and object to which to assign the monitor to, you can use: - ids and names, mode=0, required dict keys: “Name”, “Type”, “ID”, “Quantity”. - positions, mode=1, required dict keys: “Name”, “Type”, “Geometry Assignment”, “Location”, “Quantity”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the monitor object.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.insert_monitor_object_from_dict(monitor_dict={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict.rst.txt)

# insert_monitor_object_from_dict 

Monitor.insert_monitor_object_from_dict(_monitor_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _mode : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a monitor. 

Parameters: 
     

**monitor_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing monitor object information. 

**mode**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Integer to select the information to handle. To identify the faces, vertices, surfaces, and object to which to assign the monitor to, you can use: - ids and names, mode=0, required dict keys: “Name”, “Type”, “ID”, “Quantity”. - positions, mode=1, required dict keys: “Name”, “Type”, “Geometry Assignment”, “Location”, “Quantity”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the monitor object.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.insert_monitor_object_from_dict(monitor_dict={"Name": "Value"})

```
Copy to clipboard