---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_q_factor_report.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_q_factor_report 

Hfss.create_q_factor_report(_modes =None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a CSV file of the EigenQ plot. 

Parameters: 
     

**modes**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modes to plot. The default is the first mode, `1`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup in the format `"SetupName : LastAdaptive"`. The default is `None`, in which case `nominal_adaptive` is used. 

**variations**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**primary_sweep: str, optional**
    
X-axis variable. The default is `"X"`. 

**name: str, optional**
     

Returns: 
     

`report_standard.Standard` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="Eigenmode")
>>> hfss.create_q_factor_report(modes=[1])

```
Copy to clipboard
# create_q_factor_report 

Hfss.create_q_factor_report(_modes =None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a CSV file of the EigenQ plot. 

Parameters: 
     

**modes**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modes to plot. The default is the first mode, `1`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup in the format `"SetupName : LastAdaptive"`. The default is `None`, in which case `nominal_adaptive` is used. 

**variations**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**primary_sweep: str, optional**
    
X-axis variable. The default is `"X"`. 

**name: str, optional**
     

Returns: 
     

`report_standard.Standard` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="Eigenmode")
>>> hfss.create_q_factor_report(modes=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_q_factor_report.rst.txt)

# create_q_factor_report 

Hfss.create_q_factor_report(_modes =None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a CSV file of the EigenQ plot. 

Parameters: 
     

**modes**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modes to plot. The default is the first mode, `1`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup in the format `"SetupName : LastAdaptive"`. The default is `None`, in which case `nominal_adaptive` is used. 

**variations**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**primary_sweep: str, optional**
    
X-axis variable. The default is `"X"`. 

**name: str, optional**
     

Returns: 
     

`report_standard.Standard` or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="Eigenmode")
>>> hfss.create_q_factor_report(modes=[1])

```
Copy to clipboard