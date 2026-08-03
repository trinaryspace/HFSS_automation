---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_objects_by_material.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_objects_by_material 

Modeler3D.get_objects_by_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of objects either of a specified material or classified by material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. The default is `None`. 

Returns: 
     

list of class:ansys.aedt.core.modeler.cad.object_3d.Object3d 
    
If a material name is not provided, the method returns a list of dictionaries where keys are material names of conductors, dielectrics, gases, and liquids respectively in the design and values are objects assigned to these materials. If a material name is provided, the method returns a list of objects assigned to the material.
References

```
>>> oEditor.GetObjectsByMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_objects_by_material(material="copper")

```
Copy to clipboard
# get_objects_by_material 

Modeler3D.get_objects_by_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of objects either of a specified material or classified by material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. The default is `None`. 

Returns: 
     

list of class:ansys.aedt.core.modeler.cad.object_3d.Object3d 
    
If a material name is not provided, the method returns a list of dictionaries where keys are material names of conductors, dielectrics, gases, and liquids respectively in the design and values are objects assigned to these materials. If a material name is provided, the method returns a list of objects assigned to the material.
References

```
>>> oEditor.GetObjectsByMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_objects_by_material(material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_objects_by_material.rst.txt)

# get_objects_by_material 

Modeler3D.get_objects_by_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of objects either of a specified material or classified by material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. The default is `None`. 

Returns: 
     

list of class:ansys.aedt.core.modeler.cad.object_3d.Object3d 
    
If a material name is not provided, the method returns a list of dictionaries where keys are material names of conductors, dielectrics, gases, and liquids respectively in the design and values are objects assigned to these materials. If a material name is provided, the method returns a list of objects assigned to the material.
References

```
>>> oEditor.GetObjectsByMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_objects_by_material(material="copper")

```
Copy to clipboard