---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.plane_wave.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# plane_wave 

Hfss.plane_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _vector_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Spherical'_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polarization : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _propagation_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _wave_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Propagating'_, _wave_type_properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a plane wave excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more objects or faces to assign finite conductivity to. The default is `None`, in which case the excitation is assigned to anything. 

**vector_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vector input format. Options are `"Spherical"` or `"Cartesian"`. The default is `"Spherical"`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Excitation location and zero phase position. The default is `["0mm", "0mm", "0mm"]`. 

**polarization**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Electric field polarization vector. If `"Vertical"` or `"Horizontal"` is passed, the method computes the electric polarization vector. If a `list` is passed, the user can customize the input vector. If `vector_format` is `"Cartesian"`, the vector has three coordinates which corresponds to `["Ex", "Ey", "Ez"]`. If `vector_format` is `"Spherical"`, the vector has two coordinates which corresponds to `["Ephi", "Etheta"]`. The default is `"Vertical"`. 

**propagation_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Propagation vector. If `vector_format` is `"Cartesian"` the type must be a `list` with three elements. If `vector_format` is `"Spherical"` the type must be a `list` with two elements. The first element corresponds to the phi sweep, which must be a `list` of three elements: start, stop, and number of points. The second element has the same format, it corresponds to the theta sweep. The default is `[0.0, 0.0, 1.0]` for `"Cartesian"` and `[["0.0deg", "0.0deg", 1], ["0.0deg", "0.0deg", 1]]` for `"Spherical"`. 

**wave_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of plane wave. Options are `"Propagating"`, `"Evanescent"`, or `"Elliptical"`. The default is `"Propagating"`. 

**wave_type_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties of the plane wave type. If `"Propagating"` is used, no additional properties are needed. The default is `None`. If `"Evanescent"` is selected, the propagation constant is expressed as both real and imaginary components. The default is `[0.0, 1.0]`. If `"Elliptical"` is used, the polarization angle and ratio are defined. The default is `["0deg", 1.0]`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

`ansys.aedt.core.modules.Boundary.BoundaryObject`
    
Port object.
References

```
>>> oModule.AssignPlaneWave

```
Copy to clipboard
Examples
Create a plane wave excitation.

```
>>> port1 = hfss.plane_wave(vector_format="Spherical",
 ...                        polarization="Vertical",
 ...                        propagation_vector=[["0deg","90deg", 25], ["0deg","0deg", 1]])
>>> port2 = hfss.plane_wave(vector_format="Cartesian",
 ...                        polarization=[1, 1, 0], propagation_vector=[0, 0, 1])

```
Copy to clipboard
# plane_wave 

Hfss.plane_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _vector_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Spherical'_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polarization : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _propagation_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _wave_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Propagating'_, _wave_type_properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a plane wave excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more objects or faces to assign finite conductivity to. The default is `None`, in which case the excitation is assigned to anything. 

**vector_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vector input format. Options are `"Spherical"` or `"Cartesian"`. The default is `"Spherical"`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Excitation location and zero phase position. The default is `["0mm", "0mm", "0mm"]`. 

**polarization**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Electric field polarization vector. If `"Vertical"` or `"Horizontal"` is passed, the method computes the electric polarization vector. If a `list` is passed, the user can customize the input vector. If `vector_format` is `"Cartesian"`, the vector has three coordinates which corresponds to `["Ex", "Ey", "Ez"]`. If `vector_format` is `"Spherical"`, the vector has two coordinates which corresponds to `["Ephi", "Etheta"]`. The default is `"Vertical"`. 

**propagation_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Propagation vector. If `vector_format` is `"Cartesian"` the type must be a `list` with three elements. If `vector_format` is `"Spherical"` the type must be a `list` with two elements. The first element corresponds to the phi sweep, which must be a `list` of three elements: start, stop, and number of points. The second element has the same format, it corresponds to the theta sweep. The default is `[0.0, 0.0, 1.0]` for `"Cartesian"` and `[["0.0deg", "0.0deg", 1], ["0.0deg", "0.0deg", 1]]` for `"Spherical"`. 

