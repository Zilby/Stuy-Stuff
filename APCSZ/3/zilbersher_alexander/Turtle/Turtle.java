import java.util.*;
import java.io.*;

public class Turtle
{
    public String name;
    public int age;
    public int speed;

    public Turtle {
	name = "Basic Turtle";
	age = 0;
	speed = 1;
    }
    public Turtle(String name) {
	name = n;
	age = 0;
	speed = 5;
    }
    public void speedUp(int n) {
	speed += n;
    }
     public void slowDown(int n) {
	speed += n;
    }
    public void getOlder(){
	age += 1;
    }
    public String getName(){
	return name;
    }
    public int getAge(){
	return age;
    }
    public int getSpeed(){
	return speed;
    }
}
	
    