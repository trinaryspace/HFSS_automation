---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_3d_component_array.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_3d_component_array 

Hfss.create_3d_component_array(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [ComponentArray](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray "ansys.aedt.core.modeler.cad.component_array.ComponentArray") 
    
Create a 3D component array from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the array information. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary to add or edit. 

Returns: 
     

`ComponentArray`
    
ComponentArray object.
Examples
Add a 3D component array from a json file. Below is the content of a json file that will be used in the following code sample.

```
{
    "primarylattice": "MyFirstLattice",
    "secondarylattice": "MySecondLattice",
    "useairobjects": true,
    "rowdimension": 4,
    "columndimension": 4,
    "visible": true,
    "showcellnumber": true,
    "paddingcells": 0,
    "referencecs": "Global",
    "MyFirstCell": "path/to/firstcell.a3dcomp",
    "MySecondCell": "path/to/secondcell.a3dcomp",
    "MyThirdCell": "path/to/thirdcell.a3dcomp",
    "cells": {
        "(1,1)": {
            "name": "MyFirstCell",
            "color": "(255,0,20)",
            "active": true,
            "postprocessing": true,
            "rotation": 0.0
        },
        "(1,2)": {
            "name": "MySecondCell",
            "rotation": 90.0
        }
    }
}

```
Copy to clipboard

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> hfss_app = Hfss()
>>> dict_in = read_configuration_file(r"path\to\json_file")
>>> component_array = hfss_app.create_3d_component_array(dict_in)

```
Copy to clipboard
# create_3d_component_array 

Hfss.create_3d_component_array(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [ComponentArray](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray "ansys.aedt.core.modeler.cad.component_array.ComponentArray") 
    
Create a 3D component array from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the array information. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary to add or edit. 

Returns: 
     

`ComponentArray`
    
ComponentArray object.
Examples
Add a 3D component array from a json file. Below is the content of a json file that will be used in the following code sample.

```
{
    "primarylattice": "MyFirstLattice",
    "secondarylattice": "MySecondLattice",
    "useairobjects": true,
    "rowdimension": 4,
    "columndimension": 4,
    "visible": true,
    "showcellnumber": true,
    "paddingcells": 0,
    "referencecs": "Global",
    "MyFirstCell": "path/to/firstcell.a3dcomp",
    "MySecondCell": "path/to/secondcell.a3dcomp",
    "MyThirdCell": "path/to/thirdcell.a3dcomp",
    "cells": {
        "(1,1)": {
            "name": "MyFirstCell",
            "color": "(255,0,20)",
            "active": true,
            "postprocessing": true,
            "rotation": 0.0
        },
        "(1,2)": {
            "name": "MySecondCell",
            "rotation": 90.0
        }
    }
}

```
Copy to clipboard

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> hfss_app = Hfss()
>>> dict_in = read_configuration_file(r"path\to\json_file")
>>> component_array = hfss_app.create_3d_component_array(dict_in)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_3d_component_array.rst.txt)

# create_3d_component_array 

Hfss.create_3d_component_array(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [ComponentArray](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray "ansys.aedt.core.modeler.cad.component_array.ComponentArray") 
    
Create a 3D component array from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the array information. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary to add or edit. 

Returns: 
     

`ComponentArray`
    
ComponentArray object.
Examples
Add a 3D component array from a json file. Below is the content of a json file that will be used in the following code sample.

```
{
    "primarylattice": "MyFirstLattice",
    "secondarylattice": "MySecondLattice",
    "useairobjects": true,
    "rowdimension": 4,
    "columndimension": 4,
    "visible": true,
    "showcellnumber": true,
    "paddingcells": 0,
    "referencecs": "Global",
    "MyFirstCell": "path/to/firstcell.a3dcomp",
    "MySecondCell": "path/to/secondcell.a3dcomp",
    "MyThirdCell": "path/to/thirdcell.a3dcomp",
    "cells": {
        "(1,1)": {
            "name": "MyFirstCell",
            "color": "(255,0,20)",
            "active": true,
            "postprocessing": true,
            "rotation": 0.0
        },
        "(1,2)": {
            "name": "MySecondCell",
            "rotation": 90.0
        }
    }
}

```
Copy to clipboard

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> hfss_app = Hfss()
>>> dict_in = read_configuration_file(r"path\to\json_file")
>>> component_array = hfss_app.create_3d_component_array(dict_in)

```
Copy to clipboard