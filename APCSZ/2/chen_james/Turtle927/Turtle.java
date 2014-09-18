import java.io.*;
import java.util.*;

public class Turtle {
   
    public int speed;
    public int age;
    public String name;
   

    public Turtle () {
	name = "Mushroom";
	age = 100;
	speed = 6;
     }
    
    public Turtle (String tName) {    
	name = tName;
	age = 5;
	speed = 5;
    }

    public Turtle (String tName, int tSpeed, int tAge){
	name = tName;
	age = tAge;
	speed = tSpeed;   
    }

    public void speedUp (int n) {
	speed += n;
	//speed = speed + n;
    }

    public void slowDown (int n) {
	speed -= n;
    }

    public void addOlder() {
	age ++;
    }

    public String getName() {
	return "This Turtle's name is: " + name;
    }

    public int getSpeed() {
	//	String sSpeed = String.valueOf(speed);

	// String strSpeed =  String.valueOf(s);
	return speed;
    }

    public int getAge() {
	//	String sAge = String.valueOf(age);
	return age;
    }
    

}

