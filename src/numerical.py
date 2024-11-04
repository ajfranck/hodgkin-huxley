import numpy as np

"""
Implementation of several numerical methods for solving differential equations, including Euler-Cromer, Runge-Kutta, and Adams-Bashforth methods.
"""

def euler_cromer(func, y0, t_span, dt):
    """
    Args:
        func: Function that returns derivatives
        y0: Initial conditions
        t_span: Time span [t_start, t_end]
        dt: Time step
    """
    t = np.arange(t_span[0], t_span[1], dt)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, len(t)):
        y[i] = y[i-1] + dt * func(t[i-1], y[i-1])
    
    return t, y

def runge_kutta(func, y0, t_span, dt):
    """
    Args:
        func: Function that returns derivatives
        y0: Initial conditions
        t_span: Time span [t_start, t_end]
        dt: Time step
    """
    t = np.arange(t_span[0], t_span[1], dt)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, len(t)):
        k1 = dt * func(t[i-1], y[i-1])
        k2 = dt * func(t[i-1] + dt/2, y[i-1] + k1/2)
        k3 = dt * func(t[i-1] + dt/2, y[i-1] + k2/2)
        k4 = dt * func(t[i-1] + dt, y[i-1] + k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, y

def adams_bashforth(func, y0, t_span, dt):
    """
    Args:
        func: Function that returns derivatives
        y0: Initial conditions
        t_span: Time span [t_start, t_end]
        dt: Time step
    """
    t = np.arange(t_span[0], t_span[1], dt)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, 4):
        k1 = dt * func(t[i-1], y[i-1])
        k2 = dt * func(t[i-1] + dt/2, y[i-1] + k1/2)
        k3 = dt * func(t[i-1] + dt/2, y[i-1] + k2/2)
        k4 = dt * func(t[i-1] + dt, y[i-1] + k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    for i in range(4, len(t)):
        y[i] = y[i-1] + dt/24 * (55 * func(t[i-1], y[i-1]) - 59 * func(t[i-2], y[i-2]) + 37 * func(t[i-3], y[i-3]) - 9 * func(t[i-4], y[i-4]))
    
    return t, y
