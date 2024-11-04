import numpy as np

"""
Functions for calculating ion channel gate variables. We include alpha and beta rate constants for n, m, and h.
"""

def alpha_n(V):
    """Potassium activation rate."""
    return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

def beta_n(V):
    """Potassium deactivation rate."""
    return 0.125 * np.exp(-(V + 65) / 80)

def alpha_m(V):
    """Sodium activation rate."""
    return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))

def beta_m(V):
    """Sodium deactivation rate."""
    return 4 * np.exp(-(V + 65) / 18)

def alpha_h(V):
    """Sodium inactivation rate."""
    return 0.07 * np.exp(-(V + 65) / 20)

def beta_h(V):
    """Sodium deinactivation rate."""
    return 1 / (1 + np.exp(-(V + 35) / 10))

