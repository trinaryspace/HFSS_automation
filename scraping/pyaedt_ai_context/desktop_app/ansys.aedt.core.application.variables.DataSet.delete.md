---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.delete.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# delete 

DataSet.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.DeleteDataset
>>> oDesign.DeleteDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.delete()

```
Copy to clipboard
# delete 

DataSet.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.DeleteDataset
>>> oDesign.DeleteDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.delete()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.delete.rst.txt)

# delete 

DataSet.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.DeleteDataset
>>> oDesign.DeleteDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.delete()

```
Copy to clipboard