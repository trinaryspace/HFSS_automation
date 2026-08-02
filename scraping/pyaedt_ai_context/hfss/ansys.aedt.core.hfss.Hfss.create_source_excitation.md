---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_source_excitation.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_source_excitation 

Hfss.create_source_excitation(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _point1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _point2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Voltage'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a source excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet. 

**point1**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
First point of the source excitation. 

**point2**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Second point of the source excitation. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source. 

**source_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the source. The default is `"Voltage"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignVoltage
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rect = hfss.modeler.create_rectangle([0, 0, 0], [10, 10])
>>> excitation = hfss.create_source_excitation(rect.name, [0, 0, 5], [0, 0, 10], "my_source")

```
Copy to clipboard
# create_source_excitation 

Hfss.create_source_excitation(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _point1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _point2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Voltage'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a source excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet. 

**point1**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
First point of the source excitation. 

**point2**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Second point of the source excitation. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source. 

**source_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the source. The default is `"Voltage"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignVoltage
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rect = hfss.modeler.create_rectangle([0, 0, 0], [10, 10])
>>> excitation = hfss.create_source_excitation(rect.name, [0, 0, 5], [0, 0, 10], "my_source")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_source_excitation.rst.txt)

# create_source_excitation 

Hfss.create_source_excitation(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _point1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _point2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Voltage'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a source excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet. 

**point1**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
First point of the source excitation. 

**point2**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Second point of the source excitation. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the source. 

**source_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the source. The default is `"Voltage"`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignVoltage
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rect = hfss.modeler.create_rectangle([0, 0, 0], [10, 10])
>>> excitation = hfss.create_source_excitation(rect.name, [0, 0, 5], [0, 0, 10], "my_source")

```
Copy to clipboard