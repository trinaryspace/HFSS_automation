---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.available_report_quantities.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# available_report_quantities 

PostProcessorIcepak.available_report_quantities(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantities_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _differential_pairs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report quantities of a given report quantity category. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. The default is `None`, in which case the default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Display Type. The default is `None`, in which case the default type is used. In most of the cases the default type is “Rectangular Plot”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**quantities_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The category that the quantities belong to. It must be one of the `available_quantities_categories` method. The default is `None`, in which case the first default quantity is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

**differential_pairs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if return differential pairs traces or not. Default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllQuantities

```
Copy to clipboard
Examples
The example shows how to get report expressions for a Maxwell design with Eddy current solution. The context has to be provided as a dictionary where the key is the name of the original matrix and the value is the name of the reduced matrix. >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(solution_type=”AC Magnetic”) >>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name=”Sheet1”) >>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name=”Sheet2”) >>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name=”Sheet3”) >>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name=”Cur1”) >>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name=”Cur2”) >>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name=”Cur3”) >>> L = m3d.assign_matrix(assignment=[“Cur1”, “Cur2”, “Cur3”], matrix_name=”Matrix1”) >>> out = L.join_series(sources=[“Cur1”, “Cur2”], matrix_name=”ReducedMatrix1”) >>> expressions = m3d.post.available_report_quantities( … report_category=”AC Magnetic”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> expressions = m3d.post.available_report_quantities( … report_category=”EddyCurrent”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> m3d.desktop_class.release_desktop(False, False)
# available_report_quantities 

PostProcessorIcepak.available_report_quantities(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantities_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _differential_pairs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report quantities of a given report quantity category. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. The default is `None`, in which case the default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Display Type. The default is `None`, in which case the default type is used. In most of the cases the default type is “Rectangular Plot”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**quantities_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The category that the quantities belong to. It must be one of the `available_quantities_categories` method. The default is `None`, in which case the first default quantity is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

**differential_pairs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if return differential pairs traces or not. Default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllQuantities

```
Copy to clipboard
Examples
The example shows how to get report expressions for a Maxwell design with Eddy current solution. The context has to be provided as a dictionary where the key is the name of the original matrix and the value is the name of the reduced matrix. >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(solution_type=”AC Magnetic”) >>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name=”Sheet1”) >>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name=”Sheet2”) >>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name=”Sheet3”) >>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name=”Cur1”) >>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name=”Cur2”) >>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name=”Cur3”) >>> L = m3d.assign_matrix(assignment=[“Cur1”, “Cur2”, “Cur3”], matrix_name=”Matrix1”) >>> out = L.join_series(sources=[“Cur1”, “Cur2”], matrix_name=”ReducedMatrix1”) >>> expressions = m3d.post.available_report_quantities( … report_category=”AC Magnetic”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> expressions = m3d.post.available_report_quantities( … report_category=”EddyCurrent”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> m3d.desktop_class.release_desktop(False, False)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.available_report_quantities.rst.txt)

# available_report_quantities 

PostProcessorIcepak.available_report_quantities(_report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _display_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantities_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _is_siwave_dc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _differential_pairs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Compute the list of all available report quantities of a given report quantity category. 

Parameters: 
     

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Category. The default is `None`, in which case the default category is used. 

**display_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Display Type. The default is `None`, in which case the default type is used. In most of the cases the default type is “Rectangular Plot”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report Setup. The default is `None`, in which case the first nominal adaptive solution is used. 

**quantities_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The category that the quantities belong to. It must be one of the `available_quantities_categories` method. The default is `None`, in which case the first default quantity is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Report Context. The default is `None`, in which case the default context is used. For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. 

**is_siwave_dc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the setup is SIwave DCIR or not. Default is `False`. 

**differential_pairs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if return differential pairs traces or not. Default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
References

```
>>> oModule.GetAllQuantities

```
Copy to clipboard
Examples
The example shows how to get report expressions for a Maxwell design with Eddy current solution. The context has to be provided as a dictionary where the key is the name of the original matrix and the value is the name of the reduced matrix. >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(solution_type=”AC Magnetic”) >>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name=”Sheet1”) >>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name=”Sheet2”) >>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name=”Sheet3”) >>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name=”Cur1”) >>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name=”Cur2”) >>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name=”Cur3”) >>> L = m3d.assign_matrix(assignment=[“Cur1”, “Cur2”, “Cur3”], matrix_name=”Matrix1”) >>> out = L.join_series(sources=[“Cur1”, “Cur2”], matrix_name=”ReducedMatrix1”) >>> expressions = m3d.post.available_report_quantities( … report_category=”AC Magnetic”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> expressions = m3d.post.available_report_quantities( … report_category=”EddyCurrent”, display_type=”Data Table”, context={“Matrix1”: “ReducedMatrix1”} … ) >>> m3d.desktop_class.release_desktop(False, False)