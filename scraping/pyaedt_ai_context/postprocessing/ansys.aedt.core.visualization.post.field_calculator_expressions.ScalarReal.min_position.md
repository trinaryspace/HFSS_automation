---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.min_position.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# min_position 

ScalarReal.min_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the minimum over a geometry (calculator `MinPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the minimum position.
Examples
Find the minimum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).min_position(Surface("Sheet1")).operations[-1]
"Operation('MinPos')"

```
Copy to clipboard
# min_position 

ScalarReal.min_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the minimum over a geometry (calculator `MinPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the minimum position.
Examples
Find the minimum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).min_position(Surface("Sheet1")).operations[-1]
"Operation('MinPos')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.min_position.rst.txt)

# min_position 

ScalarReal.min_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the minimum over a geometry (calculator `MinPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the minimum position.
Examples
Find the minimum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).min_position(Surface("Sheet1")).operations[-1]
"Operation('MinPos')"

```
Copy to clipboard