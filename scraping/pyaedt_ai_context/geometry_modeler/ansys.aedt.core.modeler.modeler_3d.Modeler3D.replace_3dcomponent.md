---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.replace_3dcomponent.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# replace_3dcomponent 

Modeler3D.replace_3dcomponent(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") 
    
Replace with 3D component. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is `None`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of coordinate systems to export. The default is all coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The coordinate system reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User-defined component object.
References

```
>>> oEditor.ReplaceWith3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.replace_3dcomponent(assignment="Box1", name="MyObject")

```
Copy to clipboard
# replace_3dcomponent 

Modeler3D.replace_3dcomponent(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") 
    
Replace with 3D component. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is `None`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of coordinate systems to export. The default is all coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The coordinate system reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User-defined component object.
References

```
>>> oEditor.ReplaceWith3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.replace_3dcomponent(assignment="Box1", name="MyObject")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.replace_3dcomponent.rst.txt)

# replace_3dcomponent 

Modeler3D.replace_3dcomponent(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") 
    
Replace with 3D component. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is `None`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of coordinate systems to export. The default is all coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The coordinate system reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User-defined component object.
References

```
>>> oEditor.ReplaceWith3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.replace_3dcomponent(assignment="Box1", name="MyObject")

```
Copy to clipboard