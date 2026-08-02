---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.far_field_wave.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# far_field_wave 

Hfss.far_field_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _simulate_source : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _preserve_source_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a far field wave excitation. 

Parameters: 
     

**assignment**`ansys.aedt.core.Hfss` or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source HFSS object from which to link the far field data, or path to an external far field data file (.ffd file). 

**setup**`optional` 
    
Name of the setup. The default is `None`, in which case a name is automatically assigned. This parameter is only used when `assignment` is an HFSS object. 

**simulate_source**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to force the source design to solve. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**preserve_source_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preserve the source solution. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use for the source. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Far field boundary object.
References

```
>>> oModule.AssignFarFieldWave

```
Copy to clipboard
Examples
Create a far field wave excitation from another design in the same project.

```
>>> from ansys.aedt.core import Hfss
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="target_project.aedt", design="Source_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external project.

```
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="source_project.aedt", design="Array_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external data file.

```
>>> target = Hfss(project="target_project.aedt")
>>> far_field_wave_src = target.far_field_wave(assignment="/path/to/farfield.ffd")

```
Copy to clipboard
# far_field_wave 

Hfss.far_field_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _simulate_source : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _preserve_source_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a far field wave excitation. 

Parameters: 
     

**assignment**`ansys.aedt.core.Hfss` or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source HFSS object from which to link the far field data, or path to an external far field data file (.ffd file). 

**setup**`optional` 
    
Name of the setup. The default is `None`, in which case a name is automatically assigned. This parameter is only used when `assignment` is an HFSS object. 

**simulate_source**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to force the source design to solve. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**preserve_source_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preserve the source solution. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use for the source. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Far field boundary object.
References

```
>>> oModule.AssignFarFieldWave

```
Copy to clipboard
Examples
Create a far field wave excitation from another design in the same project.

```
>>> from ansys.aedt.core import Hfss
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="target_project.aedt", design="Source_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external project.

```
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="source_project.aedt", design="Array_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external data file.

```
>>> target = Hfss(project="target_project.aedt")
>>> far_field_wave_src = target.far_field_wave(assignment="/path/to/farfield.ffd")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.far_field_wave.rst.txt)

# far_field_wave 

Hfss.far_field_wave(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _simulate_source : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _preserve_source_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a far field wave excitation. 

Parameters: 
     

**assignment**`ansys.aedt.core.Hfss` or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source HFSS object from which to link the far field data, or path to an external far field data file (.ffd file). 

**setup**`optional` 
    
Name of the setup. The default is `None`, in which case a name is automatically assigned. This parameter is only used when `assignment` is an HFSS object. 

**simulate_source**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to force the source design to solve. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**preserve_source_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preserve the source solution. The default is `True`. This parameter is only used when `assignment` is an HFSS object. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system to use for the source. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the excitation. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Far field boundary object.
References

```
>>> oModule.AssignFarFieldWave

```
Copy to clipboard
Examples
Create a far field wave excitation from another design in the same project.

```
>>> from ansys.aedt.core import Hfss
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="target_project.aedt", design="Source_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external project.

```
>>> target = Hfss(project="target_project.aedt")
>>> source = Hfss(project="source_project.aedt", design="Array_Design")
>>> setup = source.create_setup("Setup1", Frequency="10GHz")
>>> far_field_wave_src = target.far_field_wave(assignment=source, setup=setup)

```
Copy to clipboard
Create a far field wave excitation from an external data file.

```
>>> target = Hfss(project="target_project.aedt")
>>> far_field_wave_src = target.far_field_wave(assignment="/path/to/farfield.ffd")

```
Copy to clipboard