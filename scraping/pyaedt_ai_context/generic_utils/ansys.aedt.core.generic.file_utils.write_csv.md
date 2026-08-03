---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.write_csv.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# write_csv 

ansys.aedt.core.generic.file_utils.write_csv(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _list_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _delimiter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ','_, _quote_char : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '|'_, _quoting : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Write data to a CSV . 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the file to write the data to. 

**list_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be written to the specified output file. 

**delimiter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Delimiter. The default value is `"|"`. 

**quote_char**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quote character. The default value is `"|"` 

**quoting**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Quoting character. The default value is `"csv.QUOTE_MINIMAL"`. It can take one any of the following module constants:
  * 

`"csv.QUOTE_MINIMAL"` means only when required, for example, when a
    
field contains either the quote char or the delimiter
  * `"csv.QUOTE_ALL"` means that quotes are always placed around fields.
  * 

`"csv.QUOTE_NONNUMERIC"` means that quotes are always placed around
    
fields which do not parse as integers or floating point numbers.
  * `"csv.QUOTE_NONE"` means that quotes are never placed around fields.

Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_csv
>>> data = [["Freq", "Gain"], [1e9, 10.5]]
>>> write_csv(r"C:\Temp\gain.csv", data)

```
Copy to clipboard
# write_csv 

ansys.aedt.core.generic.file_utils.write_csv(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _list_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _delimiter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ','_, _quote_char : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '|'_, _quoting : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Write data to a CSV . 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the file to write the data to. 

**list_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be written to the specified output file. 

**delimiter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Delimiter. The default value is `"|"`. 

**quote_char**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quote character. The default value is `"|"` 

**quoting**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Quoting character. The default value is `"csv.QUOTE_MINIMAL"`. It can take one any of the following module constants:
  * 

`"csv.QUOTE_MINIMAL"` means only when required, for example, when a
    
field contains either the quote char or the delimiter
  * `"csv.QUOTE_ALL"` means that quotes are always placed around fields.
  * 

`"csv.QUOTE_NONNUMERIC"` means that quotes are always placed around
    
fields which do not parse as integers or floating point numbers.
  * `"csv.QUOTE_NONE"` means that quotes are never placed around fields.

Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_csv
>>> data = [["Freq", "Gain"], [1e9, 10.5]]
>>> write_csv(r"C:\Temp\gain.csv", data)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.write_csv.rst.txt)

# write_csv 

ansys.aedt.core.generic.file_utils.write_csv(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _list_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _delimiter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ','_, _quote_char : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '|'_, _quoting : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Write data to a CSV . 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name of the file to write the data to. 

**list_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be written to the specified output file. 

**delimiter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Delimiter. The default value is `"|"`. 

**quote_char**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Quote character. The default value is `"|"` 

**quoting**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Quoting character. The default value is `"csv.QUOTE_MINIMAL"`. It can take one any of the following module constants:
  * 

`"csv.QUOTE_MINIMAL"` means only when required, for example, when a
    
field contains either the quote char or the delimiter
  * `"csv.QUOTE_ALL"` means that quotes are always placed around fields.
  * 

`"csv.QUOTE_NONNUMERIC"` means that quotes are always placed around
    
fields which do not parse as integers or floating point numbers.
  * `"csv.QUOTE_NONE"` means that quotes are never placed around fields.

Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_csv
>>> data = [["Freq", "Gain"], [1e9, 10.5]]
>>> write_csv(r"C:\Temp\gain.csv", data)

```
Copy to clipboard