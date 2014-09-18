import java.io.*;
import java.util.*;

public class Wizard extends Character{
   public Wizard(String name, int strClass, int dexClass, int intClass) {
	super(name,strClass,dexClass,intClass);

	
    }
    
    public String toString() {
	return super.toString()+" the Wise";
    }
      public void attack(Character other2){
	rollDice();
	if (roll > this.dexterity) {
	    
	    other2.health = other2.health - ((int)this.dmg+50);
	//Wizards are broken and do stupid amounts of magic dog
	    System.out.println(this.toString() + " shoots a massive undodgeable fireball at " + other2.name + "");
	    }
	}
}