---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# Monitor 

class ansys.aedt.core.visualization.post.monitor_icepak.Monitor(_p_app_) 
    
Provides Icepak monitor methods.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()

```
Copy to clipboard
Methods  
| [`Monitor.assign_face_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor")(face_id[, ...])  | Assign a face monitor.  |  
| --- | --- |  
| [`Monitor.assign_point_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor")(point_position)  | Create and assign a point monitor.  |  
| [`Monitor.assign_point_monitor_in_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object")(name)  | Assign a point monitor in the centroid of a specific object.  |  
| [`Monitor.assign_point_monitor_to_vertex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex")(vertex_id)  | Create and assign a point monitor to a vertex.  |  
| [`Monitor.assign_surface_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor")(surface_name)  | Assign a surface monitor.  |  
| [`Monitor.delete_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor")(monitor_name)  | Delete monitor object.  |  
| [`Monitor.get_icepak_monitor_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object")(monitor_name)  | Get Icepak monitor object.  |  
| [`Monitor.get_monitor_object_assignment`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment")(monitor)  | Get the object that the monitor is applied to.  |  
| [`Monitor.insert_monitor_object_from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict")(...)  | Insert a monitor.  |  
Attributes  
| [`Monitor.all_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors")  | Get all monitor objects.  |  
| --- | --- |  
| [`Monitor.face_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors")  | Get point monitor objects.  |  
| [`Monitor.point_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors")  | Get face monitor objects.  |  
| [`Monitor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir")  | Shortcut for dir(self).  |  
# Monitor 

class ansys.aedt.core.visualization.post.monitor_icepak.Monitor(_p_app_) 
    
Provides Icepak monitor methods.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()

```
Copy to clipboard
Methods  
| [`Monitor.assign_face_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor")(face_id[, ...])  | Assign a face monitor.  |  
| --- | --- |  
| [`Monitor.assign_point_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor")(point_position)  | Create and assign a point monitor.  |  
| [`Monitor.assign_point_monitor_in_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object")(name)  | Assign a point monitor in the centroid of a specific object.  |  
| [`Monitor.assign_point_monitor_to_vertex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex")(vertex_id)  | Create and assign a point monitor to a vertex.  |  
| [`Monitor.assign_surface_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor")(surface_name)  | Assign a surface monitor.  |  
| [`Monitor.delete_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor")(monitor_name)  | Delete monitor object.  |  
| [`Monitor.get_icepak_monitor_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object")(monitor_name)  | Get Icepak monitor object.  |  
| [`Monitor.get_monitor_object_assignment`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment")(monitor)  | Get the object that the monitor is applied to.  |  
| [`Monitor.insert_monitor_object_from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict")(...)  | Insert a monitor.  |  
Attributes  
| [`Monitor.all_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors")  | Get all monitor objects.  |  
| --- | --- |  
| [`Monitor.face_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors")  | Get point monitor objects.  |  
| [`Monitor.point_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors")  | Get face monitor objects.  |  
| [`Monitor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.rst.txt)

# Monitor 

class ansys.aedt.core.visualization.post.monitor_icepak.Monitor(_p_app_) 
    
Provides Icepak monitor methods.
Examples

```
>>> from ansys.aedt.core.visualization.post.monitor_icepak import Monitor
>>> obj = Monitor()

```
Copy to clipboard
Methods  
| [`Monitor.assign_face_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_face_monitor")(face_id[, ...])  | Assign a face monitor.  |  
| --- | --- |  
| [`Monitor.assign_point_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor")(point_position)  | Create and assign a point monitor.  |  
| [`Monitor.assign_point_monitor_in_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_in_object")(name)  | Assign a point monitor in the centroid of a specific object.  |  
| [`Monitor.assign_point_monitor_to_vertex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_point_monitor_to_vertex")(vertex_id)  | Create and assign a point monitor to a vertex.  |  
| [`Monitor.assign_surface_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.assign_surface_monitor")(surface_name)  | Assign a surface monitor.  |  
| [`Monitor.delete_monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.delete_monitor")(monitor_name)  | Delete monitor object.  |  
| [`Monitor.get_icepak_monitor_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_icepak_monitor_object")(monitor_name)  | Get Icepak monitor object.  |  
| [`Monitor.get_monitor_object_assignment`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.get_monitor_object_assignment")(monitor)  | Get the object that the monitor is applied to.  |  
| [`Monitor.insert_monitor_object_from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.insert_monitor_object_from_dict")(...)  | Insert a monitor.  |  
Attributes  
| [`Monitor.all_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.all_monitors")  | Get all monitor objects.  |  
| --- | --- |  
| [`Monitor.face_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.face_monitors")  | Get point monitor objects.  |  
| [`Monitor.point_monitors`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.point_monitors")  | Get face monitor objects.  |  
| [`Monitor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir.html#ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir "ansys.aedt.core.visualization.post.monitor_icepak.Monitor.public_dir")  | Shortcut for dir(self).  |