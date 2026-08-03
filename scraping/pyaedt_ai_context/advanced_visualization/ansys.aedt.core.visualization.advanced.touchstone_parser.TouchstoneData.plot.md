---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot 

TouchstoneData.plot(_index_couples : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot a list of curves. 

Parameters: 
     

**index_couples**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of indexes couple to plot. The default value is `None` to plot all `port_tuples`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to plot. The default value is `True`. 

Returns: 
     

`matplotlib.plt`
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot(index_couples=["Box1"], show=True)

```
Copy to clipboard
# plot 

TouchstoneData.plot(_index_couples : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot a list of curves. 

Parameters: 
     

**index_couples**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of indexes couple to plot. The default value is `None` to plot all `port_tuples`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to plot. The default value is `True`. 

Returns: 
     

`matplotlib.plt`
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot(index_couples=["Box1"], show=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot.rst.txt)

# plot 

TouchstoneData.plot(_index_couples : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot a list of curves. 

Parameters: 
     

**index_couples**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of indexes couple to plot. The default value is `None` to plot all `port_tuples`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to plot. The default value is `True`. 

Returns: 
     

`matplotlib.plt`
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot(index_couples=["Box1"], show=True)

```
Copy to clipboard