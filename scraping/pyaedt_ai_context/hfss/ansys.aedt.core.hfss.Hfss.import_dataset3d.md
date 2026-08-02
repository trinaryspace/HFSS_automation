---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_dataset3d.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# import_dataset3d 

Hfss.import_dataset3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8-sig'_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 3D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the tab/csv/xlsx file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding to be provided for csv. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.import_dataset3d(r"C:\temp\dataset.tab")

```
Copy to clipboard
# import_dataset3d 

Hfss.import_dataset3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8-sig'_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 3D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the tab/csv/xlsx file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding to be provided for csv. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.import_dataset3d(r"C:\temp\dataset.tab")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_dataset3d.rst.txt)

# import_dataset3d 

Hfss.import_dataset3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8-sig'_, _is_project_dataset : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [DataSet](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet") 
    
Import a 3D dataset. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the tab/csv/xlsx file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the dataset. The default is the file name. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding to be provided for csv. 

**is_project_dataset**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether it is a project data set. The default is `True`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.application.variables.DataSet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html#ansys.aedt.core.application.variables.DataSet "ansys.aedt.core.application.variables.DataSet")
    
References

```
>>> oProject.AddDataset

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.import_dataset3d(r"C:\temp\dataset.tab")

```
Copy to clipboard