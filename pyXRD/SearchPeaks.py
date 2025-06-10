import numpy as np
from numpy.lib.stride_tricks import sliding_window_view



from typing import Callable, Union, List

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from typing import Callable, Union, List

def sliding_window_filter(
    y: np.ndarray,
    window_size: int,
    func: Union[Callable, List[Callable]],
    mode: str = 'edge'    ) -> Union[np.ndarray, List[np.ndarray]]:
    """
    Apply a sliding window filter with a given aggregation function(s).
    
    Args:
        y: 1D input signal.
        window_size: Size of the sliding window, odd number if even increse of one
        func: Aggregation function (e.g., np.max) or list of functions.
        mode: Padding mode ('edge', 'reflect', 'constant', etc.).
        
    Returns:
        Filtered signal (or list of signals if `func` is a list).
    """
    window_size = window_size  if  window_size % 2 else window_size +1
    print()
    # Pad the signal to handle edges
    pad = window_size // 2
    y_padded = np.pad(y, pad, mode=mode)
    
    # Create sliding windows
    windows = sliding_window_view(y_padded, window_shape=window_size)
    
    # Apply function(s)
    if isinstance(func, list):
        return [f(windows, axis=1) for f in func]
    else:
        return func(windows, axis=1)
    

def bkg(array2D, axis):
    return(array2D[:, 0] + array2D[:, -1]) / 2

def SearchPeaks(data, window_size=5, threshold=0.1):
    """
    Search for peaks in a 1D numpy array using a max filter.
    
    Parameters:
    - data: 1D numpy array of data to search for peaks.
    - window_size: Size of the sliding window to use for peak detection.
    - threshold: Minimum value a peak must exceed to be considered valid.
    
    Returns:
    - indices: Indices of detected peaks in the original data.
    """
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("data must be a 1D numpy array")
    
    max_values = sliding_window_filter(data, window_size, np.max)
    bkg_values = sliding_window_filter(data, window_size, bkg)    
    peak_indices = np.where((data == max_values) & ((max_values - bkg_values) > threshold))[0] 
    return peak_indices


