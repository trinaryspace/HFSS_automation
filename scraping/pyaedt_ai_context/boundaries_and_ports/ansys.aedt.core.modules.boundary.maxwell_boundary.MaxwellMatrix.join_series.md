---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# join_series 

MaxwellMatrix.join_series(_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _join_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrix](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix") 
    
Create matrix reduction by joining sources in series. 

Parameters: 
     

**sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sources to be included in matrix reduction. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reduced matrix name. 

**join_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Join operation. 

Returns: 
     

[`MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")
    
Reduced matrix object.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellMatrix
>>> obj = MaxwellMatrix()
>>> obj.join_series(sources=["Box1"])

```
Copy to clipboard
# join_series 

MaxwellMatrix.join_series(_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _join_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrix](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix") 
    
Create matrix reduction by joining sources in series. 

Parameters: 
     

**sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sources to be included in matrix reduction. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reduced matrix name. 

**join_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Join operation. 

Returns: 
     

[`MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")
    
Reduced matrix object.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellMatrix
>>> obj = MaxwellMatrix()
>>> obj.join_series(sources=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series.rst.txt)

# join_series 

MaxwellMatrix.join_series(_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _join_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrix](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix") 
    
Create matrix reduction by joining sources in series. 

Parameters: 
     

**sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sources to be included in matrix reduction. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reduced matrix name. 

**join_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Join operation. 

Returns: 
     

[`MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")
    
Reduced matrix object.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellMatrix
>>> obj = MaxwellMatrix()
>>> obj.join_series(sources=["Box1"])

```
Copy to clipboard