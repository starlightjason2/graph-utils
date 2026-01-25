"""Curve fitting functions for data analysis."""

import numpy as np


def line_func(x, m, b):
    """Linear fitting function: y = m*x + b.
    
    Args:
        x: Input values
        m: Slope parameter
        b: Y-intercept parameter
        
    Returns:
        Fitted y values
    """
    return m * x + b


def exp_func(x, a, b):
    """Exponential/logarithmic fitting function: y = a * log(b * x).
    
    Args:
        x: Input values
        a: Amplitude parameter
        b: Scale parameter
        
    Returns:
        Fitted y values
    """
    return a * np.log(b * x)
