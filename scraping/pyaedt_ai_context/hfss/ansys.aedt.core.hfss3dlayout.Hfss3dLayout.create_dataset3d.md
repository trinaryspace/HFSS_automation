---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_dataset3d.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_dataset3d 

Hfss3dLayout.create_dataset3d(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _z_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _v_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a 3D dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**z_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**v_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
Dataset object when the dataset is created, `False` otherwise.
References

```
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset3d("dataset3d", [0, 1], [0, 1], [0, 1], [1, 2], x_unit="mm")

```
Copy to clipboard
# create_dataset3d 

Hfss3dLayout.create_dataset3d(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _z_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _v_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a 3D dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**z_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**v_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
Dataset object when the dataset is created, `False` otherwise.
References

```
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset3d("dataset3d", [0, 1], [0, 1], [0, 1], [1, 2], x_unit="mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_dataset3d.rst.txt)

# create_dataset3d 

Hfss3dLayout.create_dataset3d(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _z_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _v_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Create a 3D dataset. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the dataset (without a prefix for a project dataset). 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**z_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**v_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
Dataset object when the dataset is created, `False` otherwise.
References

```
>>> oDesign.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.create_dataset3d("dataset3d", [0, 1], [0, 1], [0, 1], [1, 2], x_unit="mm")

```
Copy to clipboard