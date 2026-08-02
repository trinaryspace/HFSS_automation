---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_priorities 

IcepakMesh.assign_priorities(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set objects priorities. 

Parameters: 
     

**assignment**`List`[`List`[`Union`[`Object3d`, `UserDefinedComponent`, [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
List of lists of objects. Each list corresponds to one priority level from low to high. This means that the first list has the lowest priority while the last list has the highest priority. Objects not explicitly passed in the lists are assigned to a priority level lower than the objects in the first list. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, “False” when failed.
References

```
>>> oEditor.UpdatePriorityList

```
Copy to clipboard
Examples

```
>>> ipk.mesh.assign_priorities([["Box1", "Rectangle1"], ["Box2", "Fan1_1"], ["Heatsink1_1"]])

```
Copy to clipboard
# assign_priorities 

IcepakMesh.assign_priorities(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set objects priorities. 

Parameters: 
     

**assignment**`List`[`List`[`Union`[`Object3d`, `UserDefinedComponent`, [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
List of lists of objects. Each list corresponds to one priority level from low to high. This means that the first list has the lowest priority while the last list has the highest priority. Objects not explicitly passed in the lists are assigned to a priority level lower than the objects in the first list. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, “False” when failed.
References

```
>>> oEditor.UpdatePriorityList

```
Copy to clipboard
Examples

```
>>> ipk.mesh.assign_priorities([["Box1", "Rectangle1"], ["Box2", "Fan1_1"], ["Heatsink1_1"]])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities.rst.txt)

# assign_priorities 

IcepakMesh.assign_priorities(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set objects priorities. 

Parameters: 
     

**assignment**`List`[`List`[`Union`[`Object3d`, `UserDefinedComponent`, [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
List of lists of objects. Each list corresponds to one priority level from low to high. This means that the first list has the lowest priority while the last list has the highest priority. Objects not explicitly passed in the lists are assigned to a priority level lower than the objects in the first list. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, “False” when failed.
References

```
>>> oEditor.UpdatePriorityList

```
Copy to clipboard
Examples

```
>>> ipk.mesh.assign_priorities([["Box1", "Rectangle1"], ["Box2", "Fan1_1"], ["Heatsink1_1"]])

```
Copy to clipboard