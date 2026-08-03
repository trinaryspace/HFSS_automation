---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_choke.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_choke 

Modeler3D.create_choke(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Create a choke from a JSON setting file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the JSON file with the choke settings. 

Returns: 
     

`List` `of` 
     

bool
    
`True` when successful, `False` when failed. 

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object core. 

list of
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object winding. 

list
    
list of point coordinates of the winding. for each winding. [bool, core_obj, [first_winding_obj, first_winding_point_list], [second_winding_obj, second_winding_point_list], etc…]
Examples
Json file has to be like the following example.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")
>>> mychoke = hfss.modeler.create_choke("C:/Example/Of/Path/myJsonFile_Corrected.json")

```
Copy to clipboard
# create_choke 

Modeler3D.create_choke(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Create a choke from a JSON setting file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the JSON file with the choke settings. 

Returns: 
     

`List` `of` 
     

bool
    
`True` when successful, `False` when failed. 

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object core. 

list of
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object winding. 

list
    
list of point coordinates of the winding. for each winding. [bool, core_obj, [first_winding_obj, first_winding_point_list], [second_winding_obj, second_winding_point_list], etc…]
Examples
Json file has to be like the following example.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")
>>> mychoke = hfss.modeler.create_choke("C:/Example/Of/Path/myJsonFile_Corrected.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_choke.rst.txt)

# create_choke 

Modeler3D.create_choke(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Create a choke from a JSON setting file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the JSON file with the choke settings. 

Returns: 
     

`List` `of` 
     

bool
    
`True` when successful, `False` when failed. 

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object core. 

list of
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object winding. 

list
    
list of point coordinates of the winding. for each winding. [bool, core_obj, [first_winding_obj, first_winding_point_list], [second_winding_obj, second_winding_point_list], etc…]
Examples
Json file has to be like the following example.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")
>>> mychoke = hfss.modeler.create_choke("C:/Example/Of/Path/myJsonFile_Corrected.json")

```
Copy to clipboard