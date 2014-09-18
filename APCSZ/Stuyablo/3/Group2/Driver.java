import java.util.*;
import java.io.*;

public class Driver {
    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	Random randGen = new Random();
	System.out.println("Would you like to be an (1) Elf or a (2) Student?");
	int classChoice = sc.nextInt();
	Character p1;
	if (classChoice == 1) {
		p1 = new Elf();
	} else if (classChoice == 2) {
		p1 = new Student();
	} else {
		int randChoice = randGen.nextInt(2);
		if (randChoice == 0) {
			p1 = new Elf();
			System.out.println("You have failed to choose correctly.");
			System.out.println("You have randomly been assigned the Elf type.");
		} else {
			p1 = new Student();
			System.out.println("You have failed to choose correctly.");
			System.out.println("You have randomly been assigned the Student type.");
		}
	}
	Character c1 = new Teacher("Evil Bob", p1.getLevel());
	Homework h1 = new Homework("English Teacher", p1.getLevel());
	Encounter e = new Encounter();
	System.out.println("How long do you want the game to be? (1) Short (2) Medium (3) Long (4) Never-ending");
	int len = sc.nextInt();
	if (len == 1) 
	    len=5;
	else if (len == 2)
	    len=10;
	else if (len == 30)
	    len=20;
	else
	    len=999999999;
	for (;len>0;len--) {
	    Random r = new Random();
	    int nextgoon = r.nextInt(3);
	    h1 = new Homework("Evil Homework", p1.getLevel());
	    c1 = new Teacher("English Teacher", p1.getLevel());
	    if (nextgoon != 2) {
		System.out.println(c1.getStats());
		System.out.println(p1.getStats());
		try {
		    Thread.sleep(1000);
		} catch(InterruptedException ex) {
		    Thread.currentThread().interrupt();
		}
		e.encounter(p1,c1);
		try {
		    Thread.sleep(1000);
		} catch(InterruptedException ex) {
		    Thread.currentThread().interrupt();
		}
	    }
	    else {
		System.out.println(h1.getStats());
		System.out.println(p1.getStats());
		try {
		    Thread.sleep(1000);
		} catch(InterruptedException ex) {
		    Thread.currentThread().interrupt();
		}
		e.encounter(p1,h1);
		try {
		    Thread.sleep(1000);
		} catch(InterruptedException ex) {
		    Thread.currentThread().interrupt();
		}
	    }
	}
    }
}
