# Binary Encoded GA
# Single Point Crossover
# Bit Flip Mutation
# Roulette Wheel Selection
import math
import numpy as np

class GA:
    def __init__(self, objective_function, dimension, sample_size, bounds, soln_len, var_len, prob_crossover, prob_mutation):
        self.objective_function = objective_function
        self.sample_size = sample_size
        self.dimension = dimension
        self.population = []
        self.bounds = bounds
        self.soln_len = soln_len
        self.var_len = var_len
        self.fitnesses = [0 for _ in range(sample_size)]
        self.prob_selection = []
        self.prob_crossover = prob_crossover
        self.prob_mutation = prob_mutation

    # Initialize population randomly
    def initializePopulation(self):
        self.population = []
        for _ in range(self.sample_size):
            x = np.random.random_integers(0, (2 ** self.var_len) - 1, self.dimension)
            self.population.append(self.encode(x))
    
    # Calculate Fitness for all population
    def calculateFitnesses(self):
        fitnesses = []
        for soln in self.population:
            X = self.getVariables(soln) #   x1, x2, ... xn
            fit = self.objective_function.getFitness(X)
            fitnesses.append(fit);
        self.fitnesses = fitnesses
    
    # Calcualte Probabilities for each soln depending on fitness
    def calculateProbabilitiesRoulette(self):
        self.prob_selection = []
        total_fitness = np.sum(self.fitnesses)
        for i in range(self.sample_size):
            self.prob_selection.append(self.fitnesses[i] / total_fitness)

    # Select from population
    def rouletteWheelSelection(self):
        mating_pool = {}
        for i in range(self.sample_size):
            p1 = self.population[i]
            p2 = self.population[np.random.choice(self.sample_size, p=self.prob_selection)]
            mating_pool[p1] = p2
        return mating_pool

    # Crossover
    def crossover(self, mating_pool):
        children = []
        for key in mating_pool:
            rnd = np.random.uniform(0,1)
            p1 = key
            p2 = mating_pool[key]
            if rnd > self.prob_crossover:
                children.append(p1)
                children.append(p2)
            else:
                crossover_site = np.random.randint(1, self.soln_len - 1)
                temp1 = p1[crossover_site:]
                temp2 = p2[crossover_site:]
                c1 = p1[:crossover_site] + temp2
                c2 = p2[:crossover_site] + temp1
                children.append(c1)
                children.append(c2)
        return children

    # Mutation
    def mutate(self, children):
        offsprings = []
        for child in children:
            t = ''
            for i in range(self.soln_len):
                rnd = np.random.uniform(0,1)
                if(rnd > self.prob_mutation):
                    t += child[i]
                else:
                    t += '0' if child[i] == '1' else '0'
            offsprings.append(t)
        return offsprings
    
    # Select survivor using Elitism
    def selectEliteSurvivor(self, mutated_children):
        k = math.ceil(len(mutated_children) * 0.05)
        fitnesses = [self.objective_function.getFitness(self.getVariables(child)) for child in mutated_children]
        best_k_indices = np.argpartition(fitnesses, k)[-k:]
        # print(len(best_k_indices))
        survivors = []
        for i in best_k_indices:
            survivors.append(mutated_children[i])
        random_survivors_indices = np.random.randint(0, len(mutated_children)-1, self.sample_size - k);
        # print(len(random_survivors_indices))
        for i in random_survivors_indices:
            survivors.append(mutated_children[i])
        return survivors

    # Get all dimensional variables from the solution string
    def getVariables(self, soln):
        X = []
        for i in range(0, self.soln_len, self.var_len):
            X.append(self.decodeString(soln[i:i+self.var_len]))
        return X
    
    # Update generation
    def updateGeneration(self, children):
        self.population = children

    # Get the individual with best fitness
    def getResult(self):
        self.calculateFitnesses()
        best_idx = np.argmax(self.fitnesses)
        res = self.getVariables(self.population[best_idx])
        return res

    # Encode value to binary string
    def encode(self, X):
        s = ""
        for x in X:
            t = bin(x).replace("0b", "")
            remain = self.var_len - len(t)
            for _ in range(remain):
                t = '0' + t;
            s += t;
        return s

    # Decode binary string to value in bounds
    def decodeString(self, var_string):
        # mask = np.int64(1)
        temp = int('0b' + var_string, 2)
        # for ch in reversed(var_string):
        #     temp += mask * (ch == '1')
        #     mask <<= 1
        return self.bounds[0] + ((self.bounds[1] - self.bounds[0]) / ((2**self.var_len) - 1)) * temp
    
