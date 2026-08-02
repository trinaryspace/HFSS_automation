---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_cylindrical_gap 

Mesh.assign_cylindrical_gap(_entity : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _band_mapping_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _clone_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _moving_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _static_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → MeshOperation 
    
Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle. 

Parameters: 
     

**entity**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to assign cylindrical gap to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh. The default is `None`, in which case the default name is used. 

**clone_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the mesh. This parameter is valid only for 3D design. The default is `False`. If `True`, the solid bodies adjacent to the band are detected to identify the clone object. 

**band_mapping_angle**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Band mapping angle in degrees. The recommended band mapping angle (the angle the rotor rotates in one time step) typically equals the rotational speed multiplied by the time step. The band mapping angle must be between 0.0005 and 3 degrees. The default is `None`.
  * For a 2D design, if a value is provided, the option `Use band mapping angle` is automatically enabled.
  * For a 3D design, the `Clone Mesh` option has to be enabled first.

**moving_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the moving side. The valid ranges are integers greater or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

**static_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the static side. The valid ranges are integers greater than or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Mesh operation object or `False` if it fails.
References

```
>>> oModule.AssignCylindricalGapOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_cylindrical_gap(entity=["Box1"])

```
Copy to clipboard
# assign_cylindrical_gap 

Mesh.assign_cylindrical_gap(_entity : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _band_mapping_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _clone_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _moving_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _static_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → MeshOperation 
    
Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle. 

Parameters: 
     

**entity**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to assign cylindrical gap to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh. The default is `None`, in which case the default name is used. 

**clone_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the mesh. This parameter is valid only for 3D design. The default is `False`. If `True`, the solid bodies adjacent to the band are detected to identify the clone object. 

**band_mapping_angle**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Band mapping angle in degrees. The recommended band mapping angle (the angle the rotor rotates in one time step) typically equals the rotational speed multiplied by the time step. The band mapping angle must be between 0.0005 and 3 degrees. The default is `None`.
  * For a 2D design, if a value is provided, the option `Use band mapping angle` is automatically enabled.
  * For a 3D design, the `Clone Mesh` option has to be enabled first.

**moving_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the moving side. The valid ranges are integers greater or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

**static_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the static side. The valid ranges are integers greater than or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Mesh operation object or `False` if it fails.
References

```
>>> oModule.AssignCylindricalGapOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_cylindrical_gap(entity=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap.rst.txt)

# assign_cylindrical_gap 

Mesh.assign_cylindrical_gap(_entity : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _band_mapping_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _clone_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _moving_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _static_side_layers : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → MeshOperation 
    
Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle. 

Parameters: 
     

**entity**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to assign cylindrical gap to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh. The default is `None`, in which case the default name is used. 

**clone_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to clone the mesh. This parameter is valid only for 3D design. The default is `False`. If `True`, the solid bodies adjacent to the band are detected to identify the clone object. 

**band_mapping_angle**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Band mapping angle in degrees. The recommended band mapping angle (the angle the rotor rotates in one time step) typically equals the rotational speed multiplied by the time step. The band mapping angle must be between 0.0005 and 3 degrees. The default is `None`.
  * For a 2D design, if a value is provided, the option `Use band mapping angle` is automatically enabled.
  * For a 3D design, the `Clone Mesh` option has to be enabled first.

**moving_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the moving side. The valid ranges are integers greater or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

**static_side_layers**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh layers on the static side. The valid ranges are integers greater than or equal to 1. This parameter is valid only for a 3D design. The default is `1`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Mesh operation object or `False` if it fails.
References

```
>>> oModule.AssignCylindricalGapOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_cylindrical_gap(entity=["Box1"])

```
Copy to clipboard