---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.add_limit_line_from_equation.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# add_limit_line_from_equation 

Fields.add_limit_line_from_equation(_start_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _equation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'x'_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**start_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start X value. 

**stop_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stop X value. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X step value. 

**equation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y equation to apply. The default is Y=X. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the X axis. The default is `"GHz"`. 

**y_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_equation(0, 10, 1, "x", "GHz", 1)

```
Copy to clipboard
# add_limit_line_from_equation 

Fields.add_limit_line_from_equation(_start_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _equation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'x'_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**start_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start X value. 

**stop_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stop X value. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X step value. 

**equation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y equation to apply. The default is Y=X. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the X axis. The default is `"GHz"`. 

**y_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_equation(0, 10, 1, "x", "GHz", 1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.add_limit_line_from_equation.rst.txt)

# add_limit_line_from_equation 

Fields.add_limit_line_from_equation(_start_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _equation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'x'_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**start_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start X value. 

**stop_x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stop X value. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X step value. 

**equation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y equation to apply. The default is Y=X. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the X axis. The default is `"GHz"`. 

**y_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is `1`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_equation(0, 10, 1, "x", "GHz", 1)

```
Copy to clipboard