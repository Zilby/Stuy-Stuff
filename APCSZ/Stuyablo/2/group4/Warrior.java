import java.io.*;
import java.util.*;

public class Warrior extends Character {


    public Warrior(String n){  //Constructor to set up crap
	name=n;
	health = 8;
	strength = 8;
	intelligence = 8;
	dexterity = 8;
    }
    
    public void attack(Character other) {
        Random r= new Random();
        int roll=r.nextInt(18); /*three six-sided die roll implementation by Matthew*/
        if ( 2*roll < dexterity) {
            System.out.println("IT'S SUPER EFFECTIVE!!!");
            health = health - (other.getStr() * 2);
        }
        else if (roll < dexterity) {
            System.out.println("A hit!");
            health = health - other.getStr();
            /* do the attack:
               print out the attempt and the result and update
               all relavent variables
            */
        }
        else {
            System.out.println("A miss...");
	    
	    
	    
	}
	
    }
}