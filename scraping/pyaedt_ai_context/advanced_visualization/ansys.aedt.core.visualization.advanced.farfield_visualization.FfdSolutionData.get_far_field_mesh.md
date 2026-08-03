---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.get_far_field_mesh.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_far_field_mesh 

FfdSolutionData.get_far_field_mesh(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_) → UnstructuredGrid 
    
Generate a PyVista `UnstructuredGrid` object that represents the far field mesh. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

Returns: 
     

`Pyvista.Plotter`
    
`UnstructuredGrid` object representing the far field mesh.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.farfield_visualization import FfdSolutionData
>>> obj = FfdSolutionData()
>>> obj.get_far_field_mesh(quantity=1, quantity_format=1)

```
Copy to clipboard
# get_far_field_mesh 

FfdSolutionData.get_far_field_mesh(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_) → UnstructuredGrid 
    
Generate a PyVista `UnstructuredGrid` object that represents the far field mesh. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

Returns: 
     

`Pyvista.Plotter`
    
`UnstructuredGrid` object representing the far field mesh.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.farfield_visualization import FfdSolutionData
>>> obj = FfdSolutionData()
>>> obj.get_far_field_mesh(quantity=1, quantity_format=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.get_far_field_mesh.rst.txt)

# get_far_field_mesh 

FfdSolutionData.get_far_field_mesh(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_) → UnstructuredGrid 
    
Generate a PyVista `UnstructuredGrid` object that represents the far field mesh. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

Returns: 
     

`Pyvista.Plotter`
    
`UnstructuredGrid` object representing the far field mesh.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.farfield_visualization import FfdSolutionData
>>> obj = FfdSolutionData()
>>> obj.get_far_field_mesh(quantity=1, quantity_format=1)

```
Copy to clipboard