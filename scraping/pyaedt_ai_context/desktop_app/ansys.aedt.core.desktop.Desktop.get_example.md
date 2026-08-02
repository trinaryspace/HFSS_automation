---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_example.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# get_example 

Desktop.get_example(_example_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '.'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Retrieve the path to a built-in example project. 

Parameters: 
     

**example_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the example for which the full path is desired. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the subfolder in the `"Examples"` folder where the example having `example_name` can be found. The default is `"."` which points to `self.install_path / "Examples"` 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
Return the path to the example file if found, otherwise `None`.
Examples
Create a copy of a built-in example.

```
>>> import shutil
>>> from ansys.aedt.core import Desktop
>>> from pathlib import Path
>>> working_folder = Path("C:/") / "path" / "to" / "target_folder"  # Windows
>>> d = Desktop(version=261)
>>> example_path = d.get_example("5G_SIW_Aperture_Antenna")
>>> new_project = working_folder / example_path.name
>>> working_folder.mkdir(parents=True, exist_ok=True)
>>> shutil.copytree(example_path, new_project)  # Copy example to new working folder.

```
Copy to clipboard
# get_example 

Desktop.get_example(_example_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '.'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Retrieve the path to a built-in example project. 

Parameters: 
     

**example_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the example for which the full path is desired. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the subfolder in the `"Examples"` folder where the example having `example_name` can be found. The default is `"."` which points to `self.install_path / "Examples"` 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
Return the path to the example file if found, otherwise `None`.
Examples
Create a copy of a built-in example.

```
>>> import shutil
>>> from ansys.aedt.core import Desktop
>>> from pathlib import Path
>>> working_folder = Path("C:/") / "path" / "to" / "target_folder"  # Windows
>>> d = Desktop(version=261)
>>> example_path = d.get_example("5G_SIW_Aperture_Antenna")
>>> new_project = working_folder / example_path.name
>>> working_folder.mkdir(parents=True, exist_ok=True)
>>> shutil.copytree(example_path, new_project)  # Copy example to new working folder.

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_example.rst.txt)

# get_example 

Desktop.get_example(_example_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '.'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Retrieve the path to a built-in example project. 

Parameters: 
     

**example_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the example for which the full path is desired. 

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the subfolder in the `"Examples"` folder where the example having `example_name` can be found. The default is `"."` which points to `self.install_path / "Examples"` 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
Return the path to the example file if found, otherwise `None`.
Examples
Create a copy of a built-in example.

```
>>> import shutil
>>> from ansys.aedt.core import Desktop
>>> from pathlib import Path
>>> working_folder = Path("C:/") / "path" / "to" / "target_folder"  # Windows
>>> d = Desktop(version=261)
>>> example_path = d.get_example("5G_SIW_Aperture_Antenna")
>>> new_project = working_folder / example_path.name
>>> working_folder.mkdir(parents=True, exist_ok=True)
>>> shutil.copytree(example_path, new_project)  # Copy example to new working folder.

```
Copy to clipboard