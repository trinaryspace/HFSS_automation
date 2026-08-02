---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/Mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Mesh operations
The `Mesh` module includes these classes:
  * `Mesh` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `IcepakMesh` for Icepak
  * `Mesh3d` for HFSS 3D Layout

They are accessible through the mesh property:  
| [`mesh.Mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.html#ansys.aedt.core.modules.mesh.Mesh "ansys.aedt.core.modules.mesh.Mesh")  | Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D).  |  
| --- | --- |  
| [`mesh_icepak.IcepakMesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh")  | Manages Icepak meshes.  |  
| [`mesh_3d_layout.Mesh3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d")  | Manages mesh operations for HFSS 3D Layout.  |  

```
from ansys.aedt.core import Maxwell3d

app = Maxwell3d(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
# This call returns the Mesh class
my_mesh = app.mesh
# This call executes a ``Mesh`` method and creates an object to control the mesh operation
mesh_operation_object = my_mesh.assign_surface_mesh("MyBox", 2)
...

```
Copy to clipboard
## Icepak mesh
These objects are relevant objects while using the `MeshIcepak` class:  
| [`Region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.html#ansys.aedt.core.modules.mesh_icepak.Region "ansys.aedt.core.modules.mesh_icepak.Region")  | Provides Icepak global mesh region properties and methods.  |  
| --- | --- |  
| [`SubRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.html#ansys.aedt.core.modules.mesh_icepak.SubRegion "ansys.aedt.core.modules.mesh_icepak.SubRegion")  | Provides Icepak mesh subregions properties and methods.  |  
| [`MeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion")  | Provides Icepak subregions mesh properties and methods.  |  
| [`GlobalMeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion.html#ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion "ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion")  | Provides Icepak global mesh properties and methods.  |  
# Mesh operations
The `Mesh` module includes these classes:
  * `Mesh` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `IcepakMesh` for Icepak
  * `Mesh3d` for HFSS 3D Layout

They are accessible through the mesh property:  
| [`mesh.Mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.html#ansys.aedt.core.modules.mesh.Mesh "ansys.aedt.core.modules.mesh.Mesh")  | Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D).  |  
| --- | --- |  
| [`mesh_icepak.IcepakMesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh")  | Manages Icepak meshes.  |  
| [`mesh_3d_layout.Mesh3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d")  | Manages mesh operations for HFSS 3D Layout.  |  

```
from ansys.aedt.core import Maxwell3d

app = Maxwell3d(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
# This call returns the Mesh class
my_mesh = app.mesh
# This call executes a ``Mesh`` method and creates an object to control the mesh operation
mesh_operation_object = my_mesh.assign_surface_mesh("MyBox", 2)
...

```
Copy to clipboard
## Icepak mesh
These objects are relevant objects while using the `MeshIcepak` class:  
| [`Region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.html#ansys.aedt.core.modules.mesh_icepak.Region "ansys.aedt.core.modules.mesh_icepak.Region")  | Provides Icepak global mesh region properties and methods.  |  
| --- | --- |  
| [`SubRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.html#ansys.aedt.core.modules.mesh_icepak.SubRegion "ansys.aedt.core.modules.mesh_icepak.SubRegion")  | Provides Icepak mesh subregions properties and methods.  |  
| [`MeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion")  | Provides Icepak subregions mesh properties and methods.  |  
| [`GlobalMeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion.html#ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion "ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion")  | Provides Icepak global mesh properties and methods.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/Mesh.rst.txt)

# Mesh operations
The `Mesh` module includes these classes:
  * `Mesh` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `IcepakMesh` for Icepak
  * `Mesh3d` for HFSS 3D Layout

They are accessible through the mesh property:  
| [`mesh.Mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.html#ansys.aedt.core.modules.mesh.Mesh "ansys.aedt.core.modules.mesh.Mesh")  | Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D).  |  
| --- | --- |  
| [`mesh_icepak.IcepakMesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh")  | Manages Icepak meshes.  |  
| [`mesh_3d_layout.Mesh3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d")  | Manages mesh operations for HFSS 3D Layout.  |  

```
from ansys.aedt.core import Maxwell3d

app = Maxwell3d(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
# This call returns the Mesh class
my_mesh = app.mesh
# This call executes a ``Mesh`` method and creates an object to control the mesh operation
mesh_operation_object = my_mesh.assign_surface_mesh("MyBox", 2)
...

```
Copy to clipboard
## Icepak mesh
These objects are relevant objects while using the `MeshIcepak` class:  
| [`Region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.html#ansys.aedt.core.modules.mesh_icepak.Region "ansys.aedt.core.modules.mesh_icepak.Region")  | Provides Icepak global mesh region properties and methods.  |  
| --- | --- |  
| [`SubRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.SubRegion.html#ansys.aedt.core.modules.mesh_icepak.SubRegion "ansys.aedt.core.modules.mesh_icepak.SubRegion")  | Provides Icepak mesh subregions properties and methods.  |  
| [`MeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion")  | Provides Icepak subregions mesh properties and methods.  |  
| [`GlobalMeshRegion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion.html#ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion "ansys.aedt.core.modules.mesh_icepak.GlobalMeshRegion")  | Provides Icepak global mesh properties and methods.  |