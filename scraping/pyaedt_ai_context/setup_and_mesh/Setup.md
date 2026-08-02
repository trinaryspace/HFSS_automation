---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/Setup.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Setup
This section lists setup modules:
  * `Setup` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `Setup3DLayout` for HFSS 3D Layout
  * `SetupCircuit` for Circuit and Twin Builder

The `Setup` object is accessible through the `create_setup` method and `setups` object list.  
| [`SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS")  | Initializes, creates, and updates an HFSS setup.  |  
| --- | --- |  
| [`SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")  | Initializes, creates, and updates an HFSS Auto setup.  |  
| [`SetupSBR`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupSBR.html#ansys.aedt.core.modules.solve_setup.SetupSBR "ansys.aedt.core.modules.solve_setup.SetupSBR")  | Initializes, creates, and updates an HFSS SBR+ or HFSS Auto setup.  |  
| [`SetupQ3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupQ3D.html#ansys.aedt.core.modules.solve_setup.SetupQ3D "ansys.aedt.core.modules.solve_setup.SetupQ3D")  | Initializes, creates, and updates an Q3D setup.  |  
| [`SetupMaxwell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupMaxwell.html#ansys.aedt.core.modules.solve_setup.SetupMaxwell "ansys.aedt.core.modules.solve_setup.SetupMaxwell")  | Initializes, creates, and updates a Maxwell setup.  |  
| [`Setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.html#ansys.aedt.core.modules.solve_setup.Setup "ansys.aedt.core.modules.solve_setup.Setup")  | Initializes, creates, and updates a 3D setup.  |  
| [`Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")  | Initializes, creates, and updates a 3D Layout setup.  |  
| [`SetupCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupCircuit.html#ansys.aedt.core.modules.solve_setup.SetupCircuit "ansys.aedt.core.modules.solve_setup.SetupCircuit")  | Manages a circuit setup.  |  

```
from ansys.aedt.core import Hfss

app = Hfss(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)

# This call returns the Setup class
my_setup = app.setups[0]

# This call returns a Setup object
setup = app.create_setup("MySetup")

...

```
Copy to clipboard
# Sweep classes
This section lists sweep classes and their default values:
  * `SweepHFSS` for HFSS
  * `SweepHFSS3DLayout` for HFSS 3D Layout
  * `SweepMatrix` for Q3D and 2D Extractor

The `Setup` object is accessible through the methods available for sweep creation.  
| [`SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")  | Initializes, creates, and updates sweeps in HFSS.  |  
| --- | --- |  
| [`SweepHFSS3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout "ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout")  | Initializes, creates, and updates sweeps in HFSS 3D Layout.  |  
| [`SweepMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepMatrix.html#ansys.aedt.core.modules.solve_sweeps.SweepMatrix "ansys.aedt.core.modules.solve_sweeps.SweepMatrix")  | Initializes, creates, and updates sweeps in Q3D.  |  
# Setup
This section lists setup modules:
  * `Setup` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `Setup3DLayout` for HFSS 3D Layout
  * `SetupCircuit` for Circuit and Twin Builder

The `Setup` object is accessible through the `create_setup` method and `setups` object list.  
| [`SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS")  | Initializes, creates, and updates an HFSS setup.  |  
| --- | --- |  
| [`SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")  | Initializes, creates, and updates an HFSS Auto setup.  |  
| [`SetupSBR`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupSBR.html#ansys.aedt.core.modules.solve_setup.SetupSBR "ansys.aedt.core.modules.solve_setup.SetupSBR")  | Initializes, creates, and updates an HFSS SBR+ or HFSS Auto setup.  |  
| [`SetupQ3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupQ3D.html#ansys.aedt.core.modules.solve_setup.SetupQ3D "ansys.aedt.core.modules.solve_setup.SetupQ3D")  | Initializes, creates, and updates an Q3D setup.  |  
| [`SetupMaxwell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupMaxwell.html#ansys.aedt.core.modules.solve_setup.SetupMaxwell "ansys.aedt.core.modules.solve_setup.SetupMaxwell")  | Initializes, creates, and updates a Maxwell setup.  |  
| [`Setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.html#ansys.aedt.core.modules.solve_setup.Setup "ansys.aedt.core.modules.solve_setup.Setup")  | Initializes, creates, and updates a 3D setup.  |  
| [`Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")  | Initializes, creates, and updates a 3D Layout setup.  |  
| [`SetupCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupCircuit.html#ansys.aedt.core.modules.solve_setup.SetupCircuit "ansys.aedt.core.modules.solve_setup.SetupCircuit")  | Manages a circuit setup.  |  

```
from ansys.aedt.core import Hfss

app = Hfss(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)

# This call returns the Setup class
my_setup = app.setups[0]

# This call returns a Setup object
setup = app.create_setup("MySetup")

...

```
Copy to clipboard
# Sweep classes
This section lists sweep classes and their default values:
  * `SweepHFSS` for HFSS
  * `SweepHFSS3DLayout` for HFSS 3D Layout
  * `SweepMatrix` for Q3D and 2D Extractor

The `Setup` object is accessible through the methods available for sweep creation.  
| [`SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")  | Initializes, creates, and updates sweeps in HFSS.  |  
| --- | --- |  
| [`SweepHFSS3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout "ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout")  | Initializes, creates, and updates sweeps in HFSS 3D Layout.  |  
| [`SweepMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepMatrix.html#ansys.aedt.core.modules.solve_sweeps.SweepMatrix "ansys.aedt.core.modules.solve_sweeps.SweepMatrix")  | Initializes, creates, and updates sweeps in Q3D.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/Setup.rst.txt)

# Setup
This section lists setup modules:
  * `Setup` for HFSS, Maxwell 2D, Maxwell 3D, Q2D Extractor, and Q3D Extractor
  * `Setup3DLayout` for HFSS 3D Layout
  * `SetupCircuit` for Circuit and Twin Builder

The `Setup` object is accessible through the `create_setup` method and `setups` object list.  
| [`SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS")  | Initializes, creates, and updates an HFSS setup.  |  
| --- | --- |  
| [`SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto")  | Initializes, creates, and updates an HFSS Auto setup.  |  
| [`SetupSBR`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupSBR.html#ansys.aedt.core.modules.solve_setup.SetupSBR "ansys.aedt.core.modules.solve_setup.SetupSBR")  | Initializes, creates, and updates an HFSS SBR+ or HFSS Auto setup.  |  
| [`SetupQ3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupQ3D.html#ansys.aedt.core.modules.solve_setup.SetupQ3D "ansys.aedt.core.modules.solve_setup.SetupQ3D")  | Initializes, creates, and updates an Q3D setup.  |  
| [`SetupMaxwell`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupMaxwell.html#ansys.aedt.core.modules.solve_setup.SetupMaxwell "ansys.aedt.core.modules.solve_setup.SetupMaxwell")  | Initializes, creates, and updates a Maxwell setup.  |  
| [`Setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.html#ansys.aedt.core.modules.solve_setup.Setup "ansys.aedt.core.modules.solve_setup.Setup")  | Initializes, creates, and updates a 3D setup.  |  
| [`Setup3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup3DLayout.html#ansys.aedt.core.modules.solve_setup.Setup3DLayout "ansys.aedt.core.modules.solve_setup.Setup3DLayout")  | Initializes, creates, and updates a 3D Layout setup.  |  
| [`SetupCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupCircuit.html#ansys.aedt.core.modules.solve_setup.SetupCircuit "ansys.aedt.core.modules.solve_setup.SetupCircuit")  | Manages a circuit setup.  |  

```
from ansys.aedt.core import Hfss

app = Hfss(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)

# This call returns the Setup class
my_setup = app.setups[0]

# This call returns a Setup object
setup = app.create_setup("MySetup")

...

```
Copy to clipboard
# Sweep classes
This section lists sweep classes and their default values:
  * `SweepHFSS` for HFSS
  * `SweepHFSS3DLayout` for HFSS 3D Layout
  * `SweepMatrix` for Q3D and 2D Extractor

The `Setup` object is accessible through the methods available for sweep creation.  
| [`SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")  | Initializes, creates, and updates sweeps in HFSS.  |  
| --- | --- |  
| [`SweepHFSS3DLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout "ansys.aedt.core.modules.solve_sweeps.SweepHFSS3DLayout")  | Initializes, creates, and updates sweeps in HFSS 3D Layout.  |  
| [`SweepMatrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepMatrix.html#ansys.aedt.core.modules.solve_sweeps.SweepMatrix "ansys.aedt.core.modules.solve_sweeps.SweepMatrix")  | Initializes, creates, and updates sweeps in Q3D.  |