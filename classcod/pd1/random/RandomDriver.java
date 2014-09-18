import java.io.*;
import java.util.*;

public class RandomDriver{
    public static void main(String[] args) {
	

	/* Using Math.random
	double r;
	r = Math.random();
	System.out.println(r);

	int r2 = (int)(r*100);
	System.out.println(r2);
	*/
	
	/* using the Random class */
	Random r = new Random( );
	System.out.println(r.nextDouble());
	System.out.println(r.nextInt());
	System.out.println(r.nextInt(10));

	System.out.println(3!=4&&2!=4);
    }

}
