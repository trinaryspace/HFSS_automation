---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.circuit_port.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# circuit_port 

Hfss.circuit_port(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _reference : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _port_location : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _renormalize : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '50'_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a circuit port from two objects.
The integration line is from edge 2 to edge 1. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Signal object. 

**reference**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Reference object. 

**port_location**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port when an object different from an edge is provided. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the port. The default is `""`. 

**impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `"50"`. You can also enter a string that looks like this: `"50+1i*55"`. 

**renormalize**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize the mode. The default is `False`. This parameter is ignored for a driven terminal. 

**renorm_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `50`. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed the port. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCircuitPort

```
Copy to clipboard
Examples
Create two rectangles in the XY plane. Select the first edge of each rectangle created previously. Create a circuit port from the first edge of the first rectangle toward the first edge of the second rectangle.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> plane = Plane.XY
>>> rectangle1 = hfss.modeler.create_rectangle(plane, [10, 10, 10], [10, 10], name="rectangle1_for_port")
>>> edges1 = hfss.modeler.get_object_edges(rectangle1.id)
>>> first_edge = edges1[0]
>>> rectangle2 = hfss.modeler.create_rectangle(plane, [30, 10, 10], [10, 10], name="rectangle2_for_port")
>>> edges2 = hfss.modeler.get_object_edges(rectangle2.id)
>>> second_edge = edges2[0]
>>> hfss.solution_type = "Modal"
>>> hfss.circuit_port(
...     first_edge, second_edge, impedance=50.1, name="PortExample", renormalize=False, renorm_impedance="50"
... )
'PortExample'

```
Copy to clipboard
# circuit_port 

Hfss.circuit_port(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _reference : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _port_location : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _renormalize : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '50'_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a circuit port from two objects.
The integration line is from edge 2 to edge 1. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Signal object. 

**reference**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Reference object. 

**port_location**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port when an object different from an edge is provided. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the port. The default is `""`. 

**impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `"50"`. You can also enter a string that looks like this: `"50+1i*55"`. 

**renormalize**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize the mode. The default is `False`. This parameter is ignored for a driven terminal. 

**renorm_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `50`. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed the port. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCircuitPort

```
Copy to clipboard
Examples
Create two rectangles in the XY plane. Select the first edge of each rectangle created previously. Create a circuit port from the first edge of the first rectangle toward the first edge of the second rectangle.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> plane = Plane.XY
>>> rectangle1 = hfss.modeler.create_rectangle(plane, [10, 10, 10], [10, 10], name="rectangle1_for_port")
>>> edges1 = hfss.modeler.get_object_edges(rectangle1.id)
>>> first_edge = edges1[0]
>>> rectangle2 = hfss.modeler.create_rectangle(plane, [30, 10, 10], [10, 10], name="rectangle2_for_port")
>>> edges2 = hfss.modeler.get_object_edges(rectangle2.id)
>>> second_edge = edges2[0]
>>> hfss.solution_type = "Modal"
>>> hfss.circuit_port(
...     first_edge, second_edge, impedance=50.1, name="PortExample", renormalize=False, renorm_impedance="50"
... )
'PortExample'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.circuit_port.rst.txt)

# circuit_port 

Hfss.circuit_port(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _reference : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _port_location : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _renormalize : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '50'_, _deembed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a circuit port from two objects.
The integration line is from edge 2 to edge 1. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Signal object. 

**reference**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") `or` 
     

`ansys.aedt.core.modeler.cad.FacePrimitive`or :class:`ansys.aedt.core.modeler.cad.EdgePrimitive`
    
Reference object. 

**port_location**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Position of the port when an object different from an edge is provided. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the port. The default is `""`. 

**impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `"50"`. You can also enter a string that looks like this: `"50+1i*55"`. 

**renormalize**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize the mode. The default is `False`. This parameter is ignored for a driven terminal. 

**renorm_impedance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Impedance. The default is `50`. 

**deembed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to deembed the port. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCircuitPort

```
Copy to clipboard
Examples
Create two rectangles in the XY plane. Select the first edge of each rectangle created previously. Create a circuit port from the first edge of the first rectangle toward the first edge of the second rectangle.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> plane = Plane.XY
>>> rectangle1 = hfss.modeler.create_rectangle(plane, [10, 10, 10], [10, 10], name="rectangle1_for_port")
>>> edges1 = hfss.modeler.get_object_edges(rectangle1.id)
>>> first_edge = edges1[0]
>>> rectangle2 = hfss.modeler.create_rectangle(plane, [30, 10, 10], [10, 10], name="rectangle2_for_port")
>>> edges2 = hfss.modeler.get_object_edges(rectangle2.id)
>>> second_edge = edges2[0]
>>> hfss.solution_type = "Modal"
>>> hfss.circuit_port(
...     first_edge, second_edge, impedance=50.1, name="PortExample", renormalize=False, renorm_impedance="50"
... )
'PortExample'

```
Copy to clipboard