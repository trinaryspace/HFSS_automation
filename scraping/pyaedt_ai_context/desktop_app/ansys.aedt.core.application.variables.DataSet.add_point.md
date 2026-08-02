---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.add_point.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# add_point 

DataSet.add_point(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _v : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a point to the dataset. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X coordinate of the point. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y coordinate of the point. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**v**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

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
>>> dataset.add_point(2, 3)

```
Copy to clipboard
# add_point 

DataSet.add_point(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _v : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a point to the dataset. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X coordinate of the point. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y coordinate of the point. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**v**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

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
>>> dataset.add_point(2, 3)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.add_point.rst.txt)

# add_point 

DataSet.add_point(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _v : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a point to the dataset. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X coordinate of the point. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y coordinate of the point. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**v**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

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
>>> dataset.add_point(2, 3)

```
Copy to clipboard