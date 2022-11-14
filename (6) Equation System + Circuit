import numpy as np

'''Define function to create a system of equations'''
def equation_system():
    matrix = np.array([[1, 2, 3, 4],
                       [2, 3, 4, 7],
                       [3, 4, 6, 9],
                       [4, 5, 7, 8]], float)
    vector = np.array([1, 8, 3, 5], float)
    for i in range(len(vector)):
        div = matrix[i, i]
        matrix[i, :] /= div
        vector[i] /= div
        for j in range(i + 1, len(vector)):
            factor = matrix[j, i]
            matrix[j, :] -= factor * matrix[i, :]
            vector[j] -= factor * vector[i]
    x = np.zeros(len(vector), float)
    for i in range(len(vector) - 1, -1, -1):
        x[i] = vector[i]
        for j in range(i + 1, len(vector)):
            x[i] -= matrix[i, j] * x[j]
    return x

'''Define a function to find currents and voltage in a circuit'''
def circuit():
    #Using Maxwell Loop method
    matrix = np.array([[1, 0, 9, -1, 0],
                       [0, 6, 0, 1, 0],
                       [0, 0, -1, 1, 0],
                       [0, 0, 0, -2, 3],
                       [-1, 1, -1, 12, -10]], float)
    vector = np.array([0, -12, 0.1, -1, -12], float)
    for i in range(len(vector)):
        div = matrix[i, i]
        matrix[i, :] /= div
        vector[i] /= div
        for j in range(i + 1, len(vector)):
            factor = matrix[j, i]
            matrix[j, :] -= factor * matrix[i, :]
            vector[j] -= factor * vector[i]
    x = np.zeros(len(vector), float)
    for i in range(len(vector) - 1, -1, -1):
        x[i] = vector[i]
        for j in range(i + 1, len(vector)):
            x[i] -= matrix[i, j] * x[j]
    #Voltage
    U = x[0]
    #Currents
    I2 = -x[1] - x[3]
    I3 = x[3] - x[4]
    I4 = I2 + 0.1
    I5 = -x[1]
    I6 = I5 - I4
    I7 = x[4]
    I8 = I9 = I6 + 0.1
    return [U, I2, I3, I4, I5, I6, I7, I8, I9]
