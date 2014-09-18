
public class Rational {
    private int n,d;


    /* Constructors */
    public void init(int n, int d) {
	this.n=n;
	this.d=d;
	reduce();
    }
    public Rational(int n, int d) {
	init(n,d);
    }
    public Rational(int n) {
	init(n,1);
    }
    public Rational() {
	init(0,1);
    }

    /* For debugging */
    public String toString() {
	return ""+n+"/"+d;
    }

    /* Getter / Setters */
    public void setRat(int n, int d) {
	this.n=n;
	this.d=d;
	reduce();
    }
    
    /* Internal utility functions */
    private int gcd(int a,int b) {
	if (b==0)
	    return a;
	else {
	    return gcd(b,a%b);
	} 
    }
    public void reduce() {
	int g = gcd(n,d);
	n=n/g;
	d=d/g;
    }

    /* operators */
    public Rational mult(Rational other) {
	int newN = this.n*other.n;
	int newD = this.d*other.d;
	Rational r = new Rational(newN,newD);
	return r;
    }
    
    /* comparisons */	    
    public boolean equals(Rational other) {
	// since our numbers are always reduced we
	// can just do this
	return this.n==other.n && this.d==other.d;
    }

    public int compareTo(Rational other) {
	// again, since we're already reduced

	
	return (int)((double)this.n*(double)other.d - (double)this.d*(double)other.n);
	
	// or we could have don
	//return (int)(((double)this.d)/this.d - ((double)other.n)/other.d);

    }



}
