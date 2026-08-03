---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# write 

FieldsCalculator.write(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save the content of the stack register for future reuse in a later Field Calculator session. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File path to save the stack entry to. File extension must be either `.fld` or `.reg`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> file_path = Path(hfss.working_directory) / "my_expr.fld"
>>> hfss.post.fields_calculator.write("voltage_line", file_path, hfss.nominal_adaptive)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# write 

FieldsCalculator.write(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save the content of the stack register for future reuse in a later Field Calculator session. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File path to save the stack entry to. File extension must be either `.fld` or `.reg`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> file_path = Path(hfss.working_directory) / "my_expr.fld"
>>> hfss.post.fields_calculator.write("voltage_line", file_path, hfss.nominal_adaptive)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write.rst.txt)

# write 

FieldsCalculator.write(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Save the content of the stack register for future reuse in a later Field Calculator session. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File path to save the stack entry to. File extension must be either `.fld` or `.reg`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> file_path = Path(hfss.working_directory) / "my_expr.fld"
>>> hfss.post.fields_calculator.write("voltage_line", file_path, hfss.nominal_adaptive)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard