---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_results.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# export_results 

Hfss3dLayout.export_results(_export_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Original'_, _matrix_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _touchstone_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MagPhase'_, _touchstone_number_precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 15_, _length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1meter'_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50_, _include_gamma_comment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _support_non_standard_touchstone_extension : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _variations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export all available reports to a file, including profile, and convergence and sNp when applicable. 

Parameters: 
     

**export_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project folder. The default is `None`, in which case the working directory is used. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Matrix to specify to export touchstone file. The default is `Original`, in which case default matrix is taken. This argument applies only to 2DExtractor and Q3D setups where Matrix reduction is computed and needed to export touchstone file. 

**matrix_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of matrix to export. The default is `S` to export a touchstone file. Available values are `S`, `Y`, `Z`. `Y` and `Z` matrices will be exported as tab file. 

**touchstone_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Touchstone format. The default is `MagPahse`. Available values are: `MagPahse`, `DbPhase`, `RealImag`. 

**length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length of the model to export. The default is `1meter`. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Real impedance value in ohms, for renormalization. The default is `50`. 

**touchstone_number_precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Touchstone number of digits precision. The default is `15`. 

**include_gamma_comment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to include Gamma and Impedance comments. The default is `True`. 

**support_non_standard_touchstone_extension**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to support non-standard Touchstone extensions for mixed reference impedance. The default is `False`. 

**variations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variation values with units. The default is all variations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all exported files.
References

```
>>> oModule.GetAllPortsList
>>> oDesign.ExportProfile
>>> oModule.ExportToFile
>>> oModule.ExportConvergence
>>> oModule.ExportNetworkData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> aedtapp.analyze()
>>> exported_files = aedtapp.export_results()

```
Copy to clipboard
# export_results 

Hfss3dLayout.export_results(_export_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Original'_, _matrix_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _touchstone_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MagPhase'_, _touchstone_number_precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 15_, _length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1meter'_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50_, _include_gamma_comment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _support_non_standard_touchstone_extension : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _variations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export all available reports to a file, including profile, and convergence and sNp when applicable. 

Parameters: 
     

**export_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project folder. The default is `None`, in which case the working directory is used. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Matrix to specify to export touchstone file. The default is `Original`, in which case default matrix is taken. This argument applies only to 2DExtractor and Q3D setups where Matrix reduction is computed and needed to export touchstone file. 

**matrix_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of matrix to export. The default is `S` to export a touchstone file. Available values are `S`, `Y`, `Z`. `Y` and `Z` matrices will be exported as tab file. 

**touchstone_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Touchstone format. The default is `MagPahse`. Available values are: `MagPahse`, `DbPhase`, `RealImag`. 

**length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length of the model to export. The default is `1meter`. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Real impedance value in ohms, for renormalization. The default is `50`. 

**touchstone_number_precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Touchstone number of digits precision. The default is `15`. 

**include_gamma_comment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to include Gamma and Impedance comments. The default is `True`. 

**support_non_standard_touchstone_extension**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to support non-standard Touchstone extensions for mixed reference impedance. The default is `False`. 

**variations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variation values with units. The default is all variations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all exported files.
References

```
>>> oModule.GetAllPortsList
>>> oDesign.ExportProfile
>>> oModule.ExportToFile
>>> oModule.ExportConvergence
>>> oModule.ExportNetworkData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> aedtapp.analyze()
>>> exported_files = aedtapp.export_results()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.export_results.rst.txt)

# export_results 

Hfss3dLayout.export_results(_export_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matrix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Original'_, _matrix_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _touchstone_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MagPhase'_, _touchstone_number_precision : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 15_, _length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1meter'_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50_, _include_gamma_comment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _support_non_standard_touchstone_extension : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _variations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export all available reports to a file, including profile, and convergence and sNp when applicable. 

Parameters: 
     

**export_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project folder. The default is `None`, in which case the working directory is used. 

**matrix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Matrix to specify to export touchstone file. The default is `Original`, in which case default matrix is taken. This argument applies only to 2DExtractor and Q3D setups where Matrix reduction is computed and needed to export touchstone file. 

**matrix_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of matrix to export. The default is `S` to export a touchstone file. Available values are `S`, `Y`, `Z`. `Y` and `Z` matrices will be exported as tab file. 

**touchstone_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Touchstone format. The default is `MagPahse`. Available values are: `MagPahse`, `DbPhase`, `RealImag`. 

**length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length of the model to export. The default is `1meter`. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Real impedance value in ohms, for renormalization. The default is `50`. 

**touchstone_number_precision**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Touchstone number of digits precision. The default is `15`. 

**include_gamma_comment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to include Gamma and Impedance comments. The default is `True`. 

**support_non_standard_touchstone_extension**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Specifies whether to support non-standard Touchstone extensions for mixed reference impedance. The default is `False`. 

**variations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variation values with units. The default is all variations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all exported files.
References

```
>>> oModule.GetAllPortsList
>>> oDesign.ExportProfile
>>> oModule.ExportToFile
>>> oModule.ExportConvergence
>>> oModule.ExportNetworkData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> aedtapp.analyze()
>>> exported_files = aedtapp.export_results()

```
Copy to clipboard