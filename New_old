import numpy as np


class ABC:
    def __init__(self, objective_function, dimension, colony_size, bounds):
        self.objective_function = objective_function
        self.dimension = dimension
        self.bounds = bounds
        self.colony_size = colony_size
        self.n_employed_bees = int(self.colony_size / 2)
        self.n_onlooker_bees = self.n_employed_bees
        self.n_food_sources = self.n_employed_bees
        self.limit_scout = self.n_employed_bees * self.dimension
        self.foodSources = []
        self.fitnesses = []
        self.trials = []

    # Initialize Population Randomly
    def initializeFoodSources(self):
        self.foodSources = [
            np.random.uniform(self.bounds[0], self.bounds[1], self.dimension)
            for _ in range(self.n_food_sources)
        ]

    # Calculate fitness for every individual of the population
    def calculateFitnesses(self):
        self.fitnesses = [
            self.objective_function.getFitness(food) for food in self.foodSources
        ]

    # Perform the employed bee phase
    def performEmployedBeePhase(self):
        for i in range(self.n_employed_bees):
            # Generate new solution
            new_soln = self.generateNewSolution(i)

            # Evaluate the fitness of the new solution
            new_fitness = self.objective_function.getFitness(new_soln)

            # Greedy selection
            if new_fitness > self.fitnesses[i]:
                self.foodSources[i] = new_soln
                self.fitnesses[i] = new_fitness
                self.trials[i] = 0
            else:
                self.trials[i] = self.trials[i] + 1

    # Onlooker Bee Phase
    def performOnlookerBeePhase(self, prob_selection):
        i = 0
        j = 0

        # Allocate food sources to each onlooker bee
        while i < self.n_onlooker_bees:
            rnd = np.random.uniform(0, 1)
            if rnd <= prob_selection[j]:
                # Generate a new solution
                new_soln = self.generateNewSolution(j)

                # Evaluate the fitness of the new solution
                new_fitness = self.objective_function.getFitness(new_soln)

                # Greedy selection
                if new_fitness > self.fitnesses[j]:
                    self.foodSources[j] = new_soln
                    self.fitnesses[j] = new_fitness
                    self.trials[j] = 0
                else:
                    self.trials[j] = self.trials[j] + 1

                i = i + 1

            j = (j + 1) % self.n_food_sources

    # Scout Bee Phase
    def performScoutBeePhase(self):
        # Get the index of soln with max number of trials
        k = np.argmax(self.trials)

        # Do nothing if the trial value <= limit
        if self.trials[k] <= self.limit_scout:
            return

        # Replace the kth solution with a random solution
        self.foodSources[k] = np.random.uniform(
            self.bounds[0], self.bounds[1], self.dimension
        )

        # Evaluate the new fitness
        self.fitnesses[k] = self.objective_function.getFitness(self.foodSources[k])

    # Generate Probability of selection for each food source before onlooker bee phase
    def generateProbabilities(self):
        total_fitness = np.sum(self.fitnesses)
        return [fit / total_fitness for fit in self.fitnesses]

    # Random integer in a range excluding an integer
    def generateRandomInteger(self, low, high, dont_include):
        rnd = np.random.randint(low, high)
        return (
            self.generateRandomInteger(low, high, dont_include)
            if rnd == dont_include
            else rnd
        )

    # Reset all trials to 0
    def resetTrials(self):
        self.trials = [0 for _ in range(self.n_employed_bees)]

    # Generate a new solution
    def generateNewSolution(self, i):
        # Current Solution
        current = self.foodSources[i]

        # Partner Solution
        partner = self.foodSources[
            self.generateRandomInteger(0, self.n_employed_bees, dont_include=i)
        ]

        # New solution
        new_soln = np.copy(current)

        # Random index is chosen to modify
        j = np.random.randint(0, self.dimension)
        new_soln[j] = current[j] + np.random.uniform(-1, 1) * (current[j] - partner[j])

        # Bound the new solution
        if new_soln[j] < self.bounds[0]:
            new_soln[j] = self.bounds[0]
        elif new_soln[j] > self.bounds[1]:
            new_soln[j] = self.bounds[1]

        return new_soln

    # Get the index of soln with best fitness
    def getCurrentBest(self):
        ind = np.argmax(self.fitnesses)
        return self.fitnesses[ind], self.foodSources[ind]
