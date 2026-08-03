---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.max_position.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# max_position 

ScalarReal.max_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the maximum over a geometry (calculator `MaxPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the maximum position.
Examples
Find the maximum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).max_position(Surface("Sheet1")).operations[-1]
"Operation('MaxPos')"

```
Copy to clipboard
# max_position 

ScalarReal.max_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the maximum over a geometry (calculator `MaxPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the maximum position.
Examples
Find the maximum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).max_position(Surface("Sheet1")).operations[-1]
"Operation('MaxPos')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.max_position.rst.txt)

# max_position 

ScalarReal.max_position(_over : CalculatorGeometry_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Position of the maximum over a geometry (calculator `MaxPos`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression locating the maximum position.
Examples
Find the maximum position on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).max_position(Surface("Sheet1")).operations[-1]
"Operation('MaxPos')"

```
Copy to clipboard