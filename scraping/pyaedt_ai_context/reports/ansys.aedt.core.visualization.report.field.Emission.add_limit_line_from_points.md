---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Emission.add_limit_line_from_points.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# add_limit_line_from_points 

Emission.add_limit_line_from_points(_x_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Y1'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**x_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float inputs. 

**y_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float y values. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `x_list` parameter. The default is `""`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `y_list` parameter. The default is `""`. 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is “Y1”. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_points([0, 0], [0, 0], "GHz", "V", "Y1")

```
Copy to clipboard
# add_limit_line_from_points 

Emission.add_limit_line_from_points(_x_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Y1'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**x_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float inputs. 

**y_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float y values. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `x_list` parameter. The default is `""`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `y_list` parameter. The default is `""`. 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is “Y1”. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_points([0, 0], [0, 0], "GHz", "V", "Y1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Emission.add_limit_line_from_points.rst.txt)

# add_limit_line_from_points 

Emission.add_limit_line_from_points(_x_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _y_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Y1'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Cartesian limit line from point lists. This method works only in graphical mode. 

Parameters: 
     

**x_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float inputs. 

**y_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of float y values. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `x_list` parameter. The default is `""`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the `y_list` parameter. The default is `""`. 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Y axis. The default is “Y1”. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.add_limit_line_from_points([0, 0], [0, 0], "GHz", "V", "Y1")

```
Copy to clipboard