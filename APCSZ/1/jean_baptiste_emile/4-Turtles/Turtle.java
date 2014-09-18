import java.io.*;
import java.util.*;

public class Turtle {
    private String name;
    private int age,speed;

    public Turtle() {
	name = "Mark";
	age = 4;
	speed = 2;
    }
    public Turtle(String name1) {
	name = name1;
	age = 5;
	speed = 1;
    }
    public Turtle(String name1,int age1,int speed1) {
	name = name1;
	age = age1;
	speed = speed1;
    }

    public void speedUp(int n) {
	speed = speed + n;
    }
    public void slowDown(int n) {
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
}