---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.get_sources_for_plot.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# get_sources_for_plot 

Matrix.get_sources_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") = 'C'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Return a list of source of specified matrix ready to be used in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if self terms have to be returned or not. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if mutual terms have to be returned or not. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to first element of equation. It accepts * and ? as special characters. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to second element of equation. It accepts * and ? as special characters. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D"), `optional` 
    
Plot category name as in the report. Eg. “C” is category Capacitance. Matrix CATEGORIES property can be used to map available categories. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(project_path)
>>> q3d.matrices[0].get_sources_for_plot(
...     first_element_filter="Bo?1", second_element_filter="GND*", category="DCL"
... )

```
Copy to clipboard
# get_sources_for_plot 

Matrix.get_sources_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") = 'C'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Return a list of source of specified matrix ready to be used in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if self terms have to be returned or not. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if mutual terms have to be returned or not. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to first element of equation. It accepts * and ? as special characters. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to second element of equation. It accepts * and ? as special characters. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D"), `optional` 
    
Plot category name as in the report. Eg. “C” is category Capacitance. Matrix CATEGORIES property can be used to map available categories. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(project_path)
>>> q3d.matrices[0].get_sources_for_plot(
...     first_element_filter="Bo?1", second_element_filter="GND*", category="DCL"
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.get_sources_for_plot.rst.txt)

# get_sources_for_plot 

Matrix.get_sources_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [MatrixOperationsQ3D](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D") = 'C'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Return a list of source of specified matrix ready to be used in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if self terms have to be returned or not. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if mutual terms have to be returned or not. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to first element of equation. It accepts * and ? as special characters. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to second element of equation. It accepts * and ? as special characters. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.generic.constants.MatrixOperationsQ3D`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.MatrixOperationsQ3D "ansys.aedt.core.generic.constants.MatrixOperationsQ3D"), `optional` 
    
Plot category name as in the report. Eg. “C” is category Capacitance. Matrix CATEGORIES property can be used to map available categories. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Q3d
>>> q3d = Q3d(project_path)
>>> q3d.matrices[0].get_sources_for_plot(
...     first_element_filter="Bo?1", second_element_filter="GND*", category="DCL"
... )

```
Copy to clipboard