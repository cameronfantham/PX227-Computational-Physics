import numpy as np
import scipy.integrate as integrate

'''Define a function to calculate the x-position
   and velocity of a particle, at a given time.
'''
def motion(time):
    #Define velocity function
    def velocity(time):
        if 0 <= time < 10:
            v1 = integrate.quad(lambda t: 2.5/(1+np.exp((t-8)/0.8)), 0, time)
            v2 = [0,0]
            v3 = [0,0]
        elif 10 <= time <= 40:
            v1 = integrate.quad(lambda t: 2.5/(1 + np.exp((t-8)/0.8)), 0, 10)
            v2 = integrate.quad(lambda t: 0, 10, time)
            v3 = [0,0]
        elif time > 40:
            v1 = integrate.quad(lambda t: 2.5/(1 + np.exp((t-8)/0.8)), 0, 10)
            v2 = integrate.quad(lambda t: 0, 10, 40)
            v3 = integrate.quad(lambda t: -2.5*(1 - 1/(1 + np.exp((t-47)/1.2))), 40, time)
        else:
            print("Cannot accept negative time values as input.")
        v = v1[0]+v2[0]+v3[0]
        error_of_v= v1[1]+v2[1]+v3[1]
        return [v, error_of_v]
    #Define x-position function
    def x_position(time):
            x = integrate.quad(lambda t: velocity(t)[0], 0, time)
            position = x[0]
            error_of_position = x[1]
            return [position, error_of_position]
    return x_position(u), velocity(u)
