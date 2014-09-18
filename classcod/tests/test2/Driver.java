
public class Driver {
    public static void main(String[] args) {
	Ascii a = new Ascii();
	
	System.out.println(a.rect(3,8,"Y"));
	System.out.println(a.triangle1(5));
	System.out.println(a.triangle2(5));

	Loops l = new Loops();
	System.out.println(l.diag(5));
	System.out.println(l.diagWord("Hello"));
	System.out.println(l.fence(5,8));

	System.out.println();
	Rational r1 = new Rational(4,8);
	Rational r2 = new Rational(2,3);
	System.out.println(r1+" "+r2);
	System.out.println(r1.mult(r2));
	System.out.println(r1.equals(r1));
	System.out.println(r1.equals(r2));
	System.out.println(r1.compareTo(r1));
	System.out.println(r1.compareTo(r2));
	System.out.println(r2.compareTo(r1));
	    

    }

}
