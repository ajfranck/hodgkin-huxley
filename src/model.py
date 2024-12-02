import numpy as np
from .gates import (alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h, n_infinity, m_infinity, h_infinity)
from .numerical import *

"""
Core implementation of the Hodgkin-Huxley model.
Contains the main differential equations and parameters.
"""

class HodgkinHuxleyModel:
    def __init__(self):
        self.C_m = 1.0  # Membrane capacitance (muF/cm^2)
        self.g_Na = 120.0  # Sodium conductance (mS/cm^2)
        self.g_K = 36.0  # Potassium conductance (mS/cm^2)
        self.g_L = 0.3  # Leak conductance (mS/cm^2)
        self.E_Na = 55.0  # Sodium reversal potential (mV)
        self.E_K = -77.0  # Potassium reversal potential (mV)
        self.E_L = -54.4  # Leak reversal potential (mV)
        
        # Initial conditions
        self.reset_state()
    
    def reset_state(self):
        """Reset state variables to resting conditions."""
        self.V = -65.0  # Initial membrane potential (mV)
        self.n = n_infinity(self.V)  # Initial potassium activation
        self.m = m_infinity(self.V)  # Initial sodium activation
        self.h = h_infinity(self.V)  # Initial sodium inactivation
        
    def dV_dt(self, V, n, m, h, I_ext=0):
        """Calculate membrane potential derivative."""
        I_Na = self.g_Na * m**3 * h * (V - self.E_Na)
        I_K = self.g_K * n**4 * (V - self.E_K)
        I_L = self.g_L * (V - self.E_L)
        return (I_ext - I_Na - I_K - I_L) / self.C_m
    
    def dn_dt(self, V, n):
        """Calculate potassium activation derivative."""
        return alpha_n(V) * (1 - n) - beta_n(V) * n
    
    def dm_dt(self, V, m):
        """Calculate sodium activation derivative."""
        return alpha_m(V) * (1 - m) - beta_m(V) * m
    
    def dh_dt(self, V, h):
        """Calculate sodium inactivation derivative."""
        return alpha_h(V) * (1 - h) - beta_h(V) * h
    
    def derivatives(self, t, state, I_ext=0):
        """Calculate all derivatives for the current state."""
        V, n, m, h = state
        dV = self.dV_dt(V, n, m, h, I_ext)
        dn = self.dn_dt(V, n)
        dm = self.dm_dt(V, m)
        dh = self.dh_dt(V, h)
        return np.array([dV, dn, dm, dh])
    
    
    def simulate(self, t_span, dt=0.01, method='euler_c', I_ext_func=lambda t: 0):
        """
        Run simulation for given time span and external current function.
        
        Args:
            t_span: [t_start, t_end] in milliseconds
            dt: Time step in milliseconds
            method: Integration method ('euler_c', 'rk', or 'adams_bashforth')
            I_ext_func: Function of time that returns external current
        """
        y0 = np.array([self.V, self.n, self.m, self.h])
        
        if method == 'euler_c':
            integrator = euler_cromer
        elif method == 'rk':
            integrator = runge_kutta
        elif method == 'adams_bashforth':
            integrator = adams_bashforth
        else:
            raise ValueError("Method not recognized. Use 'euler_c', 'rk', or 'adams_bashforth'")
        
        def func(t, y):
            return self.derivatives(t, y, I_ext_func(t))
        
        t, y = integrator(func, y0, t_span, dt)
        
        V, n, m, h = y[:, 0], y[:, 1], y[:, 2], y[:, 3]
        
        self.V, self.n, self.m, self.h = V[-1], n[-1], m[-1], h[-1]
        return t, V, n, m, h
