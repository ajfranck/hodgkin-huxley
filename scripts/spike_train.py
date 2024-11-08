import numpy as np
import matplotlib.pyplot as plt
from src.model import HodgkinHuxleyModel
from src.visualization import plot_membrane_potential
"""
Script to analyze spike train dynamics with constant current input.
"""

def analyze_spike_frequency(V, t, threshold=-20):
    """
    Analyze spike frequency in membrane potential data.
    Returns spike times and inter-spike intervals.
    """
    spike_mask = (V[:-1] < threshold) & (V[1:] >= threshold)
    spike_times = t[1:][spike_mask]
    
    if len(spike_times) > 1:
        intervals = np.diff(spike_times)
        return spike_times, intervals
    return spike_times, np.array([])

def main():
    t_span = [0, 100]  # 100ms simulation
    dt = 0.01
    current_values = [0, 2, 5, 10, 15]  # Different current amplitudes
    
    model = HodgkinHuxleyModel()
    
    plt.figure(figsize=(15, 10))
    for i, I_amp in enumerate(current_values):
        t, V, n, m, h = model.simulate(t_span, I_ext_func=lambda t: I_amp)
        
        spike_times, intervals = analyze_spike_frequency(V, t)
        
        plt.subplot(len(current_values), 1, i+1)
        plt.plot(t, V)
        plt.title(f"I = {I_amp} μA/cm²")
        if intervals.size > 0:
            freq = 1000/np.mean(intervals)
            plt.title(f"I = {I_amp} μA/cm² (freq: {freq:.1f} Hz)")
        plt.grid(True)
        
        if i == len(current_values)-1:
            plt.xlabel("Time (ms)")
        plt.ylabel("V (mV)")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()