---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.generate_temp_project_directory.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# generate_temp_project_directory 

Hfss.generate_temp_project_directory(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate a unique directory string to save a project to.
This method creates a directory for storage of a project in the `temp` directory of the AEDT installation because this location is guaranteed to exist. If the `name` parameter is defined, a subdirectory is added within the `temp` directory and a hash suffix is added to ensure that this directory is empty and has a unique name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Base name of the subdirectory to create in the `temp` directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Base name of the created subdirectory.
Examples

```
>>> m3d = Maxwell3d()
>>> proj_directory = m3d.generate_temp_project_directory("Example")

```
Copy to clipboard
# generate_temp_project_directory 

Hfss.generate_temp_project_directory(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate a unique directory string to save a project to.
This method creates a directory for storage of a project in the `temp` directory of the AEDT installation because this location is guaranteed to exist. If the `name` parameter is defined, a subdirectory is added within the `temp` directory and a hash suffix is added to ensure that this directory is empty and has a unique name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Base name of the subdirectory to create in the `temp` directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Base name of the created subdirectory.
Examples

```
>>> m3d = Maxwell3d()
>>> proj_directory = m3d.generate_temp_project_directory("Example")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.generate_temp_project_directory.rst.txt)

# generate_temp_project_directory 

Hfss.generate_temp_project_directory(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate a unique directory string to save a project to.
This method creates a directory for storage of a project in the `temp` directory of the AEDT installation because this location is guaranteed to exist. If the `name` parameter is defined, a subdirectory is added within the `temp` directory and a hash suffix is added to ensure that this directory is empty and has a unique name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Base name of the subdirectory to create in the `temp` directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Base name of the created subdirectory.
Examples

```
>>> m3d = Maxwell3d()
>>> proj_directory = m3d.generate_temp_project_directory("Example")

```
Copy to clipboard