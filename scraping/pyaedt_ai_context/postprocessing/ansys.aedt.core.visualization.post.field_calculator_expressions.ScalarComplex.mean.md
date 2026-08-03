---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.mean.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# mean 

ScalarComplex.mean(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Mean`.
Examples
Compute the mean of a complex scalar field on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").mean(Surface("Sheet1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard
# mean 

ScalarComplex.mean(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Mean`.
Examples
Compute the mean of a complex scalar field on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").mean(Surface("Sheet1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.mean.rst.txt)

# mean 

ScalarComplex.mean(_over : CalculatorGeometry_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression reduced with `Mean`.
Examples
Compute the mean of a complex scalar field on a surface.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Surface
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").mean(Surface("Sheet1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard