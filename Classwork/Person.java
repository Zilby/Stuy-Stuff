import java.util.*;
import java.io.*;

public class Person {
    public String name;
    public String turtle;

    public Person(String n){
	name = n;
    }

    public void setTurtle(Turtle t) {
	turtle = t;
    }

    public Turtle getPet() {
	return turtle;
    }

    public int getTurtleSpeed(){
	return turtle.getSpeed();

    }
}