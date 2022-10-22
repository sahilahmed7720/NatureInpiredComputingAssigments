from math import floor
from algorithms.DE import DE
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

    # Optimize Using Differential Evolution
    def optimizeUsingDE(self, population_size=100, iterations=1000):
        print("Running differential evolution...")

        # Parameters
        prob_recombination = 0.7
        beta = 0.5
        n_diff_vectors = 1
        population_size = max(population_size, 2 * n_diff_vectors + 1)
        sample_size = population_size
        n_generations = iterations
        gamma = 1
        gamma_step = 1 / n_generations

        # DE Object
        de = DE(
            self, self.dimension, sample_size, self.bounds, beta, prob_recombination
        )
        de.initializePopulation()

        for _ in range(n_generations):
            new_population = []
            de.calculateFitnesses()
            for i in range(sample_size):
                # Get parent
                parent = de.population[i]
                # Evaluate fitness of the parent
                fitness_parent = de.fitnesses[i]
                # Generate trial vector by mutating the parent
                trial_vector = de.mutate(i, n_diff_vectors, gamma)
                # Generate a child by crossover
                child = de.binomialCrossover(parent, trial_vector)
                # Evaluate the fitness of the child
                fitness_child = self.getFitness(child)
                # Select the individual with better fitness for next generation
                if fitness_child > fitness_parent:
                    new_population.append(child)
                else:
                    new_population.append(parent)

            de.updatePopulation(new_population)
            # gamma = gamma + gamma_step

        X_res = de.getResult()
        opt_value = self.eval(X_res)
        return X_res, opt_value