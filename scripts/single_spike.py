import numpy as np
import matplotlib.pyplot as plt
from src.model import HodgkinHuxleyModel
from src.visualization import plot_membrane_potential, plot_gate_variables

def create_pulse_stimulus(t, start=60, duration=1, amplitude=10):
    """Create a pulse stimulus current."""
    I = np.zeros_like(t)
    pulse_mask = (t >= start) & (t < start + duration)
    I[pulse_mask] = amplitude
    return I

def main():
    t_span = [0, 100]
    dt = 0.01
    model = HodgkinHuxleyModel()
    
    t = np.arange(t_span[0], t_span[1], dt)
    I_ext = create_pulse_stimulus(t)
    
    # t, V, n, m, h = model.simulate(t_span, dt=0.01, method='adams_bashforth', lambda t: I_ext[int(t/dt)])
    t, V, n, m, h = model.simulate(t_span, I_ext_func=lambda t:I_ext[int(t/dt)])
    
    fig1 = plot_membrane_potential(t, V, "Single Spike Response", I_ext)
    plt.savefig('./data/results/single_spike_probs.png')
    fig2 = plot_gate_variables(t, n, m, h)
    plt.savefig('./data/results/single_spike_potential.png')
    plt.show()

if __name__ == "__main__":
    main()