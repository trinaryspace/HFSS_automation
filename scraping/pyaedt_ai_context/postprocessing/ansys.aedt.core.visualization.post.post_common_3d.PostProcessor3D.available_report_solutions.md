---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.available_report_solutions.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# available_report_solutions 

PostProcessor3D.available_report_solutions(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of available solutions that can be used for the reports.
This list differs from the one obtained with `app.existing_analysis_sweeps`, because it includes additional elements like “AdaptivePass”. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. Default is `None` which takes default category. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAvailableSolutions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_report_solutions()

```
Copy to clipboard
# available_report_solutions 

PostProcessor3D.available_report_solutions(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of available solutions that can be used for the reports.
This list differs from the one obtained with `app.existing_analysis_sweeps`, because it includes additional elements like “AdaptivePass”. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. Default is `None` which takes default category. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAvailableSolutions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_report_solutions()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.available_report_solutions.rst.txt)

# available_report_solutions 

PostProcessor3D.available_report_solutions(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of available solutions that can be used for the reports.
This list differs from the one obtained with `app.existing_analysis_sweeps`, because it includes additional elements like “AdaptivePass”. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. Default is `None` which takes default category. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAvailableSolutions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_report_solutions()

```
Copy to clipboard