"""
Plotting functions for visualizing simulation results.
"""
"""
Plotting functions for visualizing simulation results.
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_membrane_potential(t, V, title="Membrane Potential", I_ext=None):
    """Plot membrane potential over time with optional current stimulus."""
    if I_ext is not None:
        fig, (ax1, ax2) = plt.subplots(
            2, 1,
            figsize=(10, 8),
            sharex=True
        )
    else:
        fig, ax1 = plt.subplots(
            1, 1,
            figsize=(10, 6),
            sharex=True
        )
    
    ax1.plot(t, V)
    ax1.set_title(title)
    ax1.set_ylabel("Membrane Potential (mV)")
    ax1.grid(True)
    
    if I_ext is not None:
        ax2.plot(t, I_ext)
        ax2.set_xlabel("Time (ms)")
        ax2.set_ylabel("External Current (μA/cm²)")
        ax2.grid(True)
    else:
        ax1.set_xlabel("Time (ms)")
    
    plt.tight_layout()
    return fig

def plot_gate_variables(t, n, m, h):
    """Plot gate variables over time."""
    #use subplot to plot multiple plots in the same figure
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    axs[0].plot(t, n, label='n (K⁺ activation)')
    axs[0].set_ylabel("Probability")
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(t, m, label='m (Na⁺ activation)')
    axs[1].set_ylabel("Probability")
    axs[1].grid(True)
    axs[1].legend()

    axs[2].plot(t, h, label='h (Na⁺ inactivation)')
    axs[2].set_xlabel("Time (ms)")
    axs[2].set_ylabel("Probability")
    axs[2].grid(True)
    axs[2].legend()

    return plt.gcf()

def plot_steady_states(V_range):
    """Plot steady state values and time constants."""
    from .gates import (n_infinity, m_infinity, h_infinity,
                       tau_n, tau_m, tau_h)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    ax1.plot(V_range, n_infinity(V_range), label='n∞')
    ax1.plot(V_range, m_infinity(V_range), label='m∞')
    ax1.plot(V_range, h_infinity(V_range), label='h∞')
    ax1.set_title("Steady State Values")
    ax1.set_xlabel("Membrane Potential (mV)")
    ax1.set_ylabel("Steady State Value")
    ax1.grid(True)
    ax1.legend()
    
    ax2.plot(V_range, tau_n(V_range), label='τn')
    ax2.plot(V_range, tau_m(V_range), label='τm')
    ax2.plot(V_range, tau_h(V_range), label='τh')
    ax2.set_title("Time Constants")
    ax2.set_xlabel("Membrane Potential (mV)")
    ax2.set_ylabel("Time Constant (ms)")
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

def plot_phase_plane(V, n, m, h):
    """Plot phase plane trajectories."""
    fig = plt.figure(figsize=(15, 5))
    
    ax1 = fig.add_subplot(131)
    ax1.plot(V, n)
    ax1.set_xlabel("V (mV)")
    ax1.set_ylabel("n")
    ax1.set_title("V-n Phase Plane")
    ax1.grid(True)
    
    ax2 = fig.add_subplot(132)
    ax2.plot(V, m)
    ax2.set_xlabel("V (mV)")
    ax2.set_ylabel("m")
    ax2.set_title("V-m Phase Plane")
    ax2.grid(True)
    
    ax3 = fig.add_subplot(133)
    ax3.plot(V, h)
    ax3.set_xlabel("V (mV)")
    ax3.set_ylabel("h")
    ax3.set_title("V-h Phase Plane")
    ax3.grid(True)
    
    plt.tight_layout()
    return fig