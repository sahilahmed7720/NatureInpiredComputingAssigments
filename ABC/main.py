from functions.Ackley import Ackley
from functions.Rastrigin import Rastrigin
from functions.Rosenbrock import Rosenbrock
from functions.Sphere import Sphere
import pandas as pd


# Main
def main():
    # Rastrigin
    rastrigin = Rastrigin(10, [-5.12, 5.12])
    x, o = rastrigin.optimizeUsingABC(swarm_size=200, iterations=1000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Ackley
    ackley = Ackley(2, [-5, 5])
    x, o = ackley.optimizeUsingABC(swarm_size=200, iterations=1000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Sphere
    sphere = Sphere(10, [-100, 100])
    x, o = sphere.optimizeUsingABC(swarm_size=200, iterations=1000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Rosenbrock
    rosen = Rosenbrock(10, [-100, 100])
    x, o = rosen.optimizeUsingABC(swarm_size=200, iterations=1000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")


if __name__ == "__main__":
    main()
