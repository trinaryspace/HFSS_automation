---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# TransientProfile 

class ansys.aedt.core.modules.profile.TransientProfile(_data_) 
    
Profile data for a transient solution. 

Parameters: 
     

**data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Node representing the *Transient Solution Group*.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import TransientProfile
>>> obj = TransientProfile()

```
Copy to clipboard
Methods  
| [`TransientProfile.table`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.table.html#ansys.aedt.core.modules.profile.TransientProfile.table "ansys.aedt.core.modules.profile.TransientProfile.table")([columns])  | Return a summary of profile step metrics.  |  
| --- | --- |  
| [`TransientProfile.time_step_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_step_keys.html#ansys.aedt.core.modules.profile.TransientProfile.time_step_keys "ansys.aedt.core.modules.profile.TransientProfile.time_step_keys")(max_time)  | Return time-step labels up to a limit.  |  
Attributes  
| [`TransientProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.cpu_time.html#ansys.aedt.core.modules.profile.TransientProfile.cpu_time "ansys.aedt.core.modules.profile.TransientProfile.cpu_time")  | CPU time for this step.  |  
| --- | --- |  
| [`TransientProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_memory.html#ansys.aedt.core.modules.profile.TransientProfile.max_memory "ansys.aedt.core.modules.profile.TransientProfile.max_memory")  | Maximum memory over this step and all descendants.  |  
| [`TransientProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_time.html#ansys.aedt.core.modules.profile.TransientProfile.max_time "ansys.aedt.core.modules.profile.TransientProfile.max_time")  | Largest time step in seconds, if any.  |  
| [`TransientProfile.process_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.process_steps.html#ansys.aedt.core.modules.profile.TransientProfile.process_steps "ansys.aedt.core.modules.profile.TransientProfile.process_steps")  | Names of nested process steps, if any.  |  
| [`TransientProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.public_dir.html#ansys.aedt.core.modules.profile.TransientProfile.public_dir "ansys.aedt.core.modules.profile.TransientProfile.public_dir")  | Shortcut for dir(self).  |  
| [`TransientProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.real_time.html#ansys.aedt.core.modules.profile.TransientProfile.real_time "ansys.aedt.core.modules.profile.TransientProfile.real_time")  | Real time for this step.  |  
| [`TransientProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_steps.html#ansys.aedt.core.modules.profile.TransientProfile.time_steps "ansys.aedt.core.modules.profile.TransientProfile.time_steps")  | Retrieve time steps.  |  
# TransientProfile 

class ansys.aedt.core.modules.profile.TransientProfile(_data_) 
    
Profile data for a transient solution. 

Parameters: 
     

**data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Node representing the *Transient Solution Group*.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import TransientProfile
>>> obj = TransientProfile()

```
Copy to clipboard
Methods  
| [`TransientProfile.table`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.table.html#ansys.aedt.core.modules.profile.TransientProfile.table "ansys.aedt.core.modules.profile.TransientProfile.table")([columns])  | Return a summary of profile step metrics.  |  
| --- | --- |  
| [`TransientProfile.time_step_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_step_keys.html#ansys.aedt.core.modules.profile.TransientProfile.time_step_keys "ansys.aedt.core.modules.profile.TransientProfile.time_step_keys")(max_time)  | Return time-step labels up to a limit.  |  
Attributes  
| [`TransientProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.cpu_time.html#ansys.aedt.core.modules.profile.TransientProfile.cpu_time "ansys.aedt.core.modules.profile.TransientProfile.cpu_time")  | CPU time for this step.  |  
| --- | --- |  
| [`TransientProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_memory.html#ansys.aedt.core.modules.profile.TransientProfile.max_memory "ansys.aedt.core.modules.profile.TransientProfile.max_memory")  | Maximum memory over this step and all descendants.  |  
| [`TransientProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_time.html#ansys.aedt.core.modules.profile.TransientProfile.max_time "ansys.aedt.core.modules.profile.TransientProfile.max_time")  | Largest time step in seconds, if any.  |  
| [`TransientProfile.process_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.process_steps.html#ansys.aedt.core.modules.profile.TransientProfile.process_steps "ansys.aedt.core.modules.profile.TransientProfile.process_steps")  | Names of nested process steps, if any.  |  
| [`TransientProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.public_dir.html#ansys.aedt.core.modules.profile.TransientProfile.public_dir "ansys.aedt.core.modules.profile.TransientProfile.public_dir")  | Shortcut for dir(self).  |  
| [`TransientProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.real_time.html#ansys.aedt.core.modules.profile.TransientProfile.real_time "ansys.aedt.core.modules.profile.TransientProfile.real_time")  | Real time for this step.  |  
| [`TransientProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_steps.html#ansys.aedt.core.modules.profile.TransientProfile.time_steps "ansys.aedt.core.modules.profile.TransientProfile.time_steps")  | Retrieve time steps.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.rst.txt)

# TransientProfile 

class ansys.aedt.core.modules.profile.TransientProfile(_data_) 
    
Profile data for a transient solution. 

Parameters: 
     

**data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Node representing the *Transient Solution Group*.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import TransientProfile
>>> obj = TransientProfile()

```
Copy to clipboard
Methods  
| [`TransientProfile.table`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.table.html#ansys.aedt.core.modules.profile.TransientProfile.table "ansys.aedt.core.modules.profile.TransientProfile.table")([columns])  | Return a summary of profile step metrics.  |  
| --- | --- |  
| [`TransientProfile.time_step_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_step_keys.html#ansys.aedt.core.modules.profile.TransientProfile.time_step_keys "ansys.aedt.core.modules.profile.TransientProfile.time_step_keys")(max_time)  | Return time-step labels up to a limit.  |  
Attributes  
| [`TransientProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.cpu_time.html#ansys.aedt.core.modules.profile.TransientProfile.cpu_time "ansys.aedt.core.modules.profile.TransientProfile.cpu_time")  | CPU time for this step.  |  
| --- | --- |  
| [`TransientProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_memory.html#ansys.aedt.core.modules.profile.TransientProfile.max_memory "ansys.aedt.core.modules.profile.TransientProfile.max_memory")  | Maximum memory over this step and all descendants.  |  
| [`TransientProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.max_time.html#ansys.aedt.core.modules.profile.TransientProfile.max_time "ansys.aedt.core.modules.profile.TransientProfile.max_time")  | Largest time step in seconds, if any.  |  
| [`TransientProfile.process_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.process_steps.html#ansys.aedt.core.modules.profile.TransientProfile.process_steps "ansys.aedt.core.modules.profile.TransientProfile.process_steps")  | Names of nested process steps, if any.  |  
| [`TransientProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.public_dir.html#ansys.aedt.core.modules.profile.TransientProfile.public_dir "ansys.aedt.core.modules.profile.TransientProfile.public_dir")  | Shortcut for dir(self).  |  
| [`TransientProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.real_time.html#ansys.aedt.core.modules.profile.TransientProfile.real_time "ansys.aedt.core.modules.profile.TransientProfile.real_time")  | Real time for this step.  |  
| [`TransientProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.time_steps.html#ansys.aedt.core.modules.profile.TransientProfile.time_steps "ansys.aedt.core.modules.profile.TransientProfile.time_steps")  | Retrieve time steps.  |