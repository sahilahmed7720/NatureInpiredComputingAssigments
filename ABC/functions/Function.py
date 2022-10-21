from math import floor
from algorithms.ABC import ABC
import numpy as np


class Function:
    def __init__(self, dimension, bounds):
        print("Optimization Function : ", end="")

        self.dimension = dimension
        self.bounds = bounds

    # Get Fitness
    def getFitness(self, X):
        f = self.eval(X)
        return 1 / (1 + f) if f >= 0 else 1 + abs(f)

    # Evaluate function
    # Optimize using Artificial Bee Colony
    def optimizeUsingABC(self, swarm_size=100, iterations=1000):
        # Parameters
        colony_size = swarm_size
        n_iterations = iterations

        # Initialize the ABC Object
        abc = ABC(self, self.dimension, colony_size, self.bounds)

        # Initialize (Move the scouts)
        abc.initializeFoodSources()
        abc.calculateFitnesses()
        abc.resetTrials()

        # Memorize the best solution
        best_fitness, best_soln = abc.getCurrentBest()

        for _ in range(n_iterations):
            # Employeed Bee Phase
            abc.performEmployedBeePhase()
            # Generate prob of selection of each solution before onlooker bee phase
            prob_selection = abc.generateProbabilities()
            # Onlooker Bee Phase
            abc.performOnlookerBeePhase(prob_selection)
            # Memorize the best soln
            temp_fitness, temp_soln = abc.getCurrentBest()
            if temp_fitness > best_fitness:
                best_fitness = temp_fitness
                best_soln = temp_soln
            # Scout Bee Phase
            abc.performScoutBeePhase()

        opt_val = self.eval(best_soln)
        return best_soln, opt_val
