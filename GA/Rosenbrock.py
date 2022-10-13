import numpy as np
import random as rd


# defining objective funtion (we will use this function as fitness as well and make it subject to minimization)
def rosenbrock(x):
    sum = 0
    i = 0
    while i < (len(x) - 1):
        sum += 100 * ((x[i+1] - (x[i]*x[i]))**2)
        sum += (1-x[i])**2
        i += 1
    return sum


# initialize population and store fitness in first column and genes in second column
def initialization(pop):
    p = []
    for b in range(0, pop):
        x = []
        for a in range(0, 10):
            x.append(10*rd.uniform(0, 1) - 5)
        r = rosenbrock(x)
        p.append([r, x])
    return p


# helper function to print only the fitness of a solution
def print_pop(pop):
    print("[", end="")
    for x in pop:
        print(x[0], end=", ")
    print("]")


# function to calculate average fitness of population
def avfitness(p):
    sum = 0.0
    for x in p:
        sum += x[0]
    return sum/len(p)


# formula to get probabality according to rank
def rankprob(i, n):
    s = 1.2
    prob = ((2-s)/n) + (2*i*(s-1))/(n*(n-1))
    return prob


# selection - rank based selection
def selection(pop, selected):
    pop.sort(reverse=True)  # sort from worst to best

    # calculation of selection probability for the entire population
    prob = [rankprob(i, len(pop)) for i in range(0, len(pop))]
    cumprob = []
    sum = 0
    for i in range(0, len(prob)):  # calculation of cumulative probability
        sum += prob[i]
        cumprob.append(sum)

    mating_pool = []
    for i in range(0, selected):
        r = rd.uniform(0, 1)
        j = 0
        while (r > cumprob[j]):  # adding to mating pool using cumulative probability
            j += 1
        mating_pool.append(pop[j])
    return mating_pool


# whole arithmetic recombination with alpha 0.2
# and with some recombination probablity for each gene,
# making 2 children, choosing better one
def recombination(a, b, rec_prob):
    alpha = 0.4
    alphainv = 1-alpha
    child1 = [0 for i in range(0, 10)]
    child2 = [0 for i in range(0, 10)]
    for i in range(0, 10):
        rand = rd.uniform(0, 1)
        # either using recombination or copying the parents directly using recombination probablity
        if(rand < rec_prob):
            child1[i] = (alpha*a[i]) + (alphainv*b[i])
            child2[i] = (alpha*a[i]) + (alphainv*b[i])
        else:
            child1[i] = a[i]
            child2[i] = b[i]
    # choosing and returning the better child
    ras1 = rosenbrock(child1)
    ras2 = rosenbrock(child2)
    res = []
    if(ras1 < ras2):
        res = [ras1, child1]
    else:
        res = [ras2, child2]
    return res


# applying recombination to entire mating pool
def crossover(mating_pool, rec_prob):
    i = 0
    children = []
    while(i < len(mating_pool)):
        children.append(recombination(
            mating_pool[i][1], mating_pool[i+1][1], rec_prob))
        i += 2
    return children


# applying mutation using Non-Uniform mutation with mutation probablity
def mutation(children, mut_prob):
    for x in children:
        for g in x[1]:
            r = rd.uniform(0, 1)
            if(r < mut_prob):
                mutation = rd.gauss(0, 1)
                g += mutation

                # clamping the mutated gene within the search range
                if(g > 5):
                    g = 5.00
                if(g < -5):
                    g = -5.00

        # recalculatng fitness
        x[0] = rosenbrock(x[1])

    return children


# replacing worst 50% by best of chidren and parents combined
def replace_worst(pop, children):
    pop_temp = pop + children
    pop_temp.sort()
    return pop_temp[0:pop_size]


# main
pop_size = 3000
selected = 6000
rec_prob = 0.9
mut_prob = 0.95
max_gen = 100

# initialize population and store fitness
pop = initialization(pop_size)

gen = 0
while gen < max_gen:
    gen += 1

    # getting mating pool
    mating_pool = selection(pop, selected)

    # getting children (crosover)
    children = crossover(mating_pool, rec_prob)

    # applying mutation to children
    children = mutation(children, mut_prob)

    # replacing worst
    pop = replace_worst(pop, children)

    print("Average Fitness after Generation " + str(gen), end=" is ")
    print(format(avfitness(pop), '.10f'))

pop.sort()
print("Best solution has fitness ", end="")
print(str(format(pop[0][0], '.10f')))
print(pop[0][1])
