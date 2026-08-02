---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_index.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# remove_point_from_index 

DataSet.remove_point_from_index(_id_to_remove : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an index. 

Parameters: 
     

**id_to_remove**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the index. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.EditDataset
>>> oDesign.EditDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.remove_point_from_index(0)

```
Copy to clipboard
# remove_point_from_index 

DataSet.remove_point_from_index(_id_to_remove : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an index. 

Parameters: 
     

**id_to_remove**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the index. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.EditDataset
>>> oDesign.EditDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.remove_point_from_index(0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_index.rst.txt)

# remove_point_from_index 

DataSet.remove_point_from_index(_id_to_remove : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an index. 

Parameters: 
     

**id_to_remove**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the index. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.EditDataset
>>> oDesign.EditDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.remove_point_from_index(0)

```
Copy to clipboard