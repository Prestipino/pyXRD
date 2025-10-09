import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import matplotlib.pyplot as plt

from typing import Callable, Union, List


from numpy.lib.stride_tricks import sliding_window_view
from typing import Callable, Union, List


def sliding_window_filter(
        y: np.ndarray,
        window_size: int,
        func: Union[Callable, List[Callable]],
        mode: str = 'reflect') -> Union[np.ndarray, List[np.ndarray]]:
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
    window_size = window_size if window_size % 2 else window_size + 1
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


# def bkg(array2D, axis):
#    return(array2D[:, 0] + array2D[:, -1]) / 2


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
    # bkg_values = sliding_window_filter(data, window_size, bkg)
    peak_indices = np.where((data == max_values) & (max_values  > threshold))[0]
    return peak_indices


def grey_opening_1d(signal, window_size=3):
    """
    Apply grey opening (erosion + dilation) on a 1D signal.

    Parameters:
        signal (np.ndarray): Input 1D array.
        window_size (int): Size of the structuring element (must be odd).

    Returns:
        np.ndarray: Opened signal.
    """
    eroded = SP.sliding_window_filter(signal, window_size, func=np.min)  # Erosion
    opened = SP.sliding_window_filter(eroded, window_size, func=np.max)  # Dilation
    return opened


def snip_background(signal, num_iterations=100, initial_window=1):
    """
    Vectorized SNIP algorithm using sliding_window_view for background estimation.

    Parameters:
        signal (np.ndarray): Input spectrum (1D array)
        num_iterations (int): Number of clipping iterations
        initial_window (int): Initial window size (grows with iterations)

    Returns:
        np.ndarray: Estimated background
    """
    background = sliding_window_filter(signal, 1 + 2 * initial_window, func=np.mean)

    length = len(signal)

    for i in range(1, num_iterations + 1):
        window_size = 1 + initial_window * i
        avg_neighbors = sliding_window_filter(background, window_size, func=bkg)
        # Update background with element-wise minimum
        background = np.minimum(background, avg_neighbors)

    return sliding_window_filter(background, 1 + 2 * i, func=np.mean)


def select_background_points(signal, max_error=0.05, min_points=5):
    """
    Selects minimal background points where linear interpolation stays within max_error of original.
    Pure NumPy implementation (no Scipy dependency).

    Args:
        signal: 1D array of spectral data
        max_error: Maximum allowed relative error (default 5%)
        min_points: Minimum number of points to keep

    Returns:
        Tuple of (selected_indices, interpolated_background)
    """
    n = len(signal)
    x = np.arange(n)
    selected = np.array([0, n - 1])  # Always keep endpoints
    error = np.inf

    while len(selected) < min_points or error > max_error:
        # Calculate current interpolation
        interp_vals = np.interp(x, x[selected], signal[selected])

        # Compute relative errors (avoid division by zero)
        abs_errors = np.abs(interp_vals - signal)
        rel_errors = abs_errors / (np.abs(signal) + 1e-9)  # Add small constant

        # Mask already selected points
        rel_errors[selected] = -1

        # Select new point with maximum error
        new_point = np.argmax(rel_errors)
        selected = np.unique(np.append(selected, new_point))

        # Update maximum error
        error = np.max(rel_errors)

        # Early exit if we've selected all points
        if len(selected) == n:
            break

    return selected


def search_bkg_points(signal, num_iterations=100, initial_window=1, max_error=0.05, min_points=5):
    bkg = snip_background(signal, num_iterations=num_iterations, initial_window=initial_window)
    bkgpoints = select_background_points(bkg, max_error=0.05, min_points=5)
    y_bkg = bkg[bkgpoints]
    y_bkg[bkgpoints[0]] = signal[bkgpoints[0]]
    return bkgpoints, y_bkg, bkg


def peakdet(y, delta=0.03, x=None, plot=True, simple=True,
            add_peaks=None, add_valleys=None, lookformax=False):
    """Peak determination routine
    finds the local maxima and minima ("peaks") in the vector y.
    a local minimum or maximumis defined as a the numerical min/max that it is at list
    higher than delta
    It is supposed to start with a minimum

    Args:
        y (np.array type): vector on which seach the maximum and minimum,
                          it is supposed to start with a minimum
        x (np.array type): vector with corresponding x in respect of y
        delta (float): step limit % of (max-min) if negative just absolute value
        bkg_f (float): np.inf  Non ho idea
        plot (bool): create a plot showng valley and peaks
        simple (bool) : if True returns the value of index(x) for peak and valleys
                        if Falsereturns index and value ,
        add_peaks= array to add a peaks
        add_valleys=array to add a valley

    Returns:
        peaks  (1/2D np.array): position /intensity of peaks
        valley (1/2D np.array): position /intensity of valley

    Examples:
    peaks, valleys=FP.peakdet(y, x = x, delta=0.02, plot=True)



    % Converted from MATLAB script at http://billauer.co.il/peakdet.html
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    % quite modified already ; )

    """
    maxtab = []
    mintab = []

    if x is None:
        x = np.arange(len(y))

    y = np.asarray(y)

    if delta:
        if delta > 0:
            delta *= (y.max() - y.min())
        else:
            delta *= -1
    else:
        delta = 0.03 * (y.max() - y.min())

    assert len(y) == len(x), IOError(
        'Input vectors v and x must have same length')

    assert np.isscalar(delta), IOError('Input argument delta must be a scalar')

    mn, mx = np.Inf, -np.Inf
    mnpos, mxpos = np.NaN, np.NaN

    #lookformax = True

    for i, this in enumerate(y):
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx - delta:
                # if len(maxtab) == 0:   # add first minimum
                #    mintab.append((mnpos, mn))
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn + delta:
                #if mn < mintab[-1][1]:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    if not(lookformax):           # add last minimum
        mintab.append((mnpos, mn))

    peaks, valleys = np.array(maxtab).T, np.array(mintab).T

    assert len(peaks) > 1, IOError('Too high delta 0-1')

    if add_peaks:
        for pic in add_peaks:
            if peaks[0][-1] < pic:
                ipic = len(peaks)
            else:
                ipic = np.argmax(peaks > pic)
            ipeak = index_of(x, pic)
            peaks = np.insert(peaks, ipic, [x[ipeak], y[ipeak]], axis=1)

    if add_valleys:
        for val in add_valleys:
            if valleys[0][-1] < val:
                ival = len(peaks)
            else:
                ival = np.argmax(peaks > val)
            ipeak = index_of(x, val)
            peaks = np.insert(peaks, ival, [x[ipeak], y[ipeak]], axis=1)

    if plot:
        plt.figure()
        plt.plot(x, y, label='exp')
        # plt.xlim(18,58)
        plt.plot(peaks[0], peaks[1], 'ro', picker=5)
        plt.plot(valleys[0], valleys[1], 'bo', picker=5)
        plt.legend()

    if simple:
        return peaks[0], valleys[0]
    else:
        return peaks, valleys
    
############################################################################

def add_peak(peaklist, peak):
    if peak > peaklist[-1]:
        return np.append(peaklist, peak)
    else:
        return np.insert(peaklist, np.argmax(peaklist > peak), peak)


def del_peak(peaklist, peak):
    return np.delete(peaklist, index_of(peaklist, peak))