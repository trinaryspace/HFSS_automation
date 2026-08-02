---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_model_resolution 

Mesh.assign_model_resolution(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _defeature_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign the model resolution. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to defeature. 

**defeature_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeaturing length in millimeters. The default is `None`, in which case automatic defeaturing is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignModelResolutionOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")

```
Copy to clipboard
# assign_model_resolution 

Mesh.assign_model_resolution(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _defeature_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign the model resolution. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to defeature. 

**defeature_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeaturing length in millimeters. The default is `None`, in which case automatic defeaturing is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignModelResolutionOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution.rst.txt)

# assign_model_resolution 

Mesh.assign_model_resolution(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _defeature_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign the model resolution. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to defeature. 

**defeature_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeaturing length in millimeters. The default is `None`, in which case automatic defeaturing is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignModelResolutionOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")

```
Copy to clipboard