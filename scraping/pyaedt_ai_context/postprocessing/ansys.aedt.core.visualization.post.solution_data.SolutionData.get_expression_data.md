---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.get_expression_data.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_expression_data 

SolutionData.get_expression_data(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'real'_, _convert_to_SI : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_quantity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweeps : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)"), [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")] 
    
Retrieve the real part of the data for an expression. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Name of the expression. The default is `None`, in which case the active expression is used. 

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data type to be retrieved. Default is `real`. Options are `real`, `imag`, `mag`, `magnitude`, `db10`, `db20`, `phase`, `phaserad`. 

**convert_to_SI**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to convert the data to the SI unit system. The default is `False`. 

**use_quantity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to output data in `Quantity` format or not. It impacts on performances as it returns array of objects. 

**sweeps**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of sweeps to consider for the data retrieval. The default is `None`, which actually takes the primary sweep. 

Returns: 
     

(`np.array`, `np.array`)
    
X and Y data for the expression.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.get_expression_data(expression="dB(S(1,1))", formula=1)

```
Copy to clipboard
# get_expression_data 

SolutionData.get_expression_data(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'real'_, _convert_to_SI : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_quantity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweeps : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)"), [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")] 
    
Retrieve the real part of the data for an expression. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Name of the expression. The default is `None`, in which case the active expression is used. 

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data type to be retrieved. Default is `real`. Options are `real`, `imag`, `mag`, `magnitude`, `db10`, `db20`, `phase`, `phaserad`. 

**convert_to_SI**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to convert the data to the SI unit system. The default is `False`. 

**use_quantity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to output data in `Quantity` format or not. It impacts on performances as it returns array of objects. 

**sweeps**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of sweeps to consider for the data retrieval. The default is `None`, which actually takes the primary sweep. 

Returns: 
     

(`np.array`, `np.array`)
    
X and Y data for the expression.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.get_expression_data(expression="dB(S(1,1))", formula=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.get_expression_data.rst.txt)

# get_expression_data 

SolutionData.get_expression_data(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'real'_, _convert_to_SI : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_quantity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweeps : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)"), [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")] 
    
Retrieve the real part of the data for an expression. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Name of the expression. The default is `None`, in which case the active expression is used. 

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data type to be retrieved. Default is `real`. Options are `real`, `imag`, `mag`, `magnitude`, `db10`, `db20`, `phase`, `phaserad`. 

**convert_to_SI**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to convert the data to the SI unit system. The default is `False`. 

**use_quantity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to output data in `Quantity` format or not. It impacts on performances as it returns array of objects. 

**sweeps**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of sweeps to consider for the data retrieval. The default is `None`, which actually takes the primary sweep. 

Returns: 
     

(`np.array`, `np.array`)
    
X and Y data for the expression.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.get_expression_data(expression="dB(S(1,1))", formula=1)

```
Copy to clipboard