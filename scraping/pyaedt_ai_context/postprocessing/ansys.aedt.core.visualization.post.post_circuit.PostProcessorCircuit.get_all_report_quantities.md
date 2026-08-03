---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.get_all_report_quantities.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_all_report_quantities 

PostProcessorCircuit.get_all_report_quantities(_solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Return all the possible report categories organized by report types, solution and categories. 

Parameters: 
     

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Solution to get the report quantities. The default is `None`, in which case the all solutions are used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
A dictionary with primary key the report type, secondary key the solution type and third key the report categories.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_all_report_quantities()

```
Copy to clipboard
# get_all_report_quantities 

PostProcessorCircuit.get_all_report_quantities(_solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Return all the possible report categories organized by report types, solution and categories. 

Parameters: 
     

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Solution to get the report quantities. The default is `None`, in which case the all solutions are used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
A dictionary with primary key the report type, secondary key the solution type and third key the report categories.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_all_report_quantities()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.get_all_report_quantities.rst.txt)

# get_all_report_quantities 

PostProcessorCircuit.get_all_report_quantities(_solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Return all the possible report categories organized by report types, solution and categories. 

Parameters: 
     

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Solution to get the report quantities. The default is `None`, in which case the all solutions are used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
A dictionary with primary key the report type, secondary key the solution type and third key the report categories.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_all_report_quantities()

```
Copy to clipboard