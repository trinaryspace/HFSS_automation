---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_rcs_data.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_rcs_data 

Hfss.get_rcs_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'ComplexMonostaticRCSTheta'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _variation_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MonostaticRCSExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") | Path | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export monostatic radar cross-section (RCS) data from HFSS.
This method exports RCS simulation data into a standardized metadata format and returns a `MonostaticRCSExporter` object for further processing.
Note
For advanced RCS analysis and visualization, install the radar explorer toolkit:

```
pip install ansys-aedt-toolkits-radar-explorer

```
Copy to clipboard
Then use `MonostaticRCSData` and `MonostaticRCSPlotter` from the toolkit. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to export. Frequencies can be specified as floats (in Hz) or strings with units. For example, `"77GHz"`. The default is `None`, in which case all available frequencies from the setup are used. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and sweep to use in the format `"SetupName : SweepName"`. The default is `None`, in which case `nominal_adaptive` is used. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic RCS expression name to export. Available options include `"ComplexMonostaticRCSTheta"`, `"ComplexMonostaticRCSPhi"`, etc. The default is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variation variables and their values. The default is `None`, in which case the nominal variation is used. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite existing metadata files if they already exist. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return a `MonostaticRCSExporter` object (`True`) or just the metadata file path (`False`). When `True`, the returned object maintains a connection to the HFSS instance. When `False`, returns the path to the metadata file, allowing offline analysis. The default is `True`. 

**variation_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name to assign to this RCS solution variation. If provided, overrides the default solution name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
  * If `link_to_hfss=True`: Returns a `MonostaticRCSExporter` object.
  * If `link_to_hfss=False`: Returns a `Path` object pointing to the metadata file.
  * Returns `False` if frequencies cannot be obtained.

Examples
Export RCS data with default settings:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(project="MyRCSProject", design="MyRCSDesign")
>>> rcs_exporter = hfss.get_rcs_data()
>>> metadata_file = rcs_exporter.metadata_file

```
Copy to clipboard
Export RCS data for specific frequencies:

```
>>> frequencies = [9e9, 10e9, 11e9]  # Frequencies in Hz
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, setup="Setup1 : Sweep1", expression="ComplexMonostaticRCSTheta"
... )

```
Copy to clipboard
Export with frequency strings and custom variation:

```
>>> frequencies = ["9GHz", "10GHz", "11GHz"]
>>> variations = {"angle": "0deg", "distance": "100mm"}
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, variations=variations, variation_name="angle_0deg"
... )

```
Copy to clipboard
Export only metadata file (no link to HFSS):

```
>>> metadata_path = hfss.get_rcs_data(frequencies=[77e9], link_to_hfss=False)
>>> print(f"RCS data exported to: {metadata_path}")

```
Copy to clipboard
Use with radar explorer toolkit for advanced analysis:

```
>>> # Export RCS data from HFSS
>>> rcs_exporter = hfss.get_rcs_data(frequencies=[77e9])
>>> metadata_file = rcs_exporter.metadata_file
>>>
>>> # Close HFSS and use toolkit for offline analysis
>>> hfss.close_project()
>>>
>>> # Advanced analysis with radar explorer toolkit
>>> # pip install ansys-aedt-toolkits-radar-explorer
>>> from ansys.aedt.toolkits.radar_explorer.rcs_visualization import MonostaticRCSData
>>> rcs_data = MonostaticRCSData(str(metadata_file))
>>> rcs_data.plot_3d()

```
Copy to clipboard
# get_rcs_data 

Hfss.get_rcs_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'ComplexMonostaticRCSTheta'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _variation_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MonostaticRCSExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") | Path | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export monostatic radar cross-section (RCS) data from HFSS.
This method exports RCS simulation data into a standardized metadata format and returns a `MonostaticRCSExporter` object for further processing.
Note
For advanced RCS analysis and visualization, install the radar explorer toolkit:

```
pip install ansys-aedt-toolkits-radar-explorer

```
Copy to clipboard
Then use `MonostaticRCSData` and `MonostaticRCSPlotter` from the toolkit. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to export. Frequencies can be specified as floats (in Hz) or strings with units. For example, `"77GHz"`. The default is `None`, in which case all available frequencies from the setup are used. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and sweep to use in the format `"SetupName : SweepName"`. The default is `None`, in which case `nominal_adaptive` is used. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic RCS expression name to export. Available options include `"ComplexMonostaticRCSTheta"`, `"ComplexMonostaticRCSPhi"`, etc. The default is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variation variables and their values. The default is `None`, in which case the nominal variation is used. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite existing metadata files if they already exist. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return a `MonostaticRCSExporter` object (`True`) or just the metadata file path (`False`). When `True`, the returned object maintains a connection to the HFSS instance. When `False`, returns the path to the metadata file, allowing offline analysis. The default is `True`. 

**variation_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name to assign to this RCS solution variation. If provided, overrides the default solution name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
  * If `link_to_hfss=True`: Returns a `MonostaticRCSExporter` object.
  * If `link_to_hfss=False`: Returns a `Path` object pointing to the metadata file.
  * Returns `False` if frequencies cannot be obtained.

Examples
Export RCS data with default settings:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(project="MyRCSProject", design="MyRCSDesign")
>>> rcs_exporter = hfss.get_rcs_data()
>>> metadata_file = rcs_exporter.metadata_file

```
Copy to clipboard
Export RCS data for specific frequencies:

```
>>> frequencies = [9e9, 10e9, 11e9]  # Frequencies in Hz
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, setup="Setup1 : Sweep1", expression="ComplexMonostaticRCSTheta"
... )

```
Copy to clipboard
Export with frequency strings and custom variation:

```
>>> frequencies = ["9GHz", "10GHz", "11GHz"]
>>> variations = {"angle": "0deg", "distance": "100mm"}
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, variations=variations, variation_name="angle_0deg"
... )

```
Copy to clipboard
Export only metadata file (no link to HFSS):

```
>>> metadata_path = hfss.get_rcs_data(frequencies=[77e9], link_to_hfss=False)
>>> print(f"RCS data exported to: {metadata_path}")

```
Copy to clipboard
Use with radar explorer toolkit for advanced analysis:

```
>>> # Export RCS data from HFSS
>>> rcs_exporter = hfss.get_rcs_data(frequencies=[77e9])
>>> metadata_file = rcs_exporter.metadata_file
>>>
>>> # Close HFSS and use toolkit for offline analysis
>>> hfss.close_project()
>>>
>>> # Advanced analysis with radar explorer toolkit
>>> # pip install ansys-aedt-toolkits-radar-explorer
>>> from ansys.aedt.toolkits.radar_explorer.rcs_visualization import MonostaticRCSData
>>> rcs_data = MonostaticRCSData(str(metadata_file))
>>> rcs_data.plot_3d()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_rcs_data.rst.txt)

# get_rcs_data 

Hfss.get_rcs_data(_frequencies : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'ComplexMonostaticRCSTheta'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _link_to_hfss : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _variation_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MonostaticRCSExporter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") | Path | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export monostatic radar cross-section (RCS) data from HFSS.
This method exports RCS simulation data into a standardized metadata format and returns a `MonostaticRCSExporter` object for further processing.
Note
For advanced RCS analysis and visualization, install the radar explorer toolkit:

```
pip install ansys-aedt-toolkits-radar-explorer

```
Copy to clipboard
Then use `MonostaticRCSData` and `MonostaticRCSPlotter` from the toolkit. 

Parameters: 
     

**frequencies**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency value or list of frequencies to export. Frequencies can be specified as floats (in Hz) or strings with units. For example, `"77GHz"`. The default is `None`, in which case all available frequencies from the setup are used. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and sweep to use in the format `"SetupName : SweepName"`. The default is `None`, in which case `nominal_adaptive` is used. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic RCS expression name to export. Available options include `"ComplexMonostaticRCSTheta"`, `"ComplexMonostaticRCSPhi"`, etc. The default is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variation variables and their values. The default is `None`, in which case the nominal variation is used. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite existing metadata files if they already exist. The default is `True`. 

**link_to_hfss**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return a `MonostaticRCSExporter` object (`True`) or just the metadata file path (`False`). When `True`, the returned object maintains a connection to the HFSS instance. When `False`, returns the path to the metadata file, allowing offline analysis. The default is `True`. 

**variation_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name to assign to this RCS solution variation. If provided, overrides the default solution name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
  * If `link_to_hfss=True`: Returns a `MonostaticRCSExporter` object.
  * If `link_to_hfss=False`: Returns a `Path` object pointing to the metadata file.
  * Returns `False` if frequencies cannot be obtained.

Examples
Export RCS data with default settings:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(project="MyRCSProject", design="MyRCSDesign")
>>> rcs_exporter = hfss.get_rcs_data()
>>> metadata_file = rcs_exporter.metadata_file

```
Copy to clipboard
Export RCS data for specific frequencies:

```
>>> frequencies = [9e9, 10e9, 11e9]  # Frequencies in Hz
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, setup="Setup1 : Sweep1", expression="ComplexMonostaticRCSTheta"
... )

```
Copy to clipboard
Export with frequency strings and custom variation:

```
>>> frequencies = ["9GHz", "10GHz", "11GHz"]
>>> variations = {"angle": "0deg", "distance": "100mm"}
>>> rcs_exporter = hfss.get_rcs_data(
...     frequencies=frequencies, variations=variations, variation_name="angle_0deg"
... )

```
Copy to clipboard
Export only metadata file (no link to HFSS):

```
>>> metadata_path = hfss.get_rcs_data(frequencies=[77e9], link_to_hfss=False)
>>> print(f"RCS data exported to: {metadata_path}")

```
Copy to clipboard
Use with radar explorer toolkit for advanced analysis:

```
>>> # Export RCS data from HFSS
>>> rcs_exporter = hfss.get_rcs_data(frequencies=[77e9])
>>> metadata_file = rcs_exporter.metadata_file
>>>
>>> # Close HFSS and use toolkit for offline analysis
>>> hfss.close_project()
>>>
>>> # Advanced analysis with radar explorer toolkit
>>> # pip install ansys-aedt-toolkits-radar-explorer
>>> from ansys.aedt.toolkits.radar_explorer.rcs_visualization import MonostaticRCSData
>>> rcs_data = MonostaticRCSData(str(metadata_file))
>>> rcs_data.plot_3d()

```
Copy to clipboard