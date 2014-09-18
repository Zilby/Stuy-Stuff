import java.util.*;
import java.io.*;

public class Human extends Character {

    public Human (String name) {
	super(name);
    }

     public boolean flee() {
	 boolean result = true;
	 Scanner sc = new Scanner(System.in);
	 System.out.println("Would you like to flee? Please answer YES or NO.\n");
	 String response = sc.nextLine();
	 /*
	 while (response != "YES" && response != "NO") {
	     System.out.println("Sorry, this is not a valid answer. Please try again.\n");
	     response = sc.nextLine();
	 }
	 */
	 if (response == "YES") {
	     int roll = this.roll();
	     if (roll < this.dexterity && roll%2==0) {
		     result = true;
	     }
	     else {
		     result = false;
	     }
	 }
	 else if (response == "NO") {
	     result = false;
	 }
	 return result;
    }

    public void attack (Character other) {
	Random r = new Random();
	int random = r.nextInt(100);
	if (random > 50) {
	    other.health = other.health - 1;
	}
    }
}


	

    
