---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.submit_job.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# submit_job 

Hfss.submit_job(_cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for the license to be validated. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `*.areg` format. The default value is `None` in which case a default template will be used. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.submit_job(cluster_name="my_cluster", cores=32)

```
Copy to clipboard
# submit_job 

Hfss.submit_job(_cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for the license to be validated. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `*.areg` format. The default value is `None` in which case a default template will be used. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.submit_job(cluster_name="my_cluster", cores=32)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.submit_job.rst.txt)

# submit_job 

Hfss.submit_job(_cluster_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _aedt_full_exe_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _nodes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _cores : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 32_, _wait_for_license : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _setting_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Submit a job to be solved on a cluster. 

Parameters: 
     

**cluster_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the cluster to submit the job to. 

**aedt_full_exe_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDT executable file. The default is `None`, in which case `"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"` is used. 

**nodes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of nodes. The default is `1`. 

**cores**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of cores. The default is `32`. 

**wait_for_license**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to wait for the license to be validated. The default is `True`. 

**setting_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Job settings file. The file has the `*.areg` format. The default value is `None` in which case a default template will be used. 

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
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.submit_job(cluster_name="my_cluster", cores=32)

```
Copy to clipboard