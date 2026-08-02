---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# DataSet 

class ansys.aedt.core.application.variables.DataSet(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x_ , _y_ , _z =None_, _v =None_, _xunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _yunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _zunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _vunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages datasets. 

Parameters: 
     

**app**
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the app. 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**xunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**yunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**zunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**vunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard
Methods  
| [`DataSet.add_point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.add_point.html#ansys.aedt.core.application.variables.DataSet.add_point "ansys.aedt.core.application.variables.DataSet.add_point")(x, y[, z, v])  | Add a point to the dataset.  |  
| --- | --- |  
| [`DataSet.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.create.html#ansys.aedt.core.application.variables.DataSet.create "ansys.aedt.core.application.variables.DataSet.create")()  | Create a dataset.  |  
| [`DataSet.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.delete.html#ansys.aedt.core.application.variables.DataSet.delete "ansys.aedt.core.application.variables.DataSet.delete")()  | Delete the dataset.  |  
| [`DataSet.export`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.export.html#ansys.aedt.core.application.variables.DataSet.export "ansys.aedt.core.application.variables.DataSet.export")([output_dir])  | Export the dataset.  |  
| [`DataSet.remove_point_from_index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_index.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_index "ansys.aedt.core.application.variables.DataSet.remove_point_from_index")(id_to_remove)  | Remove a point from an index.  |  
| [`DataSet.remove_point_from_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_x.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_x "ansys.aedt.core.application.variables.DataSet.remove_point_from_x")(x)  | Remove a point from an X-axis value.  |  
| [`DataSet.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.update.html#ansys.aedt.core.application.variables.DataSet.update "ansys.aedt.core.application.variables.DataSet.update")()  | Update the dataset.  |  
Attributes  
| [`DataSet.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.public_dir.html#ansys.aedt.core.application.variables.DataSet.public_dir "ansys.aedt.core.application.variables.DataSet.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# DataSet 

class ansys.aedt.core.application.variables.DataSet(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x_ , _y_ , _z =None_, _v =None_, _xunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _yunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _zunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _vunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages datasets. 

Parameters: 
     

**app**
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the app. 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**xunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**yunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**zunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**vunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard
Methods  
| [`DataSet.add_point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.add_point.html#ansys.aedt.core.application.variables.DataSet.add_point "ansys.aedt.core.application.variables.DataSet.add_point")(x, y[, z, v])  | Add a point to the dataset.  |  
| --- | --- |  
| [`DataSet.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.create.html#ansys.aedt.core.application.variables.DataSet.create "ansys.aedt.core.application.variables.DataSet.create")()  | Create a dataset.  |  
| [`DataSet.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.delete.html#ansys.aedt.core.application.variables.DataSet.delete "ansys.aedt.core.application.variables.DataSet.delete")()  | Delete the dataset.  |  
| [`DataSet.export`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.export.html#ansys.aedt.core.application.variables.DataSet.export "ansys.aedt.core.application.variables.DataSet.export")([output_dir])  | Export the dataset.  |  
| [`DataSet.remove_point_from_index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_index.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_index "ansys.aedt.core.application.variables.DataSet.remove_point_from_index")(id_to_remove)  | Remove a point from an index.  |  
| [`DataSet.remove_point_from_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_x.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_x "ansys.aedt.core.application.variables.DataSet.remove_point_from_x")(x)  | Remove a point from an X-axis value.  |  
| [`DataSet.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.update.html#ansys.aedt.core.application.variables.DataSet.update "ansys.aedt.core.application.variables.DataSet.update")()  | Update the dataset.  |  
Attributes  
| [`DataSet.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.public_dir.html#ansys.aedt.core.application.variables.DataSet.public_dir "ansys.aedt.core.application.variables.DataSet.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.DataSet.rst.txt)

# DataSet 

class ansys.aedt.core.application.variables.DataSet(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _x_ , _y_ , _z =None_, _v =None_, _xunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _yunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _zunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _vunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _sort : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages datasets. 

Parameters: 
     

**app**
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the app. 

**x**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X-axis values for the dataset. 

**y**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Y-axis values for the dataset. 

**z**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Z-axis values for a 3D dataset only. The default is `None`. 

**v**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of V-axis values for a 3D dataset only. The default is `None`. 

**xunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the X axis. The default is `""`. 

**yunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Y axis. The default is `""`. 

**zunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the Z axis for a 3D dataset only. The default is `""`. 

**vunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the V axis for a 3D dataset only. The default is `""`. 

**sort**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Sort dataset. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> dataset = hfss.create_dataset1d_project("MyCurve", [0, 1], [1, 2])
>>> dataset.export()

```
Copy to clipboard
Methods  
| [`DataSet.add_point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.add_point.html#ansys.aedt.core.application.variables.DataSet.add_point "ansys.aedt.core.application.variables.DataSet.add_point")(x, y[, z, v])  | Add a point to the dataset.  |  
| --- | --- |  
| [`DataSet.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.create.html#ansys.aedt.core.application.variables.DataSet.create "ansys.aedt.core.application.variables.DataSet.create")()  | Create a dataset.  |  
| [`DataSet.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.delete.html#ansys.aedt.core.application.variables.DataSet.delete "ansys.aedt.core.application.variables.DataSet.delete")()  | Delete the dataset.  |  
| [`DataSet.export`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.export.html#ansys.aedt.core.application.variables.DataSet.export "ansys.aedt.core.application.variables.DataSet.export")([output_dir])  | Export the dataset.  |  
| [`DataSet.remove_point_from_index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_index.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_index "ansys.aedt.core.application.variables.DataSet.remove_point_from_index")(id_to_remove)  | Remove a point from an index.  |  
| [`DataSet.remove_point_from_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.remove_point_from_x.html#ansys.aedt.core.application.variables.DataSet.remove_point_from_x "ansys.aedt.core.application.variables.DataSet.remove_point_from_x")(x)  | Remove a point from an X-axis value.  |  
| [`DataSet.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.update.html#ansys.aedt.core.application.variables.DataSet.update "ansys.aedt.core.application.variables.DataSet.update")()  | Update the dataset.  |  
Attributes  
| [`DataSet.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.DataSet.public_dir.html#ansys.aedt.core.application.variables.DataSet.public_dir "ansys.aedt.core.application.variables.DataSet.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |