---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.read_design_data.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# read_design_data 

Hfss3dLayout.read_design_data() → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Read back the design data as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of design data.
Examples
After generating design data and storing it as .json file, retrieve it as a dictionary.

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d(solution_type="Transient")
>>> m2d["width"] = "10mm"
>>> m2d["height"] = "15mm"
>>> m2d.modeler.create_rectangle(origin=[0, 0, 0], sizes=["width", "height"])
>>> m2d.generate_design_data()
>>> data = m2d.read_design_data()
>>> m2d.release_desktop(True, True)

```
Copy to clipboard
# read_design_data 

Hfss3dLayout.read_design_data() → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Read back the design data as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of design data.
Examples
After generating design data and storing it as .json file, retrieve it as a dictionary.

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d(solution_type="Transient")
>>> m2d["width"] = "10mm"
>>> m2d["height"] = "15mm"
>>> m2d.modeler.create_rectangle(origin=[0, 0, 0], sizes=["width", "height"])
>>> m2d.generate_design_data()
>>> data = m2d.read_design_data()
>>> m2d.release_desktop(True, True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.read_design_data.rst.txt)

# read_design_data 

Hfss3dLayout.read_design_data() → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Read back the design data as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of design data.
Examples
After generating design data and storing it as .json file, retrieve it as a dictionary.

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d(solution_type="Transient")
>>> m2d["width"] = "10mm"
>>> m2d["height"] = "15mm"
>>> m2d.modeler.create_rectangle(origin=[0, 0, 0], sizes=["width", "height"])
>>> m2d.generate_design_data()
>>> data = m2d.read_design_data()
>>> m2d.release_desktop(True, True)

```
Copy to clipboard