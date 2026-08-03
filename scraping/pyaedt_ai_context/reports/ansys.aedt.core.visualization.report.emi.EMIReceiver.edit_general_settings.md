---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.edit_general_settings.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# edit_general_settings 

EMIReceiver.edit_general_settings(_background_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _plot_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _enable_y_stripes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _field_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _use_scientific_notation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit general settings for the plot. 

Parameters: 
     

**background_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Backgoround (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**plot_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Plot (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**enable_y_stripes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable Y stripes. The default is `True`. 

**field_width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field width. The default is `4`. 

**precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field precision. The default is `4`. 

**use_scientific_notation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable scientific notation. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_general_settings()

```
Copy to clipboard
# edit_general_settings 

EMIReceiver.edit_general_settings(_background_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _plot_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _enable_y_stripes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _field_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _use_scientific_notation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit general settings for the plot. 

Parameters: 
     

**background_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Backgoround (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**plot_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Plot (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**enable_y_stripes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable Y stripes. The default is `True`. 

**field_width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field width. The default is `4`. 

**precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field precision. The default is `4`. 

**use_scientific_notation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable scientific notation. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_general_settings()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.edit_general_settings.rst.txt)

# edit_general_settings 

EMIReceiver.edit_general_settings(_background_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _plot_color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (255, 255, 255)_, _enable_y_stripes : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _field_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _use_scientific_notation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit general settings for the plot. 

Parameters: 
     

**background_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Backgoround (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**plot_color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Plot (R, G, B) color. The default is `(255, 255, 255)`. Each color value must be an integer in a range from 0 to 255. 

**enable_y_stripes**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable Y stripes. The default is `True`. 

**field_width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field width. The default is `4`. 

**precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Field precision. The default is `4`. 

**use_scientific_notation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable scientific notation. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_general_settings()

```
Copy to clipboard