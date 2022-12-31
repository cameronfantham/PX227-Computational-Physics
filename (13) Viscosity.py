'''Program to calculate viscosity of liquid'''

import random
import math
import numpy as np

def  viscosity():
    #Error in: sphere_mass, sphere_radius, liquid_volume, liquid_mass, fall
    error_1 = 0.0005
    #Error in timings
    time_error = 0.05
    g = 9.81
    viscosities = []
    for n in range(10000):
        sphere_mass = 0.021 + random.uniform(-1, 1)*error_1
        sphere_radius = 0.01 + random.uniform(-1, 1)*error_1
        liquid_volume = 0.1 + random.uniform(-1, 1)*error_1
        liquid_mass = 0.14 + random.uniform(-1, 1)*error_1
        fall = 0.1 + random.uniform(-1, 1)*error_1
        time = 3.2 + random.uniform(-1, 1)*time_error
        v = 2*(sphere_mass/((4/3)*math.pi*sphere_radius**3) -
               liquid_mass/liquid_volume)*g*sphere_radius**2*time/(9*fall)
        viscosities.append(v)
    return np.mean(viscosities), np.std(viscosities)
        
