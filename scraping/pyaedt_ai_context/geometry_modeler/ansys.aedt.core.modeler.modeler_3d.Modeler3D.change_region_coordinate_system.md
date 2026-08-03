---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.change_region_coordinate_system.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# change_region_coordinate_system 

Modeler3D.change_region_coordinate_system(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Region coordinate system. Default is `Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.create_coordinate_system(origin=[1, 1, 1], name="NewCS")
>>> app.modeler.change_region_coordinate_system(assignment="NewCS")

```
Copy to clipboard
# change_region_coordinate_system 

Modeler3D.change_region_coordinate_system(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Region coordinate system. Default is `Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.create_coordinate_system(origin=[1, 1, 1], name="NewCS")
>>> app.modeler.change_region_coordinate_system(assignment="NewCS")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.change_region_coordinate_system.rst.txt)

# change_region_coordinate_system 

Modeler3D.change_region_coordinate_system(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Region'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change region coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Region coordinate system. Default is `Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Region name. Default is `Region`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, else `None`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Icepak()
>>> app.modeler.create_coordinate_system(origin=[1, 1, 1], name="NewCS")
>>> app.modeler.change_region_coordinate_system(assignment="NewCS")

```
Copy to clipboard