---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# assign_point_monitor 

Monitor.assign_point_monitor(_point_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor. 

Parameters: 
     

**point_position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the point or name of the point. Also, multiple monitor assignment with list of list with coordinates or list of strings with points names. 

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
Create two temperature monitor at the points `[0, 0, 0]` and `[1, 1, 1]`.

```
>>> icepak.monitor.assign_point_monitor([[0, 0, 0], [1, 1, 1]], monitor_name="monitor1")
['monitor1', 'monitor2']

```
Copy to clipboard
# assign_point_monitor 

Monitor.assign_point_monitor(_point_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor. 

Parameters: 
     

**point_position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the point or name of the point. Also, multiple monitor assignment with list of list with coordinates or list of strings with points names. 

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
Create two temperature monitor at the points `[0, 0, 0]` and `[1, 1, 1]`.

```
>>> icepak.monitor.assign_point_monitor([[0, 0, 0], [1, 1, 1]], monitor_name="monitor1")
['monitor1', 'monitor2']

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor.rst.txt)

# assign_point_monitor 

Monitor.assign_point_monitor(_point_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create and assign a point monitor. 

Parameters: 
     

**point_position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the point or name of the point. Also, multiple monitor assignment with list of list with coordinates or list of strings with points names. 

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
Create two temperature monitor at the points `[0, 0, 0]` and `[1, 1, 1]`.

```
>>> icepak.monitor.assign_point_monitor([[0, 0, 0], [1, 1, 1]], monitor_name="monitor1")
['monitor1', 'monitor2']

```
Copy to clipboard