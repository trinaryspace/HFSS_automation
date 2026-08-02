---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.create.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# create 

DataSet.create() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.application.variables import DataSet
>>> hfss = Hfss()
>>> dataset = DataSet(hfss, "MyCurve", [0, 1], [1, 2])
>>> dataset.create()

```
Copy to clipboard
# create 

DataSet.create() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.application.variables import DataSet
>>> hfss = Hfss()
>>> dataset = DataSet(hfss, "MyCurve", [0, 1], [1, 2])
>>> dataset.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.create.rst.txt)

# create 

DataSet.create() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a dataset. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.application.variables import DataSet
>>> hfss = Hfss()
>>> dataset = DataSet(hfss, "MyCurve", [0, 1], [1, 2])
>>> dataset.create()

```
Copy to clipboard