---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Emission.edit_header.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# edit_header 

Emission.edit_header(_company_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'PyAEDT'_, _show_design_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _font : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Arial'_, _title_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _subtitle_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _italic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _bold : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the plot header. 

Parameters: 
     

**company_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Company name. The default is `PyAEDT`. 

**show_design_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the design name in the plot. The default is `True`. 

**font**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Font name. The default is `"Arial"`. 

**title_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Title font size. The default is `12`. 

**subtitle_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subtitle font size. The default is `12`. 

**italic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use italic type. The default is `False`. 

**bold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use bold type. The default is `False`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Title (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_header()

```
Copy to clipboard
# edit_header 

Emission.edit_header(_company_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'PyAEDT'_, _show_design_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _font : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Arial'_, _title_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _subtitle_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _italic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _bold : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the plot header. 

Parameters: 
     

**company_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Company name. The default is `PyAEDT`. 

**show_design_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the design name in the plot. The default is `True`. 

**font**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Font name. The default is `"Arial"`. 

**title_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Title font size. The default is `12`. 

**subtitle_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subtitle font size. The default is `12`. 

**italic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use italic type. The default is `False`. 

**bold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use bold type. The default is `False`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Title (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_header()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Emission.edit_header.rst.txt)

# edit_header 

Emission.edit_header(_company_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'PyAEDT'_, _show_design_name : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _font : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Arial'_, _title_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _subtitle_size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 12_, _italic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _bold : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 0, 0)_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit the plot header. 

Parameters: 
     

**company_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Company name. The default is `PyAEDT`. 

**show_design_name**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the design name in the plot. The default is `True`. 

**font**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Font name. The default is `"Arial"`. 

**title_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Title font size. The default is `12`. 

**subtitle_size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subtitle font size. The default is `12`. 

**italic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use italic type. The default is `False`. 

**bold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use bold type. The default is `False`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Title (R, G, B) color. The default is `(0, 0, 0)`. Each color value must be an integer in a range from 0 to 255. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.edit_header()

```
Copy to clipboard