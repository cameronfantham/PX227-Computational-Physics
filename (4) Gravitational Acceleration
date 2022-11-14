import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import sem

''' Define a function to plot the gravitational acceleration of an object
    relative to it's height
'''
def  gravitational_acceleration(filename):
    #Example input: gravitational_acceleration("px277_Aq4.csv")
    #Load and process data
    data = np.loadtxt(filename, delimiter = ",")
    height = data[:, 0]
    time = data[:, 1]
    time_error = data[:, 2]

    #Use the SUVAT equation: s = u * t + 0.5 * a * t ** 2
    #Where u: initial velocity (0 ms^-1), a: g (~10 ms^-2), s: height, t: time
    def height(t, g = 10):
        return 0.5 * g * t ** 2
    gravity, var_g = curve_fit(h, time, height, 10, height(time_error))
    #Plot height against time
    plt.scatter(time, height)
    plt.ylabel("Height (Metres)")
    plt.xlabel("Time (Seconds)")
    #Add the least-squares curve fit to the graph
    x_axis = np.linspace(0, int(np.amax(time)), len(time))
    y_axis = height(x_axis, gravity[0])
    plt.plot(x_axis, y_axis, "r-")
    #Save the figure
    plt.savefig("q4u1619962.pdf")
    #Return the initial gravity and its error
    return [gravity[0], (var_g[0][0]) ** 0.5]
