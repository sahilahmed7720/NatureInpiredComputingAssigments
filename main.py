from functions.Ackley import Ackley
from functions.Rastrigin import Rastrigin
from algorithms.GA import GA
from functions.Rosenbrock import Rosenbrock
from functions.Sphere import Sphere
import pandas as pd

# Main
def main():
    indices = ["Rastrigin Optimization", "Ackely Optimization", "Sphere Optimization", "Rosenbrock Optimization"]
    columns = ["Solution", "Optimal Value"]
    solns = []

    # Rastrigin
    rastrigin = Rastrigin(2, [-5.12, 5.12])
    # x, o = rastrigin.optimizeUsingGA(population_size=100, iterations=1000)
    # solns.append([x, o])
    # x, o = rastrigin.optimizeUsingDE(population_size=100, iterations=1000)
    # solns.append([x, o])
    # x, o = rastrigin.optimizeUsingABC(swarm_size=200, iterations=1000)
    # solns.append([x, o])
    x, o = rastrigin.optimizeUsingPSO(population_size=200, iterations=1000)
    solns.append([x, o])

    # # Ackley
    ackley = Ackley(2, [-5, 5])
    # x, o = ackley.optimizeUsingGA(population_size=100, iterations=1000)
    # solns.append([x, o])
    # x, o = ackley.optimizeUsingDE(population_size=100, iterations=1000)
    # solns.append([x, o])
    # x, o = ackley.optimizeUsingABC(swarm_size=200, iterations=1000)
    # solns.append([x, o])
    x, o = ackley.optimizeUsingPSO(population_size=200, iterations=1000)
    solns.append([x, o])

    # # Sphere
    sphere = Sphere(2, [-100, 100])
    # x, o = sphere.optimizeUsingGA(population_size=200, iterations=1000)
    # solns.append([x, o])
    # x, o = sphere.optimizeUsingDE(population_size=200, iterations=1000)
    # solns.append([x, o])
    # x, o = sphere.optimizeUsingABC(swarm_size=200, iterations=1000)
    # solns.append([x, o])
    x, o = sphere.optimizeUsingPSO(population_size=200, iterations=1000)
    solns.append([x, o])

    # Rosenbrock
    rosen = Rosenbrock(2, [-100, 100])
    # x, o = rosen.optimizeUsingGA(population_size=200, iterations=1000)
    # solns.append([x, o])
    # x, o = rosen.optimizeUsingDE(population_size=200, iterations=5000)
    # solns.append([x, o])
    # x, o = rosen.optimizeUsingABC(swarm_size=200, iterations=2000)
    # solns.append([x, o])
    x, o = rosen.optimizeUsingPSO(population_size=200, iterations=1000)
    solns.append([x, o])

    df = pd.DataFrame(solns, indices, columns)
    print(df)


if __name__ == "__main__":
    main()
