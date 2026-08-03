---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pdf.AnsysReport.add_table.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# add_table 

AnsysReport.add_table(_title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _content : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")]_, _formatting : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _col_widths : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new table from a list of data.
Data shall be a list of list where every line is either a row or a column. 

Parameters: 
     

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table title. 

**content**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Table content. 

**formatting**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of formatting elements for the table rows. The length of the formatting has to be equal to the length of content. Every element is a list of two elements (color, background_color). Color is a RGB list. 

**col_widths**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of column widths.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pdf import AnsysReport
>>> obj = AnsysReport()
>>> obj.add_table("Table Title", [["Header1", "Header2"], ["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]])

```
Copy to clipboard
# add_table 

AnsysReport.add_table(_title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _content : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")]_, _formatting : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _col_widths : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new table from a list of data.
Data shall be a list of list where every line is either a row or a column. 

Parameters: 
     

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table title. 

**content**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Table content. 

**formatting**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of formatting elements for the table rows. The length of the formatting has to be equal to the length of content. Every element is a list of two elements (color, background_color). Color is a RGB list. 

**col_widths**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of column widths.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pdf import AnsysReport
>>> obj = AnsysReport()
>>> obj.add_table("Table Title", [["Header1", "Header2"], ["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pdf.AnsysReport.add_table.rst.txt)

# add_table 

AnsysReport.add_table(_title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _content : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")]_, _formatting : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _col_widths : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new table from a list of data.
Data shall be a list of list where every line is either a row or a column. 

Parameters: 
     

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Table title. 

**content**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Table content. 

**formatting**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of formatting elements for the table rows. The length of the formatting has to be equal to the length of content. Every element is a list of two elements (color, background_color). Color is a RGB list. 

**col_widths**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of column widths.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pdf import AnsysReport
>>> obj = AnsysReport()
>>> obj.add_table("Table Title", [["Header1", "Header2"], ["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]])

```
Copy to clipboard