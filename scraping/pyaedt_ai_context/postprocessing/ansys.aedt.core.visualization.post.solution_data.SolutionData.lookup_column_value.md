---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.lookup_column_value.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# lookup_column_value 

static SolutionData.lookup_column_value(_array : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _match_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _match_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _output_column : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -1_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Filters rows in a NumPy array based on column-value matches, and returns the last column value of all matching rows. 

Parameters: 
     

**array**[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
The input array (2D). 

**match_columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Column indices to match. 

**match_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Values to match at each column. 

**output_column**[`any`](https://docs.python.org/3.11/library/functions.html#any "\(in Python v3.11\)") 
    
Value to return if no match is found. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") or `default` 
    
Array of last column values for matching rows, or default if none found.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.lookup_column_value(array=1, match_columns=["Box1"], match_values=["Box1"])

```
Copy to clipboard
# lookup_column_value 

static SolutionData.lookup_column_value(_array : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _match_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _match_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _output_column : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -1_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Filters rows in a NumPy array based on column-value matches, and returns the last column value of all matching rows. 

Parameters: 
     

**array**[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
The input array (2D). 

**match_columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Column indices to match. 

**match_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Values to match at each column. 

**output_column**[`any`](https://docs.python.org/3.11/library/functions.html#any "\(in Python v3.11\)") 
    
Value to return if no match is found. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") or `default` 
    
Array of last column values for matching rows, or default if none found.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.lookup_column_value(array=1, match_columns=["Box1"], match_values=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.lookup_column_value.rst.txt)

# lookup_column_value 

static SolutionData.lookup_column_value(_array : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _match_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _match_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _output_column : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -1_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Filters rows in a NumPy array based on column-value matches, and returns the last column value of all matching rows. 

Parameters: 
     

**array**[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
The input array (2D). 

**match_columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Column indices to match. 

**match_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Values to match at each column. 

**output_column**[`any`](https://docs.python.org/3.11/library/functions.html#any "\(in Python v3.11\)") 
    
Value to return if no match is found. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") or `default` 
    
Array of last column values for matching rows, or default if none found.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.lookup_column_value(array=1, match_columns=["Box1"], match_values=["Box1"])

```
Copy to clipboard