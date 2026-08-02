---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# MaxwellMatrix 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix(_app_ , _name_ , _props =None_, _schema : [MatrixElectric](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric") | [MatrixMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic") | [MatrixACMagnetic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic") | [MatrixACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides methods to interact with matrices in Maxwell.
This class allows sources in a reduced matrix to be listed, updated, and deleted. 

Parameters: 
     

**app**`ansys.aedt.core.Maxwell3d` , `ansys.aedt.core.Maxwell2d` 
    
Parent Maxwell application instance. 

**schema**`MaxwellMatrixSchema` , `optional` 
    
Schema defining the matrix assignment. Can be one of: `MatrixElectric`, `MatrixMagnetostatic`, `MatrixACMagnetic`, or `MatrixACMagneticAPhi`. The default is `None`.
Examples
Setup a Maxwell 2D model in Electrostatic (valid for all electric solvers).

```
>>> from ansys.aedt.core import Maxwell2d
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixElectric
>>> m2d = Maxwell2d(version="2026.1", solution_type=SolutionsMaxwell2D.ElectroStaticXY)
>>> rectangle1 = m2d.modeler.create_rectangle([0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m2d.modeler.create_rectangle([9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m2d.modeler.create_rectangle([16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> voltage1 = m2d.assign_voltage([rectangle1], amplitude=1, name="Voltage1")
>>> voltage2 = m2d.assign_voltage([rectangle2], amplitude=1, name="Voltage2")
>>> voltage3 = m2d.assign_voltage([rectangle3], amplitude=1, name="Voltage3")

```
Copy to clipboard
Define matrix assignments by instantiating the MatrixElectric class.

```
>>> matrix_args = MatrixElectric(
...     signal_sources=[voltage1.name, voltage2.name],
...     ground_sources=[voltage3.name],
...     matrix_name="test_matrix",
... )

```
Copy to clipboard
Assign matrix. The method returns a MaxwellParameters object.

