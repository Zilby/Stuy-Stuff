import java.io.*;
import java.util.*;


public class Turtle {
    private String name;
    private int speed, age;


    /*Constructors:*/
    public Turtle (){
	name = "Your Turtle's name is" + " "+"Tim Tom";
	age = 33;
	speed = 2;
    }
    public Turtle (String tName) {
	name ="Your Turtle's name is"+ " "+ tName;
	age=2;
	speed=15;
    }
    public Turtle (String tName,int tSpeed, int tAge) {
	name = "Your Turtle's name is"+ " "+ tName;
	speed = tSpeed;
	age = tAge;
    } 

    /*Set Methods:*/
    public void setSpeedUp(int n){
	speed = speed + n;
    }
    public void setSlowDown(int n){
	speed = speed - n;
    }
    public void setOlder(){
	age = age + 1;
    }


    /*Get Methods:*/
    public int getSpeed() {
	return speed;
    }
    public int getAge(){
	return age;
    }
    public String getName() {
	return name;
    }

}
