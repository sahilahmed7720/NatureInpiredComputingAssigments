package ABC;

import java.util.Random;

public class Driver {
	public static int n=2;
	public static int popsize=5;
	public static double limtrial=20;
public static void main(String args[]) {
	Population initialpop=new Population(popsize,true,n);
	initialpop.displaypop();
	int trial[]=new int[popsize];
	double fit[]=new double[popsize];
	
//	Algorithm gen=new Algorithm();
	double fittest=100;
	Individual fitsol = null;
	int gener=0;
while(fittest!=0&&gener!=10) {
	for(int x=0;x<initialpop.individuals.length;x++) {

		double phi=-1+Math.random()*2;
		int j=(int) (1+Math.random()*(n-1));
		int p=0;
		do {
			p=(int) (1+Math.random()*(initialpop.individuals.length-1));
		}while(p==x);
		
		double [] y=new double[n];
		for(int l=0;l<n;l++) {
			if(l==j) {
				y[l]=(initialpop.individuals[x].genes[j]+
						phi*(initialpop.individuals[x].genes[j]-
								initialpop.individuals[p].genes[j]));
			}
			else 
				y[l]=  initialpop.individuals[x].genes[l];
			}
		
		FitnessCalc fitc=new FitnessCalc();
		int div=2;
		Individual Y=new Individual(y);
		double fitx=fitc.rosenbrockindi(initialpop.individuals[x],div );
		double fity=fitc.rosenbrockindi(Y,div );
		if(fitx>=fity) {
//			System.out.println("Hello  "+x);
//			initialpop.individuals[x].displayind();
			for(int m=0;m<n;m++) {
				initialpop.individuals[x].genes[m]=y[m];
			}
			trial[x]=0;
			fit[x]=fity;
//			initialpop.individuals[x].displayind();
//			initialpop.displaypop();
		}
		else {
			trial[x]++;
			fit[x]=fitx;
		}
		if(fittest>fity) {
//			System.out.println("Hello  "+x);
			fittest=fity;
			
			fitsol=initialpop.individuals[x];
		
		}
//		initialpop.displaypop();


	}	
	int mxtrial=0;
	int idxtr=0;
	for(int i=0;i<popsize;i++) {
		if(mxtrial<trial[i]) {mxtrial=trial[i];
		idxtr=i;}
	}
	if(mxtrial>limtrial) {
		for (int i = 0; i < n; i++) {
        	Random random = new Random();
        	
//            int gene = random.nextInt();
        	int gene=(int) (0+Math.random()*20);
           initialpop.individuals[idxtr].genes[i] = gene;
        }
	}
	System.out.println("Generation "+gener+" completed!");
	System.out.println("Best Function value till now : "+fittest);
	System.out.println("Solution is: ");
	fitsol.displayind();
	
//	
	gener++;
}
//initialpop.displaypop();


	}
}