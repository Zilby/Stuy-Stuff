import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	Greeter g,g2;
	String result;
	g = new Greeter();
	g.setGreeting("Hello");
	g2 = new Greeter();
	g2.setGreeting("How are you doing");
	result = g.greet("Tom");
	System.out.println(result);
	result = g2.greet("Sarah");
	System.out.println(result);

	g2 = new Greeter("sub");
	System.out.println(g2.greet("harry"));
	/* 1. Try:
	   g.setGreeting("Howdy");
	   g.greet("Tom");
	   g.setGreeting("sup");
	   g.greet("Fred");
	*/


    }
}
