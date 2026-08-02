---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.change_validation_settings.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# change_validation_settings 

Hfss3dLayout.change_validation_settings(_entity_check_level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Strict'_, _ignore_unclassified : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _skip_intersections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Update the validation design settings. 

Parameters: 
     

**entity_check_level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Entity check level. The default is `"Strict"`. Options are `"Strict"`, `"Basic"`, `"Warning Only"`, `"None"`. 

**ignore_unclassified**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to ignore unclassified elements. The default is `False`. 

**skip_intersections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to skip intersections. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDesignSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.change_validation_settings(entity_check_level="Strict", ignore_unclassified=True)

```
Copy to clipboard
# change_validation_settings 

Hfss3dLayout.change_validation_settings(_entity_check_level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Strict'_, _ignore_unclassified : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _skip_intersections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Update the validation design settings. 

Parameters: 
     

**entity_check_level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Entity check level. The default is `"Strict"`. Options are `"Strict"`, `"Basic"`, `"Warning Only"`, `"None"`. 

**ignore_unclassified**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to ignore unclassified elements. The default is `False`. 

**skip_intersections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to skip intersections. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDesignSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.change_validation_settings(entity_check_level="Strict", ignore_unclassified=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.change_validation_settings.rst.txt)

# change_validation_settings 

Hfss3dLayout.change_validation_settings(_entity_check_level : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Strict'_, _ignore_unclassified : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _skip_intersections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) 
    
Update the validation design settings. 

Parameters: 
     

**entity_check_level**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Entity check level. The default is `"Strict"`. Options are `"Strict"`, `"Basic"`, `"Warning Only"`, `"None"`. 

**ignore_unclassified**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to ignore unclassified elements. The default is `False`. 

**skip_intersections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to skip intersections. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDesignSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.change_validation_settings(entity_check_level="Strict", ignore_unclassified=True)

```
Copy to clipboard