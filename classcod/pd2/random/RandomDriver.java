import java.util.*;

public class RandomDriver{
    public static void main(String[] args) {

	/* using Math and Math.random 
	System.out.println(Math.PI);
	System.out.println(Math.pow(2,3));
	double r;
	r = Math.random();
	System.out.println(r);
	int val = (int)(r*100);
	System.out.println(val);
	*/

	/* Using the Random class */
	Random r = new Random(123);
	System.out.println(r.nextDouble());
	System.out.println(r.nextDouble());

	System.out.println(r.nextInt());
	System.out.println(r.nextInt());

	System.out.println(r.nextInt(100));
	System.out.println(r.nextInt(100));

	System.out.println(4==3||7<2);


    }

}
