---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.ProfileStepSummary.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# ProfileStepSummary 

class ansys.aedt.core.modules.profile.ProfileStepSummary(_props : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) 
    
Summary information for a single profile step.
This light-weight container extracts a small set of common metrics (CPU time, real time, memory) from a `properties` dictionary. 

Parameters: 
     

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**Properties dictionary as parsed from the solver profile.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStepSummary
>>> obj = ProfileStepSummary({"Name": "Pass 1", "Cpu time": "00:00:05"})
>>> obj.cpu_time
datetime.timedelta(seconds=5)

```
Copy to clipboard
Attributes  
| [`ProfileStepSummary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir.html#ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir "ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# ProfileStepSummary 

class ansys.aedt.core.modules.profile.ProfileStepSummary(_props : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) 
    
Summary information for a single profile step.
This light-weight container extracts a small set of common metrics (CPU time, real time, memory) from a `properties` dictionary. 

Parameters: 
     

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**Properties dictionary as parsed from the solver profile.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStepSummary
>>> obj = ProfileStepSummary({"Name": "Pass 1", "Cpu time": "00:00:05"})
>>> obj.cpu_time
datetime.timedelta(seconds=5)

```
Copy to clipboard
Attributes  
| [`ProfileStepSummary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir.html#ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir "ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.ProfileStepSummary.rst.txt)

# ProfileStepSummary 

class ansys.aedt.core.modules.profile.ProfileStepSummary(_props : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) 
    
Summary information for a single profile step.
This light-weight container extracts a small set of common metrics (CPU time, real time, memory) from a `properties` dictionary. 

Parameters: 
     

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**Properties dictionary as parsed from the solver profile.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStepSummary
>>> obj = ProfileStepSummary({"Name": "Pass 1", "Cpu time": "00:00:05"})
>>> obj.cpu_time
datetime.timedelta(seconds=5)

```
Copy to clipboard
Attributes  
| [`ProfileStepSummary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir.html#ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir "ansys.aedt.core.modules.profile.ProfileStepSummary.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |