---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.read_csv_pandas.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# read_csv_pandas 

ansys.aedt.core.generic.file_utils.read_csv_pandas(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_) → [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Read information from a CSV file and return a list. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the CSV file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding for the CSV file. The default is `"utf-8"`. 

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
CSV file content.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_csv_pandas
>>> read_csv_pandas(r"C:\Temp\losses.csv")

```
Copy to clipboard
# read_csv_pandas 

ansys.aedt.core.generic.file_utils.read_csv_pandas(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_) → [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Read information from a CSV file and return a list. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the CSV file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding for the CSV file. The default is `"utf-8"`. 

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
CSV file content.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_csv_pandas
>>> read_csv_pandas(r"C:\Temp\losses.csv")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.read_csv_pandas.rst.txt)

# read_csv_pandas 

ansys.aedt.core.generic.file_utils.read_csv_pandas(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | Path_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_) → [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Read information from a CSV file and return a list. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path and name for the CSV file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
File encoding for the CSV file. The default is `"utf-8"`. 

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
CSV file content.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_csv_pandas
>>> read_csv_pandas(r"C:\Temp\losses.csv")

```
Copy to clipboard