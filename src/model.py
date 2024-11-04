import numpy as np
from .gates import alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h
from .numerical import euler_cromer

"""
Core Hodgkin-Huxley model.
Contains main differential equations and their parameters.
"""

class HodgkinHuxleyModel:
    def __init__(self):
        self.C_m = 1.0  # Membrane capacitance (μF/cm²)
        self.g_Na = 120.0  # Sodium conductance (mS/cm²)
        self.g_K = 36.0  # Potassium conductance (mS/cm²)
        self.g_L = 0.3  # Leak conductance (mS/cm²)
        self.E_Na = 55.0  # Sodium reversal potential (mV)
        self.E_K = -77.0  # Potassium reversal potential (mV)
        self.E_L = -54.4  # Leak reversal potential (mV)
        
        # Initial conditions
        self.V = -65.0  # Initial membrane potential (mV)
        self.n = 0.0  # Initial potassium activation
        self.m = 0.0  # Initial sodium activation
        self.h = 0.0  # Initial sodium inactivation

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
    
    def simulate(self, t_span, I_ext):
        dt = t_span[1] - t_span[0]
        n_points = len(t_span)
        V = np.zeros(n_points)
        n = np.zeros(n_points)
        m = np.zeros(n_points)
        h = np.zeros(n_points)

        V[0] = self.V
        n[0] = self.n
        m[0] = self.m
        h[0] = self.h

        for i in range(1, n_points):
            V[i] = euler_cromer(self.dV_dt, V[i-1], n[i-1], m[i-1], h[i-1], I_ext, dt)
            n[i] = euler_cromer(self.dn_dt, V[i-1], n[i-1], dt)
            m[i] = euler_cromer(self.dm_dt, V[i-1], m[i-1], dt)
            h[i] = euler_cromer(self.dh_dt, V[i-1], h[i-1], dt)

        return V, n, m, h





