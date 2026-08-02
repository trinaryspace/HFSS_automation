---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_antenna_data.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_antenna_data 

Hfss.get_antenna_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [FfdSolutionDataExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter") | [FfdSolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the antenna parameters to Far Field Data (FFD) files and return an instance of the `FfdSolutionDataExporter` object.
For phased array cases, only one phased array is calculated. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to compute far field data. The default is `None,` in which case all available frequencies are computed. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. The default is `None,` in which case `nominal_adaptive` is used. 

**sphere**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Infinite sphere to use. The default is `None`, in which case an existing sphere is used or a new one is created. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Variation dictionary. The default is `None`, in which case the nominal variation is exported. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite FFD files. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return an instance of the `ansys.aedt.core.visualization.advanced.farfield_exporter.FfdSolutionDataExporter` class, which requires a connection to an instance of the [`Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") class. The default is `True`. If `False`, returns an instance of [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class, which is independent of the running HFSS instance. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `True`. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`. 

Returns: 
     

`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionDataExporter` `or` 
     

[`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
SolutionData object or False if frequencies could not be obtained.
Examples
The method [`get_antenna_data()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_antenna_data.html#ansys.aedt.core.hfss.Hfss.get_antenna_data "ansys.aedt.core.hfss.Hfss.get_antenna_data") is used to export the farfield of each element of the design.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ffdata = hfss.get_antenna_data()
>>> ffdata.farfield_data.plot_cut(primary_sweep="theta", theta=0, is_polar=False)

```
Copy to clipboard
# get_antenna_data 

Hfss.get_antenna_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [FfdSolutionDataExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter") | [FfdSolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the antenna parameters to Far Field Data (FFD) files and return an instance of the `FfdSolutionDataExporter` object.
For phased array cases, only one phased array is calculated. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to compute far field data. The default is `None,` in which case all available frequencies are computed. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. The default is `None,` in which case `nominal_adaptive` is used. 

**sphere**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Infinite sphere to use. The default is `None`, in which case an existing sphere is used or a new one is created. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Variation dictionary. The default is `None`, in which case the nominal variation is exported. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite FFD files. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return an instance of the `ansys.aedt.core.visualization.advanced.farfield_exporter.FfdSolutionDataExporter` class, which requires a connection to an instance of the [`Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") class. The default is `True`. If `False`, returns an instance of [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class, which is independent of the running HFSS instance. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `True`. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`. 

Returns: 
     

`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionDataExporter` `or` 
     

[`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
SolutionData object or False if frequencies could not be obtained.
Examples
The method [`get_antenna_data()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_antenna_data.html#ansys.aedt.core.hfss.Hfss.get_antenna_data "ansys.aedt.core.hfss.Hfss.get_antenna_data") is used to export the farfield of each element of the design.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ffdata = hfss.get_antenna_data()
>>> ffdata.farfield_data.plot_cut(primary_sweep="theta", theta=0, is_polar=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_antenna_data.rst.txt)

# get_antenna_data 

Hfss.get_antenna_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sphere : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [FfdSolutionDataExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter") | [FfdSolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export the antenna parameters to Far Field Data (FFD) files and return an instance of the `FfdSolutionDataExporter` object.
For phased array cases, only one phased array is calculated. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to compute far field data. The default is `None,` in which case all available frequencies are computed. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. The default is `None,` in which case `nominal_adaptive` is used. 

**sphere**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Infinite sphere to use. The default is `None`, in which case an existing sphere is used or a new one is created. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Variation dictionary. The default is `None`, in which case the nominal variation is exported. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite FFD files. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return an instance of the `ansys.aedt.core.visualization.advanced.farfield_exporter.FfdSolutionDataExporter` class, which requires a connection to an instance of the [`Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") class. The default is `True`. If `False`, returns an instance of [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class, which is independent of the running HFSS instance. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `True`. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`. 

Returns: 
     

`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionDataExporter` `or` 
     

[`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
SolutionData object or False if frequencies could not be obtained.
Examples
The method [`get_antenna_data()`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_antenna_data.html#ansys.aedt.core.hfss.Hfss.get_antenna_data "ansys.aedt.core.hfss.Hfss.get_antenna_data") is used to export the farfield of each element of the design.
Open a design and create the objects.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ffdata = hfss.get_antenna_data()
>>> ffdata.farfield_data.plot_cut(primary_sweep="theta", theta=0, is_polar=False)

```
Copy to clipboard