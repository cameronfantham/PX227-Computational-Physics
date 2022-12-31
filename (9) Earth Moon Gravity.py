'''Function to track the motion of a light object (in x-y plane)
   in the gravitational fields of the Earth and Moon'''

import numpy as np
import scipy.integrate as spy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def satellite():
    '''Define function'''
    def ode(z, t):
        '''Define system of 2nd order odes'''
        #mass ratio (mu)
        mu = 0.012277471
        x = z[0]
        y = z[1]
        u = z[2]
        v = z[3]
        #u = dx/dt
        #v = dy/dt
        r = ((x + mu)**2 + y**2)**0.5
        s = ((x - 1 + mu)**2 + y**2)**0.5
        eq_1 = x + 2*v - (1 - mu)*(x + mu)/(r**3)-mu*(x - 1 + mu)/(s**3)
        eq_2 = y - 2*u - (1 - mu)*y/(r**3) - mu*y/(s**3)
        #eq_1 = du/dt = d^2x/dt^2
        #eq_2 = dv/dt = d^2y/dt^2
        #position'(t) = velocity(t) = [u, v]
        #velocity'(t) = [eq_1, eq_2]
        return [u, v, eq_1, eq_2]

    # Set number of steps
    steps = 10000
    # Set range of t points
    t_points = np.linspace(0.0, 18.0, steps)
    #Solve ode
    solution = spy.odeint(ode, [0.994, 0.0, 0.0, -2.0015851], t_points)
    # Make lists for points
    x_position = []
    y_position = []
    x_velocity = []
    y_velocity = []
    for n in range(steps):
        x_position.append(solution[n][0])
        y_position.append(solution[n][1])
        x_velocity.append(solution[n][2])
        y_velocity.append(solution[n][3])
    # Plot graphs
    plt.figure(1)
    plt.plot(x_position, y_position)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.savefig('q9u1619962a.pdf')
    plt.figure(2)
    plt.plot(t_points, y_position)
    plt.plot(t_points, x_position)
    plt.xlabel('Time')
    plt.ylabel('Position')
    y_points = mpatches.Patch(color='blue', label='Y position')
    x_points = mpatches.Patch(color='green', label='X position')
    plt.legend(handles=[y_points, x_points])
    plt.savefig('q9u1619962b.pdf')
    plt.figure(3)
    plt.plot(x_velocity, y_velocity)
    plt.xlabel('X Velocity')
    plt.ylabel('Y Velocity')
    plt.savefig('q9u1619962c.pdf')
