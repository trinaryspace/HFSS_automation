---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_summary.FieldSummary.get_field_summary_data.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_field_summary_data 

FieldSummary.get_field_summary_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _pandas_output : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Get field summary output computation. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use for the computation. The default is `None`, in which case the nominal variation is used. 

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing the design variation to use for the computation. The default is `{}`, in which case nominal variation is used. 

**intrinsics**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic values to use for the computation. The default is `""`, which is suitable when no frequency needs to be selected. 

**pandas_output**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use pandas output. The default is `False`, in which case the dictionary output is used. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") 
    
Output type depending on the Boolean `pandas_output` parameter. The output consists of information exported from the field summary.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.get_field_summary_data(setup="Setup1", variation={"Name": "Value"})

```
Copy to clipboard
# get_field_summary_data 

FieldSummary.get_field_summary_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _pandas_output : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Get field summary output computation. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use for the computation. The default is `None`, in which case the nominal variation is used. 

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing the design variation to use for the computation. The default is `{}`, in which case nominal variation is used. 

**intrinsics**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic values to use for the computation. The default is `""`, which is suitable when no frequency needs to be selected. 

**pandas_output**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use pandas output. The default is `False`, in which case the dictionary output is used. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") 
    
Output type depending on the Boolean `pandas_output` parameter. The output consists of information exported from the field summary.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.get_field_summary_data(setup="Setup1", variation={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_summary.FieldSummary.get_field_summary_data.rst.txt)

# get_field_summary_data 

FieldSummary.get_field_summary_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _pandas_output : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Get field summary output computation. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use for the computation. The default is `None`, in which case the nominal variation is used. 

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing the design variation to use for the computation. The default is `{}`, in which case nominal variation is used. 

**intrinsics**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic values to use for the computation. The default is `""`, which is suitable when no frequency needs to be selected. 

**pandas_output**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use pandas output. The default is `False`, in which case the dictionary output is used. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") 
    
Output type depending on the Boolean `pandas_output` parameter. The output consists of information exported from the field summary.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_summary import FieldSummary
>>> obj = FieldSummary()
>>> obj.get_field_summary_data(setup="Setup1", variation={"Name": "Value"})

```
Copy to clipboard