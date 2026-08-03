---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_rcs 

MonostaticRCSExporter.export_rcs(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'rcs_data'_, _metadata_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'pyaedt_rcs_metadata'_, _only_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Export RCS solution data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the RCS data file. The default is `"rcs_data"`. 

**metadata_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the metadata file. The default is `"pyaedt_rcs_metadata"`. 

**only_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export only the geometry. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Metadata file.
Examples

```
>>> from ansys.aedt.core.visualization.post.rcs_exporter import MonostaticRCSExporter
>>> obj = MonostaticRCSExporter()
>>> obj.export_rcs(name="MyObject", metadata_name=1)

```
Copy to clipboard
# export_rcs 

MonostaticRCSExporter.export_rcs(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'rcs_data'_, _metadata_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'pyaedt_rcs_metadata'_, _only_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Export RCS solution data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the RCS data file. The default is `"rcs_data"`. 

**metadata_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the metadata file. The default is `"pyaedt_rcs_metadata"`. 

**only_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export only the geometry. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Metadata file.
Examples

```
>>> from ansys.aedt.core.visualization.post.rcs_exporter import MonostaticRCSExporter
>>> obj = MonostaticRCSExporter()
>>> obj.export_rcs(name="MyObject", metadata_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs.rst.txt)

# export_rcs 

MonostaticRCSExporter.export_rcs(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'rcs_data'_, _metadata_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'pyaedt_rcs_metadata'_, _only_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Export RCS solution data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the RCS data file. The default is `"rcs_data"`. 

**metadata_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the metadata file. The default is `"pyaedt_rcs_metadata"`. 

**only_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Export only the geometry. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Metadata file.
Examples

```
>>> from ansys.aedt.core.visualization.post.rcs_exporter import MonostaticRCSExporter
>>> obj = MonostaticRCSExporter()
>>> obj.export_rcs(name="MyObject", metadata_name=1)

```
Copy to clipboard