---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# vector_constant 

FieldExpressions.vector_constant(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Create a constant real vector. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X component. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y component. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Z component. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Vector_Constant`.
Examples
Create a constant vector through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector_constant(1, 0, 0).operations
['Vector_Constant(1, 0, 0)']

```
Copy to clipboard
# vector_constant 

FieldExpressions.vector_constant(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Create a constant real vector. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X component. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y component. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Z component. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Vector_Constant`.
Examples
Create a constant vector through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector_constant(1, 0, 0).operations
['Vector_Constant(1, 0, 0)']

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant.rst.txt)

# vector_constant 

FieldExpressions.vector_constant(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _z : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") 
    
Create a constant real vector. 

Parameters: 
     

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X component. 

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y component. 

**z**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Z component. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal")
    
Real vector expression seeded with `Vector_Constant`.
Examples
Create a constant vector through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector_constant(1, 0, 0).operations
['Vector_Constant(1, 0, 0)']

```
Copy to clipboard