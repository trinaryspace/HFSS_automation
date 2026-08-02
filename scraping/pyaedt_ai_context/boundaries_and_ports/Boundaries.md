---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/Boundaries.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# Boundary objects
This section lists classes for creating and editing boundaries in the 3D tools. These objects are returned by app methods and can be used to edit or delete a boundary condition.  
| [`common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")  | Manages boundary data and execution.  |  
| --- | --- |  
| [`hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup")  | Manages Far Field Component data and execution.  |  
| [`hfss_boundary.NearFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup")  | Manages Near Field Component data and execution.  |  
| [`q3d_boundary.Matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.html#ansys.aedt.core.modules.boundary.q3d_boundary.Matrix "ansys.aedt.core.modules.boundary.q3d_boundary.Matrix")  | Manages Matrix in Q3d and Q2d Projects.  |  
| [`maxwell_boundary.MaxwellParameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters")  | Manages parameters data and execution.  |  
| [`maxwell_boundary.MaxwellMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix")  | Provides methods to interact with matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")  | Provides methods to interact with reduced matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")  | Represent a reduced matrix operation in Maxwell (join in series or parallel).  |  
| [`maxwell_boundary.MaxwellForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce")  | Initialize Maxwell force.  |  
| [`maxwell_boundary.MaxwellTorque`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque")  | Initialize Maxwell torque.  |  
| [`maxwell_boundary.MaxwellLayoutForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce")  | Initialize Maxwell layout force.  |  
| [`layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")  | Manages boundary data and execution for Hfss3dLayout.  |  
| [`icepak_boundary.NetworkObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.html#ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject "ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject")  | Manages networks in Icepak projects.  |  
## Maxwell Matrices
To facilitate matrix assignment in Maxwell, multiple classes have been created. These classes help to easily create matrix for different Maxwell solvers for both Maxwell3D and Maxwell2D.  
| [`MatrixElectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric")  | Matrix assignment for electric solvers.  |  
| --- | --- |  
| [`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")  | Source definition for magnetostatic solver.  |  
| [`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")  | Group sources definition for magnetostatic solver.  |  
| [`MatrixMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic")  | Matrix assignment for magnetostatic solver.  |  
| [`SourceACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic")  | Sources for AC Magnetic solver.  |  
| [`MatrixACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic")  | Matrix assignment for AC Magnetic solver.  |  
| [`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")  | RL sources for AC Magnetic A-Phi solver.  |  
| [`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")  | GC sources for AC Magnetic A-Phi solver.  |  
| [`MatrixACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi")  | Matrix assignment for AC Magnetic A-Phi solver.  |  
## Circuit excitations
To facilitate excitations assignment in Circuit, multiple classes have been created.  
| [`Sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.Sources.html#ansys.aedt.core.modules.boundary.circuit_boundary.Sources "ansys.aedt.core.modules.boundary.circuit_boundary.Sources")  | Manages sources in Circuit projects.  |  
| --- | --- |  
| [`PowerSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource")  | Power Sinusoidal Class.  |  
| [`PowerIQSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource")  | Power IQ Class.  |  
| [`VoltageFrequencyDependentSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource")  | Voltage Frequency Dependent Class.  |  
| [`VoltageDCSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource")  | Power Sinusoidal Class.  |  
| [`VoltageSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource")  | Power Sinusoidal Class.  |  
| [`CurrentSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource")  | Current Sinusoidal Class.  |  
## Native components
When native components object are created, the `NativeComponentObject` class is returned. For PCB components, `NativeComponentPCB` is returned.  
| [`NativeComponentPCB`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB")  | Manages native component PCB data and execution.  |  
| --- | --- |  
| [`NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")  | Manages Native Component data and execution.  |  
| [`PCBSettingsDeviceParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts")  | Handle device part settings of the PCB component.  |  
| [`PCBSettingsPackageParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts")  | Handle package part settings of the PCB component.  |  
`Native Component Object` example:

```
from ansys.aedt.core import Icepak

ipk = Icepak()
component_name = "RadioBoard1"
pcb_comp = self.aedtapp.create_ipk_3dcomponent_pcb(
    component_name,
    link_data,
    solution_freq,
    resolution,
    custom_x_resolution=400,
    custom_y_resolution=500,
)
# pcb_comp is a NativeComponentPCB
...
ipk.release_desktop()

```
Copy to clipboard
## Icepak transient assignments
To facilitate transient assignment handling in Icepak, it is possible to use one of the following classes:  
| [`SinusoidalDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary")  | Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class.  |  
| --- | --- |  
| [`LinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary")  | Manages linear conditions assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PowerLawDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary")  | Manages power law condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`ExponentialDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary")  | Manages exponential condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`SquareWaveDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary")  | Manages square wave condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PieceWiseLinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary")  | Manages dataset condition assignments, which are children of the `BoundaryDictionary` class.  |  
It is possible to initialize the class manually or through a method:

```
bc_transient = ipk.create_sinusoidal_transient_assignment(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
# bc_transient will be SinusoidalDictionary type
ipk.assign_solid_block("Cylinder1", bc_transient)

# or

bc_transient = SinusoidalDictionary(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
ipk.assign_solid_block("Cylinder1", bc_transient)

```
Copy to clipboard
# Boundary objects
This section lists classes for creating and editing boundaries in the 3D tools. These objects are returned by app methods and can be used to edit or delete a boundary condition.  
| [`common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")  | Manages boundary data and execution.  |  
| --- | --- |  
| [`hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup")  | Manages Far Field Component data and execution.  |  
| [`hfss_boundary.NearFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup")  | Manages Near Field Component data and execution.  |  
| [`q3d_boundary.Matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.html#ansys.aedt.core.modules.boundary.q3d_boundary.Matrix "ansys.aedt.core.modules.boundary.q3d_boundary.Matrix")  | Manages Matrix in Q3d and Q2d Projects.  |  
| [`maxwell_boundary.MaxwellParameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters")  | Manages parameters data and execution.  |  
| [`maxwell_boundary.MaxwellMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix")  | Provides methods to interact with matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")  | Provides methods to interact with reduced matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")  | Represent a reduced matrix operation in Maxwell (join in series or parallel).  |  
| [`maxwell_boundary.MaxwellForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce")  | Initialize Maxwell force.  |  
| [`maxwell_boundary.MaxwellTorque`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque")  | Initialize Maxwell torque.  |  
| [`maxwell_boundary.MaxwellLayoutForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce")  | Initialize Maxwell layout force.  |  
| [`layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")  | Manages boundary data and execution for Hfss3dLayout.  |  
| [`icepak_boundary.NetworkObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.html#ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject "ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject")  | Manages networks in Icepak projects.  |  
## Maxwell Matrices
To facilitate matrix assignment in Maxwell, multiple classes have been created. These classes help to easily create matrix for different Maxwell solvers for both Maxwell3D and Maxwell2D.  
| [`MatrixElectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric")  | Matrix assignment for electric solvers.  |  
| --- | --- |  
| [`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")  | Source definition for magnetostatic solver.  |  
| [`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")  | Group sources definition for magnetostatic solver.  |  
| [`MatrixMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic")  | Matrix assignment for magnetostatic solver.  |  
| [`SourceACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic")  | Sources for AC Magnetic solver.  |  
| [`MatrixACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic")  | Matrix assignment for AC Magnetic solver.  |  
| [`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")  | RL sources for AC Magnetic A-Phi solver.  |  
| [`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")  | GC sources for AC Magnetic A-Phi solver.  |  
| [`MatrixACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi")  | Matrix assignment for AC Magnetic A-Phi solver.  |  
## Circuit excitations
To facilitate excitations assignment in Circuit, multiple classes have been created.  
| [`Sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.Sources.html#ansys.aedt.core.modules.boundary.circuit_boundary.Sources "ansys.aedt.core.modules.boundary.circuit_boundary.Sources")  | Manages sources in Circuit projects.  |  
| --- | --- |  
| [`PowerSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource")  | Power Sinusoidal Class.  |  
| [`PowerIQSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource")  | Power IQ Class.  |  
| [`VoltageFrequencyDependentSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource")  | Voltage Frequency Dependent Class.  |  
| [`VoltageDCSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource")  | Power Sinusoidal Class.  |  
| [`VoltageSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource")  | Power Sinusoidal Class.  |  
| [`CurrentSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource")  | Current Sinusoidal Class.  |  
## Native components
When native components object are created, the `NativeComponentObject` class is returned. For PCB components, `NativeComponentPCB` is returned.  
| [`NativeComponentPCB`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB")  | Manages native component PCB data and execution.  |  
| --- | --- |  
| [`NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")  | Manages Native Component data and execution.  |  
| [`PCBSettingsDeviceParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts")  | Handle device part settings of the PCB component.  |  
| [`PCBSettingsPackageParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts")  | Handle package part settings of the PCB component.  |  
`Native Component Object` example:

```
from ansys.aedt.core import Icepak

ipk = Icepak()
component_name = "RadioBoard1"
pcb_comp = self.aedtapp.create_ipk_3dcomponent_pcb(
    component_name,
    link_data,
    solution_freq,
    resolution,
    custom_x_resolution=400,
    custom_y_resolution=500,
)
# pcb_comp is a NativeComponentPCB
...
ipk.release_desktop()

```
Copy to clipboard
## Icepak transient assignments
To facilitate transient assignment handling in Icepak, it is possible to use one of the following classes:  
| [`SinusoidalDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary")  | Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class.  |  
| --- | --- |  
| [`LinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary")  | Manages linear conditions assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PowerLawDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary")  | Manages power law condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`ExponentialDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary")  | Manages exponential condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`SquareWaveDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary")  | Manages square wave condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PieceWiseLinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary")  | Manages dataset condition assignments, which are children of the `BoundaryDictionary` class.  |  
It is possible to initialize the class manually or through a method:

```
bc_transient = ipk.create_sinusoidal_transient_assignment(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
# bc_transient will be SinusoidalDictionary type
ipk.assign_solid_block("Cylinder1", bc_transient)

# or

bc_transient = SinusoidalDictionary(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
ipk.assign_solid_block("Cylinder1", bc_transient)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/Boundaries.rst.txt)

# Boundary objects
This section lists classes for creating and editing boundaries in the 3D tools. These objects are returned by app methods and can be used to edit or delete a boundary condition.  
| [`common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")  | Manages boundary data and execution.  |  
| --- | --- |  
| [`hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup")  | Manages Far Field Component data and execution.  |  
| [`hfss_boundary.NearFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup")  | Manages Near Field Component data and execution.  |  
| [`q3d_boundary.Matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.q3d_boundary.Matrix.html#ansys.aedt.core.modules.boundary.q3d_boundary.Matrix "ansys.aedt.core.modules.boundary.q3d_boundary.Matrix")  | Manages Matrix in Q3d and Q2d Projects.  |  
| [`maxwell_boundary.MaxwellParameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters")  | Manages parameters data and execution.  |  
| [`maxwell_boundary.MaxwellMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellMatrix")  | Provides methods to interact with matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrix")  | Provides methods to interact with reduced matrices in Maxwell.  |  
| [`maxwell_boundary.MaxwellReducedMatrixOperation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellReducedMatrixOperation")  | Represent a reduced matrix operation in Maxwell (join in series or parallel).  |  
| [`maxwell_boundary.MaxwellForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellForce")  | Initialize Maxwell force.  |  
| [`maxwell_boundary.MaxwellTorque`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellTorque")  | Initialize Maxwell torque.  |  
| [`maxwell_boundary.MaxwellLayoutForce`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellLayoutForce")  | Initialize Maxwell layout force.  |  
| [`layout_boundary.BoundaryObject3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout")  | Manages boundary data and execution for Hfss3dLayout.  |  
| [`icepak_boundary.NetworkObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject.html#ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject "ansys.aedt.core.modules.boundary.icepak_boundary.NetworkObject")  | Manages networks in Icepak projects.  |  
## Maxwell Matrices
To facilitate matrix assignment in Maxwell, multiple classes have been created. These classes help to easily create matrix for different Maxwell solvers for both Maxwell3D and Maxwell2D.  
| [`MatrixElectric`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixElectric")  | Matrix assignment for electric solvers.  |  
| --- | --- |  
| [`SourceMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceMagnetostatic")  | Source definition for magnetostatic solver.  |  
| [`GroupSourcesMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.GroupSourcesMagnetostatic")  | Group sources definition for magnetostatic solver.  |  
| [`MatrixMagnetostatic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixMagnetostatic")  | Matrix assignment for magnetostatic solver.  |  
| [`SourceACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.SourceACMagnetic")  | Sources for AC Magnetic solver.  |  
| [`MatrixACMagnetic`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagnetic")  | Matrix assignment for AC Magnetic solver.  |  
| [`RLSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.RLSourceACMagneticAPhi")  | RL sources for AC Magnetic A-Phi solver.  |  
| [`GCSourceACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.GCSourceACMagneticAPhi")  | GC sources for AC Magnetic A-Phi solver.  |  
| [`MatrixACMagneticAPhi`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi "ansys.aedt.core.modules.boundary.maxwell_boundary.MatrixACMagneticAPhi")  | Matrix assignment for AC Magnetic A-Phi solver.  |  
## Circuit excitations
To facilitate excitations assignment in Circuit, multiple classes have been created.  
| [`Sources`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.Sources.html#ansys.aedt.core.modules.boundary.circuit_boundary.Sources "ansys.aedt.core.modules.boundary.circuit_boundary.Sources")  | Manages sources in Circuit projects.  |  
| --- | --- |  
| [`PowerSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource")  | Power Sinusoidal Class.  |  
| [`PowerIQSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource")  | Power IQ Class.  |  
| [`VoltageFrequencyDependentSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource")  | Voltage Frequency Dependent Class.  |  
| [`VoltageDCSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageDCSource")  | Power Sinusoidal Class.  |  
| [`VoltageSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource")  | Power Sinusoidal Class.  |  
| [`CurrentSinSource`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource")  | Current Sinusoidal Class.  |  
## Native components
When native components object are created, the `NativeComponentObject` class is returned. For PCB components, `NativeComponentPCB` is returned.  
| [`NativeComponentPCB`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB")  | Manages native component PCB data and execution.  |  
| --- | --- |  
| [`NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject")  | Manages Native Component data and execution.  |  
| [`PCBSettingsDeviceParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsDeviceParts")  | Handle device part settings of the PCB component.  |  
| [`PCBSettingsPackageParts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts.html#ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts "ansys.aedt.core.modules.boundary.layout_boundary.PCBSettingsPackageParts")  | Handle package part settings of the PCB component.  |  
`Native Component Object` example:

```
from ansys.aedt.core import Icepak

ipk = Icepak()
component_name = "RadioBoard1"
pcb_comp = self.aedtapp.create_ipk_3dcomponent_pcb(
    component_name,
    link_data,
    solution_freq,
    resolution,
    custom_x_resolution=400,
    custom_y_resolution=500,
)
# pcb_comp is a NativeComponentPCB
...
ipk.release_desktop()

```
Copy to clipboard
## Icepak transient assignments
To facilitate transient assignment handling in Icepak, it is possible to use one of the following classes:  
| [`SinusoidalDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary")  | Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class.  |  
| --- | --- |  
| [`LinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.LinearDictionary")  | Manages linear conditions assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PowerLawDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PowerLawDictionary")  | Manages power law condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`ExponentialDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.ExponentialDictionary")  | Manages exponential condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`SquareWaveDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.SquareWaveDictionary")  | Manages square wave condition assignments, which are children of the `BoundaryDictionary` class.  |  
| [`PieceWiseLinearDictionary`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary.html#ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary "ansys.aedt.core.modules.boundary.icepak_boundary.PieceWiseLinearDictionary")  | Manages dataset condition assignments, which are children of the `BoundaryDictionary` class.  |  
It is possible to initialize the class manually or through a method:

```
bc_transient = ipk.create_sinusoidal_transient_assignment(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
# bc_transient will be SinusoidalDictionary type
ipk.assign_solid_block("Cylinder1", bc_transient)

# or

bc_transient = SinusoidalDictionary(
    vertical_offset="1W", vertical_scaling="3", period="2", period_offset="0.5s"
)
ipk.assign_solid_block("Cylinder1", bc_transient)

```
Copy to clipboard