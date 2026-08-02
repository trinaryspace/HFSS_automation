---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_dataset1d_design.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_dataset1d_design 

Hfss3dLayout.create_dataset1d_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a design dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset1d_design("curve1", [0, 1, 2], [10, 20, 30], x_unit="GHz")

```
Copy to clipboard
# create_dataset1d_design 

Hfss3dLayout.create_dataset1d_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a design dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset1d_design("curve1", [0, 1, 2], [10, 20, 30], x_unit="GHz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_dataset1d_design.rst.txt)

# create_dataset1d_design 

Hfss3dLayout.create_dataset1d_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a design dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset1d_design("curve1", [0, 1, 2], [10, 20, 30], x_unit="GHz")

```
Copy to clipboard