---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.add_operation.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_operation 

Matrix.add_operation(_operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D")_, _source_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _new_net_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_source_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_sink_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new operation to existing matrix. 

Parameters: 
     

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") 
    
Operation to perform 

**source_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List or str containing the content of the matrix reduction (eg. source name). 

**new_net_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new net. The default is `None`. 

**new_source_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new source. The default is `None`. 

**new_sink_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new sink. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core.modules.boundary.q3d_boundary import Matrix
>>> obj = Matrix()
>>> obj.add_operation(operation_type=1)

```
Copy to clipboard
# add_operation 

Matrix.add_operation(_operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D")_, _source_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _new_net_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_source_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_sink_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new operation to existing matrix. 

Parameters: 
     

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") 
    
Operation to perform 

**source_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List or str containing the content of the matrix reduction (eg. source name). 

**new_net_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new net. The default is `None`. 

**new_source_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new source. The default is `None`. 

**new_sink_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new sink. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core.modules.boundary.q3d_boundary import Matrix
>>> obj = Matrix()
>>> obj.add_operation(operation_type=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.add_operation.rst.txt)

# add_operation 

Matrix.add_operation(_operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D")_, _source_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _new_net_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_source_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _new_sink_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new operation to existing matrix. 

Parameters: 
     

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") 
    
Operation to perform 

**source_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List or str containing the content of the matrix reduction (eg. source name). 

**new_net_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new net. The default is `None`. 

**new_source_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new source. The default is `None`. 

**new_sink_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new sink. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core.modules.boundary.q3d_boundary import Matrix
>>> obj = Matrix()
>>> obj.add_operation(operation_type=1)

```
Copy to clipboard