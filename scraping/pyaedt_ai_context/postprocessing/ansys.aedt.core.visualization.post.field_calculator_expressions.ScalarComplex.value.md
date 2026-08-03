---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.value.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# value 

ScalarComplex.value(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression evaluated on the provided geometry.
Examples
Sample a complex scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard
# value 

ScalarComplex.value(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression evaluated on the provided geometry.
Examples
Sample a complex scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.value.rst.txt)

# value 

ScalarComplex.value(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Sample the quantity on a geometry without integrating. 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the field-value lookup. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression evaluated on the provided geometry.
Examples
Sample a complex scalar quantity on a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").value(Line("Polyline1")).operations[-1]
"Operation('LineValue')"

```
Copy to clipboard