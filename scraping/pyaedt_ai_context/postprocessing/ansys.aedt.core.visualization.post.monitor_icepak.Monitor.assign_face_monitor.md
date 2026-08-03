---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# assign_face_monitor 

Monitor.assign_face_monitor(_face_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a face monitor. 

Parameters: 
     

**face_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Face id or list of ids 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignFaceMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_face_monitor(face_id=[1])

```
Copy to clipboard
# assign_face_monitor 

Monitor.assign_face_monitor(_face_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a face monitor. 

Parameters: 
     

**face_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Face id or list of ids 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignFaceMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_face_monitor(face_id=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor.rst.txt)

# assign_face_monitor 

Monitor.assign_face_monitor(_face_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a face monitor. 

Parameters: 
     

**face_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Face id or list of ids 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignFaceMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_face_monitor(face_id=[1])

```
Copy to clipboard