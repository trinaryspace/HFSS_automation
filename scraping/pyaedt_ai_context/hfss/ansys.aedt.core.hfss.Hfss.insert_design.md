---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.insert_design.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# insert_design 

Hfss.insert_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Add a design of a specified type.
The default design type is taken from the derived application class. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design. The default is `None`, in which case the default design name is `<Design-Type>Design<_index>`. If the given or default design name is in use, then an underscore and index is added to ensure that the design name is unique. The inserted object is assigned to the `Design` object. 

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution type to apply to the design. The default is `None`, in which case the default type is applied. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the design.
References

```
>>> oProject.InsertDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.insert_design(name="HFSSDesign1")

```
Copy to clipboard
# insert_design 

Hfss.insert_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Add a design of a specified type.
The default design type is taken from the derived application class. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design. The default is `None`, in which case the default design name is `<Design-Type>Design<_index>`. If the given or default design name is in use, then an underscore and index is added to ensure that the design name is unique. The inserted object is assigned to the `Design` object. 

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution type to apply to the design. The default is `None`, in which case the default type is applied. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the design.
References

```
>>> oProject.InsertDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.insert_design(name="HFSSDesign1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.insert_design.rst.txt)

# insert_design 

Hfss.insert_design(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Add a design of a specified type.
The default design type is taken from the derived application class. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design. The default is `None`, in which case the default design name is `<Design-Type>Design<_index>`. If the given or default design name is in use, then an underscore and index is added to ensure that the design name is unique. The inserted object is assigned to the `Design` object. 

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution type to apply to the design. The default is `None`, in which case the default type is applied. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the design.
References

```
>>> oProject.InsertDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.insert_design(name="HFSSDesign1")

```
Copy to clipboard