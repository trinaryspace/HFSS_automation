---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/Application.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# Application and solvers
The PyAEDT API includes classes for different applications available in Ansys Electronics Desktop (AEDT). You must initialize AEDT to get access to all PyAEDT modules and methods.
[![Ansys Electronics Desktop \(AEDT\) is a platform that enables true electronics system design.](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png) ](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png)
Available PyAEDT apps are:  
| [`ansys.aedt.core.desktop.Desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.html#ansys.aedt.core.desktop.Desktop "ansys.aedt.core.desktop.Desktop")(*args, **kwargs)  | Provides the Ansys Electronics Desktop (AEDT) interface.  |  
| --- | --- |  
| [`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")([project, design, ...])  | Provides the HFSS application interface.  |  
| [`ansys.aedt.core.q3d.Q3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q3d.html#ansys.aedt.core.q3d.Q3d "ansys.aedt.core.q3d.Q3d")([project, design, ...])  | Provides the Q3D app interface.  |  
| [`ansys.aedt.core.q3d.Q2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.html#ansys.aedt.core.q3d.Q2d "ansys.aedt.core.q3d.Q2d")([project, design, ...])  | Provides the Q2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d")([project, ...])  | Provides the Maxwell 2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d")([project, ...])  | Provides the Maxwell 3D app interface.  |  
| [`ansys.aedt.core.icepak.Icepak`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.icepak.Icepak.html#ansys.aedt.core.icepak.Icepak "ansys.aedt.core.icepak.Icepak")([project, ...])  | Provides the Icepak application interface.  |  
| [`ansys.aedt.core.hfss3dlayout.Hfss3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.html#ansys.aedt.core.hfss3dlayout.Hfss3dLayout "ansys.aedt.core.hfss3dlayout.Hfss3dLayout")([...])  | Provides the HFSS 3D Layout application interface.  |  
| [`ansys.aedt.core.mechanical.Mechanical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.mechanical.Mechanical.html#ansys.aedt.core.mechanical.Mechanical "ansys.aedt.core.mechanical.Mechanical")([...])  | Provides the Mechanical application interface.  |  
| [`ansys.aedt.core.rmxprt.Rmxprt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.rmxprt.Rmxprt.html#ansys.aedt.core.rmxprt.Rmxprt "ansys.aedt.core.rmxprt.Rmxprt")([project, ...])  | Provides the RMxprt app interface.  |  
| [`ansys.aedt.core.circuit.Circuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.circuit.Circuit.html#ansys.aedt.core.circuit.Circuit "ansys.aedt.core.circuit.Circuit")([project, ...])  | Provides the Circuit application interface.  |  
| [`ansys.aedt.core.maxwellcircuit.MaxwellCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwellcircuit.MaxwellCircuit.html#ansys.aedt.core.maxwellcircuit.MaxwellCircuit "ansys.aedt.core.maxwellcircuit.MaxwellCircuit")([...])  | Provide the Maxwell Circuit application interface.  |  
| [`ansys.aedt.core.emit.Emit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.emit.Emit.html#ansys.aedt.core.emit.Emit "ansys.aedt.core.emit.Emit")([project, design, ...])  | Provides the EMIT application interface.  |  
| [`ansys.aedt.core.twinbuilder.TwinBuilder`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.twinbuilder.TwinBuilder.html#ansys.aedt.core.twinbuilder.TwinBuilder "ansys.aedt.core.twinbuilder.TwinBuilder")([...])  | Provides the Twin Builder application interface.  |  
All other classes and methods are inherited into the app class. AEDT, which is also referred to as the desktop app, is implicitly launched in any PyAEDT app. Before accessing a PyAEDT app, the desktop app must be launched and initialized. The desktop app can be explicitly or implicitly initialized as in the following examples.
Example with `Desktop` class explicit initialization:

```
from ansys.aedt.core import launch_desktop, Circuit

d = launch_desktop(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
d.release_desktop()

```
Copy to clipboard
Example with `Desktop` class implicit initialization:

```
from ansys.aedt.core import Circuit

circuit = Circuit(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
circuit.release_desktop()

```
Copy to clipboard
# Application and solvers
The PyAEDT API includes classes for different applications available in Ansys Electronics Desktop (AEDT). You must initialize AEDT to get access to all PyAEDT modules and methods.
[![Ansys Electronics Desktop \(AEDT\) is a platform that enables true electronics system design.](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png) ](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png)
Available PyAEDT apps are:  
| [`ansys.aedt.core.desktop.Desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.html#ansys.aedt.core.desktop.Desktop "ansys.aedt.core.desktop.Desktop")(*args, **kwargs)  | Provides the Ansys Electronics Desktop (AEDT) interface.  |  
| --- | --- |  
| [`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")([project, design, ...])  | Provides the HFSS application interface.  |  
| [`ansys.aedt.core.q3d.Q3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q3d.html#ansys.aedt.core.q3d.Q3d "ansys.aedt.core.q3d.Q3d")([project, design, ...])  | Provides the Q3D app interface.  |  
| [`ansys.aedt.core.q3d.Q2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.html#ansys.aedt.core.q3d.Q2d "ansys.aedt.core.q3d.Q2d")([project, design, ...])  | Provides the Q2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d")([project, ...])  | Provides the Maxwell 2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d")([project, ...])  | Provides the Maxwell 3D app interface.  |  
| [`ansys.aedt.core.icepak.Icepak`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.icepak.Icepak.html#ansys.aedt.core.icepak.Icepak "ansys.aedt.core.icepak.Icepak")([project, ...])  | Provides the Icepak application interface.  |  
| [`ansys.aedt.core.hfss3dlayout.Hfss3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.html#ansys.aedt.core.hfss3dlayout.Hfss3dLayout "ansys.aedt.core.hfss3dlayout.Hfss3dLayout")([...])  | Provides the HFSS 3D Layout application interface.  |  
| [`ansys.aedt.core.mechanical.Mechanical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.mechanical.Mechanical.html#ansys.aedt.core.mechanical.Mechanical "ansys.aedt.core.mechanical.Mechanical")([...])  | Provides the Mechanical application interface.  |  
| [`ansys.aedt.core.rmxprt.Rmxprt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.rmxprt.Rmxprt.html#ansys.aedt.core.rmxprt.Rmxprt "ansys.aedt.core.rmxprt.Rmxprt")([project, ...])  | Provides the RMxprt app interface.  |  
| [`ansys.aedt.core.circuit.Circuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.circuit.Circuit.html#ansys.aedt.core.circuit.Circuit "ansys.aedt.core.circuit.Circuit")([project, ...])  | Provides the Circuit application interface.  |  
| [`ansys.aedt.core.maxwellcircuit.MaxwellCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwellcircuit.MaxwellCircuit.html#ansys.aedt.core.maxwellcircuit.MaxwellCircuit "ansys.aedt.core.maxwellcircuit.MaxwellCircuit")([...])  | Provide the Maxwell Circuit application interface.  |  
| [`ansys.aedt.core.emit.Emit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.emit.Emit.html#ansys.aedt.core.emit.Emit "ansys.aedt.core.emit.Emit")([project, design, ...])  | Provides the EMIT application interface.  |  
| [`ansys.aedt.core.twinbuilder.TwinBuilder`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.twinbuilder.TwinBuilder.html#ansys.aedt.core.twinbuilder.TwinBuilder "ansys.aedt.core.twinbuilder.TwinBuilder")([...])  | Provides the Twin Builder application interface.  |  
All other classes and methods are inherited into the app class. AEDT, which is also referred to as the desktop app, is implicitly launched in any PyAEDT app. Before accessing a PyAEDT app, the desktop app must be launched and initialized. The desktop app can be explicitly or implicitly initialized as in the following examples.
Example with `Desktop` class explicit initialization:

```
from ansys.aedt.core import launch_desktop, Circuit

d = launch_desktop(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
d.release_desktop()

```
Copy to clipboard
Example with `Desktop` class implicit initialization:

```
from ansys.aedt.core import Circuit

circuit = Circuit(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
circuit.release_desktop()

```
Copy to clipboard
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/Application.rst.txt)

# Application and solvers
The PyAEDT API includes classes for different applications available in Ansys Electronics Desktop (AEDT). You must initialize AEDT to get access to all PyAEDT modules and methods.
[![Ansys Electronics Desktop \(AEDT\) is a platform that enables true electronics system design.](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png) ](https://aedt.docs.pyansys.com/version/stable/_images/aedt_2.png)
Available PyAEDT apps are:  
| [`ansys.aedt.core.desktop.Desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.html#ansys.aedt.core.desktop.Desktop "ansys.aedt.core.desktop.Desktop")(*args, **kwargs)  | Provides the Ansys Electronics Desktop (AEDT) interface.  |  
| --- | --- |  
| [`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")([project, design, ...])  | Provides the HFSS application interface.  |  
| [`ansys.aedt.core.q3d.Q3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q3d.html#ansys.aedt.core.q3d.Q3d "ansys.aedt.core.q3d.Q3d")([project, design, ...])  | Provides the Q3D app interface.  |  
| [`ansys.aedt.core.q3d.Q2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.html#ansys.aedt.core.q3d.Q2d "ansys.aedt.core.q3d.Q2d")([project, design, ...])  | Provides the Q2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d")([project, ...])  | Provides the Maxwell 2D app interface.  |  
| [`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d")([project, ...])  | Provides the Maxwell 3D app interface.  |  
| [`ansys.aedt.core.icepak.Icepak`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.icepak.Icepak.html#ansys.aedt.core.icepak.Icepak "ansys.aedt.core.icepak.Icepak")([project, ...])  | Provides the Icepak application interface.  |  
| [`ansys.aedt.core.hfss3dlayout.Hfss3dLayout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.html#ansys.aedt.core.hfss3dlayout.Hfss3dLayout "ansys.aedt.core.hfss3dlayout.Hfss3dLayout")([...])  | Provides the HFSS 3D Layout application interface.  |  
| [`ansys.aedt.core.mechanical.Mechanical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.mechanical.Mechanical.html#ansys.aedt.core.mechanical.Mechanical "ansys.aedt.core.mechanical.Mechanical")([...])  | Provides the Mechanical application interface.  |  
| [`ansys.aedt.core.rmxprt.Rmxprt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.rmxprt.Rmxprt.html#ansys.aedt.core.rmxprt.Rmxprt "ansys.aedt.core.rmxprt.Rmxprt")([project, ...])  | Provides the RMxprt app interface.  |  
| [`ansys.aedt.core.circuit.Circuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.circuit.Circuit.html#ansys.aedt.core.circuit.Circuit "ansys.aedt.core.circuit.Circuit")([project, ...])  | Provides the Circuit application interface.  |  
| [`ansys.aedt.core.maxwellcircuit.MaxwellCircuit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwellcircuit.MaxwellCircuit.html#ansys.aedt.core.maxwellcircuit.MaxwellCircuit "ansys.aedt.core.maxwellcircuit.MaxwellCircuit")([...])  | Provide the Maxwell Circuit application interface.  |  
| [`ansys.aedt.core.emit.Emit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.emit.Emit.html#ansys.aedt.core.emit.Emit "ansys.aedt.core.emit.Emit")([project, design, ...])  | Provides the EMIT application interface.  |  
| [`ansys.aedt.core.twinbuilder.TwinBuilder`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.twinbuilder.TwinBuilder.html#ansys.aedt.core.twinbuilder.TwinBuilder "ansys.aedt.core.twinbuilder.TwinBuilder")([...])  | Provides the Twin Builder application interface.  |  
All other classes and methods are inherited into the app class. AEDT, which is also referred to as the desktop app, is implicitly launched in any PyAEDT app. Before accessing a PyAEDT app, the desktop app must be launched and initialized. The desktop app can be explicitly or implicitly initialized as in the following examples.
Example with `Desktop` class explicit initialization:

```
from ansys.aedt.core import launch_desktop, Circuit

d = launch_desktop(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
d.release_desktop()

```
Copy to clipboard
Example with `Desktop` class implicit initialization:

```
from ansys.aedt.core import Circuit

circuit = Circuit(
    version="2026.1",
    non_graphical=False,
    new_desktop=True,
    close_on_exit=True,
    student_version=False,
)
circuit = Circuit()
# ...
# Any error here will be caught by Desktop.
# ...
circuit.release_desktop()

```
Copy to clipboard