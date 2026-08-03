---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.curl.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# curl 

VectorComplex.curl() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Curl `∇×v` (calculator `Curl`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression containing the curl.
Examples
Compute the curl of a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").curl().operations[-1]
"Operation('Curl')"

```
Copy to clipboard
# curl 

VectorComplex.curl() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Curl `∇×v` (calculator `Curl`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression containing the curl.
Examples
Compute the curl of a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").curl().operations[-1]
"Operation('Curl')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.curl.rst.txt)

# curl 

VectorComplex.curl() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Curl `∇×v` (calculator `Curl`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression containing the curl.
Examples
Compute the curl of a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").curl().operations[-1]
"Operation('Curl')"

```
Copy to clipboard