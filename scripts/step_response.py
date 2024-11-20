import numpy as np
import matplotlib.pyplot as plt
from src.model import HodgkinHuxleyModel
from src.visualization import plot_membrane_potential

def create_step_stimulus(t, I1, dI, step_time=20):
    """Create a two-phase current stimulus."""
    I = np.ones_like(t) * I1
    step_mask = t >= step_time
    I[step_mask] = I1 + dI
    return I

def analyze_step_cases():
    """Analyze the four cases specified in the project."""
    cases = [
        (4, 2.0),
        (4, 10.0),
        (8, 2.0),
        (8, 10.0),
    ]
    
    t_span = [0, 40]  # 40ms simulation
    dt = 0.01
    model = HodgkinHuxleyModel()
    
    plt.figure(figsize=(15, 10))
    for i, (I1, dI) in enumerate(cases):
        t = np.arange(t_span[0], t_span[1], dt)
        I_ext = create_step_stimulus(t, I1, dI)
        
        t, V, n, m, h = model.simulate(t_span, I_ext_func=lambda t: I_ext[int(t/dt)])
        
        plt.subplot(2, 2, i+1)
        plt.plot(t, V)
        plt.plot(t, I_ext, 'r--', alpha=0.5)
        plt.title(f"I₁ = {I1}μA, δI = {dI}μA")
        plt.xlabel("Time (ms)")
        plt.ylabel("V (mV) / I (μA/cm²)")
        plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('./data/results/step_response.png')
    plt.show()

if __name__ == "__main__":
    analyze_step_cases()