import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	Greeter g,g2;
	String result;
	/*
	g = new Greeter();
	g.setGreeting("Hello");
	g2 = new Greeter();
	result = g.greet("Tom");
	g2.setGreeting("How are you doing");
	System.out.println(result);
	result = g2.greet("Sarah");
	System.out.println(result);

	g.setGreeting("sup");
	System.out.println(g.greet("Harry"));
	System.out.println(g2.greet("Sue"));
	*/

	g = new Greeter("Get lost");
	g2 = new Greeter();
	System.out.println(g.greet("Tom"));
	System.out.println(g2.greet("Sarah"));
    }
}
