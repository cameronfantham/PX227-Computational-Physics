'''Function to solve first order ODE'''
import math
import numpy as np
import matplotlib.pyplot as plt
def temperature(apar, bpar, xmax):
    '''Define funtion'''
    def ode(yyy, xxx):
        '''Define differential equation'''
        return apar*math.exp(-2*xxx) - bpar*(yyy**4-1)
    # Set number of steps
    start = 0.0
    steps = 50000
    step_size = (xmax - start)/ steps
    # initial condition
    y = 0.0
    # Set range of x points
    xpoints = np.arange(start, xmax, step_size)
    # Make list for y points
    ypoints = []
    # Get y points
    for x in xpoints:
        ypoints.append(y)
        k_1 = step_size*ode(y, x)
        k_2 = step_size*ode(y + 0.5*k_1, x + 0.5*step_size)
        k_3 = step_size*ode(y + 0.5*k_2, x + 0.5*step_size)
        k_4 = step_size*ode(y+k_3, x + step_size)
        y += (k_1 + 2*k_2 + 2*k_3 + k_4)/6
    # Find coordinates of Max Temperature value
    max_T = max(ypoints)
    max_T_index = ypoints.index(max_T)
    max_T_time = xpoints[max_T_index]
    # Make plot of Temperature as a function of Time
    plt.plot(xpoints, ypoints)
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.savefig("q8u1619962.pdf")

    return max_T, max_T_time
