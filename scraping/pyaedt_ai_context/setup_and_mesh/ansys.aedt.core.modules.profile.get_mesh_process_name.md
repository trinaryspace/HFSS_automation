---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.get_mesh_process_name.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# get_mesh_process_name 

ansys.aedt.core.modules.profile.get_mesh_process_name(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Return the name of the meshing process group if present. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
    
Simulation group node. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
     

`"Initial Meshing Group"`, `or` `"Meshing Process Group"` `when` `present`, `otherwise` `None`.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import get_mesh_process_name
>>> get_mesh_process_name(group_data=1)

```
Copy to clipboard
# get_mesh_process_name 

ansys.aedt.core.modules.profile.get_mesh_process_name(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Return the name of the meshing process group if present. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
    
Simulation group node. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
     

`"Initial Meshing Group"`, `or` `"Meshing Process Group"` `when` `present`, `otherwise` `None`.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import get_mesh_process_name
>>> get_mesh_process_name(group_data=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.get_mesh_process_name.rst.txt)

# get_mesh_process_name 

ansys.aedt.core.modules.profile.get_mesh_process_name(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Return the name of the meshing process group if present. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
    
Simulation group node. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
     

`"Initial Meshing Group"`, `or` `"Meshing Process Group"` `when` `present`, `otherwise` `None`.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import get_mesh_process_name
>>> get_mesh_process_name(group_data=1)

```
Copy to clipboard