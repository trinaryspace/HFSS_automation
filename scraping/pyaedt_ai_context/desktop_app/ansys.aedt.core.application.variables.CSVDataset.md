---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# CSVDataset 

class ansys.aedt.core.application.variables.CSVDataset(_csv_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _separator : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _append_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) 
    
Reads in a CSV file and extracts data, which can be augmented with constant values. 

Parameters: 
     

**csv_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Input file consisting of delimited data with the first line as the header. The CSV value includes the header and data, which supports AEDT units information such as `"1.23Wb"`. You can also augment the data with constant values. 

**separator**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value to use for the delimiter. The default is``None`` in which case a comma is assumed. 

**units_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{Variable Name: unit}` to rescale the data if it is not in the desired unit system. 

**append_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{New Variable Name: value}` to add variables with constant values to all data points. This dictionary is used to add multiple sweeps to one result file.
Examples

```
>>> from ansys.aedt.core.application.variables import CSVDataset
>>> dataset = CSVDataset("results.csv")
>>> dataset.number_of_rows

```
Copy to clipboard
Methods  
| [`CSVDataset.next`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.next.html#ansys.aedt.core.application.variables.CSVDataset.next "ansys.aedt.core.application.variables.CSVDataset.next")()  | Yield the next row.  |  
| --- | --- |  
Attributes  
| [`CSVDataset.data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.data.html#ansys.aedt.core.application.variables.CSVDataset.data "ansys.aedt.core.application.variables.CSVDataset.data")  | Data.  |  
| --- | --- |  
| [`CSVDataset.header`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.header.html#ansys.aedt.core.application.variables.CSVDataset.header "ansys.aedt.core.application.variables.CSVDataset.header")  | Header.  |  
| [`CSVDataset.number_of_columns`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_columns.html#ansys.aedt.core.application.variables.CSVDataset.number_of_columns "ansys.aedt.core.application.variables.CSVDataset.number_of_columns")  | Number of columns.  |  
| [`CSVDataset.number_of_rows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_rows.html#ansys.aedt.core.application.variables.CSVDataset.number_of_rows "ansys.aedt.core.application.variables.CSVDataset.number_of_rows")  | Number of rows.  |  
| [`CSVDataset.path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.path.html#ansys.aedt.core.application.variables.CSVDataset.path "ansys.aedt.core.application.variables.CSVDataset.path")  | Path.  |  
| [`CSVDataset.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.public_dir.html#ansys.aedt.core.application.variables.CSVDataset.public_dir "ansys.aedt.core.application.variables.CSVDataset.public_dir")  | Shortcut for dir(self).  |  
# CSVDataset 

class ansys.aedt.core.application.variables.CSVDataset(_csv_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _separator : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _append_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) 
    
Reads in a CSV file and extracts data, which can be augmented with constant values. 

Parameters: 
     

**csv_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Input file consisting of delimited data with the first line as the header. The CSV value includes the header and data, which supports AEDT units information such as `"1.23Wb"`. You can also augment the data with constant values. 

**separator**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value to use for the delimiter. The default is``None`` in which case a comma is assumed. 

**units_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{Variable Name: unit}` to rescale the data if it is not in the desired unit system. 

**append_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{New Variable Name: value}` to add variables with constant values to all data points. This dictionary is used to add multiple sweeps to one result file.
Examples

```
>>> from ansys.aedt.core.application.variables import CSVDataset
>>> dataset = CSVDataset("results.csv")
>>> dataset.number_of_rows

```
Copy to clipboard
Methods  
| [`CSVDataset.next`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.next.html#ansys.aedt.core.application.variables.CSVDataset.next "ansys.aedt.core.application.variables.CSVDataset.next")()  | Yield the next row.  |  
| --- | --- |  
Attributes  
| [`CSVDataset.data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.data.html#ansys.aedt.core.application.variables.CSVDataset.data "ansys.aedt.core.application.variables.CSVDataset.data")  | Data.  |  
| --- | --- |  
| [`CSVDataset.header`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.header.html#ansys.aedt.core.application.variables.CSVDataset.header "ansys.aedt.core.application.variables.CSVDataset.header")  | Header.  |  
| [`CSVDataset.number_of_columns`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_columns.html#ansys.aedt.core.application.variables.CSVDataset.number_of_columns "ansys.aedt.core.application.variables.CSVDataset.number_of_columns")  | Number of columns.  |  
| [`CSVDataset.number_of_rows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_rows.html#ansys.aedt.core.application.variables.CSVDataset.number_of_rows "ansys.aedt.core.application.variables.CSVDataset.number_of_rows")  | Number of rows.  |  
| [`CSVDataset.path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.path.html#ansys.aedt.core.application.variables.CSVDataset.path "ansys.aedt.core.application.variables.CSVDataset.path")  | Path.  |  
| [`CSVDataset.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.public_dir.html#ansys.aedt.core.application.variables.CSVDataset.public_dir "ansys.aedt.core.application.variables.CSVDataset.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.rst.txt)

# CSVDataset 

class ansys.aedt.core.application.variables.CSVDataset(_csv_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _separator : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _append_dict : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) 
    
Reads in a CSV file and extracts data, which can be augmented with constant values. 

Parameters: 
     

**csv_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Input file consisting of delimited data with the first line as the header. The CSV value includes the header and data, which supports AEDT units information such as `"1.23Wb"`. You can also augment the data with constant values. 

**separator**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value to use for the delimiter. The default is``None`` in which case a comma is assumed. 

**units_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{Variable Name: unit}` to rescale the data if it is not in the desired unit system. 

**append_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary consisting of `{New Variable Name: value}` to add variables with constant values to all data points. This dictionary is used to add multiple sweeps to one result file.
Examples

```
>>> from ansys.aedt.core.application.variables import CSVDataset
>>> dataset = CSVDataset("results.csv")
>>> dataset.number_of_rows

```
Copy to clipboard
Methods  
| [`CSVDataset.next`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.next.html#ansys.aedt.core.application.variables.CSVDataset.next "ansys.aedt.core.application.variables.CSVDataset.next")()  | Yield the next row.  |  
| --- | --- |  
Attributes  
| [`CSVDataset.data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.data.html#ansys.aedt.core.application.variables.CSVDataset.data "ansys.aedt.core.application.variables.CSVDataset.data")  | Data.  |  
| --- | --- |  
| [`CSVDataset.header`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.header.html#ansys.aedt.core.application.variables.CSVDataset.header "ansys.aedt.core.application.variables.CSVDataset.header")  | Header.  |  
| [`CSVDataset.number_of_columns`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_columns.html#ansys.aedt.core.application.variables.CSVDataset.number_of_columns "ansys.aedt.core.application.variables.CSVDataset.number_of_columns")  | Number of columns.  |  
| [`CSVDataset.number_of_rows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.number_of_rows.html#ansys.aedt.core.application.variables.CSVDataset.number_of_rows "ansys.aedt.core.application.variables.CSVDataset.number_of_rows")  | Number of rows.  |  
| [`CSVDataset.path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.path.html#ansys.aedt.core.application.variables.CSVDataset.path "ansys.aedt.core.application.variables.CSVDataset.path")  | Path.  |  
| [`CSVDataset.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.CSVDataset.public_dir.html#ansys.aedt.core.application.variables.CSVDataset.public_dir "ansys.aedt.core.application.variables.CSVDataset.public_dir")  | Shortcut for dir(self).  |