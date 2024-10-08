import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# RC CIRCUIT

# Defining symbols
q, t = sym.symbols('q, t')
c = sym.symbols('c')

# PLOT { Current vs. Time }
def plot_currentvstime(ioft_list, param_list):
    # Defining Time Values (time range from 0 to 5 seconds)
    t_values = np.linspace(0, 5, 1000)
    
    # Create a plot
    plt.figure(figsize=(8, 5))  # Initialize the plot

    # Iterate through each equation in the list
    for idx, ioft in enumerate(ioft_list):
        # Calculate current values for the given time points for each equation
        current_values = [ioft.subs(t, t_val) for t_val in t_values]
        
        # Extract parameters for the current equation to use in the legend
        voltage, resistance, capacitance = param_list[idx]
        
        # Plot each equation and include relevant details in the legend
        plt.plot(t_values, current_values, label=f'V={voltage}V, R={resistance}Ω, C={capacitance}F')
        
        # Highlight points for each equation
        highlighted_indices = np.arange(0, len(t_values), 200)
        plt.scatter(t_values[highlighted_indices], [current_values[i] for i in highlighted_indices], 
                    color=np.random.rand(3,), marker='o', s=100, label=f'Highlighted Points {idx + 1}')
    
    # Add labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.title('Current vs. Time for Multiple RC Circuits')
    plt.legend()  # Add legend to differentiate between the equations
    plt.grid(True)
    plt.show()

def solve_ioft(resistance, capacitance, voltage):
    # Base Equation:
    print("\nR(dq/dt) + 1/C(q) = E(t)")
    print("{}(dq/dt) + 1/{}(q) = {}".format(resistance, capacitance, voltage))
    print("-----------------------------")

    # LINEAR EQUATION
    poft_temp = (1 / capacitance) * (1 / resistance)
    poft = Fraction(poft_temp).limit_denominator()
    eoft = sym.Rational(voltage, resistance)
    print("Linear equation: dq/dt + {}q = {}".format(poft, eoft))
    print("-----------------------------")

    # Integrating Factor:
    u = sym.exp(poft * t)
    print("\nIntegrating Factor: {}".format(u))
    print("-----------------------------")

    # Equation after multiplying by integrating factor
    equation_2 = sym.integrate(eoft * u)
    print("Equation 2: {}q = {} + c".format(u, equation_2))
    print("-----------------------------")

    # Solving for q:
    q_sol = sym.Rational(1, poft) * (equation_2 + c) * sym.exp(-poft * t)
    print("\nq(t) = {}".format(q_sol))
    print("-----------------------------")

    # Initial condition q(0) = 0 (assuming the capacitor starts uncharged)
    initial_q = 0
    c_value = sym.solve(q_sol.subs(t, 0) - initial_q, c)[0]
    print("Solving for c: c = {}".format(c_value))
    print("-----------------------------")

    # Substitute c back into the q(t) equation
    qoft = q_sol.subs(c, c_value)
    print("\nFinal q(t) = {}".format(qoft))
    print("-----------------------------")

    # Deriving q(t) to get i(t):
    ioft = sym.diff(qoft, t)
    print("i(t) = {}\n".format(ioft))

    return ioft


# Initialize arrays to store ioft values and their corresponding parameters
ioft_array = []
param_array = []

# Set a maximum iteration count
max_iterations = 3
iteration = 0

while iteration < max_iterations:
    voltage = float(input("Input Voltage [Volts]: "))
    resistance = float(input("Input Resistance [Ohms]: "))
    capacitance = float(input("Input Capacitance [Farads]: "))
    print("-----------------------------")
    
    # Calculate ioft and store it in the array
    ioft = solve_ioft(resistance, capacitance, voltage)
    ioft_array.append(ioft)
    
    # Store the parameters for the current equation
    param_array.append((voltage, resistance, capacitance))
    
    iteration += 1

# PLOTTING
plot_currentvstime(ioft_array, param_array)
