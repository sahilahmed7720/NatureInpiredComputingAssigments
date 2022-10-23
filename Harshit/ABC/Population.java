package ABC;

public class Population {

    Individual[] individuals;

    /*
     * Constructors
     */
    // Create a population
    public Population(int populationSize, boolean initialise,int chromlen) {
        individuals = new Individual[populationSize];
        // Initialise population
        if (initialise) {
            // Loop and create individuals
            for (int i = 0; i < populationSize; i++) {
              individuals[i] = new Individual(chromlen);
            }
        }
    }
public void displaypop() {
	for(Individual i:individuals) {
		i.displayind();
	}
}
}
  