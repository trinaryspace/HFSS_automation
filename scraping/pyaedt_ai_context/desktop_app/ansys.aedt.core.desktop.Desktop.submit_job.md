---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.submit_job.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# submit_job 

Desktop.submit_job(_project_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**project_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file on the server. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. On linux this path should point to the Linux executable `"ansysedt"`. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for a license to become available. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `.areg` format. The default value is `None` in which case a default template will be used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the job.
References

```
>>> oDesktop.SubmitJob

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2024.2")
Use template
>>> job_id1 = desktop.submit_job(
...     project_file="my_project.aedt",
...     cluster_name="my_cluster",
...     nodes=2,
...     cores=64,
... )
>>> job_id2 = desktop.submit_job(project_file="my_project2.aedt", setting_file="my_settings_file.areg")
>>> desktop.launch_job_monitor("my_project.aedt")

```
Copy to clipboard
# submit_job 

Desktop.submit_job(_project_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**project_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file on the server. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. On linux this path should point to the Linux executable `"ansysedt"`. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for a license to become available. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `.areg` format. The default value is `None` in which case a default template will be used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the job.
References

```
>>> oDesktop.SubmitJob

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2024.2")
Use template
>>> job_id1 = desktop.submit_job(
...     project_file="my_project.aedt",
...     cluster_name="my_cluster",
...     nodes=2,
...     cores=64,
... )
>>> job_id2 = desktop.submit_job(project_file="my_project2.aedt", setting_file="my_settings_file.areg")
>>> desktop.launch_job_monitor("my_project.aedt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.submit_job.rst.txt)

# submit_job 

Desktop.submit_job(_project_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**project_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the project. 

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file on the server. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. On linux this path should point to the Linux executable `"ansysedt"`. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for a license to become available. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `.areg` format. The default value is `None` in which case a default template will be used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the job.
References

```
>>> oDesktop.SubmitJob

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2024.2")
Use template
>>> job_id1 = desktop.submit_job(
...     project_file="my_project.aedt",
...     cluster_name="my_cluster",
...     nodes=2,
...     cores=64,
... )
>>> job_id2 = desktop.submit_job(project_file="my_project2.aedt", setting_file="my_settings_file.areg")
>>> desktop.launch_job_monitor("my_project.aedt")

```
Copy to clipboard