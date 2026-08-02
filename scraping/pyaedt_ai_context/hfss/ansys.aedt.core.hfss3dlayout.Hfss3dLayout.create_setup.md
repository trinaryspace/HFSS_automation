---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_setup.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_setup 

Hfss3dLayout.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [Setup3DLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout") 
    
Create a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new setup. The default is `"MySetupAuto"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup. The default is `None`, in which case the default type is applied. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Extra arguments for setup settings. Available keys depend on the setup chosen. For more information, see [HFSS 3D Layout and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplates3DLayout.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")
    
References

```
>>> oModule.Add

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> app = Hfss3dLayout()
>>> app.create_setup(name="Setup1", MeshSizeFactor=2, SingleFrequencyDataList__AdaptiveFrequency="5GHZ")

```
Copy to clipboard
# create_setup 

Hfss3dLayout.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [Setup3DLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout") 
    
Create a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new setup. The default is `"MySetupAuto"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup. The default is `None`, in which case the default type is applied. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Extra arguments for setup settings. Available keys depend on the setup chosen. For more information, see [HFSS 3D Layout and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplates3DLayout.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")
    
References

```
>>> oModule.Add

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> app = Hfss3dLayout()
>>> app.create_setup(name="Setup1", MeshSizeFactor=2, SingleFrequencyDataList__AdaptiveFrequency="5GHZ")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_setup.rst.txt)

# create_setup 

Hfss3dLayout.create_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _setup_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [Setup3DLayout](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout") 
    
Create a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new setup. The default is `"MySetupAuto"`. 

**setup_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the setup. The default is `None`, in which case the default type is applied. 

****kwargs**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Extra arguments for setup settings. Available keys depend on the setup chosen. For more information, see [HFSS 3D Layout and arguments](https://aedt.docs.pyansys.com/version/stable/API/SetupTemplates3DLayout.html). 

Returns: 
     

[`ansys.aedt.core.modules.solve_setup.Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")
    
References

```
>>> oModule.Add

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> app = Hfss3dLayout()
>>> app.create_setup(name="Setup1", MeshSizeFactor=2, SingleFrequencyDataList__AdaptiveFrequency="5GHZ")

```
Copy to clipboard