**wave_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of plane wave. Options are `"Propagating"`, `"Evanescent"`, or `"Elliptical"`. The default is `"Propagating"`. 

**wave_type_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties of the plane wave type. If `"Propagating"` is used, no additional properties are needed. The default is `None`. If `"Evanescent"` is selected, the propagation constant is expressed as both real and imaginary components. The default is `[0.0, 1.0]`. If `"Elliptical"` is used, the polarization angle and ratio are defined. The default is `["0deg", 1.0]`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

`ansys.aedt.core.modules.Boundary.BoundaryObject`
    
Port object.
References

```
>>> oModule.AssignPlaneWave

```
Copy to clipboard
Examples
Create a plane wave excitation.

```
>>> port1 = hfss.plane_wave(vector_format="Spherical",
 ...                        polarization="Vertical",
 ...                        propagation_vector=[["0deg","90deg", 25], ["0deg","0deg", 1]])
>>> port2 = hfss.plane_wave(vector_format="Cartesian",
 ...                        polarization=[1, 1, 0], propagation_vector=[0, 0, 1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.plane_wave.rst.txt)

# plane_wave 

Hfss.plane_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _vector_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Spherical'_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polarization : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _propagation_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _wave_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Propagating'_, _wave_type_properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a plane wave excitation. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more objects or faces to assign finite conductivity to. The default is `None`, in which case the excitation is assigned to anything. 

**vector_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vector input format. Options are `"Spherical"` or `"Cartesian"`. The default is `"Spherical"`. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Excitation location and zero phase position. The default is `["0mm", "0mm", "0mm"]`. 

**polarization**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Electric field polarization vector. If `"Vertical"` or `"Horizontal"` is passed, the method computes the electric polarization vector. If a `list` is passed, the user can customize the input vector. If `vector_format` is `"Cartesian"`, the vector has three coordinates which corresponds to `["Ex", "Ey", "Ez"]`. If `vector_format` is `"Spherical"`, the vector has two coordinates which corresponds to `["Ephi", "Etheta"]`. The default is `"Vertical"`. 

**propagation_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Propagation vector. If `vector_format` is `"Cartesian"` the type must be a `list` with three elements. If `vector_format` is `"Spherical"` the type must be a `list` with two elements. The first element corresponds to the phi sweep, which must be a `list` of three elements: start, stop, and number of points. The second element has the same format, it corresponds to the theta sweep. The default is `[0.0, 0.0, 1.0]` for `"Cartesian"` and `[["0.0deg", "0.0deg", 1], ["0.0deg", "0.0deg", 1]]` for `"Spherical"`. 

**wave_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of plane wave. Options are `"Propagating"`, `"Evanescent"`, or `"Elliptical"`. The default is `"Propagating"`. 

**wave_type_properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Properties of the plane wave type. If `"Propagating"` is used, no additional properties are needed. The default is `None`. If `"Evanescent"` is selected, the propagation constant is expressed as both real and imaginary components. The default is `[0.0, 1.0]`. If `"Elliptical"` is used, the polarization angle and ratio are defined. The default is `["0deg", 1.0]`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

`ansys.aedt.core.modules.Boundary.BoundaryObject`
    
Port object.
References

```
>>> oModule.AssignPlaneWave

```
Copy to clipboard
Examples
Create a plane wave excitation.

```
>>> port1 = hfss.plane_wave(vector_format="Spherical",
 ...                        polarization="Vertical",
 ...                        propagation_vector=[["0deg","90deg", 25], ["0deg","0deg", 1]])
>>> port2 = hfss.plane_wave(vector_format="Cartesian",
 ...                        polarization=[1, 1, 0], propagation_vector=[0, 0, 1])

```
Copy to clipboard