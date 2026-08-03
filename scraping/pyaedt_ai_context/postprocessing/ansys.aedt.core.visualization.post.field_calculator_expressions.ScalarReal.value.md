---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.value.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# value 

ScalarReal.value(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated on the provided geometry.
Examples
Sample a scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard
# value 

ScalarReal.value(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated on the provided geometry.
Examples
Sample a scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.value.rst.txt)

# value 

ScalarReal.value(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated on the provided geometry.
Examples
Sample a scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard