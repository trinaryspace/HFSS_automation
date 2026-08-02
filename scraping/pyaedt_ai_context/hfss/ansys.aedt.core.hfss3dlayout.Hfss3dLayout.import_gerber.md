---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.import_gerber.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# import_gerber 

Hfss3dLayout.import_gerber(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _control_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _set_as_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_active_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a Gerber zip file into HFSS 3D Layout and assign the stackup from an XML file if present. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the Gerber zip file. 

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDB folder. For example, `"c:\temp\test.aedb"`. 

**control_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the XML file with the stackup information. The default is `None`, in which case the stackup is not edited. 

**set_as_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the Gerber zip file file as active. The default is `True`. 

**close_active_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active project after loading the Gerber zip file file. The default is ‘’False``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ImportGerber

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.import_gerber(input_file="c:/temp/design.zip")

```
Copy to clipboard
# import_gerber 

Hfss3dLayout.import_gerber(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _control_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _set_as_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_active_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a Gerber zip file into HFSS 3D Layout and assign the stackup from an XML file if present. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the Gerber zip file. 

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDB folder. For example, `"c:\temp\test.aedb"`. 

**control_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the XML file with the stackup information. The default is `None`, in which case the stackup is not edited. 

**set_as_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the Gerber zip file file as active. The default is `True`. 

**close_active_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active project after loading the Gerber zip file file. The default is ‘’False``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ImportGerber

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.import_gerber(input_file="c:/temp/design.zip")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.import_gerber.rst.txt)

# import_gerber 

Hfss3dLayout.import_gerber(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _control_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _set_as_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_active_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a Gerber zip file into HFSS 3D Layout and assign the stackup from an XML file if present. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the Gerber zip file. 

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the AEDB folder. For example, `"c:\temp\test.aedb"`. 

**control_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the XML file with the stackup information. The default is `None`, in which case the stackup is not edited. 

**set_as_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the Gerber zip file file as active. The default is `True`. 

**close_active_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active project after loading the Gerber zip file file. The default is ‘’False``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ImportGerber

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> hfss3d.import_gerber(input_file="c:/temp/design.zip")

```
Copy to clipboard