---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.insert_layout_component.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert_layout_component 

Modeler3D.insert_layout_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameter_mapping : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _layout_coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new layout component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path of the component file. Either `".aedb"` and `".aedbcomp"` are allowed. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**parameter_mapping**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the layout parameters in the target HFSS design. The default is `False`. 

**layout_coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Coordinate system to import. The default is all available coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use as reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> layout_component = "path/to/layout_component/component.aedbcomp"
>>> comp = app.modeler.insert_layout_component(layout_component)

```
Copy to clipboard
# insert_layout_component 

Modeler3D.insert_layout_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameter_mapping : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _layout_coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new layout component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path of the component file. Either `".aedb"` and `".aedbcomp"` are allowed. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**parameter_mapping**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the layout parameters in the target HFSS design. The default is `False`. 

**layout_coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Coordinate system to import. The default is all available coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use as reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> layout_component = "path/to/layout_component/component.aedbcomp"
>>> comp = app.modeler.insert_layout_component(layout_component)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.insert_layout_component.rst.txt)

# insert_layout_component 

Modeler3D.insert_layout_component(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _parameter_mapping : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _layout_coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert a new layout component. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path of the component file. Either `".aedb"` and `".aedbcomp"` are allowed. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
3D component name. The default is `None`. 

**parameter_mapping**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the layout parameters in the target HFSS design. The default is `False`. 

**layout_coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Coordinate system to import. The default is all available coordinate systems. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use as reference. The default is `"Global"`. 

Returns: 
     

`ansys.aedt.core.modeler.components_3d.UserDefinedComponent`
    
User defined component object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> layout_component = "path/to/layout_component/component.aedbcomp"
>>> comp = app.modeler.insert_layout_component(layout_component)

```
Copy to clipboard