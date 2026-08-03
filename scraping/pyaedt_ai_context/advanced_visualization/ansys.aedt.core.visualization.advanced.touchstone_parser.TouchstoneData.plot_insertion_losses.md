---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot_insertion_losses.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_insertion_losses 

TouchstoneData.plot_insertion_losses(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Plot all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of tuples representing insertion loss excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_insertion_losses(threshold=1.0, plot=True)

```
Copy to clipboard
# plot_insertion_losses 

TouchstoneData.plot_insertion_losses(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Plot all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of tuples representing insertion loss excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_insertion_losses(threshold=1.0, plot=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot_insertion_losses.rst.txt)

# plot_insertion_losses 

TouchstoneData.plot_insertion_losses(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_, _plot : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Plot all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

**plot**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of tuples representing insertion loss excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_insertion_losses(threshold=1.0, plot=True)

```
Copy to clipboard