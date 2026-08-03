---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_statistical_eye_plot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_statistical_eye_plot 

PostProcessorCircuit.create_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create a statistical QuickEye, VerifEye, and/or Statistical Eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the probes to plot in the eye diagram. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variations with relative values. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The name of the plot.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_statistical_eye_plot(
...     setup="Setup1", probe_names=["Box1"], variation_list_w_value={"Name": "Value"}
... )

```
Copy to clipboard
# create_statistical_eye_plot 

PostProcessorCircuit.create_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create a statistical QuickEye, VerifEye, and/or Statistical Eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the probes to plot in the eye diagram. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variations with relative values. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The name of the plot.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_statistical_eye_plot(
...     setup="Setup1", probe_names=["Box1"], variation_list_w_value={"Name": "Value"}
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_statistical_eye_plot.rst.txt)

# create_statistical_eye_plot 

PostProcessorCircuit.create_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe_names : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create a statistical QuickEye, VerifEye, and/or Statistical Eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the probes to plot in the eye diagram. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variations with relative values. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The name of the plot.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_statistical_eye_plot(
...     setup="Setup1", probe_names=["Box1"], variation_list_w_value={"Name": "Value"}
... )

```
Copy to clipboard