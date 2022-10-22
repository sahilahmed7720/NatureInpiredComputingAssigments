from algorithms.GA import GA
import math
import numpy as np

from functions.Function import Function

class Rosenbrock(Function):
    def __init__(self, dimension, bounds):
        Function.__init__(self, dimension, bounds)
        print('Rosenbrock Solution............(' + str(dimension) + '-dimensional)')
        self.dimension = dimension
        self.bounds = bounds

    # Evaluate function
    def eval(self, X):
        return np.sum([(100 * ((X[i+1] - (X[i]**2)) ** 2)) + ((1 - X[i]) ** 2) for i in range(self.dimension - 1)])
