import math

''' Define function to find energy of a particle, given potential and width.
    The precision to which the value is calulated can also be given.
'''
def energy(V_0, width, precision = 10.0 ** -4):
    #Constants for particle
    mc_sqrd = 511 * 10 ** 3
    hc = 197*10**6
    #Define function to give energy
    def function(E):
        #Return result of transcendental equation
        return (E - V_0) * math.tan(width*(math.sqrt((2*mc_sqrd*E))/hc))**2 + E
    E_1 = V_0
    E_2 = 100.0
    diff = 1.0 #Energy difference
    while diff > precision and 0.5 * (E_2 + E_1) != 0:
        if abs(function(E_2)) > function(E_1) > 0:
            E_2 = 0.5 * (E_2 + E_1)
        elif abs(function(E_1)) > function(E_2) > 0:
            E_1 = 0.5 * (E_2 + E_1)
        diff = abs(E_2 - E_1)
    return 0.5 * (E_2 + E_1) #Average of final two energy iterations
