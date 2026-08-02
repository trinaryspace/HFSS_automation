---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.select_scheduler.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# select_scheduler 

Desktop.select_scheduler(_scheduler_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _address : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _username : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _force_password_entry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Select a scheduler to submit the job. 

Parameters: 
     

**scheduler_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the scheduler. Options are `"RSM"`, `"Windows HPC"`, `"HPC Platform Services"`, `"Remote RSM"`, and `"Ansys Cloud Burst Compute"`. 

**address**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String specifying the IP address or hostname of the head node or for the remote host running the RSM service. 

**username**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Username string to use for remote RSM service (or blank to use username stored in current submission host user settings). If the (non-blank) username doesn’t match the username stored in current submission host user settings, then the Select Scheduler dialog is displayed to allow for password entry prior to job submission. 

**force_password_entry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Boolean used to force display of the Select Scheduler GUI to allow for
    
password entry prior to job submission. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The selected scheduler (if selection was successful, this string should match the input option string, although it could differ in upper/lowercase).
Examples

```
>>> from ansys.aedt.core import Desktop

```
Copy to clipboard

```
>>> d = Desktop(version="2026.1", new_desktop=False)
>>> d.select_scheduler("HPC Platform Services", address="https://myserver.com:8443/hps/")
>>> job_id = d.submit_job("via_gsg.aedt")
>>> d.release_desktop(False, False)

```
Copy to clipboard
# select_scheduler 

Desktop.select_scheduler(_scheduler_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _address : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _username : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _force_password_entry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Select a scheduler to submit the job. 

Parameters: 
     

**scheduler_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the scheduler. Options are `"RSM"`, `"Windows HPC"`, `"HPC Platform Services"`, `"Remote RSM"`, and `"Ansys Cloud Burst Compute"`. 

**address**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String specifying the IP address or hostname of the head node or for the remote host running the RSM service. 

**username**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Username string to use for remote RSM service (or blank to use username stored in current submission host user settings). If the (non-blank) username doesn’t match the username stored in current submission host user settings, then the Select Scheduler dialog is displayed to allow for password entry prior to job submission. 

**force_password_entry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Boolean used to force display of the Select Scheduler GUI to allow for
    
password entry prior to job submission. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The selected scheduler (if selection was successful, this string should match the input option string, although it could differ in upper/lowercase).
Examples

```
>>> from ansys.aedt.core import Desktop

```
Copy to clipboard

```
>>> d = Desktop(version="2026.1", new_desktop=False)
>>> d.select_scheduler("HPC Platform Services", address="https://myserver.com:8443/hps/")
>>> job_id = d.submit_job("via_gsg.aedt")
>>> d.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.select_scheduler.rst.txt)

# select_scheduler 

Desktop.select_scheduler(_scheduler_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _address : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _username : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _force_password_entry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Select a scheduler to submit the job. 

Parameters: 
     

**scheduler_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the scheduler. Options are `"RSM"`, `"Windows HPC"`, `"HPC Platform Services"`, `"Remote RSM"`, and `"Ansys Cloud Burst Compute"`. 

**address**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String specifying the IP address or hostname of the head node or for the remote host running the RSM service. 

**username**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Username string to use for remote RSM service (or blank to use username stored in current submission host user settings). If the (non-blank) username doesn’t match the username stored in current submission host user settings, then the Select Scheduler dialog is displayed to allow for password entry prior to job submission. 

**force_password_entry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Boolean used to force display of the Select Scheduler GUI to allow for
    
password entry prior to job submission. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The selected scheduler (if selection was successful, this string should match the input option string, although it could differ in upper/lowercase).
Examples

```
>>> from ansys.aedt.core import Desktop

```
Copy to clipboard

```
>>> d = Desktop(version="2026.1", new_desktop=False)
>>> d.select_scheduler("HPC Platform Services", address="https://myserver.com:8443/hps/")
>>> job_id = d.submit_job("via_gsg.aedt")
>>> d.release_desktop(False, False)

```
Copy to clipboard