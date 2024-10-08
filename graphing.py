import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

# PLOT { Current vs. Time }
def plot_currentvstime(ioft):
    #Defining Symbol t
    t = sym.Symbol('t')
    #Defining Time Values
    t_values = np.linspace(0, 5, 1000)
    
    # Calculate current values for the given time points
    current_values = [ioft.subs(t, t_val) for t_val in t_values]
    
    # Plot Creation
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, current_values, label='Current vs. Time')
    highlighted_indices = np.arange(50, len(t_values), 100)
    plt.scatter(t_values[highlighted_indices], [current_values[i] for i in highlighted_indices], color='red', marker='o', label='Highlighted Points', s=100)
    plt.xlabel('Time')
    plt.ylabel('Current')
    plt.title('Current vs. Time Plot')
    plt.grid(True)
    plt.show()