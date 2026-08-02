---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_link.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_link 

NetworkObject.add_link(_node1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _node2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**node1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added automatically. 

**node2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added atuomatically. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
String containing the value and unit of the connection. If a float is passed, an R-Link is added to the network and the `"cel_per_w"` unit is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the link. The default is `None`, in which case a name is automatically generated. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> connection = {"Name": "LinkTest", "Connection": [faces_ids[1], faces_ids[0]], "Value": "1cel_per_w"}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard
# add_link 

NetworkObject.add_link(_node1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _node2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**node1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added automatically. 

**node2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added atuomatically. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
String containing the value and unit of the connection. If a float is passed, an R-Link is added to the network and the `"cel_per_w"` unit is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the link. The default is `None`, in which case a name is automatically generated. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> connection = {"Name": "LinkTest", "Connection": [faces_ids[1], faces_ids[0]], "Value": "1cel_per_w"}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_link.rst.txt)

# add_link 

NetworkObject.add_link(_node1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _node2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**node1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added automatically. 

**node2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
String containing one of the node names that the link is connecting or an integer containing the ID of the face. If an ID is used and the node associated with the corresponding face is not created yet, it is added atuomatically. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
String containing the value and unit of the connection. If a float is passed, an R-Link is added to the network and the `"cel_per_w"` unit is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the link. The default is `None`, in which case a name is automatically generated. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> connection = {"Name": "LinkTest", "Connection": [faces_ids[1], faces_ids[0]], "Value": "1cel_per_w"}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard