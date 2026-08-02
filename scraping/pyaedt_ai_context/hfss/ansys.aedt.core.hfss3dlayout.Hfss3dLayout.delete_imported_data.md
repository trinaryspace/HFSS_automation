---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.delete_imported_data.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# delete_imported_data 

Hfss3dLayout.delete_imported_data(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete imported data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table to delete. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.RemoveImportData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dlayout
>>> h3d = Hfss3dlayout()
>>> table_name = h3d.import_table(input_file="my_file.csv")
>>> h3d.delete_imported_data(table_name)

```
Copy to clipboard
# delete_imported_data 

Hfss3dLayout.delete_imported_data(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete imported data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table to delete. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.RemoveImportData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dlayout
>>> h3d = Hfss3dlayout()
>>> table_name = h3d.import_table(input_file="my_file.csv")
>>> h3d.delete_imported_data(table_name)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.delete_imported_data.rst.txt)

# delete_imported_data 

Hfss3dLayout.delete_imported_data(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete imported data. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table to delete. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.RemoveImportData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dlayout
>>> h3d = Hfss3dlayout()
>>> table_name = h3d.import_table(input_file="my_file.csv")
>>> h3d.delete_imported_data(table_name)

```
Copy to clipboard