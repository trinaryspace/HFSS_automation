---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.generate_unique_project_name.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# generate_unique_project_name 

ansys.aedt.core.generic.file_utils.generate_unique_project_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aedt'_) 
    
Generate a new AEDT project name given a root name. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Root name where the new project is to be created. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the folder to create. The default is `None`, in which case a random folder is created. Use `""` if you do not want to create a subfolder. 

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name for the project. The default is `None`, in which case a random project is created. If a project with this name already exists, a new suffix is added. 

**project_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Project format. The default is `"aedt"`. Options are `"aedt"` and `"aedb"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_project_name
>>> generate_unique_project_name(root_name=r"C:\Projects", project_name="Motor", project_format="aedt")

```
Copy to clipboard
# generate_unique_project_name 

ansys.aedt.core.generic.file_utils.generate_unique_project_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aedt'_) 
    
Generate a new AEDT project name given a root name. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Root name where the new project is to be created. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the folder to create. The default is `None`, in which case a random folder is created. Use `""` if you do not want to create a subfolder. 

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name for the project. The default is `None`, in which case a random project is created. If a project with this name already exists, a new suffix is added. 

**project_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Project format. The default is `"aedt"`. Options are `"aedt"` and `"aedb"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_project_name
>>> generate_unique_project_name(root_name=r"C:\Projects", project_name="Motor", project_format="aedt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.generate_unique_project_name.rst.txt)

# generate_unique_project_name 

ansys.aedt.core.generic.file_utils.generate_unique_project_name(_root_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _project_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aedt'_) 
    
Generate a new AEDT project name given a root name. 

Parameters: 
     

**root_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Root name where the new project is to be created. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the folder to create. The default is `None`, in which case a random folder is created. Use `""` if you do not want to create a subfolder. 

**project_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name for the project. The default is `None`, in which case a random project is created. If a project with this name already exists, a new suffix is added. 

**project_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Project format. The default is `"aedt"`. Options are `"aedt"` and `"aedb"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Newly generated name.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import generate_unique_project_name
>>> generate_unique_project_name(root_name=r"C:\Projects", project_name="Motor", project_format="aedt")

```
Copy to clipboard