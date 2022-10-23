package ABC;

import java.util.Random;

public class Individual {

    double[] genes ;
    // Cache
    private int fitness = 0;
    public Individual(double [] gen) {
    	this.genes=new double[gen.length];
    	int j=0;
    	for(double i:gen) {
    		this.genes[j++]=i;
    	}
    }
    // Create a random individual
    public Individual(int len) {
    	genes=new double[len];
        for (int i = 0; i < len; i++) {
        	Random random = new Random();
        	
//            int gene = random.nextInt();
        	double gene=Math.random()*20;
            genes[i] = gene;
        }
    }
    public void displayind() {
    	for(double i:genes) {
    		System.out.print(i+" ");
    	}
    	System.out.println();
    }
}