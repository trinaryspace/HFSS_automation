---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.compute_fft.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# compute_fft 

ansys.aedt.core.generic.file_utils.compute_fft(_time_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _data_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Compute FFT of input transient data. 

Parameters: 
     

**time_values** pandas.Series 
    
Time points corresponding to the x-axis of the input transient data. 

**data_values** pandas.Series 
    
Points corresponding to the y-axis. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are “hamming”, “hanning”, “blackman”, “bartlett”. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency and values.
Examples

```
>>> import pandas as pd
>>> from ansys.aedt.core.generic.file_utils import compute_fft
>>> compute_fft(pd.Series([0.0, 1e-9, 2e-9]), pd.Series([0.0, 1.0, 0.0]))

```
Copy to clipboard
# compute_fft 

ansys.aedt.core.generic.file_utils.compute_fft(_time_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _data_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Compute FFT of input transient data. 

Parameters: 
     

**time_values** pandas.Series 
    
Time points corresponding to the x-axis of the input transient data. 

**data_values** pandas.Series 
    
Points corresponding to the y-axis. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are “hamming”, “hanning”, “blackman”, “bartlett”. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency and values.
Examples

```
>>> import pandas as pd
>>> from ansys.aedt.core.generic.file_utils import compute_fft
>>> compute_fft(pd.Series([0.0, 1e-9, 2e-9]), pd.Series([0.0, 1.0, 0.0]))

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.compute_fft.rst.txt)

# compute_fft 

ansys.aedt.core.generic.file_utils.compute_fft(_time_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _data_values : [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Compute FFT of input transient data. 

Parameters: 
     

**time_values** pandas.Series 
    
Time points corresponding to the x-axis of the input transient data. 

**data_values** pandas.Series 
    
Points corresponding to the y-axis. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are “hamming”, “hanning”, “blackman”, “bartlett”. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency and values.
Examples

```
>>> import pandas as pd
>>> from ansys.aedt.core.generic.file_utils import compute_fft
>>> compute_fft(pd.Series([0.0, 1e-9, 2e-9]), pd.Series([0.0, 1.0, 0.0]))

```
Copy to clipboard