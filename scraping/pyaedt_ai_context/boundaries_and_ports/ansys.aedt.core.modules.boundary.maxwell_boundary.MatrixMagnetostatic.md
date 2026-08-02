---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# MatrixMagnetostatic 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic(_signal_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[SourceMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")]_, _group_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GroupSourcesMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for magnetostatic solver. 

Parameters: 
     

**signal_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")] 
    
List of signal sources. 

**group_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")] 
    
List of group sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixMagnetostatic
>>> obj = MatrixMagnetostatic()

```
Copy to clipboard
Attributes  
| [`MatrixMagnetostatic.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixMagnetostatic.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources")  | Value for signal sources.  |  
| [`MatrixMagnetostatic.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources")  | Value for group sources.  |  
# MatrixMagnetostatic 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic(_signal_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[SourceMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")]_, _group_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GroupSourcesMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for magnetostatic solver. 

Parameters: 
     

**signal_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")] 
    
List of signal sources. 

**group_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")] 
    
List of group sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixMagnetostatic
>>> obj = MatrixMagnetostatic()

```
Copy to clipboard
Attributes  
| [`MatrixMagnetostatic.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixMagnetostatic.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources")  | Value for signal sources.  |  
| [`MatrixMagnetostatic.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources")  | Value for group sources.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.rst.txt)

# MatrixMagnetostatic 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic(_signal_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[SourceMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")]_, _group_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GroupSourcesMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for magnetostatic solver. 

Parameters: 
     

**signal_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")] 
    
List of signal sources. 

**group_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")] 
    
List of group sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixMagnetostatic
>>> obj = MatrixMagnetostatic()

```
Copy to clipboard
Attributes  
| [`MatrixMagnetostatic.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixMagnetostatic.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.signal_sources")  | Value for signal sources.  |  
| [`MatrixMagnetostatic.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.group_sources")  | Value for group sources.  |