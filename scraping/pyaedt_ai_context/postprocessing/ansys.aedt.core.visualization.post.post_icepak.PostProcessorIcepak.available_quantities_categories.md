---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.available_quantities_categories.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# available_quantities_categories 

PostProcessorIcepak.available_quantities_categories(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report categories. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
     

Report display type. The default is `None`, in which case the first default type
    
is used. In most cases, this default type is `"Rectangular Plot"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default context is used. For Maxwell 2D/3D eddy current solution types, the report category can be provided as a dictionary, where the key is the matrix name and the value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the setup is SIwave DCIR. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllCategories

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_quantities_categories()

```
Copy to clipboard
# available_quantities_categories 

PostProcessorIcepak.available_quantities_categories(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report categories. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
     

Report display type. The default is `None`, in which case the first default type
    
is used. In most cases, this default type is `"Rectangular Plot"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default context is used. For Maxwell 2D/3D eddy current solution types, the report category can be provided as a dictionary, where the key is the matrix name and the value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the setup is SIwave DCIR. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllCategories

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_quantities_categories()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.available_quantities_categories.rst.txt)

# available_quantities_categories 

PostProcessorIcepak.available_quantities_categories(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report categories. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
     

Report display type. The default is `None`, in which case the first default type
    
is used. In most cases, this default type is `"Rectangular Plot"`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report category. The default is `None`, in which case the first default context is used. For Maxwell 2D/3D eddy current solution types, the report category can be provided as a dictionary, where the key is the matrix name and the value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the setup is SIwave DCIR. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllCategories

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.available_quantities_categories()

```
Copy to clipboard