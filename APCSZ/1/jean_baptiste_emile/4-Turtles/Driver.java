import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {

	Turtle t,t1,t2;
	Person p;
	t = new Turtle();
	t1 = new Turtle("Leonardo");
	t2 = new Turtle("Torterra",3,8);
	p = new Person("Splinter");
        System.out.println(t.getAge());
	System.out.println(t.getName());
	System.out.println(t.getSpeed());
	System.out.println(" ");

	System.out.println(t1.getAge());
	System.out.println(t1.getName());
	System.out.println(t1.getSpeed());
	System.out.println(" ");

	System.out.println(t2.getAge());
	System.out.println(t2.getName());
	System.out.println(t2.getSpeed());
	System.out.println(" ");

	t.getOlder();
	t1.speedUp(10);
	t2.slowDown(4);

	System.out.println(t.getAge());
	System.out.println(t.getName());
	System.out.println(t.getSpeed());
	System.out.println(" ");

	System.out.println(t1.getAge());
	System.out.println(t1.getName());
	System.out.println(t1.getSpeed());
	System.out.println(" ");

	System.out.println(t2.getAge());
	System.out.println(t2.getName());
	System.out.println(t2.getSpeed());

	p.setTurtle(t1);
	System.out.println(p.getTurtleSpeed());
	System.out.println(p.getPet().getSpeed());
    }
}