---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# assign_point_monitor_to_vertex 

Monitor.assign_point_monitor_to_vertex(_vertex_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor to a vertex. 

Parameters: 
     

**vertex_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID of the vertex or list of IDs. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_point_monitor_to_vertex(vertex_id=[1])

```
Copy to clipboard
# assign_point_monitor_to_vertex 

Monitor.assign_point_monitor_to_vertex(_vertex_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor to a vertex. 

Parameters: 
     

**vertex_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID of the vertex or list of IDs. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_point_monitor_to_vertex(vertex_id=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex.rst.txt)

# assign_point_monitor_to_vertex 

Monitor.assign_point_monitor_to_vertex(_vertex_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor to a vertex. 

Parameters: 
     

**vertex_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID of the vertex or list of IDs. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of monitor names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()
>>> obj.assign_point_monitor_to_vertex(vertex_id=[1])

```
Copy to clipboard