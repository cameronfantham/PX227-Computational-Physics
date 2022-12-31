'''Function to simulate collisions'''
import random
import numpy as np
import matplotlib.pyplot as plt

def mixing():
    '''Define function'''
    objects = [*np.full(1000, 0.1, float), *np.full(1000, 1000, float)]
    collisions = 0
    while collisions != 10000:
        #Chose two random objects
        i = random.randint(0, 1999)
        j = random.randint(0, 1999)
        #Simulate collision
        energy_difference = abs(objects[i] - objects[j])/2
        if objects[i] > objects[j]:
            objects[i] -= energy_difference
            objects[j] += energy_difference
        else:
            objects[j] -= energy_difference
            objects[i] += energy_difference
        #Repeat iteration if object is chosen to collide with self
        if i != j:
            collisions += 1
    #Plot histogram
    plt.hist(objects, 100)
    plt.ylabel('Frequency')
    plt.xlabel('Energy')
    plt.savefig('q12u1619962.pdf')
    return np.mean(objects), np.std(objects)
    
