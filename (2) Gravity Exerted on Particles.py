import numpy as np
''' Define function to calculate the force vectors exerted on
    particles by an object, given their positions and their masses.
'''
def force(filename, object): #Example input: force("px277_Aq3.csv", [1,1,1,1])
    #Load and process data
    data = np.loadtxt(filename, delimiter = ",")
    x = data[:, 0] #First column x position
    y = data[:, 1] #Second column y position
    z = data[:, 2] #Third column z position
    m = data[:, 3] #Fourth column mass
    G = 6.67408 * (10**-11) #Gravitational constant
    force_x, force_y, force_z = 0, 0, 0 #x, y, z force components
    #Calculate and sum all force vectors
    for n in np.arange(0, len(data)):
        dx, dy, dz = object[0] - x[n], object[1] - y[n], object[2] - z[n]
        r = ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5 #Distance between them
        df = (G* object[3] * m[n]) / (r ** 3)
        force_x += df * dx
        force_y += df * dy
        force_z += df * dz
        total_force = ((force_x ** 2) + (force_y ** 2) + (force_z ** 2)) ** 0.5
    return [force_x, force_y, force_z, total_force]
