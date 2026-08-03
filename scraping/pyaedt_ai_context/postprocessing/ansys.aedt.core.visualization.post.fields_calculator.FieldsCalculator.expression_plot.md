---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# expression_plot 

FieldsCalculator.expression_plot(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create plots defined in the expression catalog. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Calculation type. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of assignments to apply the expression to. If the expression is not general, assignment is not needed. 

**names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the expressions to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created reports.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> reports = hfss.post.fields_calculator.expression_plot("voltage_line", "Polyline1", [name])
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# expression_plot 

FieldsCalculator.expression_plot(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create plots defined in the expression catalog. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Calculation type. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of assignments to apply the expression to. If the expression is not general, assignment is not needed. 

**names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the expressions to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created reports.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> reports = hfss.post.fields_calculator.expression_plot("voltage_line", "Polyline1", [name])
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot.rst.txt)

# expression_plot 

FieldsCalculator.expression_plot(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create plots defined in the expression catalog. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Calculation type. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of assignments to apply the expression to. If the expression is not general, assignment is not needed. 

**names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Name of the expressions to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of created reports.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> reports = hfss.post.fields_calculator.expression_plot("voltage_line", "Polyline1", [name])
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard