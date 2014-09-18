import java.io.*;
import java.util.*;

public class PC extends Character{
    
    public PC(){
	dexterity = 8;
	strength = 8;
	intelligence = 8;
	int pointsleft = 8;
	System.out.print("Enter Name: ");
	Scanner x = new Scanner(System.in);
	String n = x.nextLine();
	name = n;

	System.out.print("Add points to strength : ");
        x = new Scanner(System.in);
	int m = x.nextInt();
	if (m > pointsleft){
	    strength = strength + pointsleft;
	    pointsleft = 0;
	}
	else {
	    strength = strength + m;
	    pointsleft = pointsleft - m;
	}
	System.out.println("Points left: " + pointsleft);

	System.out.print("Add points to dexterity : ");
        x = new Scanner(System.in);
	m = x.nextInt();
	if (m > pointsleft){
	    dexterity = dexterity + pointsleft;
	    pointsleft = 0;
	}

	else {
	    dexterity = dexterity + m;
	    pointsleft = pointsleft = m;
	}
	System.out.println("Points left: " + pointsleft);

	System.out.print("Add points to intelligence : ");
	x = new Scanner(System.in);
	m = x.nextInt();
	if (m > pointsleft) {
	    intelligence = intelligence + pointsleft;
	    pointsleft = 0;
	}
	else {
	    intelligence = intelligence + m;
	    pointsleft = pointsleft = m;
	}
	
	health = 50 + ((strength - 8)*4);
    }
}

