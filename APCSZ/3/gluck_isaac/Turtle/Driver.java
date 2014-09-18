import java.io.*;
import java.util.*;

public class Driver{

    public static void main(String[] args) {
	Turtle t, tName, tAll;
	Person p;

	t = new Turtle();
	tName = new Turtle("Jonny");
	tAll = new Turtle("Speedy", 6, 10);
	p = new Person("O'hara");

	t.speedUp(1);
	t.getOlder();
	t.getInfo();

	tName.speedUp(5);
	tName.speedDown(2);
	tName.getInfo();

	tAll.getInfo();

	p.setTurtle(tAll);
	System.out.println(p.getPet());
	System.out.println(p.getTurtleSpeed());
    }

}
