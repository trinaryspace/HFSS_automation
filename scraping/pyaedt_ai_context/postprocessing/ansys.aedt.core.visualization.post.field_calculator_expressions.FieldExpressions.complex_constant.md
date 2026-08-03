---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# complex_constant 

FieldExpressions.complex_constant(_real : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _imag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Create a complex scalar constant. 

Parameters: 
     

**real**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Real part of the constant. 

**imag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Imaginary part of the constant. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression seeded with `Complex_Constant`.
Examples
Create a complex constant through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.complex_constant(1, 2).operations
['Complex_Constant(1, 2)']

```
Copy to clipboard
# complex_constant 

FieldExpressions.complex_constant(_real : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _imag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Create a complex scalar constant. 

Parameters: 
     

**real**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Real part of the constant. 

**imag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Imaginary part of the constant. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression seeded with `Complex_Constant`.
Examples
Create a complex constant through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.complex_constant(1, 2).operations
['Complex_Constant(1, 2)']

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant.rst.txt)

# complex_constant 

FieldExpressions.complex_constant(_real : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _imag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Create a complex scalar constant. 

Parameters: 
     

**real**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Real part of the constant. 

**imag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Imaginary part of the constant. 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression seeded with `Complex_Constant`.
Examples
Create a complex constant through the builder.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.complex_constant(1, 2).operations
['Complex_Constant(1, 2)']

```
Copy to clipboard