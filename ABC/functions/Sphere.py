import math
import numpy as np

from functions.Function import Function

class Sphere(Function):
    def __init__(self, dimension, bounds):
        Function.__init__(self, dimension, bounds)
        print('Sphere (' + str(dimension) + '-dimensional)')
        self.dimension = dimension
        self.bounds = bounds

    # Evaluate function
    def eval(self, X):
        return np.sum([x*x for x in X])
