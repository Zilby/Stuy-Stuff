import java.io.*;
import java.util.*;

public class Person{
    private String name;
    private Turtle turtle;

    public Person() {
	name = "default";
    }

    public Person(String n) {
	setName(n);
    }

    public void setName(String n) {
	name = n;
    }

    public void setTurtle(Turtle t) {
	turtle = t;
    }

    public Turtle getPet() {
	return turtle;
    }

    public int getTurtleSpeed() {
	return turtle.getSpeed();
    }

}
