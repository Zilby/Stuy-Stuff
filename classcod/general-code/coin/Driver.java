
public class Driver {
    public static void main(String[] args) {
	Coin q = new Coin(25);
	Coin d = new Coin(10);
	Coin n = new Coin(5);

	System.out.println(q.getValue());
	System.out.println(q);
	System.out.println(d);
	System.out.println(n);

	String s1 = "The Coin q is "+q;
	System.out.println(s1);


    }
}
