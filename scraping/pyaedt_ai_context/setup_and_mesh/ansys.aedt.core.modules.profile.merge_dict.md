---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.merge_dict.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# merge_dict 

ansys.aedt.core.modules.profile.merge_dict(_d1 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _d2 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Recursively merge two dictionaries using type-aware rules.
The merge follows these rules when a key exists in both:
  * Identical values: keep that value.
  * Both dict: merge recursively with the same algorithm.
  * Both list: concatenate and return a sorted list.
  * Both str: concatenate separated by a newline.
  * Different or otherwise incompatible types: preserve the value from

`d1` under the original key and store the value from `d2` under `"<key>_2"`.
Keys that exist in only one dictionary are copied as-is. Keys are ordered using a natural sort that extracts a trailing integer. 

Parameters: 
     

**d1**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**d2**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
     

`Merged` dictionary.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import merge_dict
>>> merge_dict({"a": 1}, {"b": 2})
{'a': 1, 'b': 2}

```
Copy to clipboard
# merge_dict 

ansys.aedt.core.modules.profile.merge_dict(_d1 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _d2 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Recursively merge two dictionaries using type-aware rules.
The merge follows these rules when a key exists in both:
  * Identical values: keep that value.
  * Both dict: merge recursively with the same algorithm.
  * Both list: concatenate and return a sorted list.
  * Both str: concatenate separated by a newline.
  * Different or otherwise incompatible types: preserve the value from

`d1` under the original key and store the value from `d2` under `"<key>_2"`.
Keys that exist in only one dictionary are copied as-is. Keys are ordered using a natural sort that extracts a trailing integer. 

Parameters: 
     

**d1**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**d2**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
     

`Merged` dictionary.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import merge_dict
>>> merge_dict({"a": 1}, {"b": 2})
{'a': 1, 'b': 2}

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.merge_dict.rst.txt)

# merge_dict 

ansys.aedt.core.modules.profile.merge_dict(_d1 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _d2 : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Recursively merge two dictionaries using type-aware rules.
The merge follows these rules when a key exists in both:
  * Identical values: keep that value.
  * Both dict: merge recursively with the same algorithm.
  * Both list: concatenate and return a sorted list.
  * Both str: concatenate separated by a newline.
  * Different or otherwise incompatible types: preserve the value from

`d1` under the original key and store the value from `d2` under `"<key>_2"`.
Keys that exist in only one dictionary are copied as-is. Keys are ordered using a natural sort that extracts a trailing integer. 

Parameters: 
     

**d1**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**d2**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
     

`Merged` dictionary.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import merge_dict
>>> merge_dict({"a": 1}, {"b": 2})
{'a': 1, 'b': 2}

```
Copy to clipboard