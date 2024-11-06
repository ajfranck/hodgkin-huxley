import numpy as np
import matplotlib.pyplot as plt
from src.model import HodgkinHuxleyModel
from src.visualization import *

def main():
    # Generate voltage range for analysis
    V_range = np.linspace(-100, 50, 1000)
    
    # Create and show steady state plots
    # fig = plot_steady_states(V_range)
    # plt.show()

    # Save figure
    # fig.savefig("./data/results/steady_states.png")

    #run simulation
    model = HodgkinHuxleyModel()
    t, V, n, m, h = model.simulate([0, 100], dt=0.01, method='adams_bashforth', I_ext_func=lambda t: 50)
    #!these are arrays that vary with time. LAST VALUE IS THE MOST RECENT VALUE

    #plot all four values V, n, m, h on seperate plots in the same figure
    fig = plot_membrane_potential(t, V)
    plt.show()
    fig = plot_gate_variables(t, n, m, h)
    plt.show()

    fig.savefig("./data/results/membrane_potential.png")



if __name__ == "__main__":
    main()