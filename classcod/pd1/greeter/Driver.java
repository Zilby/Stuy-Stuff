import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	/*
	g = new Greeter();
	g.setGreeting("Hello");
	g2 = new Greeter();
	g2.setGreeting("How are you doing");
	result = g.greet("Tom");
	System.out.println(result);
	result = g2.greet("Sarah");
	System.out.println(result);
	
	g.setGreeting("Sup");
	System.out.println(g.greet("Adam"));
	System.out.println(g2.greet("Alice"));
	*/
	Greeter g,g2;

	String result;
	g = new Greeter("Howdy");
	g2 = new Greeter();
	System.out.println(g.greet("Tom"));
	System.out.println(g2.greet("Tom"));
    }
}
