import numpy as np
import random as rd

# helper funtions for float to binary conversion and vice versa


def floattobin(a):
    neg = 0
    if(a < 0):
        a = -a
        neg = 1
    num = a
    res = ""
    while(a >= 1):
        res += str(int(a % 2))
        a /= 2

    while(len(res) < 3):
        res += '0'
    res = res[::-1]
    a = num % 1
    dec = ""
    i = 1
    den = 2
    while(i < 16):
        if(a - (1/den) >= 0):
            dec += '1'
            a -= 1/den
        else:
            dec += '0'
        i += 1
        den *= 2
    return str(neg) + res + "." + dec


def bintofloat(bin):
    splitted = str.split(bin, '.')
    if(splitted[0] == "0000" and splitted[1] == "000000000000000"):
        return 0
    neg = int(splitted[0][0])
    splitted[0] = splitted[0][::-1]
    i = 0
    mul = 1
    res = 0
    while(i < len(splitted[0])-1):
        if(splitted[0][i] == '1'):
            res += mul
        mul *= 2
        i += 1

    i = 0
    mul = 1/2
    while(i < len(splitted[1])):
        if(splitted[1][i] == '1'):
            res += mul
        mul /= 2
        i += 1
    if(neg == 1):
        res = -res
    return res


def stringtolist(s):
    a = 0
    b = 20
    res = []
    while(b <= len(s)):
        res.append(bintofloat(s[a:b]))
        a += 20
        b += 20
    # print(s)
    # print(res)
    return res


# defining objective funtion (we will use this function as fitness as well and make it subject to minimization)
def rosenbrock(s):
    x = stringtolist(s)
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
        x = ""
        for c in range(0, 10):
            x += floattobin(10*rd.uniform(0, 1) - 5)
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


# uniform crossover with probability parameter rec_prob for each gene,
# making 2 children, choosing better one
def recombination(a, b, rec_prob):
    child1 = ""
    child2 = ""
    for i in range(0, 200):
        rand = rd.uniform(0, 1)
        # either using recombination or copying the parents directly using recombination probablity
        if(rand < rec_prob):
            child1 += b[i]
            child2 += a[i]
        else:
            child1 += a[i]
            child2 += b[i]
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


# applying mutation using bit-flip mutation with mutation probablity
def mutation(children, mut_prob):
    for x in children:
        for g in x[1]:
            r = rd.uniform(0, 1)
            if(r < mut_prob):
                if(g == '0'):
                    g = '1'
                else:
                    g = '0'

        # recalculatng fitness
        x[0] = rosenbrock(x[1])

    return children


# replacing worst 50% by best of chidren and parents combined
def replace_worst(pop, children):
    pop_temp = pop + children
    pop_temp.sort()
    return pop_temp[0:pop_size]


# main
pop_size = 1500
selected = 1500
rec_prob = 0.5
mut_prob = 0.85
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
print(stringtolist(pop[0][1]))
