---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_finite_conductivity.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_finite_conductivity 

Hfss.assign_finite_conductivity(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 58000000_, _permittivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _use_thickness : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _roughness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0um'_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_two_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_internal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_shell_element : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_huray : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _radius : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5um'_, _ratio : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.9'_, _height_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign finite conductivity to one or more objects or faces of a given material. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects or faces to assign finite conductivity to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material to use. The default is `None`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The default is `58000000`. If no material is provided, a value must be supplied. 

**permittivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permittivity. The default is `1`. If no material is provided, a value must be supplied. 

**use_thickness**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use thickness. The default is `False`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value if `usethickness=True`. The default is `"0.1mm"`. 

**roughness**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Roughness value with units. The default is `"0um"`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is an infinite ground. The default is `False`. 

**is_two_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is two-sided. The default is `False`. 

**is_internal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is internal. The default is `True`. 

**is_shell_element**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is a shell element. The default is `False`. 

**use_huray**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a Huray coefficient. The default is `False`. 

**radius**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Radius value if `usehuray=True`. The default is `"0.5um"`. 

**ratio**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Ratio value if `usehuray=True`. The default is `"2.9"`. 

**height_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Height standard deviation. This parameter is only valid in SBR+ designs. The default is `0.0`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignFiniteCond

```
Copy to clipboard
Examples
Create two cylinders in the XY working plane and assign a copper coating of 0.2 mm to the inner cylinder and outer face.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> outer = hfss.modeler.create_cylinder(Plane.XY, origin, 4, 200, 0, "outer")
>>> coat = hfss.assign_finite_conductivity(
...     ["inner", outer.faces[2].id], "copper", use_thickness=True, thickness="0.2mm"
... )

```
Copy to clipboard
# assign_finite_conductivity 

Hfss.assign_finite_conductivity(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 58000000_, _permittivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _use_thickness : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _roughness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0um'_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_two_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_internal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_shell_element : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_huray : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _radius : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5um'_, _ratio : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.9'_, _height_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign finite conductivity to one or more objects or faces of a given material. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects or faces to assign finite conductivity to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material to use. The default is `None`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The default is `58000000`. If no material is provided, a value must be supplied. 

**permittivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permittivity. The default is `1`. If no material is provided, a value must be supplied. 

**use_thickness**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use thickness. The default is `False`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value if `usethickness=True`. The default is `"0.1mm"`. 

**roughness**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Roughness value with units. The default is `"0um"`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is an infinite ground. The default is `False`. 

**is_two_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is two-sided. The default is `False`. 

**is_internal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is internal. The default is `True`. 

**is_shell_element**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is a shell element. The default is `False`. 

**use_huray**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a Huray coefficient. The default is `False`. 

**radius**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Radius value if `usehuray=True`. The default is `"0.5um"`. 

**ratio**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Ratio value if `usehuray=True`. The default is `"2.9"`. 

**height_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Height standard deviation. This parameter is only valid in SBR+ designs. The default is `0.0`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignFiniteCond

```
Copy to clipboard
Examples
Create two cylinders in the XY working plane and assign a copper coating of 0.2 mm to the inner cylinder and outer face.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> outer = hfss.modeler.create_cylinder(Plane.XY, origin, 4, 200, 0, "outer")
>>> coat = hfss.assign_finite_conductivity(
...     ["inner", outer.faces[2].id], "copper", use_thickness=True, thickness="0.2mm"
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_finite_conductivity.rst.txt)

# assign_finite_conductivity 

Hfss.assign_finite_conductivity(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 58000000_, _permittivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _use_thickness : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _roughness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0um'_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_two_side : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_internal : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_shell_element : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_huray : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _radius : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5um'_, _ratio : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.9'_, _height_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign finite conductivity to one or more objects or faces of a given material. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more objects or faces to assign finite conductivity to. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material to use. The default is `None`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The default is `58000000`. If no material is provided, a value must be supplied. 

**permittivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permittivity. The default is `1`. If no material is provided, a value must be supplied. 

**use_thickness**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use thickness. The default is `False`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value if `usethickness=True`. The default is `"0.1mm"`. 

**roughness**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Roughness value with units. The default is `"0um"`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is an infinite ground. The default is `False`. 

**is_two_side**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is two-sided. The default is `False`. 

**is_internal**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is internal. The default is `True`. 

**is_shell_element**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the finite conductivity is a shell element. The default is `False`. 

**use_huray**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a Huray coefficient. The default is `False`. 

**radius**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Radius value if `usehuray=True`. The default is `"0.5um"`. 

**ratio**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Ratio value if `usehuray=True`. The default is `"2.9"`. 

**height_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Height standard deviation. This parameter is only valid in SBR+ designs. The default is `0.0`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignFiniteCond

```
Copy to clipboard
Examples
Create two cylinders in the XY working plane and assign a copper coating of 0.2 mm to the inner cylinder and outer face.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> outer = hfss.modeler.create_cylinder(Plane.XY, origin, 4, 200, 0, "outer")
>>> coat = hfss.assign_finite_conductivity(
...     ["inner", outer.faces[2].id], "copper", use_thickness=True, thickness="0.2mm"
... )

```
Copy to clipboard