import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# RC CIRCUIT

# Defining symbols
q, t = sym.symbols('q, t')
c = sym.symbols('c')

# PLOT { Current vs. Time }
def plot_currentvstime(ioft):
    #Defining Time Values
    t_values = np.linspace(0, 5, 1000)
    #print(t_values)
    
    # Calculate current values for the given time points
    current_values = [ioft.subs(t, t_val) for t_val in t_values]
    
    # Plot Creation
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, current_values, label='Current vs. Time')
    highlighted_indices = np.arange(0, len(t_values), 200)
    plt.scatter(t_values[highlighted_indices], [current_values[i] for i in highlighted_indices], color='red', marker='o', label='Highlighted Points', s=100)
    plt.xlabel('Time')
    plt.ylabel('Current')
    plt.title('Current vs. Time Plot')
    plt.grid(True)
    plt.show()


# For User Input
# NOTE: Voltage is changeable
voltage = float(input("Input Voltage[Volts]: "))
resistance = float(input("Input Resistance[Ohms]: "))
capacitance = float(input("Input Capacitance[Farads]: "))
print("-----------------------------")

# Display Base Equation:
print("\nR(dq/dt) + 1/C(q) = E(t)")
print("{}(dq/dt) + 1/{}(q) = {}".format(resistance, capacitance, voltage))
print("-----------------------------")

# LINEAR EQUATION
print("[{}(dq/dt) + 1/{}(q) = {}]1/{}".format(resistance, capacitance, voltage, resistance))
poft_temp = (1 / capacitance) * (1 / resistance)
poft = Fraction(poft_temp).limit_denominator()
eoft = sym.Rational(voltage, resistance)
print("Linear equation: dq/dt + {}q = {}".format(poft, eoft))
print("-----------------------------")

# Integrating Factor:
u = sym.exp(poft*t)
print("\nIntegrating Factor: {}".format(u))
print("-----------------------------")

# Equation 2:
print("\n∫d/dt({}q) = ∫{}{}".format(u, eoft, u))
equation_2 = sym.integrate(eoft*u)
print("Equation 2: {}q = {}".format(u, (equation_2)+c))
temp = equation_2.subs(t, 0)
print("-----------------------------")

#Solving for q:
print("\n[{}q = {}] 1/{}".format(u, (equation_2)+c, u))
u2 = sym.exp(-poft*t)
q = equation_2.subs(t, 0) + (c * u2)
print("q = {}".format(q))
print("-----------------------------")

#Solving for c:
#Where t = 0
print("\nLet, t = 0")
print("q(t) = {}".format(q))
c_temp = q.subs(t, 0)
value_c = -(c_temp.subs(c, 0))
print("c = {}".format(value_c))
print("-----------------------------")

#Plugging in c to get qoft:
qoft = q.subs(c, value_c)
print("\nq(t) = {}".format(qoft))
print("-----------------------------")

#Deriving q(t) to get i(t):
print("\ni(t) = d/dt[{}]".format(qoft))
ioft = sym.diff(qoft)
print("i(t) = {}\n".format(ioft))


# PLOTTING
plot_currentvstime(ioft)
