---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.format_timedelta.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# format_timedelta 

ansys.aedt.core.modules.profile.format_timedelta(_time_delta : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Format [`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") for tables. 

Parameters: 
     

**time_delta**[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Timedelta to be formatted. Non-timedelta values are converted to str unchanged. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
     

`"DD days HH:MM:SS"` `if` `days` `are` `present`, `otherwise` `"HH:MM:SS"`.
    
Examples

```
>>> from datetime import timedelta
>>> from ansys.aedt.core.modules.profile import format_timedelta
>>> format_timedelta(timedelta(hours=1, minutes=2, seconds=3))
'01:02:03'

```
Copy to clipboard
# format_timedelta 

ansys.aedt.core.modules.profile.format_timedelta(_time_delta : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Format [`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") for tables. 

Parameters: 
     

**time_delta**[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Timedelta to be formatted. Non-timedelta values are converted to str unchanged. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
     

`"DD days HH:MM:SS"` `if` `days` `are` `present`, `otherwise` `"HH:MM:SS"`.
    
Examples

```
>>> from datetime import timedelta
>>> from ansys.aedt.core.modules.profile import format_timedelta
>>> format_timedelta(timedelta(hours=1, minutes=2, seconds=3))
'01:02:03'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.format_timedelta.rst.txt)

# format_timedelta 

ansys.aedt.core.modules.profile.format_timedelta(_time_delta : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Format [`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") for tables. 

Parameters: 
     

**time_delta**[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Timedelta to be formatted. Non-timedelta values are converted to str unchanged. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
     

`"DD days HH:MM:SS"` `if` `days` `are` `present`, `otherwise` `"HH:MM:SS"`.
    
Examples

```
>>> from datetime import timedelta
>>> from ansys.aedt.core.modules.profile import format_timedelta
>>> format_timedelta(timedelta(hours=1, minutes=2, seconds=3))
'01:02:03'

```
Copy to clipboard