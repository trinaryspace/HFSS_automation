---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.generate_unique_name.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# generate_unique_name 

ansys.aedt.core.generic.file_utils.generate_unique_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a new name given a root name and optional suffix. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Root name to add random characters to. 

**suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Suffix to add. The default is `''`. 

**n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of random characters to add to the name. The default value is `6`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_name
>>> generate_unique_name("Setup")

```
Copy to clipboard
# generate_unique_name 

ansys.aedt.core.generic.file_utils.generate_unique_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a new name given a root name and optional suffix. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Root name to add random characters to. 

**suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Suffix to add. The default is `''`. 

**n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of random characters to add to the name. The default value is `6`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_name
>>> generate_unique_name("Setup")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.generate_unique_name.rst.txt)

# generate_unique_name 

ansys.aedt.core.generic.file_utils.generate_unique_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a new name given a root name and optional suffix. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Root name to add random characters to. 

**suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Suffix to add. The default is `''`. 

**n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of random characters to add to the name. The default value is `6`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_name
>>> generate_unique_name("Setup")

```
Copy to clipboard