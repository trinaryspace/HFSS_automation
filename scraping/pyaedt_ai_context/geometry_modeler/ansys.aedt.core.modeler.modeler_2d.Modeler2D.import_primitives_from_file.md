---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.import_primitives_from_file.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# import_primitives_from_file 

Modeler2D.import_primitives_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primitives : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Import and create primitives from a JSON file or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to a JSON file containing all primitives to import. It can be used in alternative to `parameters`. 

**primitives**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing all primitives to import. It can be used in alternative to `input_file`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created primitives.
Examples

```
>>> from ansys.aedt.core import Icepak
>>> aedtapp = Icepak()
>>> aedtapp.modeler.import_primitives_from_file("primitives.json")

```
Copy to clipboard
# import_primitives_from_file 

Modeler2D.import_primitives_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primitives : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Import and create primitives from a JSON file or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to a JSON file containing all primitives to import. It can be used in alternative to `parameters`. 

**primitives**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing all primitives to import. It can be used in alternative to `input_file`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created primitives.
Examples

```
>>> from ansys.aedt.core import Icepak
>>> aedtapp = Icepak()
>>> aedtapp.modeler.import_primitives_from_file("primitives.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.import_primitives_from_file.rst.txt)

# import_primitives_from_file 

Modeler2D.import_primitives_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primitives : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Import and create primitives from a JSON file or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to a JSON file containing all primitives to import. It can be used in alternative to `parameters`. 

**primitives**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing all primitives to import. It can be used in alternative to `input_file`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created primitives.
Examples

```
>>> from ansys.aedt.core import Icepak
>>> aedtapp = Icepak()
>>> aedtapp.modeler.import_primitives_from_file("primitives.json")

```
Copy to clipboard