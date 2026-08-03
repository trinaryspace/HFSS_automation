---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_worst_curve.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_worst_curve 

TouchstoneData.get_worst_curve(_freq_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _freq_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _worst_is_higher : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _curve_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Analyze a solution data object with multiple curves and find the worst curve.
Take the mean of the magnitude over the frequency range. 

Parameters: 
     

**freq_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum frequency to analyze in GHz (None to 0). The default value is `None`. 

**freq_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum frequency to analyze in GHz (None to max freq). The default value is `None`. 

**worst_is_higher**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Worst curve is the one with higher mean value. The default value is `True`. 

**curve_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [m,n] index of curves on which to search. None to search on all curves. The default value is `None`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot or not the chart. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Worst element, dictionary of ordered expression.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_worst_curve(freq_min=1.0, freq_max=1.0)

```
Copy to clipboard
# get_worst_curve 

TouchstoneData.get_worst_curve(_freq_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _freq_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _worst_is_higher : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _curve_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Analyze a solution data object with multiple curves and find the worst curve.
Take the mean of the magnitude over the frequency range. 

Parameters: 
     

**freq_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum frequency to analyze in GHz (None to 0). The default value is `None`. 

**freq_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum frequency to analyze in GHz (None to max freq). The default value is `None`. 

**worst_is_higher**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Worst curve is the one with higher mean value. The default value is `True`. 

**curve_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [m,n] index of curves on which to search. None to search on all curves. The default value is `None`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot or not the chart. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Worst element, dictionary of ordered expression.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_worst_curve(freq_min=1.0, freq_max=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_worst_curve.rst.txt)

# get_worst_curve 

TouchstoneData.get_worst_curve(_freq_min : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _freq_max : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _worst_is_higher : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _curve_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Analyze a solution data object with multiple curves and find the worst curve.
Take the mean of the magnitude over the frequency range. 

Parameters: 
     

**freq_min**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum frequency to analyze in GHz (None to 0). The default value is `None`. 

**freq_max**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum frequency to analyze in GHz (None to max freq). The default value is `None`. 

**worst_is_higher**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Worst curve is the one with higher mean value. The default value is `True`. 

**curve_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [m,n] index of curves on which to search. None to search on all curves. The default value is `None`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot or not the chart. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Worst element, dictionary of ordered expression.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_worst_curve(freq_min=1.0, freq_max=1.0)

```
Copy to clipboard