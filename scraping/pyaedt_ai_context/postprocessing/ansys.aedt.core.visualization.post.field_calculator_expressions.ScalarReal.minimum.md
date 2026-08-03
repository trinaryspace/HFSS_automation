---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.minimum.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# minimum 

ScalarReal.minimum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Minimum over a geometry (calculator `Minimum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Minimum`.
Examples
Compute the minimum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).minimum(Surface("Sheet1")).operations[-1]
"Operation('Minimum')"

```
Copy to clipboard
# minimum 

ScalarReal.minimum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Minimum over a geometry (calculator `Minimum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Minimum`.
Examples
Compute the minimum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).minimum(Surface("Sheet1")).operations[-1]
"Operation('Minimum')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.minimum.rst.txt)

# minimum 

ScalarReal.minimum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Minimum over a geometry (calculator `Minimum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Minimum`.
Examples
Compute the minimum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).minimum(Surface("Sheet1")).operations[-1]
"Operation('Minimum')"

```
Copy to clipboard