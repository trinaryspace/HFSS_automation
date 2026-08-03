---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.step_name_map.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# step_name_map 

ansys.aedt.core.modules.profile.step_name_map(_input_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Map verbose AEDT step labels to compact names.
Currently, recognizes labels like `"Frequency - <value>Hz"` and reduces them to `"<value>Hz"`. Falls back to the original string if no match is found. 

Parameters: 
     

**input_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Original AEDT step label. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.profile import step_name_map
>>> step_name_map("Frequency - 1.0 GHz")
'1.0 GHz'

```
Copy to clipboard
# step_name_map 

ansys.aedt.core.modules.profile.step_name_map(_input_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Map verbose AEDT step labels to compact names.
Currently, recognizes labels like `"Frequency - <value>Hz"` and reduces them to `"<value>Hz"`. Falls back to the original string if no match is found. 

Parameters: 
     

**input_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Original AEDT step label. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.profile import step_name_map
>>> step_name_map("Frequency - 1.0 GHz")
'1.0 GHz'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.step_name_map.rst.txt)

# step_name_map 

ansys.aedt.core.modules.profile.step_name_map(_input_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Map verbose AEDT step labels to compact names.
Currently, recognizes labels like `"Frequency - <value>Hz"` and reduces them to `"<value>Hz"`. Falls back to the original string if no match is found. 

Parameters: 
     

**input_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Original AEDT step label. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.profile import step_name_map
>>> step_name_map("Frequency - 1.0 GHz")
'1.0 GHz'

```
Copy to clipboard