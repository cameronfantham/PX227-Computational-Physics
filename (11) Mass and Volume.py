'''Function to find mass and volume'''
import math
import random
import numpy as np
def calculate_mass():
    def function(xx, yy):
        '''Define z as a function of x and y'''
        return math.acos((xx**2 + yy**2)**0.5)
    def integrand(zz):
        '''Define function of z to integrate
        by first integrating with respect to x or y'''
        #Integrated x = (cos(z)**2 + y**2)**0.5 between y = 0 and y = cos(z)
        return 0.25*math.pi*math.cos(zz)*abs(math.cos(zz))
    def density(xx, yy, zz):
        '''Define density as function of x, y and z'''
        return 10*abs(math.sin(zz))*math.exp(-0.2*abs(xx))*(1 - yy**2)

    n_sample = 100000
    n_accepted = 0
    #Calculate volume
    maximum = math.pi/2
    z_start = -math.pi/2
    z_end = math.pi/2
    z_length = z_end - z_start
    for n in range(n_sample):
        a = random.random()*z_length + z_start
        b = random.random()*maximum
        if b < integrand(a):
            n_accepted += 1
    #Multiply by 4 as limits only give quarter volume of shape
    volume = 4*maximum*z_length*n_accepted/n_sample
    #Calculate Mass
    densities = []
    for n in range(n_sample):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)*(math.cos(0)**2 - x**2)**0.5
        z = random.uniform(-1, 1)*function(x, y)
        densities.append(density(x, y, z))
    return volume, np.mean(densities)*volume
