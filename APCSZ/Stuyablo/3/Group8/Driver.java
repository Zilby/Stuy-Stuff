import java.util.*;
import java.io.*;

public class Driver {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	Character c = new Character();

        System.out.println("Welcome to Stuyablo!");
	c.wait(1000);
	System.out.print("Would you like to play? (y/n) ");
	String ans = sc.nextLine();
	while (ans.equals("y") == false && ans.equals("n") == false) {
	    System.out.print("Wrong answer! Try again (y/n): ");
	    ans = sc.nextLine();
	}
        if (ans.equals("n")) {
	    System.out.println("Goodbye!");
	    System.exit(1);
	}
	
	System.out.print("Would you like to be a Warrior or a Wizard? ");
	ans = sc.nextLine();
	while (ans.equals("Warrior") == false && ans.equals("Wizard") == false) {
	    System.out.print("Wrong answer! Try again: ");
	    ans = sc.nextLine();
	}
	if (ans.equals("Warrior")) {
	    Warrior w = new Warrior();
	    c = w;
	    System.out.println(w.getStatus());
	} else {
	    Wizard w = new Wizard();
	    c = w;
	    System.out.println(w.getStatus());
	}

	NPC n = new NPC();
	c.wait(1000);
	System.out.println("Alright! Let's begin!");
	c.wait(2000);
	System.out.println("\nYou have encountered an enemy!");
	int x = c.encounter(n);
	if (x == 1) 
	    System.out.println("You fled!");
	else if (x == 2)
	    System.out.println("You died!");
	else if (x == 3)
	    System.out.println("You won!");
	else
	    System.out.println("You both died!");
		
 
    }
}
