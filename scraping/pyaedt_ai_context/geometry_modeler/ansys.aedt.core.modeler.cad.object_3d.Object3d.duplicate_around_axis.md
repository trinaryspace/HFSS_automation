---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.duplicate_around_axis.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_around_axis 

Object3d.duplicate_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Duplicate the object around the axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard
# duplicate_around_axis 

Object3d.duplicate_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Duplicate the object around the axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.duplicate_around_axis.rst.txt)

# duplicate_around_axis 

Object3d.duplicate_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Duplicate the object around the axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard