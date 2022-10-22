from functions.Ackley import Ackley
from functions.Rastrigin import Rastrigin
from functions.Rosenbrock import Rosenbrock
from functions.Sphere import Sphere


# Main
def main():
    # Rastrigin
    rastrigin = Rastrigin(10, [-5.12, 5.12])
    x, o = rastrigin.optimizeUsingDE(population_size=100, iterations=5000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Ackley
    ackley = Ackley(2, [-5, 5])
    x, o = ackley.optimizeUsingDE(population_size=100, iterations=5000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Sphere
    sphere = Sphere(10, [-100, 100])
    x, o = sphere.optimizeUsingDE(population_size=200, iterations=5000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")

    # Rosenbrock
    rosen = Rosenbrock(10, [-100, 100])
    x, o = rosen.optimizeUsingDE(population_size=200, iterations=5000)
    print("Solution :")
    print(x)
    print("Optimal Value :")
    print(o, "\n")


if __name__ == "__main__":
    main()
