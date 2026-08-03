---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# tangent_vector 

FieldExpressions.tangent_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit tangent vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Tangent')` for use in tangential projections such as `dot(field, fx.tangent())`.
Examples
Seed a tangent vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.tangent_vector().operations
["Operation('Tangent')"]

```
Copy to clipboard
# tangent_vector 

FieldExpressions.tangent_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit tangent vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Tangent')` for use in tangential projections such as `dot(field, fx.tangent())`.
Examples
Seed a tangent vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.tangent_vector().operations
["Operation('Tangent')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector.rst.txt)

# tangent_vector 

FieldExpressions.tangent_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit tangent vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Tangent')` for use in tangential projections such as `dot(field, fx.tangent())`.
Examples
Seed a tangent vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.tangent_vector().operations
["Operation('Tangent')"]

```
Copy to clipboard