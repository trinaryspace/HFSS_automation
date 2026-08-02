---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_links_from_dictionaries.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_links_from_dictionaries 

NetworkObject.add_links_from_dictionaries(_connections : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**connections**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary or list of dictionaries containing the links between nodes. Each dictionary consists of these elements:
  * 

`"Link"`: a three-item list consisting of the two nodes that the link is connecting and
    
the value with unit of the link. The node of the connection can be referred to with the name (str) or face ID (int). The link type (resistance, heat transfer coefficient, or mass flow) is determined automatically from the unit.
  * `"Name"` (optional): a string specifying the name of the link.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> [network.add_face_node(faces_ids[i]) for i in range(2)]
>>> connection = {"Name": "LinkTest", "Link": [faces_ids[1], faces_ids[0], "1cel_per_w"]}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard
# add_links_from_dictionaries 

NetworkObject.add_links_from_dictionaries(_connections : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**connections**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary or list of dictionaries containing the links between nodes. Each dictionary consists of these elements:
  * 

`"Link"`: a three-item list consisting of the two nodes that the link is connecting and
    
the value with unit of the link. The node of the connection can be referred to with the name (str) or face ID (int). The link type (resistance, heat transfer coefficient, or mass flow) is determined automatically from the unit.
  * `"Name"` (optional): a string specifying the name of the link.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> [network.add_face_node(faces_ids[i]) for i in range(2)]
>>> connection = {"Name": "LinkTest", "Link": [faces_ids[1], faces_ids[0], "1cel_per_w"]}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_links_from_dictionaries.rst.txt)

# add_links_from_dictionaries 

NetworkObject.add_links_from_dictionaries(_connections : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create links in the network object. 

Parameters: 
     

**connections**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary or list of dictionaries containing the links between nodes. Each dictionary consists of these elements:
  * 

`"Link"`: a three-item list consisting of the two nodes that the link is connecting and
    
the value with unit of the link. The node of the connection can be referred to with the name (str) or face ID (int). The link type (resistance, heat transfer coefficient, or mass flow) is determined automatically from the unit.
  * `"Name"` (optional): a string specifying the name of the link.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> [network.add_face_node(faces_ids[i]) for i in range(2)]
>>> connection = {"Name": "LinkTest", "Link": [faces_ids[1], faces_ids[0], "1cel_per_w"]}
>>> network.add_links_from_dictionaries(connection)

```
Copy to clipboard