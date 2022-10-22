from algorithms.GA import GA
import math
import numpy as np

from functions.Function import Function

class Rastrigin(Function):
    def __init__(self, dimension, bounds):
        Function.__init__(self, dimension, bounds)
        print('Rastrigin Solution............(' + str(dimension) + '-dimensional)')
        self.dimension = dimension
        self.bounds = bounds
    
    # Evaluate function
    def eval(self, X):
        A = 10
        return A * self.dimension + np.sum([((x*x) - (A * math.cos(2 * math.pi * x))) for x in X])
    
