import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	ArrayStuff as = new ArrayStuff(10000000,30);
	// System.out.println(as);
	long start = System.currentTimeMillis();
	as.mode();
	long t = System.currentTimeMillis()-start;
	System.out.println("Time: "+t);
	
   }
}
