'''Function to find mass of elliptical sheet
   and force exerted on point particle by sheet'''

import math
import numpy as np
import scipy.integrate as sp

def force(position):
    a = 10
    b = 5
    density = 1000
    m_2 = 10
    #Calculate sheet mass
    A = math.pi*a*b
    m_1 = density*A
    #Calculate vector components
    G = 6.67408*10**-11
    F_x = -G*density*m_2*sp.dblquad(lambda r, t: a*b*r*(position[0] -
                                                        a*r*np.cos(t))/
                                    (((position[0] - a*r*np.cos(t))**2 +
                                      (position[1] - b*r*np.sin(t))**2 +
                                      (position[2])**2)**(1.5)), 0, 2*math.pi,
                                    lambda r: 0, lambda r: 1)[0]
    F_y = -G*density*m_2*sp.dblquad(lambda r, t: a*b*r*(position[1] -
                                                        b*r*np.sin(t))/
                                    (((position[0] - a*r*np.cos(t))**2 +
                                      (position[1] - b*r*np.sin(t))**2 +
                                      (position[2])**2)**(1.5)), 0, 2*math.pi,
                                    lambda r: 0, lambda r: 1)[0]
    F_z = -G*density*m_2*sp.dblquad(lambda r, t: a*b*r*position[2]/
                                    (((position[0] - a*r*np.cos(t))**2 +
                                      (position[1] - b*r*np.sin(t))**2 +
                                      (position[2])**2)**(1.5)), 0, 2*math.pi,
                                    lambda r: 0, lambda r: 1)[0]

    return [m_1, F_x, F_y, F_z]
