import java.io.*;
import java.util.*;

public class Moran extends Character{
<<<<<<< HEAD
    public Moran (String name, int strClass, int dexClass, int intClass){
	super(name, strClass, dexClass, intClass);
=======
>>>>>>> 76969bd48d11c1c583b9cda7774cdeda829b3aee

    public Moran (String s, int i, int j, int k){
        Random r = new Random();
        int a = r.nextInt(2) + 5;
        strength = a;
        health= strength;
        maxhealth=strength;
        dexterity= 4;
        intelligence = 8;
        
    }
    
    public String toString(){
<<<<<<< HEAD
	return super.toString() + " the Moran";

    }

 public void attack(Character other2){
	rollDice();
	if (roll > this.dexterity) {
	    
	    other2.health = other2.health - ((int)this.dmg+2);
	//Warriors do more dmg
	    System.out.println(this.toString() + " rages at " + other2.name + " and steals his phone");
	    }
	
}}
=======
        return super.toString() + " the Mister";
    }

    public void attack(Character other) {
	rollDice();
	if (roll > this.dexterity) {
	    other.health = other.health - (this.dmg + 1);
	    System.out.println("Mr. Moran descends to interrogate!");
	    System.out.println(this.toString() + "'s Health: " + this.health);
	    System.out.println(other.toString() + "'s Health: " + other.health);
	    System.out.println(this.toString() + "'s Damage: " + this.dmg);
	    System.out.println(other.toString() + "'s Damage: " + other.dmg);
	}
                
    }
}
>>>>>>> 76969bd48d11c1c583b9cda7774cdeda829b3aee
