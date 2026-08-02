---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_parametric_results.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# export_parametric_results 

Hfss3dLayout.export_parametric_results(_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _export_units : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a list of all parametric variations solved for a sweep to a CSV file. 

Parameters: 
     

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the optimetrics sweep. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the CSV file to export the results to. 

**export_units**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export units with the value. The default is `True`. When `False`, only the value is exported. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportParametricResults

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.export_parametric_results("ParametricSetup1", "results.csv")

```
Copy to clipboard
# export_parametric_results 

Hfss3dLayout.export_parametric_results(_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _export_units : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a list of all parametric variations solved for a sweep to a CSV file. 

Parameters: 
     

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the optimetrics sweep. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the CSV file to export the results to. 

**export_units**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export units with the value. The default is `True`. When `False`, only the value is exported. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportParametricResults

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.export_parametric_results("ParametricSetup1", "results.csv")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_parametric_results.rst.txt)

# export_parametric_results 

Hfss3dLayout.export_parametric_results(_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _export_units : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a list of all parametric variations solved for a sweep to a CSV file. 

Parameters: 
     

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the optimetrics sweep. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the CSV file to export the results to. 

**export_units**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export units with the value. The default is `True`. When `False`, only the value is exported. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportParametricResults

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.export_parametric_results("ParametricSetup1", "results.csv")

```
Copy to clipboard