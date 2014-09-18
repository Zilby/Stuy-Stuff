
import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	ArrayStuff as = new ArrayStuff();
	as.demo1();
	
	// this prints out the content of the args array parameter
	// it contains everything you type after "java Driver"
	// so if you typed: java Driver one two three
	// then args[0] whould have one, args[1] would have two
	// and args[2] would have three
	for (int i=0;i<args.length;i++) {
	    System.out.println("args["+i+"] : "+args[i]);
	}
    }
    
}
