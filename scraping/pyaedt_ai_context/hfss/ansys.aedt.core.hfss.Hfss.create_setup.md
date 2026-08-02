---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_setup.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_setup 

Hfss.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto") 
    
Create an analysis setup for HFSS.
Optional arguments are passed along with `setup_type` and `name`. Keyword names correspond to keyword for the `setup_type` as defined in the native AEDT API.
Note
This method overrides the `Analysis.setup()` method for the HFSS app. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"Setup1"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup, which is based on the solution type. Options are `"HFSSDrivenAuto"`, `"HFSSDriven"`, `"HFSSEigen"`, `"HFSSTransient"`, and `"HFSSSBR"`. The default is `"HFSSDriven"`. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Keyword arguments from the native AEDT API. For more information, see [HFSS templates and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesHFSS.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS"),
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")
    
3D Solver Setup object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_setup(name="Setup1", setup_type="HFSSDriven", Frequency="10GHz")

```
Copy to clipboard
# create_setup 

Hfss.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto") 
    
Create an analysis setup for HFSS.
Optional arguments are passed along with `setup_type` and `name`. Keyword names correspond to keyword for the `setup_type` as defined in the native AEDT API.
Note
This method overrides the `Analysis.setup()` method for the HFSS app. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"Setup1"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup, which is based on the solution type. Options are `"HFSSDrivenAuto"`, `"HFSSDriven"`, `"HFSSEigen"`, `"HFSSTransient"`, and `"HFSSSBR"`. The default is `"HFSSDriven"`. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Keyword arguments from the native AEDT API. For more information, see [HFSS templates and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesHFSS.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS"),
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")
    
3D Solver Setup object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_setup(name="Setup1", setup_type="HFSSDriven", Frequency="10GHz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_setup.rst.txt)

# create_setup 

Hfss.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto") 
    
Create an analysis setup for HFSS.
Optional arguments are passed along with `setup_type` and `name`. Keyword names correspond to keyword for the `setup_type` as defined in the native AEDT API.
Note
This method overrides the `Analysis.setup()` method for the HFSS app. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"Setup1"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup, which is based on the solution type. Options are `"HFSSDrivenAuto"`, `"HFSSDriven"`, `"HFSSEigen"`, `"HFSSTransient"`, and `"HFSSSBR"`. The default is `"HFSSDriven"`. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Keyword arguments from the native AEDT API. For more information, see [HFSS templates and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesHFSS.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS"),
     

[`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")
    
3D Solver Setup object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_setup(name="Setup1", setup_type="HFSSDriven", Frequency="10GHz")

```
Copy to clipboard