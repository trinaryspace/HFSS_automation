---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.maximum.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# maximum 

ScalarReal.maximum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Maximum over a geometry (calculator `Maximum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Maximum`.
Examples
Compute the maximum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).maximum(Surface("Sheet1")).operations[-1]
"Operation('Maximum')"

```
Copy to clipboard
# maximum 

ScalarReal.maximum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Maximum over a geometry (calculator `Maximum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Maximum`.
Examples
Compute the maximum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).maximum(Surface("Sheet1")).operations[-1]
"Operation('Maximum')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.maximum.rst.txt)

# maximum 

ScalarReal.maximum(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Maximum over a geometry (calculator `Maximum`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Maximum`.
Examples
Compute the maximum on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).maximum(Surface("Sheet1")).operations[-1]
"Operation('Maximum')"

```
Copy to clipboard