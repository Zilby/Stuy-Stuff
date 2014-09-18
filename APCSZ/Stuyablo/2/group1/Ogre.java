import java.io.*;
import java.util.*;

public class Ogre extends Character{
    Random r = new Random();

    public Ogre(){
	maxHealth = 16;
	name = "Angry Ogre";
	health = maxHealth - r.nextInt(4);
	strength = health;
	dexterity = 8 - r.nextInt(4);
	exp = 25;
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
