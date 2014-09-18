import java.io.*;
import java.util.*;

public class Greeter {
    
    public String greeting;
    public void setGreeting(String greet) {
	greeting = greet;
    }

    public String greet(String name) {
	String message;
	message = greeting + " " + name;
	return message;
    }
}