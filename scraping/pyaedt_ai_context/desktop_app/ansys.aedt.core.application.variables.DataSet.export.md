---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.export.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# export 

DataSet.export(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the dataset. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to export the dataset to. The default is `None`, in which case the dataset is exported to the working_directory path. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ExportDataset
>>> oDesign.ExportDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard
# export 

DataSet.export(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the dataset. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to export the dataset to. The default is `None`, in which case the dataset is exported to the working_directory path. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ExportDataset
>>> oDesign.ExportDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.export.rst.txt)

# export 

DataSet.export(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the dataset. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to export the dataset to. The default is `None`, in which case the dataset is exported to the working_directory path. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ExportDataset
>>> oDesign.ExportDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard