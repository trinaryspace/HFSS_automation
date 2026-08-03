---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_ami_initial_response_plot.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_ami_initial_response_plot 

PostProcessorCircuit.create_ami_initial_response_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _plot_initial_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_intermediate_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_final_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI initial response plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List of variations with relative values. List is deprecated. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String containing the report type. Default is `"Rectangular Plot"`. It can be `"Data Table"`, `"Rectangular Stacked Plot"``or any of the other valid AEDT Report types. The default is ``"Rectangular Plot"`. 

**plot_initial_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set either to plot the initial input response. Default is `True`. 

**plot_intermediate_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the intermediate input response. Default is `False`. 

**plot_final_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the final input response. Default is `False`. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plot.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_ami_initial_response_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard
# create_ami_initial_response_plot 

PostProcessorCircuit.create_ami_initial_response_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _plot_initial_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_intermediate_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_final_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI initial response plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List of variations with relative values. List is deprecated. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String containing the report type. Default is `"Rectangular Plot"`. It can be `"Data Table"`, `"Rectangular Stacked Plot"``or any of the other valid AEDT Report types. The default is ``"Rectangular Plot"`. 

**plot_initial_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set either to plot the initial input response. Default is `True`. 

**plot_intermediate_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the intermediate input response. Default is `False`. 

**plot_final_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the final input response. Default is `False`. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plot.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_ami_initial_response_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.create_ami_initial_response_plot.rst.txt)

# create_ami_initial_response_plot 

PostProcessorCircuit.create_ami_initial_response_plot(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ami_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _plot_initial_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_intermediate_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_final_response : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create an AMI initial response plot. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**ami_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
AMI probe name to use. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List of variations with relative values. List is deprecated. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
String containing the report type. Default is `"Rectangular Plot"`. It can be `"Data Table"`, `"Rectangular Stacked Plot"``or any of the other valid AEDT Report types. The default is ``"Rectangular Plot"`. 

**plot_initial_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set either to plot the initial input response. Default is `True`. 

**plot_intermediate_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the intermediate input response. Default is `False`. 

**plot_final_response**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set whether to plot the final input response. Default is `False`. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case a unique name is automatically assigned. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plot.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_circuit import PostProcessorCircuit
>>> obj = PostProcessorCircuit()
>>> obj.create_ami_initial_response_plot(setup="Setup1", ami_name=1, variation_list_w_value={"Name": "Value"})

```
Copy to clipboard