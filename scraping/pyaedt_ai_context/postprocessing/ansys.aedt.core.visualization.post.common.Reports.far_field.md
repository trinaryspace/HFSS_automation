---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.far_field.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# far_field 

Reports.far_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _source_context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** variations_) → [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") 
    
Create a Far Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sphere to create the far field on. 

**source_context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active source to create the far field on. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.FarField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.far_field("GainTotal", "Setup : LastAdaptive", "3D_Sphere")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
# far_field 

Reports.far_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _source_context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** variations_) → [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") 
    
Create a Far Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sphere to create the far field on. 

**source_context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active source to create the far field on. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.FarField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.far_field("GainTotal", "Setup : LastAdaptive", "3D_Sphere")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.far_field.rst.txt)

# far_field 

Reports.far_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _source_context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** variations_) → [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") 
    
Create a Far Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sphere to create the far field on. 

**source_context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active source to create the far field on. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.FarField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.far_field("GainTotal", "Setup : LastAdaptive", "3D_Sphere")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard