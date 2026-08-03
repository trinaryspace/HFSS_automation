---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# VRTFieldPlot 

class ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot(_postprocessor_ , _is_creeping_wave : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'QuantityName_SBR'_, _max_frequency : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1GHz'_, _ray_density : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _intrinsics =None_) 
    
Creates and edits VRT field plots for SBR+ and Creeping Waves. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**is_creeping_wave**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether it is a creeping wave model or not. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot or the name of the object. 

**max_frequency**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum Frequency. The default is `"1GHz"`. 

**ray_density**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Ray Density. The default is `2`. 

**bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.vrt_data import VRTFieldPlot
>>> obj = VRTFieldPlot()

```
Copy to clipboard
Methods  
| [`VRTFieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`VRTFieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete")()  | Delete the field plot.  |  
| [`VRTFieldPlot.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export")([path])  | Export the Visual Ray Tracing to `hdm` file.  |  
| [`VRTFieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update")()  | Update the field plot.  |  
Attributes  
| [`VRTFieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| --- | --- |  
| [`VRTFieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir")  | Shortcut for dir(self).  |  
# VRTFieldPlot 

class ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot(_postprocessor_ , _is_creeping_wave : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'QuantityName_SBR'_, _max_frequency : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1GHz'_, _ray_density : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _intrinsics =None_) 
    
Creates and edits VRT field plots for SBR+ and Creeping Waves. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**is_creeping_wave**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether it is a creeping wave model or not. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot or the name of the object. 

**max_frequency**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum Frequency. The default is `"1GHz"`. 

**ray_density**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Ray Density. The default is `2`. 

**bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.vrt_data import VRTFieldPlot
>>> obj = VRTFieldPlot()

```
Copy to clipboard
Methods  
| [`VRTFieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`VRTFieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete")()  | Delete the field plot.  |  
| [`VRTFieldPlot.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export")([path])  | Export the Visual Ray Tracing to `hdm` file.  |  
| [`VRTFieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update")()  | Update the field plot.  |  
Attributes  
| [`VRTFieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| --- | --- |  
| [`VRTFieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.rst.txt)

# VRTFieldPlot 

class ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot(_postprocessor_ , _is_creeping_wave : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'QuantityName_SBR'_, _max_frequency : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1GHz'_, _ray_density : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _intrinsics =None_) 
    
Creates and edits VRT field plots for SBR+ and Creeping Waves. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**is_creeping_wave**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether it is a creeping wave model or not. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot or the name of the object. 

**max_frequency**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum Frequency. The default is `"1GHz"`. 

**ray_density**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Ray Density. The default is `2`. 

**bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Name of the intrinsic dictionary. The default is `{}`.
Examples

```
>>> from ansys.aedt.core.visualization.post.vrt_data import VRTFieldPlot
>>> obj = VRTFieldPlot()

```
Copy to clipboard
Methods  
| [`VRTFieldPlot.create`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.create")()  | Create a field plot.  |  
| --- | --- |  
| [`VRTFieldPlot.delete`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.delete")()  | Delete the field plot.  |  
| [`VRTFieldPlot.export`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.export")([path])  | Export the Visual Ray Tracing to `hdm` file.  |  
| [`VRTFieldPlot.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.update")()  | Update the field plot.  |  
Attributes  
| [`VRTFieldPlot.intrinsicVar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.intrinsicVar")  | Intrinsic variable.  |  
| --- | --- |  
| [`VRTFieldPlot.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir.html#ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir "ansys.aedt.core.visualization.post.vrt_data.VRTFieldPlot.public_dir")  | Shortcut for dir(self).  |