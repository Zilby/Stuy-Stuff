import java.io.*;
import java.util.*;

public class Greeter {

    // We can initialize instance variables
    // when we declare them
    //private String greeting="default"; 

    private String greeting;

    /* 
       Examples of overloading 
       
       public void f() {
       }
       public void f(String name){
       }
       public void f(String name, String name2) {
       }
       public void f(int name) {
       }
       
       This one won't work -- String String is
       already used
       public void f(String name2, String name1) {
       }
    */

    
    public Greeter(String g) {
	setGreeting(g);
    }

    public Greeter() {
	setGreeting("hello");
    }

    public void setGreeting(String greet) {
	greeting = greet;
    }

    public String greet(String name) {
	String message;
	message = greeting + " " + name;
	return message;
    }
}
