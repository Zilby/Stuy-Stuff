import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

	/*
	System.out.print("Please enter your name:");
	String name=sc.nextLine();
	System.out.println("Welcom, "+name);
	  System.out.print("Enter a number: ");
	int i = sc.nextInt();
	System.out.println("You entered: "+i);
	System.out.println("Enter a line: ");
	String line = sc.next();
	System.out.println(line);
	line = sc.next();
	System.out.println(line);
	*/
	Scanner stringscan = new Scanner("ONE TWO THREE");
	while (stringscan.hasNext() ) {
	    System.out.println(stringscan.next());
	    // for a delay use these lines:
	    try {
		Thread.sleep(2000); // how many milliseconds to pause
	    } catch (Exception e) {
		// do nothing here 
	    }
	    // up to here

	    
	}

    }

}
