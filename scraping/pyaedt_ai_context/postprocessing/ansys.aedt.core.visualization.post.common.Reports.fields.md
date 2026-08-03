---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.fields.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# fields 

Reports.fields(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polyline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more expressions to add to the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**polyline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline to plot the field on. If a name is not provided, the report might be incorrect. The default value is `None`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Fields`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.fields("Mag_E", "Setup : LastAdaptive", "Polyline1")
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
# fields 

Reports.fields(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polyline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more expressions to add to the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**polyline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline to plot the field on. If a name is not provided, the report might be incorrect. The default value is `None`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Fields`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.fields("Mag_E", "Setup : LastAdaptive", "Polyline1")
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.fields.rst.txt)

# fields 

Reports.fields(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polyline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more expressions to add to the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**polyline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline to plot the field on. If a name is not provided, the report might be incorrect. The default value is `None`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Fields`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.fields("Mag_E", "Setup : LastAdaptive", "Polyline1")
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard