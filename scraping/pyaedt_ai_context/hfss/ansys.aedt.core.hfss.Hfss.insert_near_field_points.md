---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.insert_near_field_points.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# insert_near_field_points 

Hfss.insert_near_field_points(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearFieldSetup](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup") 
    
Create a near field from a point list file.
Note
This method is not supported by HFSS `EigenMode` and `CharacteristicMode` solution types. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Point list file with. Extension must be `.pts`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Local coordinate system to use. The default is `"Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point list. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.insert_near_field_points(input_file="field_points.pts")

```
Copy to clipboard
# insert_near_field_points 

Hfss.insert_near_field_points(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearFieldSetup](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup") 
    
Create a near field from a point list file.
Note
This method is not supported by HFSS `EigenMode` and `CharacteristicMode` solution types. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Point list file with. Extension must be `.pts`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Local coordinate system to use. The default is `"Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point list. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.insert_near_field_points(input_file="field_points.pts")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.insert_near_field_points.rst.txt)

# insert_near_field_points 

Hfss.insert_near_field_points(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearFieldSetup](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup") 
    
Create a near field from a point list file.
Note
This method is not supported by HFSS `EigenMode` and `CharacteristicMode` solution types. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Point list file with. Extension must be `.pts`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Local coordinate system to use. The default is `"Global`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the point list. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.insert_near_field_points(input_file="field_points.pts")

```
Copy to clipboard