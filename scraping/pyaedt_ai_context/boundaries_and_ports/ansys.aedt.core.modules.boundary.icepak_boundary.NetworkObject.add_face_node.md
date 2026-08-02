---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_face_node.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# add_face_node 

NetworkObject.add_face_node(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thermal_resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NoResistance'_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face node in the network. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Face ID. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the node. Default is `None`. 

**thermal_resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Thermal resistance value and unit. Default is `"NoResistance"`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material specification (required if `thermal_resistance="Compute"`). Default is `None`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value and unit (required if `thermal_resistance="Compute"`). If a float is passed, `"mm"` unit is automatically used. Default is `None`. 

**resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value and unit (required if `thermal_resistance="Specified"`). If a float is passed, `"cel_per_w"` unit is automatically used. Default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> network.add_face_node(faces_ids[0])
>>> network.add_face_node(
...     faces_ids[1], name="TestNode", thermal_resistance="Compute", material="Al-Extruded", thickness="2mm"
... )
>>> network.add_face_node(faces_ids[2], name="TestNode", thermal_resistance="Specified", resistance=2)

```
Copy to clipboard
# add_face_node 

NetworkObject.add_face_node(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thermal_resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NoResistance'_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face node in the network. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Face ID. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the node. Default is `None`. 

**thermal_resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Thermal resistance value and unit. Default is `"NoResistance"`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material specification (required if `thermal_resistance="Compute"`). Default is `None`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value and unit (required if `thermal_resistance="Compute"`). If a float is passed, `"mm"` unit is automatically used. Default is `None`. 

**resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value and unit (required if `thermal_resistance="Specified"`). If a float is passed, `"cel_per_w"` unit is automatically used. Default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> network.add_face_node(faces_ids[0])
>>> network.add_face_node(
...     faces_ids[1], name="TestNode", thermal_resistance="Compute", material="Al-Extruded", thickness="2mm"
... )
>>> network.add_face_node(faces_ids[2], name="TestNode", thermal_resistance="Specified", resistance=2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.add_face_node.rst.txt)

# add_face_node 

NetworkObject.add_face_node(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thermal_resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NoResistance'_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _resistance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face node in the network. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Face ID. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the node. Default is `None`. 

**thermal_resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Thermal resistance value and unit. Default is `"NoResistance"`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material specification (required if `thermal_resistance="Compute"`). Default is `None`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value and unit (required if `thermal_resistance="Compute"`). If a float is passed, `"mm"` unit is automatically used. Default is `None`. 

**resistance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value and unit (required if `thermal_resistance="Specified"`). If a float is passed, `"cel_per_w"` unit is automatically used. Default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if successful.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> network = ansys.aedt.core.modules.boundary.Network(app)
>>> box = app.modeler.create_box([5, 5, 5], [20, 50, 80])
>>> faces_ids = [face.id for face in box.faces]
>>> network.add_face_node(faces_ids[0])
>>> network.add_face_node(
...     faces_ids[1], name="TestNode", thermal_resistance="Compute", material="Al-Extruded", thickness="2mm"
... )
>>> network.add_face_node(faces_ids[2], name="TestNode", thermal_resistance="Specified", resistance=2)

```
Copy to clipboard