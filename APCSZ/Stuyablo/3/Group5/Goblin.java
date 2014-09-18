import java.util.*;
import java.io.*;
//Yay for Goblins! -Angela
public class Goblin extends Character {
  
    public Goblin(String nameGob){
	Random r = new Random();
	int strengthAdd = r.nextInt(3);
	int dexAdd = 4 - strengthAdd;
	strength = 4 + strengthAdd;
	dexterity = 4 + dexAdd;
	maxhealth = strength;
	health = maxhealth;
	experience = 0;
	name = nameGob;
	level = 1;
	expBase = 50;
    }

    public void attack(Character other) {
	int dice = roll();
	int attackDmg =(int) (strength / 3);
	if (dexterity <= dice){
	    try {
		Thread.sleep(1500);
	    } catch(InterruptedException ex) {
		Thread.currentThread().interrupt();
	    }
	    System.out.println(name + " successfully slapped " + other);
	    if (attackDmg > other.health)
		other.health = 0;
	    else
		other.health = other.health - attackDmg;
	}
	else {
	    try {
		Thread.sleep(1500);
	    } catch(InterruptedException ex) {
		Thread.currentThread().interrupt();
	    }
	
	    System.out.println(name + " failed to slap " + other);
    	}
    }
	   
}
