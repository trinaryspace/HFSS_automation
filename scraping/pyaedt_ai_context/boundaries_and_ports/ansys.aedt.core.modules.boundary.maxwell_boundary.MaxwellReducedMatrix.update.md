---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.update.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# update 

MaxwellReducedMatrix.update(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _new_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _new_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrixOperation](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation") 
    
Update the reduced matrix. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the reduced matrix operation. 

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source type, which can be `Series` or `Parallel`. 

**new_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
New name of the reduced matrix. The default value is the current name. 

**new_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of sources to include in the matrix reduction. The default values are the sources included already in the reduced matrix operation. 

Returns: 
     

[`MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")
    
Updated reduced matrix operation object.
Examples
Create a Maxwell 3D model in AC Magnetic solver. >>> from ansys.aedt.core import Maxwell3d >>> from ansys.aedt.core.generic.constants import SolutionsMaxwell3D >>> from ansys.aedt.core.modules.boundary.maxwell_boundary import SourceACMagnetic, MatrixACMagnetic

```
>>> m3d = Maxwell3d(version="2026.1", solution_type=SolutionsMaxwell3D.ACMagnetic)

```
Copy to clipboard
Assign a matrix and create a reduced matrix by joining sources in series. >>> box1 = m3d.modeler.create_box([0.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box2 = m3d.modeler.create_box([9, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box3 = m3d.modeler.create_box([16.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”)

```
>>> current1 = m3d.assign_current([box1.top_face_z], amplitude=1, name="Current1")
>>> current2 = m3d.assign_current([box2.top_face_z], amplitude=1, name="Current2")
>>> current3 = m3d.assign_current([box3.top_face_z], amplitude=1, name="Current3")
>>> m3d.assign_current([box1.bottom_face_z], amplitude=1, name="Current4", swap_direction=True)
>>> m3d.assign_current([box2.bottom_face_z], amplitude=1, name="Current5", swap_direction=True)
>>> m3d.assign_current([box3.bottom_face_z], amplitude=1, name="Current6", swap_direction=True)

```
Copy to clipboard
Assign matrix. >>> signal_source_1 = SourceACMagnetic(name=current1.name) >>> signal_source_2 = SourceACMagnetic(name=current2.name) >>> signal_source_3 = SourceACMagnetic(name=current3.name)

```
>>> matrix_args = MatrixACMagnetic(
...     signal_sources=[signal_source_1, signal_source_2, signal_source_3],
...     matrix_name="test_matrix",
... )
>>> matrix = m3d.assign_matrix(matrix_args)

```
Copy to clipboard
Join sources in series to create a reduced matrix. >>> reduced_matrix = matrix.join_series( … sources=[“Current1”, “Current2”, “Current3”], matrix_name=”ReducedMatrix1” … )
Get the reduced operation name. >>> operation_name = reduced_matrix.operations_reduction[0].name
Update the name of the join operation. >>> join_operation = reduced_matrix.update( … name=reduced_matrix.operations_reduction[0].name, operation_type=”series”, new_name=”my_op” … )
Update the sources of the join operation. >>> join_operation_1 = reduced_matrix.update( … name=join_operation.name, operation_type=”series”, new_sources=[“Current2”, “Current3”] … ) >>> m3d.release_desktop(True, True)
# update 

MaxwellReducedMatrix.update(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _new_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _new_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrixOperation](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation") 
    
Update the reduced matrix. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the reduced matrix operation. 

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source type, which can be `Series` or `Parallel`. 

**new_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
New name of the reduced matrix. The default value is the current name. 

**new_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of sources to include in the matrix reduction. The default values are the sources included already in the reduced matrix operation. 

Returns: 
     

[`MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")
    
Updated reduced matrix operation object.
Examples
Create a Maxwell 3D model in AC Magnetic solver. >>> from ansys.aedt.core import Maxwell3d >>> from ansys.aedt.core.generic.constants import SolutionsMaxwell3D >>> from ansys.aedt.core.modules.boundary.maxwell_boundary import SourceACMagnetic, MatrixACMagnetic

```
>>> m3d = Maxwell3d(version="2026.1", solution_type=SolutionsMaxwell3D.ACMagnetic)

```
Copy to clipboard
Assign a matrix and create a reduced matrix by joining sources in series. >>> box1 = m3d.modeler.create_box([0.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box2 = m3d.modeler.create_box([9, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box3 = m3d.modeler.create_box([16.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”)

```
>>> current1 = m3d.assign_current([box1.top_face_z], amplitude=1, name="Current1")
>>> current2 = m3d.assign_current([box2.top_face_z], amplitude=1, name="Current2")
>>> current3 = m3d.assign_current([box3.top_face_z], amplitude=1, name="Current3")
>>> m3d.assign_current([box1.bottom_face_z], amplitude=1, name="Current4", swap_direction=True)
>>> m3d.assign_current([box2.bottom_face_z], amplitude=1, name="Current5", swap_direction=True)
>>> m3d.assign_current([box3.bottom_face_z], amplitude=1, name="Current6", swap_direction=True)

```
Copy to clipboard
Assign matrix. >>> signal_source_1 = SourceACMagnetic(name=current1.name) >>> signal_source_2 = SourceACMagnetic(name=current2.name) >>> signal_source_3 = SourceACMagnetic(name=current3.name)

```
>>> matrix_args = MatrixACMagnetic(
...     signal_sources=[signal_source_1, signal_source_2, signal_source_3],
...     matrix_name="test_matrix",
... )
>>> matrix = m3d.assign_matrix(matrix_args)

```
Copy to clipboard
Join sources in series to create a reduced matrix. >>> reduced_matrix = matrix.join_series( … sources=[“Current1”, “Current2”, “Current3”], matrix_name=”ReducedMatrix1” … )
Get the reduced operation name. >>> operation_name = reduced_matrix.operations_reduction[0].name
Update the name of the join operation. >>> join_operation = reduced_matrix.update( … name=reduced_matrix.operations_reduction[0].name, operation_type=”series”, new_name=”my_op” … )
Update the sources of the join operation. >>> join_operation_1 = reduced_matrix.update( … name=join_operation.name, operation_type=”series”, new_sources=[“Current2”, “Current3”] … ) >>> m3d.release_desktop(True, True)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.update.rst.txt)

# update 

MaxwellReducedMatrix.update(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _operation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _new_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _new_sources : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [MaxwellReducedMatrixOperation](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation") 
    
Update the reduced matrix. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the reduced matrix operation. 

**operation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Source type, which can be `Series` or `Parallel`. 

**new_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
New name of the reduced matrix. The default value is the current name. 

**new_sources**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of sources to include in the matrix reduction. The default values are the sources included already in the reduced matrix operation. 

Returns: 
     

[`MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")
    
Updated reduced matrix operation object.
Examples
Create a Maxwell 3D model in AC Magnetic solver. >>> from ansys.aedt.core import Maxwell3d >>> from ansys.aedt.core.generic.constants import SolutionsMaxwell3D >>> from ansys.aedt.core.modules.boundary.maxwell_boundary import SourceACMagnetic, MatrixACMagnetic

```
>>> m3d = Maxwell3d(version="2026.1", solution_type=SolutionsMaxwell3D.ACMagnetic)

```
Copy to clipboard
Assign a matrix and create a reduced matrix by joining sources in series. >>> box1 = m3d.modeler.create_box([0.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box2 = m3d.modeler.create_box([9, 1.5, 0.5], [2.5, 5, 5], material=”copper”) >>> box3 = m3d.modeler.create_box([16.5, 1.5, 0.5], [2.5, 5, 5], material=”copper”)

```
>>> current1 = m3d.assign_current([box1.top_face_z], amplitude=1, name="Current1")
>>> current2 = m3d.assign_current([box2.top_face_z], amplitude=1, name="Current2")
>>> current3 = m3d.assign_current([box3.top_face_z], amplitude=1, name="Current3")
>>> m3d.assign_current([box1.bottom_face_z], amplitude=1, name="Current4", swap_direction=True)
>>> m3d.assign_current([box2.bottom_face_z], amplitude=1, name="Current5", swap_direction=True)
>>> m3d.assign_current([box3.bottom_face_z], amplitude=1, name="Current6", swap_direction=True)

```
Copy to clipboard
Assign matrix. >>> signal_source_1 = SourceACMagnetic(name=current1.name) >>> signal_source_2 = SourceACMagnetic(name=current2.name) >>> signal_source_3 = SourceACMagnetic(name=current3.name)

```
>>> matrix_args = MatrixACMagnetic(
...     signal_sources=[signal_source_1, signal_source_2, signal_source_3],
...     matrix_name="test_matrix",
... )
>>> matrix = m3d.assign_matrix(matrix_args)

```
Copy to clipboard
Join sources in series to create a reduced matrix. >>> reduced_matrix = matrix.join_series( … sources=[“Current1”, “Current2”, “Current3”], matrix_name=”ReducedMatrix1” … )
Get the reduced operation name. >>> operation_name = reduced_matrix.operations_reduction[0].name
Update the name of the join operation. >>> join_operation = reduced_matrix.update( … name=reduced_matrix.operations_reduction[0].name, operation_type=”series”, new_name=”my_op” … )
Update the sources of the join operation. >>> join_operation_1 = reduced_matrix.update( … name=join_operation.name, operation_type=”series”, new_sources=[“Current2”, “Current3”] … ) >>> m3d.release_desktop(True, True)