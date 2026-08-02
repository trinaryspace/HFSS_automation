---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_radar_from_json.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_sbr_radar_from_json 

Hfss.create_sbr_radar_from_json(_radar_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _relative_cs_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Radar](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar") 
    
Create an SBR+ radar setup from a JSON file.
Example of input JSON file:
> 
```
{
    "name": "Example_1Tx_1Rx",
    "version": 1,
    "number_tx":"1",
    "number_rx":"1",
    "units":"mm",
    "antennas": {
        "tx1": {
            "antenna_type":"parametric",
            "mode":"tx",
            "offset":["0" ,"0" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            },
        "rx1": {
            "antenna_type":"parametric",
            "mode":"rx",
            "offset":["0" ,"1.8" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**radar_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the directory with the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the radar file. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset relative to the global coordinate system. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radar movement speed relative to the global coordinate system if greater than `0`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system to link the radar to. The default is `None`, in which case the global coordinate system is used. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.actors.Radar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar")
    
Radar class object.
References
AEDT API Commands.

```
>>> oEditor.CreateRelativeCS
>>> oModule.SetSBRTxRxSettings
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> hfss.create_sbr_radar_from_json("radar_dir", name="Example_1Tx_1Rx", speed=3)

```
Copy to clipboard
# create_sbr_radar_from_json 

Hfss.create_sbr_radar_from_json(_radar_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _relative_cs_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Radar](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar") 
    
Create an SBR+ radar setup from a JSON file.
Example of input JSON file:
> 
```
{
    "name": "Example_1Tx_1Rx",
    "version": 1,
    "number_tx":"1",
    "number_rx":"1",
    "units":"mm",
    "antennas": {
        "tx1": {
            "antenna_type":"parametric",
            "mode":"tx",
            "offset":["0" ,"0" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            },
        "rx1": {
            "antenna_type":"parametric",
            "mode":"rx",
            "offset":["0" ,"1.8" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**radar_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the directory with the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the radar file. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset relative to the global coordinate system. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radar movement speed relative to the global coordinate system if greater than `0`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system to link the radar to. The default is `None`, in which case the global coordinate system is used. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.actors.Radar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar")
    
Radar class object.
References
AEDT API Commands.

```
>>> oEditor.CreateRelativeCS
>>> oModule.SetSBRTxRxSettings
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> hfss.create_sbr_radar_from_json("radar_dir", name="Example_1Tx_1Rx", speed=3)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_radar_from_json.rst.txt)

# create_sbr_radar_from_json 

Hfss.create_sbr_radar_from_json(_radar_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _relative_cs_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Radar](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar") 
    
Create an SBR+ radar setup from a JSON file.
Example of input JSON file:
> 
```
{
    "name": "Example_1Tx_1Rx",
    "version": 1,
    "number_tx":"1",
    "number_rx":"1",
    "units":"mm",
    "antennas": {
        "tx1": {
            "antenna_type":"parametric",
            "mode":"tx",
            "offset":["0" ,"0" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            },
        "rx1": {
            "antenna_type":"parametric",
            "mode":"rx",
            "offset":["0" ,"1.8" ,"0"],
            "rotation_axis":null,
            "rotation":null,
            "beamwidth_elevation":"10deg",
            "beamwidth_azimuth":"60deg",
            "polarization":"Vertical"
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**radar_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the directory with the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the radar file. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset relative to the global coordinate system. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Radar movement speed relative to the global coordinate system if greater than `0`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system to link the radar to. The default is `None`, in which case the global coordinate system is used. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.actors.Radar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar "ansys.aedt.core.modeler.advanced_cad.actors.Radar")
    
Radar class object.
References
AEDT API Commands.

```
>>> oEditor.CreateRelativeCS
>>> oModule.SetSBRTxRxSettings
>>> oEditor.CreateGroup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> hfss.create_sbr_radar_from_json("radar_dir", name="Example_1Tx_1Rx", speed=3)

```
Copy to clipboard