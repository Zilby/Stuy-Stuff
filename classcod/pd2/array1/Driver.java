import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	ArrayStuff as = new ArrayStuff();
	as.demo1();
	
	System.out.println("\n--------------\nargs stuff\n");
	System.out.println(args.length);
	for (int i=0;i<args.length;i++){
	    System.out.println("args["+i+"] : "+args[i]);
	}
    }

}
