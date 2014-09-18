import java.io.*;
import java.util.*;

public class Person {
    public String name;
    public Turtle turtle;

    public Person(String tName){
	name = tName;
    }
    
    public void setTurtle(Turtle t){
	turtle = t;
    }

    public Turtle getPet(){
	return turtle;
    }

    public int getTurtleSpeed(){
	return turtle.getSpeed();
    }
}
