---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# rotate 

UserDefinedComponent.rotate(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 90.0_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'deg'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Rotate the selection. 

Parameters: 
     

**axis**
    
Coordinate system axis or the a value of the enum [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis"). 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation. The units, defined by `unit`, can be either degrees or radians. The default is `90.0`. 

**units**`text` , `optional` 
    
Units for the angle. Options are `"deg"` or `"rad"`. The default is `"deg"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Rotate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.rotate(axis="Z")

```
Copy to clipboard
# rotate 

UserDefinedComponent.rotate(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 90.0_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'deg'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Rotate the selection. 

Parameters: 
     

**axis**
    
Coordinate system axis or the a value of the enum [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis"). 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation. The units, defined by `unit`, can be either degrees or radians. The default is `90.0`. 

**units**`text` , `optional` 
    
Units for the angle. Options are `"deg"` or `"rad"`. The default is `"deg"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Rotate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.rotate(axis="Z")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate.rst.txt)

# rotate 

UserDefinedComponent.rotate(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 90.0_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'deg'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Rotate the selection. 

Parameters: 
     

**axis**
    
Coordinate system axis or the a value of the enum [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis"). 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation. The units, defined by `unit`, can be either degrees or radians. The default is `90.0`. 

**units**`text` , `optional` 
    
Units for the angle. Options are `"deg"` or `"rad"`. The default is `"deg"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Rotate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.rotate(axis="Z")

```
Copy to clipboard