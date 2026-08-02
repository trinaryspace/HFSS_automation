---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_nodes_from_dictionaries.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_nodes_from_dictionaries 

NetworkObject.add_nodes_from_dictionaries(_nodes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add nodes to the network from dictionary. 

Parameters: 
     

**nodes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
One node definition or a list of node definitions to add to the network.
Face-node dictionaries use `"FaceID"` and can optionally include `"Name"`, `"ThermalResistance"`, `"Thickness"`, `"Material"`, and `"Resistance"`.
Internal-node dictionaries use `"Name"` and `"Power"` and can optionally include `"Mass"` and `"SpecificHeat"`.
Boundary-node dictionaries use `"Name"` and `"ValueType"` plus either `"Power"` or `"Temperature"` depending on the selected value type.
Temperature-dependent and transient assignments are passed as dictionaries with `"Type"`, `"Function"`, and `"Values"` keys. Supported function names are `"Linear"`, `"Power Law"`, `"Exponential"`, `"Sinusoidal"`, `"Square Wave"`, and `"Piecewise Linear"`. `"Temp Dep"` supports only `"Piecewise Linear"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful. `False` otherwise.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> nodes_dict = [
>>>         {"FaceID": faces_ids[0]},
>>>         {"Name": "TestNode", "FaceID": faces_ids[1],
>>>          "ThermalResistance": "Compute", "Thickness": "2mm"},
>>>         {"FaceID": faces_ids[2], "ThermalResistance": "Specified", "Resistance": "2cel_per_w"},
>>>         {"Name": "Junction", "Power": "1W"}]
>>> network.add_nodes_from_dictionaries(nodes_dict)

```
Copy to clipboard
# add_nodes_from_dictionaries 

NetworkObject.add_nodes_from_dictionaries(_nodes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add nodes to the network from dictionary. 

Parameters: 
     

**nodes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
One node definition or a list of node definitions to add to the network.
Face-node dictionaries use `"FaceID"` and can optionally include `"Name"`, `"ThermalResistance"`, `"Thickness"`, `"Material"`, and `"Resistance"`.
Internal-node dictionaries use `"Name"` and `"Power"` and can optionally include `"Mass"` and `"SpecificHeat"`.
Boundary-node dictionaries use `"Name"` and `"ValueType"` plus either `"Power"` or `"Temperature"` depending on the selected value type.
Temperature-dependent and transient assignments are passed as dictionaries with `"Type"`, `"Function"`, and `"Values"` keys. Supported function names are `"Linear"`, `"Power Law"`, `"Exponential"`, `"Sinusoidal"`, `"Square Wave"`, and `"Piecewise Linear"`. `"Temp Dep"` supports only `"Piecewise Linear"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful. `False` otherwise.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> nodes_dict = [
>>>         {"FaceID": faces_ids[0]},
>>>         {"Name": "TestNode", "FaceID": faces_ids[1],
>>>          "ThermalResistance": "Compute", "Thickness": "2mm"},
>>>         {"FaceID": faces_ids[2], "ThermalResistance": "Specified", "Resistance": "2cel_per_w"},
>>>         {"Name": "Junction", "Power": "1W"}]
>>> network.add_nodes_from_dictionaries(nodes_dict)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_nodes_from_dictionaries.rst.txt)

# add_nodes_from_dictionaries 

NetworkObject.add_nodes_from_dictionaries(_nodes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add nodes to the network from dictionary. 

Parameters: 
     

**nodes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
One node definition or a list of node definitions to add to the network.
Face-node dictionaries use `"FaceID"` and can optionally include `"Name"`, `"ThermalResistance"`, `"Thickness"`, `"Material"`, and `"Resistance"`.
Internal-node dictionaries use `"Name"` and `"Power"` and can optionally include `"Mass"` and `"SpecificHeat"`.
Boundary-node dictionaries use `"Name"` and `"ValueType"` plus either `"Power"` or `"Temperature"` depending on the selected value type.
Temperature-dependent and transient assignments are passed as dictionaries with `"Type"`, `"Function"`, and `"Values"` keys. Supported function names are `"Linear"`, `"Power Law"`, `"Exponential"`, `"Sinusoidal"`, `"Square Wave"`, and `"Piecewise Linear"`. `"Temp Dep"` supports only `"Piecewise Linear"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful. `False` otherwise.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> nodes_dict = [
>>>         {"FaceID": faces_ids[0]},
>>>         {"Name": "TestNode", "FaceID": faces_ids[1],
>>>          "ThermalResistance": "Compute", "Thickness": "2mm"},
>>>         {"FaceID": faces_ids[2], "ThermalResistance": "Specified", "Resistance": "2cel_per_w"},
>>>         {"Name": "Junction", "Power": "1W"}]
>>> network.add_nodes_from_dictionaries(nodes_dict)

```
Copy to clipboard