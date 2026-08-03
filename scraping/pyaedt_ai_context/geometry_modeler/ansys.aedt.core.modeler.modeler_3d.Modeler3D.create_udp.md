---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_udp.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_udp 

Modeler3D.create_udp(_dll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a user-defined primitive (UDP). 

Parameters: 
     

**dll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the UDP DLL or Python file. The default for the file format is `".dll"`. 

**parameters**
    
List of the UDP parameters. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the UDP library. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
UDP object created.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> my_udp = self.aedtapp.modeler.create_udp(
...     dll="RMxprt/ClawPoleCore", parameters=my_udpPairs, library="syslib"
... )
<class 'ansys.aedt.core.modeler.cad.object_3d.Object3d'>

```
Copy to clipboard
# create_udp 

Modeler3D.create_udp(_dll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a user-defined primitive (UDP). 

Parameters: 
     

**dll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the UDP DLL or Python file. The default for the file format is `".dll"`. 

**parameters**
    
List of the UDP parameters. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the UDP library. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
UDP object created.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> my_udp = self.aedtapp.modeler.create_udp(
...     dll="RMxprt/ClawPoleCore", parameters=my_udpPairs, library="syslib"
... )
<class 'ansys.aedt.core.modeler.cad.object_3d.Object3d'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_udp.rst.txt)

# create_udp 

Modeler3D.create_udp(_dll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a user-defined primitive (UDP). 

Parameters: 
     

**dll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the UDP DLL or Python file. The default for the file format is `".dll"`. 

**parameters**
    
List of the UDP parameters. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the UDP library. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
UDP object created.
References

```
>>> oEditor.CreateUserDefinedPart

```
Copy to clipboard
Examples

```
>>> my_udp = self.aedtapp.modeler.create_udp(
...     dll="RMxprt/ClawPoleCore", parameters=my_udpPairs, library="syslib"
... )
<class 'ansys.aedt.core.modeler.cad.object_3d.Object3d'>

```
Copy to clipboard