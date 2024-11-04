# Hodgkin-Huxley Model Simulation

## Overview
In this repo, we investigate the dynamics of nerve impulses using simulations of the Hodgkin-Huxley model. This model describes how action potentials are initiated and then propagated in neurons by the opening and closing of ion channels. The model is a system of four coupled differential equations that describe the time evolution of the membrane potential and the probabilities of the ion channels being open. In this project, we plan to explore both steady-state behavior and dynamic responses to various stimuli.

## Objectives
 * Implement the Hodgkin-Huxley differential equations in Python using numerical integration techniques.
 * Study the steady-state behavior of ion channel gates
 * Analyse the membrane's response to different current stimuli
 * Investigate threshold phenomena and spike train dynamics

## Technical Approach
We utilize Python's scientific computing libraries (NumPy, SciPy, Matplotlib), to implement:
 * Steady-state analysis of gate variables (n, m, h) as functions of membrane potential
 * Visualization tools for steady-state and time-dependent behavior
 * Parameter sweep to investigate the effects of varying parameters on the system

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Example usage of the model:
```python
from src.model import HodgkinHuxleyModel

model = HodgkinHuxleyModel()

The model can then be utilized however you prefer--but there are included tests in the repository as well.


## Project Structure
- `src/`: Core model implementation
- `scripts/`: Analysis scripts
- `tests/`: Unit tests
- `notebooks/`: Jupyter notebooks for analysis
