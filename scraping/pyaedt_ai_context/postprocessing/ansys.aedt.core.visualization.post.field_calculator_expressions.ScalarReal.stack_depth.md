---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.stack_depth.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# stack_depth 

ScalarReal.stack_depth() → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Net Fields Calculator stack depth after applying all operations.
Simulates the reverse-Polish operation stack. A well-formed scalar or vector expression resolves to exactly `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Final stack depth after simulating all operations.
Examples
Check that a simple expression resolves to one value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().stack_depth()
1

```
Copy to clipboard
# stack_depth 

ScalarReal.stack_depth() → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Net Fields Calculator stack depth after applying all operations.
Simulates the reverse-Polish operation stack. A well-formed scalar or vector expression resolves to exactly `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Final stack depth after simulating all operations.
Examples
Check that a simple expression resolves to one value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().stack_depth()
1

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.stack_depth.rst.txt)

# stack_depth 

ScalarReal.stack_depth() → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Net Fields Calculator stack depth after applying all operations.
Simulates the reverse-Polish operation stack. A well-formed scalar or vector expression resolves to exactly `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Final stack depth after simulating all operations.
Examples
Check that a simple expression resolves to one value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().stack_depth()
1

```
Copy to clipboard