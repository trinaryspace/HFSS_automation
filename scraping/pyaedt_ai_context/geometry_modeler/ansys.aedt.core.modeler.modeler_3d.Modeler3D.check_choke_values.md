---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.check_choke_values.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# check_choke_values 

Modeler3D.check_choke_values(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _create_another_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Verify the values in the json file and create another one with corrected values next to the first one. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to json file; Specific json file containing all the parameters to design your on choke. 

**create_another_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Create another file next to the first one in adding _Corrected to the file name if it is True else truncate the existing file 

Returns: 
     

`List`
    
`True` when successful, `False` when failed. 

**dictionary**`class` ‘dict’ 
    
Examples
Dictionary of the Json file has to be like the following example : dictionary = { “Number of Windings”: {“1”: True, “2”: False, “3”: False, “4”: False}, “Layer”: {“Simple”: True, “Double”: False, “Triple”: False}, “Layer Type”: {“Separate”: True, “Linked”: False}, “Similar Layer”: {“Similar”: True, “Different”: False}, “Mode”: {“Differential”: True, “Common”: False}, “Wire Section”: {“None”: False, “Hexagon”: False, “Octagon”: True, “Circle”: False}, “Core”: {“Name”: “Core”, “Material”: “ferrite”, “Inner Radius”: 11, “Outer Radius”: 17, “Height”: 7, “Chamfer”: 0.8}, “Outer Winding”: {“Name”: “Winding”, “Material”: “copper”, “Inner Radius”: 12, “Outer Radius”: 16, “Height”: 8, “Wire Diameter”: 1, “Turns”: 10, “Coil Pit(deg)”: 9, “Occupation(%)”: 0}, “Mid Winding”: {“Turns”: 8, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0}, “Inner Winding”: {“Turns”: 12, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0} }

```
>>> import json
>>> with open("C:/Example/Of/Path/myJsonFile.json", "w") as outfile:
>>>     json.dump(dictionary, outfile)
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")

```
Copy to clipboard
# check_choke_values 

Modeler3D.check_choke_values(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _create_another_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Verify the values in the json file and create another one with corrected values next to the first one. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to json file; Specific json file containing all the parameters to design your on choke. 

**create_another_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Create another file next to the first one in adding _Corrected to the file name if it is True else truncate the existing file 

Returns: 
     

`List`
    
`True` when successful, `False` when failed. 

**dictionary**`class` ‘dict’ 
    
Examples
Dictionary of the Json file has to be like the following example : dictionary = { “Number of Windings”: {“1”: True, “2”: False, “3”: False, “4”: False}, “Layer”: {“Simple”: True, “Double”: False, “Triple”: False}, “Layer Type”: {“Separate”: True, “Linked”: False}, “Similar Layer”: {“Similar”: True, “Different”: False}, “Mode”: {“Differential”: True, “Common”: False}, “Wire Section”: {“None”: False, “Hexagon”: False, “Octagon”: True, “Circle”: False}, “Core”: {“Name”: “Core”, “Material”: “ferrite”, “Inner Radius”: 11, “Outer Radius”: 17, “Height”: 7, “Chamfer”: 0.8}, “Outer Winding”: {“Name”: “Winding”, “Material”: “copper”, “Inner Radius”: 12, “Outer Radius”: 16, “Height”: 8, “Wire Diameter”: 1, “Turns”: 10, “Coil Pit(deg)”: 9, “Occupation(%)”: 0}, “Mid Winding”: {“Turns”: 8, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0}, “Inner Winding”: {“Turns”: 12, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0} }

```
>>> import json
>>> with open("C:/Example/Of/Path/myJsonFile.json", "w") as outfile:
>>>     json.dump(dictionary, outfile)
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.check_choke_values.rst.txt)

# check_choke_values 

Modeler3D.check_choke_values(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _create_another_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Verify the values in the json file and create another one with corrected values next to the first one. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to json file; Specific json file containing all the parameters to design your on choke. 

**create_another_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Create another file next to the first one in adding _Corrected to the file name if it is True else truncate the existing file 

Returns: 
     

`List`
    
`True` when successful, `False` when failed. 

**dictionary**`class` ‘dict’ 
    
Examples
Dictionary of the Json file has to be like the following example : dictionary = { “Number of Windings”: {“1”: True, “2”: False, “3”: False, “4”: False}, “Layer”: {“Simple”: True, “Double”: False, “Triple”: False}, “Layer Type”: {“Separate”: True, “Linked”: False}, “Similar Layer”: {“Similar”: True, “Different”: False}, “Mode”: {“Differential”: True, “Common”: False}, “Wire Section”: {“None”: False, “Hexagon”: False, “Octagon”: True, “Circle”: False}, “Core”: {“Name”: “Core”, “Material”: “ferrite”, “Inner Radius”: 11, “Outer Radius”: 17, “Height”: 7, “Chamfer”: 0.8}, “Outer Winding”: {“Name”: “Winding”, “Material”: “copper”, “Inner Radius”: 12, “Outer Radius”: 16, “Height”: 8, “Wire Diameter”: 1, “Turns”: 10, “Coil Pit(deg)”: 9, “Occupation(%)”: 0}, “Mid Winding”: {“Turns”: 8, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0}, “Inner Winding”: {“Turns”: 12, “Coil Pit(deg)”: 0.1, “Occupation(%)”: 0} }

```
>>> import json
>>> with open("C:/Example/Of/Path/myJsonFile.json", "w") as outfile:
>>>     json.dump(dictionary, outfile)
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dictionary_values = hfss.modeler.check_choke_values("C:/Example/Of/Path/myJsonFile.json")

```
Copy to clipboard