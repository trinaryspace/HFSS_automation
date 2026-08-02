---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launch_job_monitor.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# launch_job_monitor 

Desktop.launch_job_monitor(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Launch job monitor. This method is opening the job monitor tool. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesktop.LaunchJobMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.launch_job_monitor(input_file=r"C:\Projects\MyProject.aedt")

```
Copy to clipboard
# launch_job_monitor 

Desktop.launch_job_monitor(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Launch job monitor. This method is opening the job monitor tool. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesktop.LaunchJobMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.launch_job_monitor(input_file=r"C:\Projects\MyProject.aedt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.launch_job_monitor.rst.txt)

# launch_job_monitor 

Desktop.launch_job_monitor(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Launch job monitor. This method is opening the job monitor tool. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesktop.LaunchJobMonitor

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.launch_job_monitor(input_file=r"C:\Projects\MyProject.aedt")

```
Copy to clipboard