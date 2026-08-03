---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# assign_point_monitor_in_object 

Monitor.assign_point_monitor_in_object(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a point monitor in the centroid of a specific object. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the object to assign monitor point to. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples
Create a box named `"BlockBox1"` and assign a temperature monitor point to that object.

```
>>> box = icepak.modeler.create_box([1, 1, 1], [3, 3, 3], "BlockBox1", "copper")
>>> icepak.assign_point_monitor(box.name, monitor_name="monitor2")
"'monitor2'

```
Copy to clipboard
# assign_point_monitor_in_object 

Monitor.assign_point_monitor_in_object(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a point monitor in the centroid of a specific object. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the object to assign monitor point to. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples
Create a box named `"BlockBox1"` and assign a temperature monitor point to that object.

```
>>> box = icepak.modeler.create_box([1, 1, 1], [3, 3, 3], "BlockBox1", "copper")
>>> icepak.assign_point_monitor(box.name, monitor_name="monitor2")
"'monitor2'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object.rst.txt)

# assign_point_monitor_in_object 

Monitor.assign_point_monitor_in_object(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a point monitor in the centroid of a specific object. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the object to assign monitor point to. 

**monitor_quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Quantity being monitored. The default is `"Temperature"`. 

**monitor_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the monitor. The default is `None`, in which case the name is randomly generated. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Monitor name or list of names when successful, `False` when failed.
References

```
>>> oModule.AssignPointMonitor

```
Copy to clipboard
Examples
Create a box named `"BlockBox1"` and assign a temperature monitor point to that object.

```
>>> box = icepak.modeler.create_box([1, 1, 1], [3, 3, 3], "BlockBox1", "copper")
>>> icepak.assign_point_monitor(box.name, monitor_name="monitor2")
"'monitor2'

```
Copy to clipboard