---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_expression 

FieldsCalculator.add_expression(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _assignment_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add named expression. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Calculation type. If provided as a string, it has to be a name defined in the expression_catalog.toml. If provided as a dict, it has to contain all the necessary arguments to define an expression. For reference look at the expression_catalog.toml. 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

:class:[`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#id1)ansys.aedt.core.modeler.cad.FacePrimitive
    
Name of the object to add the named expression from. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Named expression when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> my_expression = {
...     "name": "test",
...     "description": "Voltage drop along a line",
...     "design_type": ["HFSS", "Q3D Extractor"],
...     "fields_type": ["Fields", "CG Fields"],
...     "solution_type": "",
...     "primary_sweep": "Freq",
...     "assignment": "",
...     "assignment_type": ["Line"],
...     "operations": [
...         "Fundamental_Quantity('E')",
...         "Operation('Real')",
...         "Operation('Tangent')",
...         "Operation('Dot')",
...         "EnterLine('assignment')",
...         "Operation('LineValue')",
...         "Operation('Integrate')",
...         "Operation('CmplxR')",
...     ],
...     "report": ["Data Table", "Rectangular Plot"],
... }
>>> expr_name = hfss.post.fields_calculator.add_expression(my_expression, "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# add_expression 

FieldsCalculator.add_expression(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _assignment_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add named expression. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Calculation type. If provided as a string, it has to be a name defined in the expression_catalog.toml. If provided as a dict, it has to contain all the necessary arguments to define an expression. For reference look at the expression_catalog.toml. 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

:class:[`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#id1)ansys.aedt.core.modeler.cad.FacePrimitive
    
Name of the object to add the named expression from. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Named expression when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> my_expression = {
...     "name": "test",
...     "description": "Voltage drop along a line",
...     "design_type": ["HFSS", "Q3D Extractor"],
...     "fields_type": ["Fields", "CG Fields"],
...     "solution_type": "",
...     "primary_sweep": "Freq",
...     "assignment": "",
...     "assignment_type": ["Line"],
...     "operations": [
...         "Fundamental_Quantity('E')",
...         "Operation('Real')",
...         "Operation('Tangent')",
...         "Operation('Dot')",
...         "EnterLine('assignment')",
...         "Operation('LineValue')",
...         "Operation('Integrate')",
...         "Operation('CmplxR')",
...     ],
...     "report": ["Data Table", "Rectangular Plot"],
... }
>>> expr_name = hfss.post.fields_calculator.add_expression(my_expression, "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.rst.txt)

# add_expression 

FieldsCalculator.add_expression(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _assignment_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add named expression. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Calculation type. If provided as a string, it has to be a name defined in the expression_catalog.toml. If provided as a dict, it has to contain all the necessary arguments to define an expression. For reference look at the expression_catalog.toml. 

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

:class:[`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#id1)ansys.aedt.core.modeler.cad.FacePrimitive
    
Name of the object to add the named expression from. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Named expression when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> my_expression = {
...     "name": "test",
...     "description": "Voltage drop along a line",
...     "design_type": ["HFSS", "Q3D Extractor"],
...     "fields_type": ["Fields", "CG Fields"],
...     "solution_type": "",
...     "primary_sweep": "Freq",
...     "assignment": "",
...     "assignment_type": ["Line"],
...     "operations": [
...         "Fundamental_Quantity('E')",
...         "Operation('Real')",
...         "Operation('Tangent')",
...         "Operation('Dot')",
...         "EnterLine('assignment')",
...         "Operation('LineValue')",
...         "Operation('Integrate')",
...         "Operation('CmplxR')",
...     ],
...     "report": ["Data Table", "Rectangular Plot"],
... }
>>> expr_name = hfss.post.fields_calculator.add_expression(my_expression, "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard