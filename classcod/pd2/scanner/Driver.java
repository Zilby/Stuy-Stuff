import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	/*
	Scanner sc = new Scanner(System.in);
	System.out.print("Enter your name: ");
	String name = sc.nextLine();
	System.out.println("Welcome, "+name);
	System.out.print("Enter a number: ");
	int i = sc.nextInt();
	System.out.println("You entered: "+i);
	name = sc.next();
	System.out.println("Welcome, "+name);
	name = sc.next();
	System.out.println("Welcome, "+name);
	*/

	Scanner stringscan = new Scanner("One Two THree Four Five");
	while (stringscan.hasNext() ) {
	    String item = stringscan.next();
	    System.out.println(item);
	    // for a delay take the code from here:
	    try {
		Thread.sleep(2000); // pause for that many milliseconds
	    } catch (Exception e) {
		// do nothing here - it should never get run 
	    }
	    // to here and change the Thread.sleep parameter as needed

	}

    }

}
