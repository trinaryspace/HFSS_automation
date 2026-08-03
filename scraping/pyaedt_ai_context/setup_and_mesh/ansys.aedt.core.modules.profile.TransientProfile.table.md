---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.table.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# table 

TransientProfile.table(_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → pd.DataFrame 
    
Return a summary of profile step metrics. 

Parameters: 
     

**columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Defines the columns to be included in the returned table.
Valid names are:
  * `"elapsed_time"` - Default
  * `"real_time"` - Default
  * `"cpu_time"` - Default
  * `"max_memory"` - Default
  * `"start_time"`
  * `"end_time"`
  * `"num_tets"`
  * `"nodes"` - Icepak only
  * `"faces"` - Icepak only
  * `"cells"` - Icepak only

**Names are case-sensitive. Depending on the solution profile step, some**
     

**properties are not available, in which case the value ``”NA”`` will be**
     

**returned in the table.**
     

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
Table of profile process step information for the specified property values.
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStep
>>> obj = ProfileStep()
>>> obj.table(columns=["Box1"])

```
Copy to clipboard
# table 

TransientProfile.table(_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → pd.DataFrame 
    
Return a summary of profile step metrics. 

Parameters: 
     

**columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Defines the columns to be included in the returned table.
Valid names are:
  * `"elapsed_time"` - Default
  * `"real_time"` - Default
  * `"cpu_time"` - Default
  * `"max_memory"` - Default
  * `"start_time"`
  * `"end_time"`
  * `"num_tets"`
  * `"nodes"` - Icepak only
  * `"faces"` - Icepak only
  * `"cells"` - Icepak only

**Names are case-sensitive. Depending on the solution profile step, some**
     

**properties are not available, in which case the value ``”NA”`` will be**
     

**returned in the table.**
     

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
Table of profile process step information for the specified property values.
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStep
>>> obj = ProfileStep()
>>> obj.table(columns=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.TransientProfile.table.rst.txt)

# table 

TransientProfile.table(_columns : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → pd.DataFrame 
    
Return a summary of profile step metrics. 

Parameters: 
     

**columns**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Defines the columns to be included in the returned table.
Valid names are:
  * `"elapsed_time"` - Default
  * `"real_time"` - Default
  * `"cpu_time"` - Default
  * `"max_memory"` - Default
  * `"start_time"`
  * `"end_time"`
  * `"num_tets"`
  * `"nodes"` - Icepak only
  * `"faces"` - Icepak only
  * `"cells"` - Icepak only

**Names are case-sensitive. Depending on the solution profile step, some**
     

**properties are not available, in which case the value ``”NA”`` will be**
     

**returned in the table.**
     

Returns: 
     

[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.4\)")
    
Table of profile process step information for the specified property values.
Examples

```
>>> from ansys.aedt.core.modules.profile import ProfileStep
>>> obj = ProfileStep()
>>> obj.table(columns=["Box1"])

```
Copy to clipboard