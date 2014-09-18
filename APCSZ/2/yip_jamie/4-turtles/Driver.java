import java.io.*;
import java.util.*;

public class Driver{

    public static void main(String args[]){
	Turtle t,t2,t3;
	t=new Turtle();
	System.out.println(t.getName());
   	System.out.println(t.getSpeed());
	System.out.println(t.getAge());
	t2=new Turtle("Emily");
	System.out.println(t2.getName());
       	System.out.println(t2.getSpeed());
	System.out.println(t2.getAge());
	t3=new Turtle ("Allen",9,5);
	System.out.println(t3.getName());
       	System.out.println(t3.getSpeed());
	System.out.println(t3.getAge());

	Person p = new Person("Ted");
	p.setTurtle(t3);
	System.out.println(p.getPet().getName());
	System.out.println(p.getTurtleSpeed());
	System.out.println(p.getPet().getAge());
    }
}
