---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# assign_surface_monitor 

Monitor.assign_surface_monitor(_surface_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a surface monitor. 

Parameters: 
     

**surface_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the surface or list of names. 

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
Create a rectangle named `"Surface1"` and assign a temperature monitor to that surface.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> surface = icepak.modeler.create_rectangle(Plane.XY, [0, 0, 0], [10, 20], name="Surface1")
>>> icepak.assign_surface_monitor("Surface1", monitor_name="monitor")
'monitor'

```
Copy to clipboard
# assign_surface_monitor 

Monitor.assign_surface_monitor(_surface_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a surface monitor. 

Parameters: 
     

**surface_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the surface or list of names. 

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
Create a rectangle named `"Surface1"` and assign a temperature monitor to that surface.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> surface = icepak.modeler.create_rectangle(Plane.XY, [0, 0, 0], [10, 20], name="Surface1")
>>> icepak.assign_surface_monitor("Surface1", monitor_name="monitor")
'monitor'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor.rst.txt)

# assign_surface_monitor 

Monitor.assign_surface_monitor(_surface_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _monitor_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Temperature'_, _monitor_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a surface monitor. 

Parameters: 
     

**surface_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the surface or list of names. 

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
Create a rectangle named `"Surface1"` and assign a temperature monitor to that surface.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> surface = icepak.modeler.create_rectangle(Plane.XY, [0, 0, 0], [10, 20], name="Surface1")
>>> icepak.assign_surface_monitor("Surface1", monitor_name="monitor")
'monitor'

```
Copy to clipboard