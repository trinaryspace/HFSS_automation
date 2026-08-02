---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.import_dataset1d.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# import_dataset1d 

Hfss3dLayout.import_dataset1d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 1D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the TAB file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

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
>>> app.import_dataset1d(r"C:\temp\dataset.csv")

```
Copy to clipboard
# import_dataset1d 

Hfss3dLayout.import_dataset1d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 1D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the TAB file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

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
>>> app.import_dataset1d(r"C:\temp\dataset.csv")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.import_dataset1d.rst.txt)

# import_dataset1d 

Hfss3dLayout.import_dataset1d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 1D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the TAB file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

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
>>> app.import_dataset1d(r"C:\temp\dataset.csv")

```
Copy to clipboard