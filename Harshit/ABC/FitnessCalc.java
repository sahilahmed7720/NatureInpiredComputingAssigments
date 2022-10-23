package ABC;

public class FitnessCalc {
public double rostriginindi(Individual a,int n) {
	double x[]=new double[n];
	int div=a.genes.length/n;
	for(int i=0;i<n;i++) {
		int c=div-1;
		for(int j=i*div;j<i*div+div;j++) {
			x[i]=(x[i]+a.genes[j]*Math.pow(2,c--));
		}
	}
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
	for(int i=0;i<n;i++) {
		x[i]=-5.12+((10.24)/(Math.pow(2, div)-1))*x[i];
	}
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
	double v=0;
	for(int i=0;i<n;i++) {
		v= v+(Math.pow(x[i], 2)-10*Math.cos(2*Math.PI*x[i]));
	}
	v=v+10*n;
//	System.out.println(1/v);
	
	return 1/(v+1);
}
public double ackleyind(Individual a) {
	double x=0,y=0;
	int div=a.genes.length/2;
	int c=div-1;
	for(int j=0;j<div;j++) {
		x=(x+a.genes[j]*Math.pow(2,c--));
	}
		for(int j=div;j<a.genes.length;j++) {
			y=(y+a.genes[j]*Math.pow(2,c--));
		}
			x=-5+((10)/(Math.pow(2, div)-1))*x;
			y=-5+((10)/(Math.pow(2, div)-1))*y;
			double v=0;
			v=-20*Math.exp(-0.2*Math.sqrt(0.5*(Math.pow(x, 2)+	Math.pow(y, 2))));
			v=v-Math.exp(0.5*(Math.cos(2*Math.PI*x)+Math.cos(2*Math.PI*y)));
			v=v+Math.E+20;
	return 1/v;
	
}
public double sphereind(Individual a,int n) {
	double x[]=new double[n];
	int div=a.genes.length/n;
	for(int i=0;i<n;i++) {
		int c=div-1;
		for(int j=i*div;j<i*div+div;j++) {
			x[i]=(x[i]+a.genes[j]*Math.pow(2,c--));
		}
	}
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
//	for(int i=0;i<n;i++) {
//		x[i]=-5.12+((10.24)/(Math.pow(2, div)-1))*x[i];
//	}
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
	double v=0;
	for(int i=0;i<n;i++) {
		v=v+ (Math.pow(x[i], 2));
	}
//	System.out.println(1/v);
	return 1/v;
	
}
public double rosenbrockindi(Individual a,int n) {
	double x[]=new double[n];
	int div=a.genes.length/n;
	for(int i=0;i<n;i++) {
		int c=div-1;
		for(int j=i*div;j<i*div+div;j++) {
			x[i]=(x[i]+a.genes[j]*Math.pow(2,c--));
		}
	}
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
//	for(int i=0;i<n;i++) {
//	}	x[i]=-5.12+((10.24)/(Math.pow(2, div)-1))*x[i];
//	
//	for(int i=0;i<n;i++) {
//		System.out.println(x[i]);
//	}
	double v=0;
	for(int i=0;i<n-1;i++) {
		v= v+100*Math.pow((x[i+1]-Math.pow(x[i], 2)), 2);
		v=v+Math.pow(1-x[i], 2);
	}
//	v=v+10*n;
//	System.out.println(1/v);
	return 1/v;
}
}