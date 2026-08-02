---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_boundary.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_boundary 

Hfss.create_boundary(_boundary_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_inifinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Assign a boundary condition to a sheet or surface.
This method is generally used by other methods in the `Hfss` class such as the :meth:`Hfss.assign_febi` or :meth:`Hfss.assign_radiation_boundary_to_faces` method. 

Parameters: 
     

**boundary_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of boundary condition to assign to a sheet or surface. The default is `Hfss.BoundaryType.PerfectE`. Options are the properties of the :class:`Hfss.BoundaryType` class. For example:
>   * `Hfss.BoundaryType.PerfectE`
>   * `Hfss.BoundaryType.PerfectH`
>   * `Hfss.BoundaryType.Radiation`
>   * `Hfss.BoundaryType.Impedance`
>   * `Hfss.BoundaryType.LumpedRLC`
>   * `Hfss.BoundaryType.FEBI`
> 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Name of the sheet or face to assign the boundary condition to. The default is `None`. You can provide an integer (face ID), a string (sheet), or a list of integers and strings. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

**is_inifinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the boundary is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box = hfss.modeler.create_box([0, 0, 0], [10, 10, 10])
>>> box_pec = hfss.create_boundary(boundary_type=hfss.BoundaryType.PerfectE, assignment=box.name, name="my_pec")

```
Copy to clipboard
# create_boundary 

Hfss.create_boundary(_boundary_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_inifinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Assign a boundary condition to a sheet or surface.
This method is generally used by other methods in the `Hfss` class such as the :meth:`Hfss.assign_febi` or :meth:`Hfss.assign_radiation_boundary_to_faces` method. 

Parameters: 
     

**boundary_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of boundary condition to assign to a sheet or surface. The default is `Hfss.BoundaryType.PerfectE`. Options are the properties of the :class:`Hfss.BoundaryType` class. For example:
>   * `Hfss.BoundaryType.PerfectE`
>   * `Hfss.BoundaryType.PerfectH`
>   * `Hfss.BoundaryType.Radiation`
>   * `Hfss.BoundaryType.Impedance`
>   * `Hfss.BoundaryType.LumpedRLC`
>   * `Hfss.BoundaryType.FEBI`
> 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Name of the sheet or face to assign the boundary condition to. The default is `None`. You can provide an integer (face ID), a string (sheet), or a list of integers and strings. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

**is_inifinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the boundary is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box = hfss.modeler.create_box([0, 0, 0], [10, 10, 10])
>>> box_pec = hfss.create_boundary(boundary_type=hfss.BoundaryType.PerfectE, assignment=box.name, name="my_pec")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_boundary.rst.txt)

# create_boundary 

Hfss.create_boundary(_boundary_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_inifinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Assign a boundary condition to a sheet or surface.
This method is generally used by other methods in the `Hfss` class such as the :meth:`Hfss.assign_febi` or :meth:`Hfss.assign_radiation_boundary_to_faces` method. 

Parameters: 
     

**boundary_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of boundary condition to assign to a sheet or surface. The default is `Hfss.BoundaryType.PerfectE`. Options are the properties of the :class:`Hfss.BoundaryType` class. For example:
>   * `Hfss.BoundaryType.PerfectE`
>   * `Hfss.BoundaryType.PerfectH`
>   * `Hfss.BoundaryType.Radiation`
>   * `Hfss.BoundaryType.Impedance`
>   * `Hfss.BoundaryType.LumpedRLC`
>   * `Hfss.BoundaryType.FEBI`
> 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Name of the sheet or face to assign the boundary condition to. The default is `None`. You can provide an integer (face ID), a string (sheet), or a list of integers and strings. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

**is_inifinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the boundary is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box = hfss.modeler.create_box([0, 0, 0], [10, 10, 10])
>>> box_pec = hfss.create_boundary(boundary_type=hfss.BoundaryType.PerfectE, assignment=box.name, name="my_pec")

```
Copy to clipboard