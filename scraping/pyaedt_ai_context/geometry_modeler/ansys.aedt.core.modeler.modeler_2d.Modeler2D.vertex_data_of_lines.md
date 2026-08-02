---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.vertex_data_of_lines.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# vertex_data_of_lines 

Modeler2D.vertex_data_of_lines(_text_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate a dictionary of line vertex data for all lines contained within the design. 

Parameters: 
     

**text_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text string for filtering. The default is `None`. When a text string is specified, line data is generated only if this text string is contained within the line name. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the line name with a list of vertex positions in either 2D or 3D.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.vertex_data_of_lines(text_filter=1)

```
Copy to clipboard
# vertex_data_of_lines 

Modeler2D.vertex_data_of_lines(_text_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate a dictionary of line vertex data for all lines contained within the design. 

Parameters: 
     

**text_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text string for filtering. The default is `None`. When a text string is specified, line data is generated only if this text string is contained within the line name. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the line name with a list of vertex positions in either 2D or 3D.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.vertex_data_of_lines(text_filter=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.vertex_data_of_lines.rst.txt)

# vertex_data_of_lines 

Modeler2D.vertex_data_of_lines(_text_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate a dictionary of line vertex data for all lines contained within the design. 

Parameters: 
     

**text_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text string for filtering. The default is `None`. When a text string is specified, line data is generated only if this text string is contained within the line name. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the line name with a list of vertex positions in either 2D or 3D.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.vertex_data_of_lines(text_filter=1)

```
Copy to clipboard