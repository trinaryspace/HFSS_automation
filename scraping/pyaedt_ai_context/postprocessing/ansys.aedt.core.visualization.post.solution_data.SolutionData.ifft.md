---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.ifft.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# ifft 

SolutionData.ifft(_curve_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NearE'_, _u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _window : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Create IFFT of given complex data. 

Parameters: 
     

**curve_header**`curve` header. `Solution` `data` `must` `contain` 3 `curves` `with` `X`, `Y` `and` `Z` `components` `of` `curve` header. 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**window**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if Hanning windowing has to be applied. 

Returns: 
     

`List`
    
IFFT Matrix.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft(curve_header=1, u_axis=["Box1"])

```
Copy to clipboard
# ifft 

SolutionData.ifft(_curve_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NearE'_, _u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _window : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Create IFFT of given complex data. 

Parameters: 
     

**curve_header**`curve` header. `Solution` `data` `must` `contain` 3 `curves` `with` `X`, `Y` `and` `Z` `components` `of` `curve` header. 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**window**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if Hanning windowing has to be applied. 

Returns: 
     

`List`
    
IFFT Matrix.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft(curve_header=1, u_axis=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.ifft.rst.txt)

# ifft 

SolutionData.ifft(_curve_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'NearE'_, _u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _window : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Create IFFT of given complex data. 

Parameters: 
     

**curve_header**`curve` header. `Solution` `data` `must` `contain` 3 `curves` `with` `X`, `Y` `and` `Z` `components` `of` `curve` header. 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**window**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if Hanning windowing has to be applied. 

Returns: 
     

`List`
    
IFFT Matrix.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft(curve_header=1, u_axis=["Box1"])

```
Copy to clipboard