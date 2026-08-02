---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.apply_solved_variation.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# apply_solved_variation 

Hfss3dLayout.apply_solved_variation(_variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply solved variation values to a property. 

Parameters: 
     

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the variations. Keys are variable names and values are their corresponding values. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples
# Create a simple box where all its dimensions are parametrized >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(version=”2026.1”) >>> m3d[“a”] = “10mm” >>> m3d[“b”] = “20mm” >>> m3d[“c”] = “30mm” >>> box = m3d.modeler.create_box([0, 0, 0], [“a”, “b”, “c”], name=”Box”, material=”copper”) >>> m3d.modeler.create_region([100, 100, 0, 0, 100, 100])
# Assign current excitations >>> current1 = m3d.assign_current(box.bottom_face_y, “1A”) >>> current2 = m3d.assign_current(box.top_face_y, “1A”, swap_direction=True)
# Create the parametric setup to sweep the box dimensions and analyze the variations >>> setup = m3d.create_setup() >>> param = m3d.parametrics.add(“a”, 5, 10, 2, “LinearCount”) >>> param.add_variation(“b”, 10, 20, 2, variation_type=”LinearCount”) >>> param.add_variation(“c”, 15, 30, 2, variation_type=”LinearCount”) >>> param.analyze()
# Plot the magnetic field density on the surface of the box >>> plot = m3d.post.create_fieldplot_surface(assignment=box, quantity=”Mag_B”)
# Apply solved variation >>> variations = m3d_app.available_variations.variations(f”{setup.name} : LastAdaptive”, True)

```
>>> m3d_app.apply_solved_variation(variations[0])
>>> m3d.release_desktop(False, False)

```
Copy to clipboard
# apply_solved_variation 

Hfss3dLayout.apply_solved_variation(_variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply solved variation values to a property. 

Parameters: 
     

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the variations. Keys are variable names and values are their corresponding values. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples
# Create a simple box where all its dimensions are parametrized >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(version=”2026.1”) >>> m3d[“a”] = “10mm” >>> m3d[“b”] = “20mm” >>> m3d[“c”] = “30mm” >>> box = m3d.modeler.create_box([0, 0, 0], [“a”, “b”, “c”], name=”Box”, material=”copper”) >>> m3d.modeler.create_region([100, 100, 0, 0, 100, 100])
# Assign current excitations >>> current1 = m3d.assign_current(box.bottom_face_y, “1A”) >>> current2 = m3d.assign_current(box.top_face_y, “1A”, swap_direction=True)
# Create the parametric setup to sweep the box dimensions and analyze the variations >>> setup = m3d.create_setup() >>> param = m3d.parametrics.add(“a”, 5, 10, 2, “LinearCount”) >>> param.add_variation(“b”, 10, 20, 2, variation_type=”LinearCount”) >>> param.add_variation(“c”, 15, 30, 2, variation_type=”LinearCount”) >>> param.analyze()
# Plot the magnetic field density on the surface of the box >>> plot = m3d.post.create_fieldplot_surface(assignment=box, quantity=”Mag_B”)
# Apply solved variation >>> variations = m3d_app.available_variations.variations(f”{setup.name} : LastAdaptive”, True)

```
>>> m3d_app.apply_solved_variation(variations[0])
>>> m3d.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.apply_solved_variation.rst.txt)

# apply_solved_variation 

Hfss3dLayout.apply_solved_variation(_variation : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply solved variation values to a property. 

Parameters: 
     

**variation**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the variations. Keys are variable names and values are their corresponding values. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples
# Create a simple box where all its dimensions are parametrized >>> from ansys.aedt.core import Maxwell3d >>> m3d = Maxwell3d(version=”2026.1”) >>> m3d[“a”] = “10mm” >>> m3d[“b”] = “20mm” >>> m3d[“c”] = “30mm” >>> box = m3d.modeler.create_box([0, 0, 0], [“a”, “b”, “c”], name=”Box”, material=”copper”) >>> m3d.modeler.create_region([100, 100, 0, 0, 100, 100])
# Assign current excitations >>> current1 = m3d.assign_current(box.bottom_face_y, “1A”) >>> current2 = m3d.assign_current(box.top_face_y, “1A”, swap_direction=True)
# Create the parametric setup to sweep the box dimensions and analyze the variations >>> setup = m3d.create_setup() >>> param = m3d.parametrics.add(“a”, 5, 10, 2, “LinearCount”) >>> param.add_variation(“b”, 10, 20, 2, variation_type=”LinearCount”) >>> param.add_variation(“c”, 15, 30, 2, variation_type=”LinearCount”) >>> param.analyze()
# Plot the magnetic field density on the surface of the box >>> plot = m3d.post.create_fieldplot_surface(assignment=box, quantity=”Mag_B”)
# Apply solved variation >>> variations = m3d_app.available_variations.variations(f”{setup.name} : LastAdaptive”, True)

```
>>> m3d_app.apply_solved_variation(variations[0])
>>> m3d.release_desktop(False, False)

```
Copy to clipboard