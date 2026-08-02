---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_file_based_antenna.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_sbr_file_based_antenna 

Hfss.create_sbr_file_based_antenna(_far_field_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _antenna_size : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _antenna_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50ohm'_, _representation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a linked antenna. 

Parameters: 
     

**far_field_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the FFD file. 

**antenna_size**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna size with units. The default is `"1mm"`. 

**antenna_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna impedance with units. The default is `"50ohm"`. 

**representation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the antennas. Options are `"Far Field"` and `"Near Field"`. The default is `"Far Field"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coordinate system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "full_path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)

```
Copy to clipboard
# create_sbr_file_based_antenna 

Hfss.create_sbr_file_based_antenna(_far_field_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _antenna_size : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _antenna_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50ohm'_, _representation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a linked antenna. 

Parameters: 
     

**far_field_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the FFD file. 

**antenna_size**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna size with units. The default is `"1mm"`. 

**antenna_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna impedance with units. The default is `"50ohm"`. 

**representation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the antennas. Options are `"Far Field"` and `"Near Field"`. The default is `"Far Field"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coordinate system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "full_path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_file_based_antenna.rst.txt)

# create_sbr_file_based_antenna 

Hfss.create_sbr_file_based_antenna(_far_field_data : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _antenna_size : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _antenna_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50ohm'_, _representation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field'_, _target_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_array : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _custom_array : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NativeComponentObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject") 
    
Create a linked antenna. 

Parameters: 
     

**far_field_data**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the FFD file. 

**antenna_size**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna size with units. The default is `"1mm"`. 

**antenna_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Antenna impedance with units. The default is `"50ohm"`. 

**representation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the antennas. Options are `"Far Field"` and `"Near Field"`. The default is `"Far Field"`. 

**target_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Target coordinate system. The default is `None`, in which case the active coordinate system is used. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Model units to apply to the object. The default is `None`, in which case the active modeler units are applied. 

**is_array**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to define a parametric array. The default is `False`. 

**custom_array**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Custom array file. The extensions supported are `".sarr"`. The default is `None`, in which case parametric array is created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the 3D component. The default is `None`, in which case the name is auto-generated based on the antenna type. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")
    
References

```
>>> oEditor.InsertNativeComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "full_path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)

```
Copy to clipboard