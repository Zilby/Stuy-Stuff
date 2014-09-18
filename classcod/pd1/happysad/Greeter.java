import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	//Greeter g = new Greeter("howdy","get lost");
	Greeter g = new Greeter();
	System.out.println(g.greetHappy("Fred"));
	System.out.println(g.greetSad("Fred"));
    }

}


