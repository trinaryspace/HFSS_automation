---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_antenna.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_sbr_antenna 

Hfss.create_sbr_antenna(_antenna_type ='Conical Horn'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_current_source_representation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a parametric beam antennas in SBR+. 

Parameters: 
     

**antenna_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), SbrAntennas.ConicalHorn 
    
Name of the antennas type. The enumerator `SbrAntennas` can also be used. The default is `"SbrAntennas.Conical Horn"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coodiante system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters. The default is `None`. 

**use_current_source_representation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the current source representation. The default is `False`. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
NativeComponentObject object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> parm = {"Polarization": "Vertical"}
>>> par_beam = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, parameters=parm, name="TX1")
>>> custom_array = "my_file.sarr"
>>> antenna_array = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, custom_array=custom_array)
>>> antenna_array_parametric = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, is_array=True)

```
Copy to clipboard
# create_sbr_antenna 

Hfss.create_sbr_antenna(_antenna_type ='Conical Horn'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_current_source_representation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a parametric beam antennas in SBR+. 

Parameters: 
     

**antenna_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), SbrAntennas.ConicalHorn 
    
Name of the antennas type. The enumerator `SbrAntennas` can also be used. The default is `"SbrAntennas.Conical Horn"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coodiante system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters. The default is `None`. 

**use_current_source_representation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the current source representation. The default is `False`. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
NativeComponentObject object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> parm = {"Polarization": "Vertical"}
>>> par_beam = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, parameters=parm, name="TX1")
>>> custom_array = "my_file.sarr"
>>> antenna_array = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, custom_array=custom_array)
>>> antenna_array_parametric = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, is_array=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_antenna.rst.txt)

# create_sbr_antenna 

Hfss.create_sbr_antenna(_antenna_type ='Conical Horn'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _parameters : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_current_source_representation : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a parametric beam antennas in SBR+. 

Parameters: 
     

**antenna_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), SbrAntennas.ConicalHorn 
    
Name of the antennas type. The enumerator `SbrAntennas` can also be used. The default is `"SbrAntennas.Conical Horn"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coodiante system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**parameters**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters. The default is `None`. 

**use_current_source_representation**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the current source representation. The default is `False`. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
NativeComponentObject object.
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> parm = {"Polarization": "Vertical"}
>>> par_beam = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, parameters=parm, name="TX1")
>>> custom_array = "my_file.sarr"
>>> antenna_array = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, custom_array=custom_array)
>>> antenna_array_parametric = hfss.create_sbr_antenna(hfss.SbrAntennas.ShortDipole, is_array=True)

```
Copy to clipboard