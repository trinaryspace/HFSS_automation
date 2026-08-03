---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.verify.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# verify 

VectorComplex.verify() → FieldExpression 
    
Validate that the operation chain is well-formed and return `self`.
Useful as a fast, local check before sending a long expression to AEDT, where an unbalanced or oversized operation stack can otherwise fail in confusing ways. Chainable: `expr.verify().evaluate(...)`. 

Returns: 
     

`FieldExpression`
    
The same expression instance when the stack is balanced.
Examples
Validate an expression before materializing it.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> expr = fx.vector("E").magnitude().verify()
>>> expr.operations[-1]
"Operation('Mag')"

```
Copy to clipboard
# verify 

VectorComplex.verify() → FieldExpression 
    
Validate that the operation chain is well-formed and return `self`.
Useful as a fast, local check before sending a long expression to AEDT, where an unbalanced or oversized operation stack can otherwise fail in confusing ways. Chainable: `expr.verify().evaluate(...)`. 

Returns: 
     

`FieldExpression`
    
The same expression instance when the stack is balanced.
Examples
Validate an expression before materializing it.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> expr = fx.vector("E").magnitude().verify()
>>> expr.operations[-1]
"Operation('Mag')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.verify.rst.txt)

# verify 

VectorComplex.verify() → FieldExpression 
    
Validate that the operation chain is well-formed and return `self`.
Useful as a fast, local check before sending a long expression to AEDT, where an unbalanced or oversized operation stack can otherwise fail in confusing ways. Chainable: `expr.verify().evaluate(...)`. 

Returns: 
     

`FieldExpression`
    
The same expression instance when the stack is balanced.
Examples
Validate an expression before materializing it.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> expr = fx.vector("E").magnitude().verify()
>>> expr.operations[-1]
"Operation('Mag')"

```
Copy to clipboard