```
>>> matrix = m2d.assign_matrix(matrix_args)
>>> m2d.release_desktop(True, True)

```
Copy to clipboard
Methods  
| [`MaxwellMatrix.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellMatrix.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete")()  | Delete the boundary.  |  
| [`MaxwellMatrix.join_parallel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel")(sources[, ...])  | Create matrix reduction by joining sources in parallel.  |  
| [`MaxwellMatrix.join_series`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series")(sources[, ...])  | Create matrix reduction by joining sources in series.  |  
| [`MaxwellMatrix.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellMatrix.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update")()  | Update the boundary.  |  
| [`MaxwellMatrix.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellMatrix.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellMatrix.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children")  | Retrieve children.  |  
| [`MaxwellMatrix.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellMatrix.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources")  | Retrieve gc sources.  |  
| [`MaxwellMatrix.ground_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources")  | Retrieve ground sources.  |  
| [`MaxwellMatrix.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources")  | Retrieve group sources.  |  
| [`MaxwellMatrix.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name")  | Boundary Name.  |  
| [`MaxwellMatrix.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties")  | Properties data.  |  
| [`MaxwellMatrix.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props")  | Maxwell parameter data.  |  
| [`MaxwellMatrix.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir")  | Shortcut for dir(self).  |  
| [`MaxwellMatrix.reduced_matrices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices")  | List of reduced matrix groups for the parent matrix.  |  
| [`MaxwellMatrix.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources")  | Retrieve rl sources.  |  
| [`MaxwellMatrix.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources")  | Retrieve signal sources.  |  
# MaxwellMatrix 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix(_app_ , _name_ , _props =None_, _schema : [MatrixElectric](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric") | [MatrixMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic") | [MatrixACMagnetic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic") | [MatrixACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides methods to interact with matrices in Maxwell.
This class allows sources in a reduced matrix to be listed, updated, and deleted. 

Parameters: 
     

**app**`ansys.aedt.core.Maxwell3d` , `ansys.aedt.core.Maxwell2d` 
    
Parent Maxwell application instance. 

**schema**`MaxwellMatrixSchema` , `optional` 
    
Schema defining the matrix assignment. Can be one of: `MatrixElectric`, `MatrixMagnetostatic`, `MatrixACMagnetic`, or `MatrixACMagneticAPhi`. The default is `None`.
Examples
Setup a Maxwell 2D model in Electrostatic (valid for all electric solvers).

```
>>> from ansys.aedt.core import Maxwell2d
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixElectric
>>> m2d = Maxwell2d(version="2026.1", solution_type=SolutionsMaxwell2D.ElectroStaticXY)
>>> rectangle1 = m2d.modeler.create_rectangle([0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m2d.modeler.create_rectangle([9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m2d.modeler.create_rectangle([16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> voltage1 = m2d.assign_voltage([rectangle1], amplitude=1, name="Voltage1")
>>> voltage2 = m2d.assign_voltage([rectangle2], amplitude=1, name="Voltage2")
>>> voltage3 = m2d.assign_voltage([rectangle3], amplitude=1, name="Voltage3")

```
Copy to clipboard
Define matrix assignments by instantiating the MatrixElectric class.

```
>>> matrix_args = MatrixElectric(
...     signal_sources=[voltage1.name, voltage2.name],
...     ground_sources=[voltage3.name],
...     matrix_name="test_matrix",
... )

```
Copy to clipboard
Assign matrix. The method returns a MaxwellParameters object.

```
>>> matrix = m2d.assign_matrix(matrix_args)
>>> m2d.release_desktop(True, True)

```
Copy to clipboard
Methods  
| [`MaxwellMatrix.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellMatrix.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete")()  | Delete the boundary.  |  
| [`MaxwellMatrix.join_parallel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel")(sources[, ...])  | Create matrix reduction by joining sources in parallel.  |  
| [`MaxwellMatrix.join_series`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series")(sources[, ...])  | Create matrix reduction by joining sources in series.  |  
| [`MaxwellMatrix.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellMatrix.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update")()  | Update the boundary.  |  
| [`MaxwellMatrix.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellMatrix.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellMatrix.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children")  | Retrieve children.  |  
| [`MaxwellMatrix.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellMatrix.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources")  | Retrieve gc sources.  |  
| [`MaxwellMatrix.ground_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources")  | Retrieve ground sources.  |  
| [`MaxwellMatrix.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources")  | Retrieve group sources.  |  
| [`MaxwellMatrix.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name")  | Boundary Name.  |  
| [`MaxwellMatrix.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties")  | Properties data.  |  
| [`MaxwellMatrix.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props")  | Maxwell parameter data.  |  
| [`MaxwellMatrix.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir")  | Shortcut for dir(self).  |  
| [`MaxwellMatrix.reduced_matrices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices")  | List of reduced matrix groups for the parent matrix.  |  
| [`MaxwellMatrix.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources")  | Retrieve rl sources.  |  
| [`MaxwellMatrix.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources")  | Retrieve signal sources.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rst.txt)

# MaxwellMatrix 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix(_app_ , _name_ , _props =None_, _schema : [MatrixElectric](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric") | [MatrixMagnetostatic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic") | [MatrixACMagnetic](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic") | [MatrixACMagneticAPhi](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Provides methods to interact with matrices in Maxwell.
This class allows sources in a reduced matrix to be listed, updated, and deleted. 

Parameters: 
     

**app**`ansys.aedt.core.Maxwell3d` , `ansys.aedt.core.Maxwell2d` 
    
Parent Maxwell application instance. 

**schema**`MaxwellMatrixSchema` , `optional` 
    
Schema defining the matrix assignment. Can be one of: `MatrixElectric`, `MatrixMagnetostatic`, `MatrixACMagnetic`, or `MatrixACMagneticAPhi`. The default is `None`.
Examples
Setup a Maxwell 2D model in Electrostatic (valid for all electric solvers).

```
>>> from ansys.aedt.core import Maxwell2d
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MatrixElectric
>>> m2d = Maxwell2d(version="2026.1", solution_type=SolutionsMaxwell2D.ElectroStaticXY)
>>> rectangle1 = m2d.modeler.create_rectangle([0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m2d.modeler.create_rectangle([9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m2d.modeler.create_rectangle([16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> voltage1 = m2d.assign_voltage([rectangle1], amplitude=1, name="Voltage1")
>>> voltage2 = m2d.assign_voltage([rectangle2], amplitude=1, name="Voltage2")
>>> voltage3 = m2d.assign_voltage([rectangle3], amplitude=1, name="Voltage3")

```
Copy to clipboard
Define matrix assignments by instantiating the MatrixElectric class.

```
>>> matrix_args = MatrixElectric(
...     signal_sources=[voltage1.name, voltage2.name],
...     ground_sources=[voltage3.name],
...     matrix_name="test_matrix",
... )

```
Copy to clipboard
Assign matrix. The method returns a MaxwellParameters object.

```
>>> matrix = m2d.assign_matrix(matrix_args)
>>> m2d.release_desktop(True, True)

```
Copy to clipboard
Methods  
| [`MaxwellMatrix.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellMatrix.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.delete")()  | Delete the boundary.  |  
| [`MaxwellMatrix.join_parallel`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_parallel")(sources[, ...])  | Create matrix reduction by joining sources in parallel.  |  
| [`MaxwellMatrix.join_series`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.join_series")(sources[, ...])  | Create matrix reduction by joining sources in series.  |  
| [`MaxwellMatrix.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellMatrix.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellMatrix.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update")()  | Update the boundary.  |  
| [`MaxwellMatrix.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellMatrix.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellMatrix.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.children")  | Retrieve children.  |  
| [`MaxwellMatrix.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellMatrix.gc_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.gc_sources")  | Retrieve gc sources.  |  
| [`MaxwellMatrix.ground_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.ground_sources")  | Retrieve ground sources.  |  
| [`MaxwellMatrix.group_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.group_sources")  | Retrieve group sources.  |  
| [`MaxwellMatrix.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.name")  | Boundary Name.  |  
| [`MaxwellMatrix.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.properties")  | Properties data.  |  
| [`MaxwellMatrix.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.props")  | Maxwell parameter data.  |  
| [`MaxwellMatrix.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.public_dir")  | Shortcut for dir(self).  |  
| [`MaxwellMatrix.reduced_matrices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.reduced_matrices")  | List of reduced matrix groups for the parent matrix.  |  
| [`MaxwellMatrix.rl_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.rl_sources")  | Retrieve rl sources.  |  
| [`MaxwellMatrix.signal_sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.signal_sources")  | Retrieve signal sources.  |