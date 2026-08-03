---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# use_matrix_convergence 

SetupHFSS.use_matrix_convergence(_entry_selection : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ignore_phase_when_mag_is_less_than : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _all_diagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_delta : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _max_delta_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _all_offdiagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _off_diagonal_mag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _off_diagonal_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _custom_entries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable Matrix Convergence criteria. 

Parameters: 
     

**entry_selection**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Entry Selection. `0` for All, `1` for Diagonal Entries, `2` for custom entries. 

**ignore_phase_when_mag_is_less_than**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value of magnitude when phase is ignored. 

**all_diagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether diagonal entries has to be included in convergence or not. Default is `True`. 

**max_delta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Delta S. 

**max_delta_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum delta phase in degree. 

**all_offdiagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether off-diagonal entries has to be included in convergence or not. Default is `True`. 

**off_diagonal_mag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum offdiagonal Delta S. 

**off_diagonal_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum off-diagonal delta phase in degree. 

**custom_entries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Custom entry mapping list. Every item of the lists hall be a list with 4 elements: `[port 1 name, port 2 name, max_delta_s, max_delta_angle]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.use_matrix_convergence(entry_selection=1, ignore_phase_when_mag_is_less_than=1.0)

```
Copy to clipboard
# use_matrix_convergence 

SetupHFSS.use_matrix_convergence(_entry_selection : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ignore_phase_when_mag_is_less_than : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _all_diagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_delta : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _max_delta_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _all_offdiagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _off_diagonal_mag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _off_diagonal_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _custom_entries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable Matrix Convergence criteria. 

Parameters: 
     

**entry_selection**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Entry Selection. `0` for All, `1` for Diagonal Entries, `2` for custom entries. 

**ignore_phase_when_mag_is_less_than**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value of magnitude when phase is ignored. 

**all_diagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether diagonal entries has to be included in convergence or not. Default is `True`. 

**max_delta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Delta S. 

**max_delta_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum delta phase in degree. 

**all_offdiagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether off-diagonal entries has to be included in convergence or not. Default is `True`. 

**off_diagonal_mag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum offdiagonal Delta S. 

**off_diagonal_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum off-diagonal delta phase in degree. 

**custom_entries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Custom entry mapping list. Every item of the lists hall be a list with 4 elements: `[port 1 name, port 2 name, max_delta_s, max_delta_angle]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.use_matrix_convergence(entry_selection=1, ignore_phase_when_mag_is_less_than=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence.rst.txt)

# use_matrix_convergence 

SetupHFSS.use_matrix_convergence(_entry_selection : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ignore_phase_when_mag_is_less_than : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.01_, _all_diagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_delta : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _max_delta_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _all_offdiagonal_entries : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _off_diagonal_mag : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _off_diagonal_phase : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _custom_entries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable Matrix Convergence criteria. 

Parameters: 
     

**entry_selection**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Entry Selection. `0` for All, `1` for Diagonal Entries, `2` for custom entries. 

**ignore_phase_when_mag_is_less_than**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value of magnitude when phase is ignored. 

**all_diagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether diagonal entries has to be included in convergence or not. Default is `True`. 

**max_delta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Delta S. 

**max_delta_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum delta phase in degree. 

**all_offdiagonal_entries**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether off-diagonal entries has to be included in convergence or not. Default is `True`. 

**off_diagonal_mag**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum offdiagonal Delta S. 

**off_diagonal_phase**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Maximum off-diagonal delta phase in degree. 

**custom_entries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Custom entry mapping list. Every item of the lists hall be a list with 4 elements: `[port 1 name, port 2 name, max_delta_s, max_delta_angle]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.use_matrix_convergence(entry_selection=1, ignore_phase_when_mag_is_less_than=1.0)

```
Copy to clipboard