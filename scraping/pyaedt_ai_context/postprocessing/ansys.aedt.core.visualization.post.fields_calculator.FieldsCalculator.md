---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# FieldsCalculator 

class ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator(_app_) 
    
Provides the Advanced fields calculator methods.
Provide methods to add, load and delete named expressions on top of the already existing ones in AEDT Fields calculator. 

Parameters: 
     

**app**
    
Inherited parent object.
Examples
Custom expressions can be added as dictionary on-the-fly:

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
or they can be added from the `expression_catalog.toml`:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
Methods  
| [`FieldsCalculator.add_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression")(calculation, ...)  | Add named expression.  |  
| --- | --- |  
| [`FieldsCalculator.create_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file")(...)  | Create a calculator expression file.  |  
| [`FieldsCalculator.delete_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression")([name])  | Delete a named expression.  |  
| [`FieldsCalculator.evaluate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate")(expression[, ...])  | Evaluate an expression and return the value.  |  
| [`FieldsCalculator.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export")(quantity[, ...])  | Export the field quantity at the top of the register to a file, mapping it to a grid of points.  |  
| [`FieldsCalculator.expression_plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot")(...[, setup])  | Create plots defined in the expression catalog.  |  
| [`FieldsCalculator.get_expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions")([field_type])  | Get dictionary of available Field Calculator expressions.  |  
| [`FieldsCalculator.is_expression_defined`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined")(name)  | Check if a named expression exists.  |  
| [`FieldsCalculator.is_general_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression")(name)  | Check if a named expression is general.  |  
| [`FieldsCalculator.load_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file")(input_file)  | Load expressions from an external TOML file.  |  
| [`FieldsCalculator.validate_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression")(expression)  | Validate expression file against the schema.  |  
| [`FieldsCalculator.write`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write")(expression, output_file)  | Save the content of the stack register for future reuse in a later Field Calculator session.  |  
Attributes  
| [`FieldsCalculator.expression_names`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names")  | List of available expressions.  |  
| --- | --- |  
| [`FieldsCalculator.expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions")  | Typed, fluent builder for Fields Calculator expressions.  |  
| [`FieldsCalculator.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir")  | Shortcut for dir(self).  |  
# FieldsCalculator 

class ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator(_app_) 
    
Provides the Advanced fields calculator methods.
Provide methods to add, load and delete named expressions on top of the already existing ones in AEDT Fields calculator. 

Parameters: 
     

**app**
    
Inherited parent object.
Examples
Custom expressions can be added as dictionary on-the-fly:

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
or they can be added from the `expression_catalog.toml`:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
Methods  
| [`FieldsCalculator.add_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression")(calculation, ...)  | Add named expression.  |  
| --- | --- |  
| [`FieldsCalculator.create_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file")(...)  | Create a calculator expression file.  |  
| [`FieldsCalculator.delete_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression")([name])  | Delete a named expression.  |  
| [`FieldsCalculator.evaluate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate")(expression[, ...])  | Evaluate an expression and return the value.  |  
| [`FieldsCalculator.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export")(quantity[, ...])  | Export the field quantity at the top of the register to a file, mapping it to a grid of points.  |  
| [`FieldsCalculator.expression_plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot")(...[, setup])  | Create plots defined in the expression catalog.  |  
| [`FieldsCalculator.get_expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions")([field_type])  | Get dictionary of available Field Calculator expressions.  |  
| [`FieldsCalculator.is_expression_defined`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined")(name)  | Check if a named expression exists.  |  
| [`FieldsCalculator.is_general_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression")(name)  | Check if a named expression is general.  |  
| [`FieldsCalculator.load_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file")(input_file)  | Load expressions from an external TOML file.  |  
| [`FieldsCalculator.validate_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression")(expression)  | Validate expression file against the schema.  |  
| [`FieldsCalculator.write`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write")(expression, output_file)  | Save the content of the stack register for future reuse in a later Field Calculator session.  |  
Attributes  
| [`FieldsCalculator.expression_names`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names")  | List of available expressions.  |  
| --- | --- |  
| [`FieldsCalculator.expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions")  | Typed, fluent builder for Fields Calculator expressions.  |  
| [`FieldsCalculator.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.rst.txt)

# FieldsCalculator 

class ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator(_app_) 
    
Provides the Advanced fields calculator methods.
Provide methods to add, load and delete named expressions on top of the already existing ones in AEDT Fields calculator. 

Parameters: 
     

**app**
    
Inherited parent object.
Examples
Custom expressions can be added as dictionary on-the-fly:

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
or they can be added from the `expression_catalog.toml`:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
Methods  
| [`FieldsCalculator.add_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.add_expression")(calculation, ...)  | Add named expression.  |  
| --- | --- |  
| [`FieldsCalculator.create_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.create_expression_file")(...)  | Create a calculator expression file.  |  
| [`FieldsCalculator.delete_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression")([name])  | Delete a named expression.  |  
| [`FieldsCalculator.evaluate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate")(expression[, ...])  | Evaluate an expression and return the value.  |  
| [`FieldsCalculator.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.export")(quantity[, ...])  | Export the field quantity at the top of the register to a file, mapping it to a grid of points.  |  
| [`FieldsCalculator.expression_plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_plot")(...[, setup])  | Create plots defined in the expression catalog.  |  
| [`FieldsCalculator.get_expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions")([field_type])  | Get dictionary of available Field Calculator expressions.  |  
| [`FieldsCalculator.is_expression_defined`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_expression_defined")(name)  | Check if a named expression exists.  |  
| [`FieldsCalculator.is_general_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.is_general_expression")(name)  | Check if a named expression is general.  |  
| [`FieldsCalculator.load_expression_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file")(input_file)  | Load expressions from an external TOML file.  |  
| [`FieldsCalculator.validate_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression")(expression)  | Validate expression file against the schema.  |  
| [`FieldsCalculator.write`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.write")(expression, output_file)  | Save the content of the stack register for future reuse in a later Field Calculator session.  |  
Attributes  
| [`FieldsCalculator.expression_names`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expression_names")  | List of available expressions.  |  
| --- | --- |  
| [`FieldsCalculator.expressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions")  | Typed, fluent builder for Fields Calculator expressions.  |  
| [`FieldsCalculator.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir.html#ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir "ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.public_dir")  | Shortcut for dir(self).  |