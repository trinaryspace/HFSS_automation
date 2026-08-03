---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.integrate.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# integrate 

ScalarComplex.integrate(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Integrate`.
Examples
Integrate a complex scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard
# integrate 

ScalarComplex.integrate(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Integrate`.
Examples
Integrate a complex scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.integrate.rst.txt)

# integrate 

ScalarComplex.integrate(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Integrate`.
Examples
Integrate a complex scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard