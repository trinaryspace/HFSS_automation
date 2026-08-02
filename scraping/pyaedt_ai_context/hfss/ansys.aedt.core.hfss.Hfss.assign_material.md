---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_material.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_material 

Hfss.assign_material(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a material to one or more objects. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects to assign materials to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material to assign. If this material is not present, it is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
The method [`assign_material()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_material.html#ansys.aedt.core.hfss.Hfss.assign_material "ansys.aedt.core.hfss.Hfss.assign_material") is used to assign a material to a list of objects.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([10, 10, 10], [4, 5, 5])
>>> box2 = hfss.modeler.create_box([0, 0, 0], [2, 3, 4])
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> cylinder2 = hfss.modeler.create_cylinder(orientation="Z", origin=[0, 0, 5], radius=1, height=10)

```
Copy to clipboard
Assign the material `"copper"` to all the objects.

```
>>> objects_list = [box1, box2, cylinder1, cylinder2]
>>> hfss.assign_material(objects_list, "copper")

```
Copy to clipboard
The method also accepts a list of object names.

```
>>> obj_names_list = [box1.name, box2.name, cylinder1.name, cylinder2.name]
>>> hfss.assign_material(obj_names_list, "aluminum")

```
Copy to clipboard
# assign_material 

Hfss.assign_material(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a material to one or more objects. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects to assign materials to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material to assign. If this material is not present, it is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
The method [`assign_material()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_material.html#ansys.aedt.core.hfss.Hfss.assign_material "ansys.aedt.core.hfss.Hfss.assign_material") is used to assign a material to a list of objects.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([10, 10, 10], [4, 5, 5])
>>> box2 = hfss.modeler.create_box([0, 0, 0], [2, 3, 4])
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> cylinder2 = hfss.modeler.create_cylinder(orientation="Z", origin=[0, 0, 5], radius=1, height=10)

```
Copy to clipboard
Assign the material `"copper"` to all the objects.

```
>>> objects_list = [box1, box2, cylinder1, cylinder2]
>>> hfss.assign_material(objects_list, "copper")

```
Copy to clipboard
The method also accepts a list of object names.

```
>>> obj_names_list = [box1.name, box2.name, cylinder1.name, cylinder2.name]
>>> hfss.assign_material(obj_names_list, "aluminum")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_material.rst.txt)

# assign_material 

Hfss.assign_material(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a material to one or more objects. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects to assign materials to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material to assign. If this material is not present, it is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
The method [`assign_material()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_material.html#ansys.aedt.core.hfss.Hfss.assign_material "ansys.aedt.core.hfss.Hfss.assign_material") is used to assign a material to a list of objects.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([10, 10, 10], [4, 5, 5])
>>> box2 = hfss.modeler.create_box([0, 0, 0], [2, 3, 4])
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> cylinder2 = hfss.modeler.create_cylinder(orientation="Z", origin=[0, 0, 5], radius=1, height=10)

```
Copy to clipboard
Assign the material `"copper"` to all the objects.

```
>>> objects_list = [box1, box2, cylinder1, cylinder2]
>>> hfss.assign_material(objects_list, "copper")

```
Copy to clipboard
The method also accepts a list of object names.

```
>>> obj_names_list = [box1.name, box2.name, cylinder1.name, cylinder2.name]
>>> hfss.assign_material(obj_names_list, "aluminum")

```
Copy to clipboard