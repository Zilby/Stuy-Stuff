import java.io.*;
import java.util.*;

public class Greeter {

    public String greeting; 
    /* 2. change public to private,
       test, then change back 
    */

    public Greeter(String g) {
	greeting = g;
    }
    public Greeter() {
	greeting = "hey";
    }
    

    /* 3. change public to private,
       test, then change back 
    */
    public void setGreeting(String greet) {
	greeting = greet;
    }

    public String greet(String name) {
	String message;
	message = greeting + " " + name;
	return message;
    }
}
