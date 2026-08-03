---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# plot 

ModelPlotter.plot(_export_image_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current available Data. With s key a screenshot is saved in export_image_path or in tempdir. 

Parameters: 
     

**export_image_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to image to save. Default is None 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the pyvista plot. When False, a :class::pyvista.Plotter object is created and assigned to the pv property so that it can be modified further. Default is True. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.plot(export_image_path="example.png", show=True)

```
Copy to clipboard
# plot 

ModelPlotter.plot(_export_image_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current available Data. With s key a screenshot is saved in export_image_path or in tempdir. 

Parameters: 
     

**export_image_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to image to save. Default is None 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the pyvista plot. When False, a :class::pyvista.Plotter object is created and assigned to the pv property so that it can be modified further. Default is True. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.plot(export_image_path="example.png", show=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot.rst.txt)

# plot 

ModelPlotter.plot(_export_image_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current available Data. With s key a screenshot is saved in export_image_path or in tempdir. 

Parameters: 
     

**export_image_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to image to save. Default is None 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the pyvista plot. When False, a :class::pyvista.Plotter object is created and assigned to the pv property so that it can be modified further. Default is True. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.plot(export_image_path="example.png", show=True)

```
Copy to clipboard