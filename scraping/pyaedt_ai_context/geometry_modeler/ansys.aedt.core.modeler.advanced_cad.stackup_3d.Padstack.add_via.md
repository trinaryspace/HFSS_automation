---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_via 

Padstack.add_via(_position_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _position_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _instance_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Insert a new via on this padstack. 

Parameters: 
     

**position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center x position. The default is `0`. 

**position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center y position. The default is `0`. 

**instance_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Via name. The default is `None`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use an existing reference system or create a new one. The default is `None`, in which case a new reference system is created. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object created.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()
>>> obj.add_via(position_x=1.0, position_y=1.0)

```
Copy to clipboard
# add_via 

Padstack.add_via(_position_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _position_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _instance_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Insert a new via on this padstack. 

Parameters: 
     

**position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center x position. The default is `0`. 

**position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center y position. The default is `0`. 

**instance_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Via name. The default is `None`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use an existing reference system or create a new one. The default is `None`, in which case a new reference system is created. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object created.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()
>>> obj.add_via(position_x=1.0, position_y=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Padstack.add_via.rst.txt)

# add_via 

Padstack.add_via(_position_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _position_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _instance_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _reference_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Insert a new via on this padstack. 

Parameters: 
     

**position_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center x position. The default is `0`. 

**position_y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center y position. The default is `0`. 

**instance_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Via name. The default is `None`. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use an existing reference system or create a new one. The default is `None`, in which case a new reference system is created. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object created.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Padstack
>>> obj = Padstack()
>>> obj.add_via(position_x=1.0, position_y=1.0)

```
Copy to clipboard