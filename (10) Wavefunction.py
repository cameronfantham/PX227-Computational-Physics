#!/usr/bin/env python 3.5
'''Function to find eigen-energy and wavefunction'''
import numpy as np
import scipy.integrate as spy
import matplotlib.pyplot as plt
def schroedinger():
    V0 = 5
    a = 0.75*10**5
    mc_sqrd = 511*10**3
    hc = 197*10**6
    '''Define transcendental equation'''
    def func(y, x, E, V):
        #phi'(t) = omega(t)
        #omega'(t) = (2*mc_sqrd/(hc**2))*(V - E)*phi(t)
        phi, omega = y
        dydx = [omega, (2*mc_sqrd/(hc**2))*(V - E)*phi]
        return dydx

    E = 50
    v_0 = 100
    #v_0 = initial value of derivative
    wavefunction = []
    steps = 1000
    step_size = 2*a/steps
    x_pnts = np.arange(0, 2*a, step_size)
    x_pnts_1 = np.arange(0.0, a, step_size)
    x_pnts_2 = np.arange(a, 2*a, step_size)
    phi_1 = [[], [1, 1]]
    phi_2 = [[], [1, 1]]
    while abs(phi_2[len(phi_2)-1][0]) > 10:
        phi_1 = spy.odeint(func, [0, v_0], x_pnts_1, args=(E, 0))
        phi_2 = spy.odeint(func, phi_1[len(phi_1)-1], x_pnts_2, args=(E, V0))
        E += 1
    for n in range(500):
        wavefunction.append(phi_1[n][0])
    for n in range(500):
        wavefunction.append(phi_2[n][0])
    while np.trapz(wavefunction) > 10 + 1:
        phi_1 = spy.odeint(func, [0, v_0], x_pnts_1, args=(E, 0))
        phi_2 = spy.odeint(func, phi_1[len(phi_1)-1], x_pnts_2, args=(E, V0))
        v_0 += 1

    #Plotting
    plt.figure(1)
    plt.plot(x_pnts, wavefunction)
    plt.xlabel('X Position')
    plt.ylabel('Wavefunction')
    plt.savefig('q10u1619962a.pdf')
    return E
