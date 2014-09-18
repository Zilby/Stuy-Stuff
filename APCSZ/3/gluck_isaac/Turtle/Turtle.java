import java.io.*;
import java.util.*;

public class Turtle {

    private String name;
    private int age, speed;

    public Turtle() {
	initSetAll("default", 0, 1);
    }

    public Turtle(String n) {
	initSetAll(n, 0, 1);
    }

    public Turtle(String n, int a, int s) {
	initSetAll(n, a, s);
    }

    public void setName(String n) {
	name = n;
    }

    public void setAge(int a) {
	age = a;
    }


    public void setSpeed(int s) {
	speed = s;
    }


    public void initSetAll(String n, int a, int s) {
	setName(n);
	setAge(a);
	setSpeed(s);
    }


    public void speedUp(int n) {
	speed = speed + n;
    }

    public void speedDown(int n) {
	speed = speed - n;
    }

    public void getOlder() {
	age = age + 1;
    }

    public String getName() {
	return name;
    }


    public int getAge() {
	return age;
    }


    public int getSpeed() {
	return speed;
    }

   
    public void getInfo() {
	System.out.println("The turtle's name is " + name);
	System.out.println(name + "'s age is " + age);
        System.out.println(name + "'s speed is " + speed);
    }
}
