---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.update_trace_in_report.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# update_trace_in_report 

FarField.update_trace_in_report(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update a trace in a specific report. 

Parameters: 
     

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to add. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variations. The default is `None`. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of solution context. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.update_trace_in_report(["Trace1", "Trace2"], setup_name="Setup1 : LastAdaptive")

```
Copy to clipboard
# update_trace_in_report 

FarField.update_trace_in_report(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update a trace in a specific report. 

Parameters: 
     

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to add. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variations. The default is `None`. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of solution context. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.update_trace_in_report(["Trace1", "Trace2"], setup_name="Setup1 : LastAdaptive")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.update_trace_in_report.rst.txt)

# update_trace_in_report 

FarField.update_trace_in_report(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update a trace in a specific report. 

Parameters: 
     

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to add. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variations. The default is `None`. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of solution context. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.update_trace_in_report(["Trace1", "Trace2"], setup_name="Setup1 : LastAdaptive")

```
Copy to clipboard