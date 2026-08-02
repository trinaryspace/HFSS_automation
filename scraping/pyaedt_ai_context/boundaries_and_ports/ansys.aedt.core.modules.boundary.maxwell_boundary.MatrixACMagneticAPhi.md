---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# MatrixACMagneticAPhi 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi(_rl_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[RLSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")]_, _gc_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GCSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for AC Magnetic A-Phi solver. 

Parameters: 
     

**rl_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")] 
    
List of RL sources. 

**gc_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")] 
    
List of GC sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixACMagneticAPhi
>>> obj = MatrixACMagneticAPhi()

```
Copy to clipboard
Attributes  
| [`MatrixACMagneticAPhi.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixACMagneticAPhi.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources")  | Value for rl sources.  |  
| [`MatrixACMagneticAPhi.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources")  | Value for gc sources.  |  
# MatrixACMagneticAPhi 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi(_rl_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[RLSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")]_, _gc_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GCSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for AC Magnetic A-Phi solver. 

Parameters: 
     

**rl_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")] 
    
List of RL sources. 

**gc_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")] 
    
List of GC sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixACMagneticAPhi
>>> obj = MatrixACMagneticAPhi()

```
Copy to clipboard
Attributes  
| [`MatrixACMagneticAPhi.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixACMagneticAPhi.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources")  | Value for rl sources.  |  
| [`MatrixACMagneticAPhi.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources")  | Value for gc sources.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rst.txt)

# MatrixACMagneticAPhi 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi(_rl_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[RLSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")]_, _gc_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[GCSourceACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")]_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Matrix assignment for AC Magnetic A-Phi solver. 

Parameters: 
     

**rl_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")] 
    
List of RL sources. 

**gc_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")] 
    
List of GC sources. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the matrix. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixACMagneticAPhi
>>> obj = MatrixACMagneticAPhi()

```
Copy to clipboard
Attributes  
| [`MatrixACMagneticAPhi.matrix_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.matrix_name")  | Value for matrix name.  |  
| --- | --- |  
| [`MatrixACMagneticAPhi.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.rl_sources")  | Value for rl sources.  |  
| [`MatrixACMagneticAPhi.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.gc_sources")  | Value for gc sources.  |