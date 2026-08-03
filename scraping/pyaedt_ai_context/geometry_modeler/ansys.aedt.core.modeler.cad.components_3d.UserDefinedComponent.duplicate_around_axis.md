---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_around_axis 

UserDefinedComponent.duplicate_around_axis(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the component around the axis. 

Parameters: 
     

**axis**`Value` `of` `the` [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") [`enum`](https://docs.python.org/3.11/library/enum.html#module-enum "\(in Python v3.11\)") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard
# duplicate_around_axis 

UserDefinedComponent.duplicate_around_axis(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the component around the axis. 

Parameters: 
     

**axis**`Value` `of` `the` [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") [`enum`](https://docs.python.org/3.11/library/enum.html#module-enum "\(in Python v3.11\)") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis.rst.txt)

# duplicate_around_axis 

UserDefinedComponent.duplicate_around_axis(_axis : [Axis](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis")_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 90_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _create_new_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the component around the axis. 

Parameters: 
     

**axis**`Value` `of` `the` [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") [`enum`](https://docs.python.org/3.11/library/enum.html#module-enum "\(in Python v3.11\)") 
    
Coordinate system axis of the object. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of rotation in degrees. The default is `90`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**create_new_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create copies as new objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_around_axis(axis="Z")

```
Copy to clipboard