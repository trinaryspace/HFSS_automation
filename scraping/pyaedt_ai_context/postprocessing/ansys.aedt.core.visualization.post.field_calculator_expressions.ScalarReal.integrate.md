---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.integrate.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# integrate 

ScalarReal.integrate(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with the integration reduction appended.
Examples
Integrate a scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard
# integrate 

ScalarReal.integrate(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with the integration reduction appended.
Examples
Integrate a scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.integrate.rst.txt)

# integrate 

ScalarReal.integrate(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Integrate over a geometry `∫ s dΩ` (calculator `Integrate`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the integration. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with the integration reduction appended.
Examples
Integrate a scalar field over a line.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Line
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).integrate(Line("Polyline1")).operations[-1]
"Operation('Integrate')"

```
Copy to clipboard