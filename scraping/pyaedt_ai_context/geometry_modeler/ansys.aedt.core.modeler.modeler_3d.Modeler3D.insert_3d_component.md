---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.insert_3d_component.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert_3d_component 

Modeler3D.insert_3d_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _geometry_parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _material_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _design_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password =None_, _auxiliary_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new 3D component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the component file. 

**geometry_parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Geometrical parameters. 

**material_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material parameters. The default is `""`. 

**design_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design parameters. The default is `""`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password for encrypted components. The default value is `None`. 

**auxiliary_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Enable the advanced 3d component import. It is possible to set explicitly the json file. The default is `False`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.insert_3d_component(input_file="example.txt")

```
Copy to clipboard
# insert_3d_component 

Modeler3D.insert_3d_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _geometry_parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _material_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _design_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password =None_, _auxiliary_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new 3D component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the component file. 

**geometry_parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Geometrical parameters. 

**material_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material parameters. The default is `""`. 

**design_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design parameters. The default is `""`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password for encrypted components. The default value is `None`. 

**auxiliary_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Enable the advanced 3d component import. It is possible to set explicitly the json file. The default is `False`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.insert_3d_component(input_file="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.insert_3d_component.rst.txt)

# insert_3d_component 

Modeler3D.insert_3d_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _geometry_parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _material_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _design_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password =None_, _auxiliary_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new 3D component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the component file. 

**geometry_parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Geometrical parameters. 

**material_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material parameters. The default is `""`. 

**design_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design parameters. The default is `""`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password for encrypted components. The default value is `None`. 

**auxiliary_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Enable the advanced 3d component import. It is possible to set explicitly the json file. The default is `False`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.insert_3d_component(input_file="example.txt")

```
Copy to clipboard