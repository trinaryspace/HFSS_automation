---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_group.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_group 

Modeler3D.create_group(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _groups : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Group objects or groups into one group.
At least one between `objects`, `components`, `groups` has to be defined. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects. The default is `None`, in which case a group with all objects is created. 

**components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of 3d components to group. The default is `None`. 

**groups**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of groups. The default is `None`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new group. The default is `None`. It is not possible to choose the name but a name is assigned automatically. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name assigned to the new group.
References

```
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_group(objects=["Box1"], components=["U1"])

```
Copy to clipboard
# create_group 

Modeler3D.create_group(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _groups : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Group objects or groups into one group.
At least one between `objects`, `components`, `groups` has to be defined. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects. The default is `None`, in which case a group with all objects is created. 

**components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of 3d components to group. The default is `None`. 

**groups**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of groups. The default is `None`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new group. The default is `None`. It is not possible to choose the name but a name is assigned automatically. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name assigned to the new group.
References

```
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_group(objects=["Box1"], components=["U1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_group.rst.txt)

# create_group 

Modeler3D.create_group(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _groups : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Group objects or groups into one group.
At least one between `objects`, `components`, `groups` has to be defined. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects. The default is `None`, in which case a group with all objects is created. 

**components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of 3d components to group. The default is `None`. 

**groups**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of groups. The default is `None`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new group. The default is `None`. It is not possible to choose the name but a name is assigned automatically. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name assigned to the new group.
References

```
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_group(objects=["Box1"], components=["U1"])

```
Copy to clipboard