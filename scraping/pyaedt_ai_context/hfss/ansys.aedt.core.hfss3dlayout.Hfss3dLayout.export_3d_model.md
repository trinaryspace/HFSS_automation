---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_3d_model.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# export_3d_model 

Hfss3dLayout.export_3d_model(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the Ecad model to a 3D file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full name of the file to export. The default is `None`, in which case the file name is set to the design name and saved as a SAT file in the working directory. Extensions available are `"sat"`, `"sab"`, and `"sm3"` up to AEDT 2022 R2 and Parasolid format “x_t” from AEDT 2023R1. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name if successful.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.export_3d_model()

```
Copy to clipboard
# export_3d_model 

Hfss3dLayout.export_3d_model(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the Ecad model to a 3D file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full name of the file to export. The default is `None`, in which case the file name is set to the design name and saved as a SAT file in the working directory. Extensions available are `"sat"`, `"sab"`, and `"sm3"` up to AEDT 2022 R2 and Parasolid format “x_t” from AEDT 2023R1. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name if successful.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.export_3d_model()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_3d_model.rst.txt)

# export_3d_model 

Hfss3dLayout.export_3d_model(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the Ecad model to a 3D file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full name of the file to export. The default is `None`, in which case the file name is set to the design name and saved as a SAT file in the working directory. Extensions available are `"sat"`, `"sab"`, and `"sm3"` up to AEDT 2022 R2 and Parasolid format “x_t” from AEDT 2023R1. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name if successful.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.export_3d_model()

```
Copy to clipboard