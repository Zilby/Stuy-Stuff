import java.io.*;
import java.util.*;

public class Undead extends Character{
    Random r = new Random();

    public Undead(){
        name = "The Lich King";
        maxHealth = 6 + r.nextInt(5);
        health = maxHealth;
        strength = maxHealth;
        dexterity = 8 - r.nextInt(5);
	intelligence = 8 + r.nextInt(5);
	exp = 15;
    }
    public void attack(Character other) {
	    	    
	    if(hit() == true){
		System.out.println("Hit!");
		other.takeDamage(this.strength/2);
	    }
	    else{
	        System.out.println("Just barely missed him!");
	    }
    }
}
