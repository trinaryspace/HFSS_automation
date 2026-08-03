---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# Reports 

class ansys.aedt.core.visualization.post.common.Reports(_post_app_ , _design_type_) 
    
Provides the names of default solution types.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import Reports
>>> obj = Reports()

```
Copy to clipboard
Methods  
| [`Reports.antenna_parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.antenna_parameters.html#ansys.aedt.core.visualization.post.common.Reports.antenna_parameters "ansys.aedt.core.visualization.post.common.Reports.antenna_parameters")([expressions, ...])  | Create an Antenna Parameters Report object.  |  
| --- | --- |  
| [`Reports.cg_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.cg_fields.html#ansys.aedt.core.visualization.post.common.Reports.cg_fields "ansys.aedt.core.visualization.post.common.Reports.cg_fields")([expressions, setup, polyline])  | Create a CG Field Report object in Q3D and Q2D.  |  
| [`Reports.circuit_netlist`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.circuit_netlist.html#ansys.aedt.core.visualization.post.common.Reports.circuit_netlist "ansys.aedt.core.visualization.post.common.Reports.circuit_netlist")(setup[, ...])  | Create a Circuit Netlist Report object.  |  
| [`Reports.dc_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.dc_fields.html#ansys.aedt.core.visualization.post.common.Reports.dc_fields "ansys.aedt.core.visualization.post.common.Reports.dc_fields")([expressions, setup, polyline])  | Create a DC Field Report object in Q3D.  |  
| [`Reports.eigenmode`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eigenmode.html#ansys.aedt.core.visualization.post.common.Reports.eigenmode "ansys.aedt.core.visualization.post.common.Reports.eigenmode")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.emi_receiver`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.emi_receiver.html#ansys.aedt.core.visualization.post.common.Reports.emi_receiver "ansys.aedt.core.visualization.post.common.Reports.emi_receiver")([expressions, setup_name])  | Create an EMI receiver report.  |  
| [`Reports.eye_diagram`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eye_diagram.html#ansys.aedt.core.visualization.post.common.Reports.eye_diagram "ansys.aedt.core.visualization.post.common.Reports.eye_diagram")([expressions, setup, ...])  | Create a Standard or Default Report object.  |  
| [`Reports.far_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.far_field.html#ansys.aedt.core.visualization.post.common.Reports.far_field "ansys.aedt.core.visualization.post.common.Reports.far_field")([expressions, setup, ...])  | Create a Far Field Report object.  |  
| [`Reports.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.fields.html#ansys.aedt.core.visualization.post.common.Reports.fields "ansys.aedt.core.visualization.post.common.Reports.fields")([expressions, setup, polyline])  | Create a Field Report object.  |  
| [`Reports.modal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.modal_solution.html#ansys.aedt.core.visualization.post.common.Reports.modal_solution "ansys.aedt.core.visualization.post.common.Reports.modal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.monitor.html#ansys.aedt.core.visualization.post.common.Reports.monitor "ansys.aedt.core.visualization.post.common.Reports.monitor")([expressions, setup])  | Create an Icepak Monitor Report object.  |  
| [`Reports.near_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.near_field.html#ansys.aedt.core.visualization.post.common.Reports.near_field "ansys.aedt.core.visualization.post.common.Reports.near_field")([expressions, setup])  | Create a Field Report object.  |  
| [`Reports.rl_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.rl_fields.html#ansys.aedt.core.visualization.post.common.Reports.rl_fields "ansys.aedt.core.visualization.post.common.Reports.rl_fields")([expressions, setup, polyline])  | Create an AC RL Field Report object in Q3D and Q2D.  |  
| [`Reports.spectral`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.spectral.html#ansys.aedt.core.visualization.post.common.Reports.spectral "ansys.aedt.core.visualization.post.common.Reports.spectral")([expressions, setup])  | Create a Spectral Report object.  |  
| [`Reports.standard`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.standard.html#ansys.aedt.core.visualization.post.common.Reports.standard "ansys.aedt.core.visualization.post.common.Reports.standard")([expressions, setup])  | Create a standard or default report object.  |  
| [`Reports.statistical_eye_contour`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour.html#ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour "ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour")([...])  | Create a standard statistical AMI contour plot.  |  
| [`Reports.terminal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.terminal_solution.html#ansys.aedt.core.visualization.post.common.Reports.terminal_solution "ansys.aedt.core.visualization.post.common.Reports.terminal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
Attributes  
| [`Reports.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.public_dir.html#ansys.aedt.core.visualization.post.common.Reports.public_dir "ansys.aedt.core.visualization.post.common.Reports.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# Reports 

class ansys.aedt.core.visualization.post.common.Reports(_post_app_ , _design_type_) 
    
Provides the names of default solution types.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import Reports
>>> obj = Reports()

```
Copy to clipboard
Methods  
| [`Reports.antenna_parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.antenna_parameters.html#ansys.aedt.core.visualization.post.common.Reports.antenna_parameters "ansys.aedt.core.visualization.post.common.Reports.antenna_parameters")([expressions, ...])  | Create an Antenna Parameters Report object.  |  
| --- | --- |  
| [`Reports.cg_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.cg_fields.html#ansys.aedt.core.visualization.post.common.Reports.cg_fields "ansys.aedt.core.visualization.post.common.Reports.cg_fields")([expressions, setup, polyline])  | Create a CG Field Report object in Q3D and Q2D.  |  
| [`Reports.circuit_netlist`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.circuit_netlist.html#ansys.aedt.core.visualization.post.common.Reports.circuit_netlist "ansys.aedt.core.visualization.post.common.Reports.circuit_netlist")(setup[, ...])  | Create a Circuit Netlist Report object.  |  
| [`Reports.dc_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.dc_fields.html#ansys.aedt.core.visualization.post.common.Reports.dc_fields "ansys.aedt.core.visualization.post.common.Reports.dc_fields")([expressions, setup, polyline])  | Create a DC Field Report object in Q3D.  |  
| [`Reports.eigenmode`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eigenmode.html#ansys.aedt.core.visualization.post.common.Reports.eigenmode "ansys.aedt.core.visualization.post.common.Reports.eigenmode")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.emi_receiver`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.emi_receiver.html#ansys.aedt.core.visualization.post.common.Reports.emi_receiver "ansys.aedt.core.visualization.post.common.Reports.emi_receiver")([expressions, setup_name])  | Create an EMI receiver report.  |  
| [`Reports.eye_diagram`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eye_diagram.html#ansys.aedt.core.visualization.post.common.Reports.eye_diagram "ansys.aedt.core.visualization.post.common.Reports.eye_diagram")([expressions, setup, ...])  | Create a Standard or Default Report object.  |  
| [`Reports.far_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.far_field.html#ansys.aedt.core.visualization.post.common.Reports.far_field "ansys.aedt.core.visualization.post.common.Reports.far_field")([expressions, setup, ...])  | Create a Far Field Report object.  |  
| [`Reports.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.fields.html#ansys.aedt.core.visualization.post.common.Reports.fields "ansys.aedt.core.visualization.post.common.Reports.fields")([expressions, setup, polyline])  | Create a Field Report object.  |  
| [`Reports.modal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.modal_solution.html#ansys.aedt.core.visualization.post.common.Reports.modal_solution "ansys.aedt.core.visualization.post.common.Reports.modal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.monitor.html#ansys.aedt.core.visualization.post.common.Reports.monitor "ansys.aedt.core.visualization.post.common.Reports.monitor")([expressions, setup])  | Create an Icepak Monitor Report object.  |  
| [`Reports.near_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.near_field.html#ansys.aedt.core.visualization.post.common.Reports.near_field "ansys.aedt.core.visualization.post.common.Reports.near_field")([expressions, setup])  | Create a Field Report object.  |  
| [`Reports.rl_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.rl_fields.html#ansys.aedt.core.visualization.post.common.Reports.rl_fields "ansys.aedt.core.visualization.post.common.Reports.rl_fields")([expressions, setup, polyline])  | Create an AC RL Field Report object in Q3D and Q2D.  |  
| [`Reports.spectral`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.spectral.html#ansys.aedt.core.visualization.post.common.Reports.spectral "ansys.aedt.core.visualization.post.common.Reports.spectral")([expressions, setup])  | Create a Spectral Report object.  |  
| [`Reports.standard`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.standard.html#ansys.aedt.core.visualization.post.common.Reports.standard "ansys.aedt.core.visualization.post.common.Reports.standard")([expressions, setup])  | Create a standard or default report object.  |  
| [`Reports.statistical_eye_contour`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour.html#ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour "ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour")([...])  | Create a standard statistical AMI contour plot.  |  
| [`Reports.terminal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.terminal_solution.html#ansys.aedt.core.visualization.post.common.Reports.terminal_solution "ansys.aedt.core.visualization.post.common.Reports.terminal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
Attributes  
| [`Reports.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.public_dir.html#ansys.aedt.core.visualization.post.common.Reports.public_dir "ansys.aedt.core.visualization.post.common.Reports.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.rst.txt)

# Reports 

class ansys.aedt.core.visualization.post.common.Reports(_post_app_ , _design_type_) 
    
Provides the names of default solution types.
Examples

```
>>> from ansys.aedt.core.visualization.post.common import Reports
>>> obj = Reports()

```
Copy to clipboard
Methods  
| [`Reports.antenna_parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.antenna_parameters.html#ansys.aedt.core.visualization.post.common.Reports.antenna_parameters "ansys.aedt.core.visualization.post.common.Reports.antenna_parameters")([expressions, ...])  | Create an Antenna Parameters Report object.  |  
| --- | --- |  
| [`Reports.cg_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.cg_fields.html#ansys.aedt.core.visualization.post.common.Reports.cg_fields "ansys.aedt.core.visualization.post.common.Reports.cg_fields")([expressions, setup, polyline])  | Create a CG Field Report object in Q3D and Q2D.  |  
| [`Reports.circuit_netlist`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.circuit_netlist.html#ansys.aedt.core.visualization.post.common.Reports.circuit_netlist "ansys.aedt.core.visualization.post.common.Reports.circuit_netlist")(setup[, ...])  | Create a Circuit Netlist Report object.  |  
| [`Reports.dc_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.dc_fields.html#ansys.aedt.core.visualization.post.common.Reports.dc_fields "ansys.aedt.core.visualization.post.common.Reports.dc_fields")([expressions, setup, polyline])  | Create a DC Field Report object in Q3D.  |  
| [`Reports.eigenmode`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eigenmode.html#ansys.aedt.core.visualization.post.common.Reports.eigenmode "ansys.aedt.core.visualization.post.common.Reports.eigenmode")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.emi_receiver`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.emi_receiver.html#ansys.aedt.core.visualization.post.common.Reports.emi_receiver "ansys.aedt.core.visualization.post.common.Reports.emi_receiver")([expressions, setup_name])  | Create an EMI receiver report.  |  
| [`Reports.eye_diagram`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eye_diagram.html#ansys.aedt.core.visualization.post.common.Reports.eye_diagram "ansys.aedt.core.visualization.post.common.Reports.eye_diagram")([expressions, setup, ...])  | Create a Standard or Default Report object.  |  
| [`Reports.far_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.far_field.html#ansys.aedt.core.visualization.post.common.Reports.far_field "ansys.aedt.core.visualization.post.common.Reports.far_field")([expressions, setup, ...])  | Create a Far Field Report object.  |  
| [`Reports.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.fields.html#ansys.aedt.core.visualization.post.common.Reports.fields "ansys.aedt.core.visualization.post.common.Reports.fields")([expressions, setup, polyline])  | Create a Field Report object.  |  
| [`Reports.modal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.modal_solution.html#ansys.aedt.core.visualization.post.common.Reports.modal_solution "ansys.aedt.core.visualization.post.common.Reports.modal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
| [`Reports.monitor`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.monitor.html#ansys.aedt.core.visualization.post.common.Reports.monitor "ansys.aedt.core.visualization.post.common.Reports.monitor")([expressions, setup])  | Create an Icepak Monitor Report object.  |  
| [`Reports.near_field`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.near_field.html#ansys.aedt.core.visualization.post.common.Reports.near_field "ansys.aedt.core.visualization.post.common.Reports.near_field")([expressions, setup])  | Create a Field Report object.  |  
| [`Reports.rl_fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.rl_fields.html#ansys.aedt.core.visualization.post.common.Reports.rl_fields "ansys.aedt.core.visualization.post.common.Reports.rl_fields")([expressions, setup, polyline])  | Create an AC RL Field Report object in Q3D and Q2D.  |  
| [`Reports.spectral`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.spectral.html#ansys.aedt.core.visualization.post.common.Reports.spectral "ansys.aedt.core.visualization.post.common.Reports.spectral")([expressions, setup])  | Create a Spectral Report object.  |  
| [`Reports.standard`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.standard.html#ansys.aedt.core.visualization.post.common.Reports.standard "ansys.aedt.core.visualization.post.common.Reports.standard")([expressions, setup])  | Create a standard or default report object.  |  
| [`Reports.statistical_eye_contour`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour.html#ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour "ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour")([...])  | Create a standard statistical AMI contour plot.  |  
| [`Reports.terminal_solution`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.terminal_solution.html#ansys.aedt.core.visualization.post.common.Reports.terminal_solution "ansys.aedt.core.visualization.post.common.Reports.terminal_solution")([expressions, setup])  | Create a Standard or Default Report object.  |  
Attributes  
| [`Reports.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.public_dir.html#ansys.aedt.core.visualization.post.common.Reports.public_dir "ansys.aedt.core.visualization.post.common.Reports.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |