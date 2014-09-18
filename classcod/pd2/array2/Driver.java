import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	if (args.length != 1) {
	    System.out.println("Enter array size");
	    System.exit(0);
	}
	int arraySize = Integer .parseInt(args[0]);
	long start,t;

	start = System.currentTimeMillis();
	ArrayStuff as = new ArrayStuff(arraySize,30);
	t = System.currentTimeMillis()-start;
	System.out.println("Constructor time: "+t);


	start = System.currentTimeMillis();
	as.findMaxIndex();
	t = System.currentTimeMillis()-start;
	System.out.println("Max time: "+t);

	start = System.currentTimeMillis();
	as.mode2();
	t = System.currentTimeMillis()-start;
	System.out.println("Mode time: "+t);

   }
}
