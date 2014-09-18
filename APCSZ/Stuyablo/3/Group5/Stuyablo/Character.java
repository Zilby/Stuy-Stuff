import java.util.*;
import java.io.*;
 
public class Character {

    protected int health, maxhealth;
    protected int dexterity, strength, intelligence;
    protected int experience;
    protected String name;
    protected String charClass;

    public Character(String name, int dexterity, int strength, int intelligence) {
	this.dexterity = dexterity;
	this.strength = strength;
	this.intelligence = intelligence;
	this.health = strength;
	this.maxhealth = 32;
    }

    public Character(String name) {
	dexterity = 8;
	strength = 8;
	intelligence = 8;
	health = 8;
	maxhealth = 32;
    }

    public String getName() {
	return name;
    }

    public int getHealth() {
	return health;
    }

    public int getDexterity() {
	return dexterity;
    }

    public int getStrength() {
	return strength;
    }

    public int getIntelligence() {
	return intelligence;
    }

    public int roll() {
	Random r = new Random();
	int die1 = r.nextInt(6) + 1;
	int die2 = r.nextInt(6) + 1;
	int die3 = r.nextInt(6) + 1;
	return die1 + die2 + die3;
    }

    public void attack(Character other) {
	/*return "Generic Attack"*/ 
    }

    public boolean flee() {
	int roll = this.roll();
	    if (roll < this.dexterity && roll%2==0) {
		return true;
	    }
	    else {
		return false;
	    }
    }

    public int turn(Character other) {
	int r = 0; /*this variable represents the end result of the turn.*/
	boolean otherflee = other.flee(); /*OTHER tries to flee. The variable indicates if that flee was successful.*/ 
	if (otherflee == true) {
	    r = 0; /*if OTHER flees successfully, the result is that OTHER gets away and the encounter ends (represented by 0).*/
	}
	else {
	    boolean thisflee = this.flee(); /*if OTHER does not flee, THIS has the chance to flee. The variable indicates if that flee is successful.*/
	    if (thisflee == true) {
		r = 1; /*if THIS flees successfully, the result is that THIS gets away and the encounter ends (represented by 1).*/
	    }
	    else {
		this.attack(other); /*if THIS does not flee, THIS attacks.*/
		if (other.health > 0) {
		    other.attack(this);/*if OTHER is not killed by THIS's attack, OTHER attacks.*/
		}
	        if (this.health == 0) {
		    r = 2;/*if THIS is dead, the encounter ends(represented by a 2).*/
		}
		if (other.health == 0) {
		    r = 3;/*if OTHER is dead, the encounter ends (represented by a 3).*/
		}
		if (this.health > 0 && other.health > 0) {
		    r = 4;/*if both characters are still alive, the encounter can continue (represented by a 4).*/
		}
	    }
	}
	return r;
    }

    public String encounter(Character other) {
	String result = "";
	int r = 4;
	while (r == 4) {
	    r = turn(other);
	    if (r == 0) {
		result += other.getName() + " has fled. Encounter has ended.\n";
	    }
	    else if (r == 1) {
		result += "You have fled. Encounter has ended.\n";
	    }
	    else if (r == 2) {
		result += "You are dead. Sucks for you.\n";
	    }
	    else if (r == 3) {
		result += "You have killed " + other.getName() + ". Congratulations!\n";
	    }
	    else {
		result += "Both players are alive. The encounter continues!\n";
	    }
	}
	return result;
    }
 
    /*
    public String getStatus() {
	attrib1=String.format("Str: %d Dex: %d Int: %d",
			      strength, dexterity, intelligence);
	String attrib2=String.format("Exp: %d Health: %d of %d",
				     experience,health,maxhealth);
	String locale = String.format("x: %5.2f y: %5.2f",x,y);
	String whole=String.format("%s\n%s\n%s\n%s\n",
				       name,attrib1,attrib2,locale);
	return whole;
    }

    */
 
    public String toString() {
	return name;
    }
}
