---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_boundary_node.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_boundary_node 

NetworkObject.add_boundary_node(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a boundary node to the network. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the node. 

**assignment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type assignment. Options are `"Power"` and `"Temperature"`. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
String, float, or dictionary containing the value of the assignment. If a float is passed the `"W"` or `"cel"` unit is used, depending on the selection for the `assignment_type` parameter. If `"Power"` is selected for the type, a dictionary can be passed to use temperature-dependent or transient assignment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> network.add_boundary_node("TestNode", "Temperature", 2)
>>> ds = app.create_dataset1d_design("Test_DataSet", [1, 2, 3], [3, 4, 5])
>>> network.add_boundary_node("TestNode", "Power", {"Type": "Temp Dep",
>>>                                                       "Function": "Piecewise Linear",
>>>                                                       "Values": "Test_DataSet"})

```
Copy to clipboard
# add_boundary_node 

NetworkObject.add_boundary_node(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a boundary node to the network. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the node. 

**assignment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type assignment. Options are `"Power"` and `"Temperature"`. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
String, float, or dictionary containing the value of the assignment. If a float is passed the `"W"` or `"cel"` unit is used, depending on the selection for the `assignment_type` parameter. If `"Power"` is selected for the type, a dictionary can be passed to use temperature-dependent or transient assignment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> network.add_boundary_node("TestNode", "Temperature", 2)
>>> ds = app.create_dataset1d_design("Test_DataSet", [1, 2, 3], [3, 4, 5])
>>> network.add_boundary_node("TestNode", "Power", {"Type": "Temp Dep",
>>>                                                       "Function": "Piecewise Linear",
>>>                                                       "Values": "Test_DataSet"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_boundary_node.rst.txt)

# add_boundary_node 

NetworkObject.add_boundary_node(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a boundary node to the network. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the node. 

**assignment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type assignment. Options are `"Power"` and `"Temperature"`. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
String, float, or dictionary containing the value of the assignment. If a float is passed the `"W"` or `"cel"` unit is used, depending on the selection for the `assignment_type` parameter. If `"Power"` is selected for the type, a dictionary can be passed to use temperature-dependent or transient assignment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> network.add_boundary_node("TestNode", "Temperature", 2)
>>> ds = app.create_dataset1d_design("Test_DataSet", [1, 2, 3], [3, 4, 5])
>>> network.add_boundary_node("TestNode", "Power", {"Type": "Temp Dep",
>>>                                                       "Function": "Piecewise Linear",
>>>                                                       "Values": "Test_DataSet"})

```
Copy to clipboard