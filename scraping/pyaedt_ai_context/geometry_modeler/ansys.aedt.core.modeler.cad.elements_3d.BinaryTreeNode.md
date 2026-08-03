---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# BinaryTreeNode 

class ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode(_node_ , _child_object_ , _first_level : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _get_child_obj_arg =None_, _root_name =None_, _app =None_) 
    
Manages an object’s history structure.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import BinaryTreeNode
>>> obj = BinaryTreeNode()

```
Copy to clipboard
Methods  
| [`BinaryTreeNode.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| --- | --- |  
| [`BinaryTreeNode.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BinaryTreeNode.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children")  | Retrieve children.  |  
| --- | --- |  
| [`BinaryTreeNode.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command")  | Command of the modeler hystory if available.  |  
| [`BinaryTreeNode.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties")  | Properties data.  |  
# BinaryTreeNode 

class ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode(_node_ , _child_object_ , _first_level : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _get_child_obj_arg =None_, _root_name =None_, _app =None_) 
    
Manages an object’s history structure.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import BinaryTreeNode
>>> obj = BinaryTreeNode()

```
Copy to clipboard
Methods  
| [`BinaryTreeNode.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| --- | --- |  
| [`BinaryTreeNode.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BinaryTreeNode.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children")  | Retrieve children.  |  
| --- | --- |  
| [`BinaryTreeNode.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command")  | Command of the modeler hystory if available.  |  
| [`BinaryTreeNode.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties")  | Properties data.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.rst.txt)

# BinaryTreeNode 

class ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode(_node_ , _child_object_ , _first_level : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _get_child_obj_arg =None_, _root_name =None_, _app =None_) 
    
Manages an object’s history structure.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import BinaryTreeNode
>>> obj = BinaryTreeNode()

```
Copy to clipboard
Methods  
| [`BinaryTreeNode.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| --- | --- |  
| [`BinaryTreeNode.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BinaryTreeNode.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BinaryTreeNode.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.children")  | Retrieve children.  |  
| --- | --- |  
| [`BinaryTreeNode.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.command")  | Command of the modeler hystory if available.  |  
| [`BinaryTreeNode.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.properties")  | Properties data.  |