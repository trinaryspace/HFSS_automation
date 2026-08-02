---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# ComponentArray 

class ansys.aedt.core.modeler.cad.component_array.ComponentArray(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages object attributes for a 3D component array. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS PyAEDT object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Array name. The default is `None`, in which case a random name is assigned.
Examples
Basic usage demonstrated with an HFSS design with an existing array:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]

```
Copy to clipboard
Methods  
| [`ComponentArray.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.create.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.create "ansys.aedt.core.modeler.cad.component_array.ComponentArray.create")(app, input_data[, name])  | Create a component array.  |  
| --- | --- |  
| [`ComponentArray.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete "ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete")()  | Delete the component array.  |  
| [`ComponentArray.edit_array`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array "ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array")()  | Edit component array.  |  
| [`ComponentArray.export_array_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info "ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info")([output_file])  | Export array information to a CSV file.  |  
| [`ComponentArray.get_cell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell")(row, col)  | Get cell object corresponding to a row and column.  |  
| [`ComponentArray.get_cell_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position")()  | Get cell position.  |  
| [`ComponentArray.get_component_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects")()  | Get 3D component center.  |  
| [`ComponentArray.lattice_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector "ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector")()  | Get model lattice vector.  |  
| [`ComponentArray.parse_array_info_from_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv "ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv")(...)  | Parse component array information from the CSV file.  |  
| [`ComponentArray.update_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties")()  | Update component array properties.  |  
Attributes  
| [`ComponentArray.a_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length")  | Length of the array in A direction.  |  
| --- | --- |  
| [`ComponentArray.a_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size")  | Number of cells in the vector A direction.  |  
| [`ComponentArray.a_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices")  | List of name choices for vector A.  |  
| [`ComponentArray.a_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name")  | Name of vector A.  |  
| [`ComponentArray.b_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length")  | Length of the array in B direction.  |  
| [`ComponentArray.b_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size")  | Number of cells in the vector B direction.  |  
| [`ComponentArray.b_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices")  | List of name choices for vector B.  |  
| [`ComponentArray.b_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name")  | Name of vector B.  |  
| [`ComponentArray.cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells")  | List of `ansys.aedt.core.modeler.cad.component_array.CellArray` objects.  |  
| [`ComponentArray.component_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names "ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names")  | List of component names.  |  
| [`ComponentArray.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system "ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system")  | Coordinate system name.  |  
| [`ComponentArray.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.name")  | Name of the array.  |  
| [`ComponentArray.padding_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells")  | Number of padding cells.  |  
| [`ComponentArray.post_processing_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells")  | Dictionary of each component's postprocessing cells.  |  
| [`ComponentArray.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties")  | Ordered dictionary of the properties of the component array.  |  
| [`ComponentArray.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir "ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir")  | Shortcut for dir(self).  |  
| [`ComponentArray.render`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render")  | Array rendering.  |  
| [`ComponentArray.render_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices")  | List of rendered name choices.  |  
| [`ComponentArray.render_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id")  | Array rendering ID.  |  
| [`ComponentArray.show_cell_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number "ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number")  | Flag indicating if the array cell number is shown.  |  
| [`ComponentArray.visible`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible "ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible")  | Flag indicating if the array is visible.  |  
# ComponentArray 

class ansys.aedt.core.modeler.cad.component_array.ComponentArray(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages object attributes for a 3D component array. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS PyAEDT object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Array name. The default is `None`, in which case a random name is assigned.
Examples
Basic usage demonstrated with an HFSS design with an existing array:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]

```
Copy to clipboard
Methods  
| [`ComponentArray.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.create.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.create "ansys.aedt.core.modeler.cad.component_array.ComponentArray.create")(app, input_data[, name])  | Create a component array.  |  
| --- | --- |  
| [`ComponentArray.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete "ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete")()  | Delete the component array.  |  
| [`ComponentArray.edit_array`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array "ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array")()  | Edit component array.  |  
| [`ComponentArray.export_array_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info "ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info")([output_file])  | Export array information to a CSV file.  |  
| [`ComponentArray.get_cell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell")(row, col)  | Get cell object corresponding to a row and column.  |  
| [`ComponentArray.get_cell_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position")()  | Get cell position.  |  
| [`ComponentArray.get_component_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects")()  | Get 3D component center.  |  
| [`ComponentArray.lattice_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector "ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector")()  | Get model lattice vector.  |  
| [`ComponentArray.parse_array_info_from_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv "ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv")(...)  | Parse component array information from the CSV file.  |  
| [`ComponentArray.update_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties")()  | Update component array properties.  |  
Attributes  
| [`ComponentArray.a_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length")  | Length of the array in A direction.  |  
| --- | --- |  
| [`ComponentArray.a_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size")  | Number of cells in the vector A direction.  |  
| [`ComponentArray.a_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices")  | List of name choices for vector A.  |  
| [`ComponentArray.a_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name")  | Name of vector A.  |  
| [`ComponentArray.b_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length")  | Length of the array in B direction.  |  
| [`ComponentArray.b_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size")  | Number of cells in the vector B direction.  |  
| [`ComponentArray.b_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices")  | List of name choices for vector B.  |  
| [`ComponentArray.b_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name")  | Name of vector B.  |  
| [`ComponentArray.cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells")  | List of `ansys.aedt.core.modeler.cad.component_array.CellArray` objects.  |  
| [`ComponentArray.component_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names "ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names")  | List of component names.  |  
| [`ComponentArray.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system "ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system")  | Coordinate system name.  |  
| [`ComponentArray.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.name")  | Name of the array.  |  
| [`ComponentArray.padding_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells")  | Number of padding cells.  |  
| [`ComponentArray.post_processing_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells")  | Dictionary of each component's postprocessing cells.  |  
| [`ComponentArray.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties")  | Ordered dictionary of the properties of the component array.  |  
| [`ComponentArray.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir "ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir")  | Shortcut for dir(self).  |  
| [`ComponentArray.render`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render")  | Array rendering.  |  
| [`ComponentArray.render_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices")  | List of rendered name choices.  |  
| [`ComponentArray.render_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id")  | Array rendering ID.  |  
| [`ComponentArray.show_cell_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number "ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number")  | Flag indicating if the array cell number is shown.  |  
| [`ComponentArray.visible`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible "ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible")  | Flag indicating if the array is visible.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.rst.txt)

# ComponentArray 

class ansys.aedt.core.modeler.cad.component_array.ComponentArray(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages object attributes for a 3D component array. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS PyAEDT object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Array name. The default is `None`, in which case a random name is assigned.
Examples
Basic usage demonstrated with an HFSS design with an existing array:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]

```
Copy to clipboard
Methods  
| [`ComponentArray.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.create.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.create "ansys.aedt.core.modeler.cad.component_array.ComponentArray.create")(app, input_data[, name])  | Create a component array.  |  
| --- | --- |  
| [`ComponentArray.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete "ansys.aedt.core.modeler.cad.component_array.ComponentArray.delete")()  | Delete the component array.  |  
| [`ComponentArray.edit_array`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array "ansys.aedt.core.modeler.cad.component_array.ComponentArray.edit_array")()  | Edit component array.  |  
| [`ComponentArray.export_array_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info "ansys.aedt.core.modeler.cad.component_array.ComponentArray.export_array_info")([output_file])  | Export array information to a CSV file.  |  
| [`ComponentArray.get_cell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell")(row, col)  | Get cell object corresponding to a row and column.  |  
| [`ComponentArray.get_cell_position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_cell_position")()  | Get cell position.  |  
| [`ComponentArray.get_component_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects "ansys.aedt.core.modeler.cad.component_array.ComponentArray.get_component_objects")()  | Get 3D component center.  |  
| [`ComponentArray.lattice_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector "ansys.aedt.core.modeler.cad.component_array.ComponentArray.lattice_vector")()  | Get model lattice vector.  |  
| [`ComponentArray.parse_array_info_from_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv "ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv")(...)  | Parse component array information from the CSV file.  |  
| [`ComponentArray.update_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.update_properties")()  | Update component array properties.  |  
Attributes  
| [`ComponentArray.a_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_length")  | Length of the array in A direction.  |  
| --- | --- |  
| [`ComponentArray.a_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_size")  | Number of cells in the vector A direction.  |  
| [`ComponentArray.a_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_choices")  | List of name choices for vector A.  |  
| [`ComponentArray.a_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.a_vector_name")  | Name of vector A.  |  
| [`ComponentArray.b_length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_length")  | Length of the array in B direction.  |  
| [`ComponentArray.b_size`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_size")  | Number of cells in the vector B direction.  |  
| [`ComponentArray.b_vector_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_choices")  | List of name choices for vector B.  |  
| [`ComponentArray.b_vector_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.b_vector_name")  | Name of vector B.  |  
| [`ComponentArray.cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.cells")  | List of `ansys.aedt.core.modeler.cad.component_array.CellArray` objects.  |  
| [`ComponentArray.component_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names "ansys.aedt.core.modeler.cad.component_array.ComponentArray.component_names")  | List of component names.  |  
| [`ComponentArray.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system "ansys.aedt.core.modeler.cad.component_array.ComponentArray.coordinate_system")  | Coordinate system name.  |  
| [`ComponentArray.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.name.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.name "ansys.aedt.core.modeler.cad.component_array.ComponentArray.name")  | Name of the array.  |  
| [`ComponentArray.padding_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.padding_cells")  | Number of padding cells.  |  
| [`ComponentArray.post_processing_cells`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells "ansys.aedt.core.modeler.cad.component_array.ComponentArray.post_processing_cells")  | Dictionary of each component's postprocessing cells.  |  
| [`ComponentArray.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties "ansys.aedt.core.modeler.cad.component_array.ComponentArray.properties")  | Ordered dictionary of the properties of the component array.  |  
| [`ComponentArray.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir "ansys.aedt.core.modeler.cad.component_array.ComponentArray.public_dir")  | Shortcut for dir(self).  |  
| [`ComponentArray.render`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render")  | Array rendering.  |  
| [`ComponentArray.render_choices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_choices")  | List of rendered name choices.  |  
| [`ComponentArray.render_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id "ansys.aedt.core.modeler.cad.component_array.ComponentArray.render_id")  | Array rendering ID.  |  
| [`ComponentArray.show_cell_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number "ansys.aedt.core.modeler.cad.component_array.ComponentArray.show_cell_number")  | Flag indicating if the array cell number is shown.  |  
| [`ComponentArray.visible`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible.html#ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible "ansys.aedt.core.modeler.cad.component_array.ComponentArray.visible")  | Flag indicating if the array is visible.  |