import java.io.*;
import java.util.*;

public class Greeter {

    // static makes the variable 
    // shared by all instances
    //static private String greeting; 
    
    /* You can initialize instance variables
       when you declare them, like this */
    //private String greeting="Hello"; 

    private String greeting;
    
    public Greeter(String g) {
	setGreeting(g);
    }

    public Greeter() {
	setGreeting("Hello");
    }

    // examples of method overloading
    public void f() {
    }
    public void f(String s) {
    }
    public void f(String s,String s2) {
    }
    public void f(String s,int s2) {
    }
    public void f(int s,String s2) {
    }
    /*
      but this one doesn't work becasue
      we've already used String,String -
      it's about the types, not the names

    public void f(String s2,String s1) {
    }
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
