---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_ami_statistical_eye_plot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_ami_statistical_eye_plot 

PostProcessorCircuit.create_ami_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _ami_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'InitialEye'_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI statistical eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. List is deprecated. 

**ami_plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing the report AMI type. The default is `"InitialEye"`. Options are `"EyeAfterChannel"`, `"EyeAfterProbe"```”EyeAfterSource”`, and ``"InitialEye"`.. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name starting with `"Plot"` is automatically assigned. 

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
>>> obj.create_ami_statistical_eye_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard
# create_ami_statistical_eye_plot 

PostProcessorCircuit.create_ami_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _ami_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'InitialEye'_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI statistical eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. List is deprecated. 

**ami_plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing the report AMI type. The default is `"InitialEye"`. Options are `"EyeAfterChannel"`, `"EyeAfterProbe"```”EyeAfterSource”`, and ``"InitialEye"`.. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name starting with `"Plot"` is automatically assigned. 

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
>>> obj.create_ami_statistical_eye_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_ami_statistical_eye_plot.rst.txt)

# create_ami_statistical_eye_plot 

PostProcessorCircuit.create_ami_statistical_eye_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _ami_plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'InitialEye'_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI statistical eye plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. List is deprecated. 

**ami_plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String containing the report AMI type. The default is `"InitialEye"`. Options are `"EyeAfterChannel"`, `"EyeAfterProbe"```”EyeAfterSource”`, and ``"InitialEye"`.. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name starting with `"Plot"` is automatically assigned. 

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
>>> obj.create_ami_statistical_eye_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard