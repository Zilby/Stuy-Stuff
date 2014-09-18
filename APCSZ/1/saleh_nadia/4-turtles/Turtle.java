import java.io.*;
import java.util.*;

public class Turtle {
    private String name;
    private int age,speed;
    
    public Turtle () {
	age = 16;
	speed = 9;
	name = "Billmantha";
    }

    public Turtle (String iname) {
	name = iname;
	age = 16;
	speed = 9;
    }

    public Turtle (String iname, int iage, int ispeed) {
	name = iname;
	age = iage;
	speed = ispeed;
    }

    public void speedUp (int n) {
	speed = speed + n;
    }

    public void slowDown (int n) {
	speed = speed - n;
    }

    public void getOlder () {
	age = age + 1;
    }

    public int getAge () {
	return age;
    }

    public int getSpeed () {
	return speed;
    }

    public String getName () {
	return name;
    }

}