import java.util.*;
import java.io.*;

public class Warrior extends Character{
	
    public Warrior(String name) {
	this.name = name;
    }

    public void attack(Character other) {
	int dice = roll();
	int attackDmg =(int) (strength / 3);
	System.out.println("Dice roll:" + roll());
	if (dexterity >= dice){
	    System.out.println();
	    System.out.println("You succesfully attacked " + other.name);
	    if (attackDmg > other.health) {
		other.health = 0;
		System.out.println();
		System.out.println("You killed " + other.name);
	    }
	    else
		other.health = other.health - attackDmg;
	}
	else {
	    System.out.println();
	    System.out.println("Your attack failed.");
	}
    }

    //Encounter: if other decides to flee, this gets experience, and encounter ends... 
    //if this decides to flee, other gets experience and encounter ends... 
    //otherwise, fight fight fight!

    public int encounter(Character other) {
	Scanner in = new Scanner(System.in);
	if (other.flee() == true){
	    experience ++;
	    System.out.println(other + " has fled.");
	    System.out.println();
	    System.out.println(this.getStatus());
	    System.out.println();
	    System.out.println("Your level is: " + this.level);
	    return 0;
	}
	else {
	    System.out.println();
	    System.out.println("Do you wish to attempt to flee? (Type '1' to flee or '2' to fight.)");
	    System.out.println();
	    int fleeAttempt = in.nextInt();
	    if (fleeAttempt == 1) {
		if (this.flee() == true){
		    other.experience ++;
		    System.out.println();
		    System.out.println("You have succesfully fled.");
		    return 1;
		}
		else {
		    System.out.println();
		    System.out.println("You were unable to flee.");
		    if (other.health > 0){
			other.attack(this);
			System.out.println();
			System.out.println("Your current health: " + this.health);
			System.out.println(other + "'s current health: " + other.health);
			System.out.println();
			System.out.println("~~~~~~~~~~~~~~~~");
			System.out.println();
			if (this.health <= 0) {
			    try {
				Thread.sleep(2000);
			    } catch(InterruptedException ex) {
				Thread.currentThread().interrupt();
			    }
			    System.out.println("You were defeated. You are dead :(");
			    other.experience();
			    other.level();
			    return 2;
			}
		    }
		    else {
			System.out.println(other + " was defeated. Victory is yours!");
			this.experience();
			this.level();
			System.out.println(this.getStatus());
			System.out.println("Level: " + this.level);
			return 3;
		    }
		}
	    }
	    else if (fleeAttempt == 2){
		System.out.println("You will now attack " + other +"!");
		this.attack(other);
		System.out.println();
		System.out.println("Your current health: " + this.health);
		System.out.println(other + "'s current health: " + other.health);
		System.out.println();
		System.out.println("~~~~~~~~~~~~~~");
		System.out.println();
		if (other.health > 0){
		    other.attack(this);
		    System.out.println();
		    System.out.println("Your current health: " + this.health);
		    System.out.println(other + "'s current health: " + other.health);
		    System.out.println();
		    System.out.println("~~~~~~~~~~~~~~~~");
		    System.out.println();
		    if (this.health <= 0) {
			try {
			    Thread.sleep(2000);
			} catch(InterruptedException ex) {
			    Thread.currentThread().interrupt();
			}
			System.out.println("You were defeated. You are dead :(");
			other.experience();
			other.level();
			return 2;
		    }
		}
		else {
		    System.out.println(other + " was defeated. Victory is yours!");
		    this.experience();
		    this.level();
		    System.out.println(this.getStatus());
		    System.out.println("Level: " + this.level);
		    return 3;
		}
	    }
	    else {
		if (this.health > 0){	
		    System.out.println("Invaild Choice");
		    System.out.println("YOU WILL BE STRUCK BY THUNDER FOR 5 HEALTH POINTS");
		    this.health = this.health - 5;;
		}
		else {
		    System.out.println("Killed by thunder. Good job.");
		    return 2;
		}
	    }
	    return 5;
	}
    }
}

