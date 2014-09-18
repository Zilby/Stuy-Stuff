import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args){
	Turtle A = new Turtle();
	System.out.println(A.getName());
	System.out.println(A.getSpeed());
	System.out.println(A.getAge());
	A.getOlder();
	System.out.println(A.getAge());
	A.speedUp(400);
	System.out.println(A.getSpeed());

	Turtle B = new Turtle("Bee");
	System.out.println(B.getName());
	System.out.println(B.getSpeed());
	System.out.println(B.getAge());

	Turtle C = new Turtle("Sea",64,1234321);
	System.out.println(C.getName());
	System.out.println(C.getSpeed());
	System.out.println(C.getAge());

	Person D = new Person ("Dee");
	D.setTurtle(C);
	System.out.println (D.getPet().getName());
	System.out.println (D.getTurtleSpeed());
    }
}
