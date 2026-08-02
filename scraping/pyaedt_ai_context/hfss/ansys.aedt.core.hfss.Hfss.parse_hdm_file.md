---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.parse_hdm_file.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# parse_hdm_file 

Hfss.parse_hdm_file(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [Parser](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser.html#ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser "ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse an HFSS SBR+ or Creeping Waves `hdm` file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the file to parse. 

Returns: 
     

`ansys.aedt.core.modules.hdm_parser.Parser` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.parse_hdm_file(file_name="output.hdm")

```
Copy to clipboard
# parse_hdm_file 

Hfss.parse_hdm_file(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [Parser](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser.html#ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser "ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse an HFSS SBR+ or Creeping Waves `hdm` file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the file to parse. 

Returns: 
     

`ansys.aedt.core.modules.hdm_parser.Parser` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.parse_hdm_file(file_name="output.hdm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.parse_hdm_file.rst.txt)

# parse_hdm_file 

Hfss.parse_hdm_file(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [Parser](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser.html#ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser "ansys.aedt.core.visualization.advanced.sbrplus.hdm_parser.Parser") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse an HFSS SBR+ or Creeping Waves `hdm` file. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Name of the file to parse. 

Returns: 
     

`ansys.aedt.core.modules.hdm_parser.Parser` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.parse_hdm_file(file_name="output.hdm")

```
Copy to clipboard