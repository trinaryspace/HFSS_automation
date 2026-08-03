---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.edit_grid.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# edit_grid 

FarField.edit_grid(_minor_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _minor_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _style_minor : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _style_major : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _minor_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_, _major_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the grid settings for the plot. 

Parameters: 
     

**minor_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor X grid. The default is `True`. 

**minor_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor Y grid. The default is `True`. 

**major_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major X grid. The default is `True`. 

**major_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major Y grid. The default is `True`. 

**style_minor**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Minor grid style. The default is `"Solid"`. 

**style_major**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Major grid style. The default is `"Solid"`. 

**minor_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Minor grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

**major_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Major grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_grid()

```
Copy to clipboard
# edit_grid 

FarField.edit_grid(_minor_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _minor_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _style_minor : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _style_major : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _minor_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_, _major_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the grid settings for the plot. 

Parameters: 
     

**minor_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor X grid. The default is `True`. 

**minor_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor Y grid. The default is `True`. 

**major_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major X grid. The default is `True`. 

**major_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major Y grid. The default is `True`. 

**style_minor**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Minor grid style. The default is `"Solid"`. 

**style_major**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Major grid style. The default is `"Solid"`. 

**minor_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Minor grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

**major_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Major grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_grid()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.edit_grid.rst.txt)

# edit_grid 

FarField.edit_grid(_minor_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _minor_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_x : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _major_y : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _style_minor : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _style_major : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Solid'_, _minor_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_, _major_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the grid settings for the plot. 

Parameters: 
     

**minor_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor X grid. The default is `True`. 

**minor_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the minor Y grid. The default is `True`. 

**major_x**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major X grid. The default is `True`. 

**major_y**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the major Y grid. The default is `True`. 

**style_minor**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Minor grid style. The default is `"Solid"`. 

**style_major**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Major grid style. The default is `"Solid"`. 

**minor_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Minor grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

**major_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Major grid (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_grid()

```
Copy to clipboard