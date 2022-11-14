import numpy as np
import matplotlib.pyplot as plt

''' Define a function to plot the path of a particle using
    pyplot, given a tabulated data input file. Also returns
    total distance travelled
'''
def walk(filename): #Example input: walk("px277_Aq2.csv")
    #Load and process data
    data = np.loadtxt(filename, delimiter = ",")
    x = data[:, 0] #First column is x
    y = data[:, 1] #Second column is y
    L = data[:, 2] #Third column is elevation or L
    #Calculate cumulative and total distance travelled
    s = [0.0]
    total = 0
    for n in np.arange(0, len(data) - 1):
        #Displacement interval ds
        ds = ((((x[n + 1]) - (x[n]))) ** 2 + ((y[n + 1]) - (y[n])) ** 2) ** 0.5
        s.append(ds + total)
        total += ds
    #Plot path in x-y plane
    plt.plot(x, y)
    plt.ylabel('Y position (Metres)')
    plt.xlabel('X position (Metres)')
    plt.ylim(np.amin(y), np.amax(y))
    plt.xlim(np.amin(x), np.amax(x))
    plt.savefig('xy_plane_path.pdf')
    #Plot elevation relative to distance travelled
    plt.plot(s, L)
    plt.ylabel('Elevation (Metres)')
    plt.xlabel('Distance travelled (Metres)')
    plt.ylim(np.amin(L), np.amax(L))
    plt.xlim(np.amin(s), np.amax(s))
    plt.savefig('q2u1619962.pdf')
    #Return total distance travelled in x-y plane
    return total
