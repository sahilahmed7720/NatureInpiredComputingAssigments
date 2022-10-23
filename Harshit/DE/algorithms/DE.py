# Real/Float Valued Encoding
# Mutation
# Binomial/Exponential Crossover

# DE best/1/bin

import numpy as np

class DE:
    def __init__(self, objective_function, dimension, sample_size, bounds, beta, prob_recombination):
        self.objective_function = objective_function
        self.beta = beta
        self.prob_recombination = prob_recombination
        self.dimension = dimension
        self.sample_size = sample_size
        self.bounds = bounds
        self.population = []
        self.fitnesses = []
    
    # Initialize Population Randomly
    def initializePopulation(self):
        self.population = []
        for _ in range(self.sample_size):
            X = np.random.uniform(self.bounds[0], self.bounds[1], self.dimension)
            self.population.append(X)
    
    # Calculate fitness for every individual of the population
    def calculateFitnesses(self):
        self.fitnesses = []
        for p in self.population:
            self.fitnesses.append(self.objective_function.getFitness(p))
    
    # Mutate the population
    def mutate(self, index, n_diff_vectors, gamma):
        # Add parent index to set
        set_of_indices = set()
        set_of_indices.add(index)

        # Get best vector
        best_index = np.argmax(self.fitnesses)
        best = self.population[best_index]

        # Get a target vector
        target_index = self.randomIntWithExclude(set_of_indices)
        target = self.population[target_index]
        set_of_indices.add(target_index)

        # Sum of difference vectors
        diff_vector = [0 for d in range(self.dimension)]
        for i in range(n_diff_vectors):
            diff_x1_index = self.randomIntWithExclude(set_of_indices)
            diff_x1 = self.population[diff_x1_index]
            set_of_indices.add(diff_x1_index)

            diff_x2_index = self.randomIntWithExclude(set_of_indices)
            diff_x2 = self.population[diff_x2_index]
            set_of_indices.add(diff_x2_index)

            diff_vector = diff_vector + (diff_x2 - diff_x1)

        # Generate trial Vector
        trial = (gamma * best) + ((1 - gamma) * target) + (self.beta * diff_vector)

        # Get values under bounds
        for d in range(self.dimension):
            if(trial[d] > self.bounds[1]):
                trial[d] = self.bounds[1]
            elif(trial[d] < self.bounds[0]):
                trial[d] = self.bounds[0]

        return trial
    
    # Binomial Crossover
    def binomialCrossover(self, parent, trial):
        j = np.random.randint(0, self.dimension - 1)

        child = parent
        for d in range(self.dimension):
            rnd = np.random.uniform(0,1)
            if(d == j or rnd <= self.prob_recombination):
                child[d] = trial[d]

        return child

    # Exponential Crossover
    def exponentialCrossover(self, parent, trial):
        count = 0
        j = np.random.randint(0, self.dimension - 1)

        child = parent
        while(np.random.uniform(0,1) <= self.prob_recombination and count < self.dimension):
            child[j] = trial[j]
            j = (j + 1) % self.dimension
            count += 1;

        return child
    
    # Update the population
    def updatePopulation(self, new_population):
        self.population = new_population
    
    # Get the best individual
    def getResult(self):
        fitnesses = [self.objective_function.getFitness(X) for X in self.population]
        return self.population[np.argmax(fitnesses)]

    # Generate random integer while excluding a set of integers
    def randomIntWithExclude(self, st):
        n = np.random.randint(0, self.sample_size)
        return self.randomIntWithExclude(st) if n in st else n
    