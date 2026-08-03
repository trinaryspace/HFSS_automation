---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_orthogonal_matrix.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_orthogonal_matrix 

static GeometryOperators.is_orthogonal_matrix(_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a given 3x3 matrix is orthogonal.
An orthogonal matrix is a square matrix whose rows and columns are orthonormal vectors. This method verifies if the transpose of the matrix multiplied by the matrix itself results in an identity matrix within a specified tolerance. 

Parameters: 
     

**matrix**`List`[`List`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] 
    
A 3x3 matrix represented as a list of lists. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance for numerical comparison. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if the matrix is orthogonal, False otherwise.
Examples
Check if a matrix is orthogonal:

```
>>> matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> is_orthogonal_matrix(matrix)
False

```
Copy to clipboard
# is_orthogonal_matrix 

static GeometryOperators.is_orthogonal_matrix(_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a given 3x3 matrix is orthogonal.
An orthogonal matrix is a square matrix whose rows and columns are orthonormal vectors. This method verifies if the transpose of the matrix multiplied by the matrix itself results in an identity matrix within a specified tolerance. 

Parameters: 
     

**matrix**`List`[`List`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] 
    
A 3x3 matrix represented as a list of lists. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance for numerical comparison. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if the matrix is orthogonal, False otherwise.
Examples
Check if a matrix is orthogonal:

```
>>> matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> is_orthogonal_matrix(matrix)
False

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_orthogonal_matrix.rst.txt)

# is_orthogonal_matrix 

static GeometryOperators.is_orthogonal_matrix(_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a given 3x3 matrix is orthogonal.
An orthogonal matrix is a square matrix whose rows and columns are orthonormal vectors. This method verifies if the transpose of the matrix multiplied by the matrix itself results in an identity matrix within a specified tolerance. 

Parameters: 
     

**matrix**`List`[`List`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] 
    
A 3x3 matrix represented as a list of lists. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Tolerance for numerical comparison. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if the matrix is orthogonal, False otherwise.
Examples
Check if a matrix is orthogonal:

```
>>> matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
>>> is_orthogonal_matrix(matrix)
True

```
Copy to clipboard

```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> is_orthogonal_matrix(matrix)
False

```
Copy to clipboard