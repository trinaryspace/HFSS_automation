---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_field_extremum.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_field_extremum 

PostProcessorIcepak.get_field_extremum(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_min : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Max', 'Min']_, _location : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Surface', 'Volume']_, _field : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Calculate the position and value of the field maximum or minimum. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the object to calculate the extremum for. 

**max_min**`Literal`[“Max”, “Min”] 
    
“Max” for maximum, “Min” for minimum. 

**location**`Literal`[“Surface”, “Volume”] 
    
“Surface” for surface, “Volume” for volume. 

**field** str: 
    
Name of the field. 

**intrinsics**`Optional`[[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]] 
    
Time at which to retrieve results if setup is transient. Default is None. 

**setup**`Optional`[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
The name of the setup to use. If None, the first available setup is used. Default is None. 

Returns: 
     

`Tuple`[`Tuple`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]
     

`A` [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") containing:
    
  * A tuple of three floats representing the (x, y, z) coordinates of the maximum point.
  * A float representing the value associated with the maximum point.

Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_field_extremum(assignment="Box1", max_min=1, location=1, field=1)

```
Copy to clipboard
# get_field_extremum 

PostProcessorIcepak.get_field_extremum(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_min : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Max', 'Min']_, _location : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Surface', 'Volume']_, _field : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Calculate the position and value of the field maximum or minimum. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the object to calculate the extremum for. 

**max_min**`Literal`[“Max”, “Min”] 
    
“Max” for maximum, “Min” for minimum. 

**location**`Literal`[“Surface”, “Volume”] 
    
“Surface” for surface, “Volume” for volume. 

**field** str: 
    
Name of the field. 

**intrinsics**`Optional`[[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]] 
    
Time at which to retrieve results if setup is transient. Default is None. 

**setup**`Optional`[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
The name of the setup to use. If None, the first available setup is used. Default is None. 

Returns: 
     

`Tuple`[`Tuple`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]
     

`A` [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") containing:
    
  * A tuple of three floats representing the (x, y, z) coordinates of the maximum point.
  * A float representing the value associated with the maximum point.

Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_field_extremum(assignment="Box1", max_min=1, location=1, field=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_field_extremum.rst.txt)

# get_field_extremum 

PostProcessorIcepak.get_field_extremum(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_min : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Max', 'Min']_, _location : [Literal](https://docs.python.org/3.11/library/typing.html#typing.Literal "\(in Python v3.11\)")['Surface', 'Volume']_, _field : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Calculate the position and value of the field maximum or minimum. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the object to calculate the extremum for. 

**max_min**`Literal`[“Max”, “Min”] 
    
“Max” for maximum, “Min” for minimum. 

**location**`Literal`[“Surface”, “Volume”] 
    
“Surface” for surface, “Volume” for volume. 

**field** str: 
    
Name of the field. 

**intrinsics**`Optional`[[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]] 
    
Time at which to retrieve results if setup is transient. Default is None. 

**setup**`Optional`[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
The name of the setup to use. If None, the first available setup is used. Default is None. 

Returns: 
     

`Tuple`[`Tuple`[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]
     

`A` [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") containing:
    
  * A tuple of three floats representing the (x, y, z) coordinates of the maximum point.
  * A float representing the value associated with the maximum point.

Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_field_extremum(assignment="Box1", max_min=1, location=1, field=1)

```
Copy to clipboard