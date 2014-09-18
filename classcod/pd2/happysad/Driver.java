import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String args[]) {
	Greeter g,g2;
	g = new Greeter("Hello","Eat my shorts");
	System.out.println(g.greetHappy("Tom"));
	System.out.println(g.greetSad("Tom"));
	g2 = new Greeter();
	System.out.println(g2.greetHappy("Tom"));
	System.out.println(g2.greetSad("Tom"));
    }
   
}
