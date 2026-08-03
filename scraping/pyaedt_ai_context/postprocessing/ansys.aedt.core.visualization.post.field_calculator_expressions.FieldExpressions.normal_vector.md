---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# normal_vector 

FieldExpressions.normal_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit normal vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Normal')` for use in normal-flux or projection calculations.
Examples
Seed a normal vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.normal_vector().operations
["Operation('Normal')"]

```
Copy to clipboard
# normal_vector 

FieldExpressions.normal_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit normal vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Normal')` for use in normal-flux or projection calculations.
Examples
Seed a normal vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.normal_vector().operations
["Operation('Normal')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector.rst.txt)

# normal_vector 

FieldExpressions.normal_vector() → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Push the geometry unit normal vector. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Operation('Normal')` for use in normal-flux or projection calculations.
Examples
Seed a normal vector for later projections.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.normal_vector().operations
["Operation('Normal')"]

```
Copy to clipboard