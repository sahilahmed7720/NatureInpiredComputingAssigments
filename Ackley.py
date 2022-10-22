from algorithms.GA import GA
import math
import numpy as np

from functions.Function import Function

class Ackley(Function):
    def __init__(self, dimension, bounds):
        Function.__init__(self, dimension, bounds)
        print('Ackley Solution............(' + str(dimension) + '-dimensional)')
        self.dimension = dimension
        self.bounds = bounds

    # Evaluate function
    def eval(self, X):
        t1 = -20 * (math.exp(-0.2 * (math.sqrt(0.5 * (np.sum([x*x for x in X]))))))
        t2 = -(math.exp(0.5 * (np.sum([math.cos(2 * math.pi * x) for x in X]))))
        res = t1 + t2 + math.e + 20
        return res
