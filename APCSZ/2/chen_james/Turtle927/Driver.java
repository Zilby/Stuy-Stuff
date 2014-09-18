import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String args[]) {
	Turtle t = new Turtle();
	Turtle t2 = new Turtle("Mario");
	Turtle t3 = new Turtle("Wario", 1, 50);

	System.out.println(t3.getName());
	System.out.println(t3.getSpeed());
	System.out.println(t3.getAge());

	System.out.println(t2.getName());
	System.out.println(t2.getSpeed());
	System.out.println(t2.getAge());

	System.out.println(t.getName());
	System.out.println(t.getSpeed());
	System.out.println(t.getAge());
	
	// Person.java
	Person x = new Person("James");
	x.setTurtle(t2);
	System.out.println(x.getTurtleSpeed());
	System.out.println(x.getPet().getName());
	

	

    }


}
