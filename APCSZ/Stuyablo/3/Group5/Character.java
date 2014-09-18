import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxhealth;
    protected int dexterity, strength, intelligence;
    protected int experience,expBase, expReq, level; //added instance v's for leveling/experience -A
    protected String name;
    protected String charClass;

    public Character(){
	strength = 8;
	dexterity = 8;
	intelligence = 8;
	experience = 0;
	level = 1;
	expBase = 50;
	maxhealth = strength;
	health = maxhealth;
    }

    public void CharacterS(){
	Scanner s = new Scanner(System.in);
	System.out.println("Hello. Please enter your name to go on this mystical adventure.");
	name = s.nextLine();
	System.out.print(name + ", do you prefer being a student or a warrior? Type '1' for student, '2' for warrior.");
	System.out.println();
	int player = s.nextInt();
	if (player == 1){
	    Student student = new Student(name);
	    System.out.println();
	    System.out.println("Hello Student " + name + "!");
	    System.out.println("You have 8 points to allot to either strength or dexterity. Please type and number between 0 and 8.");
	    System.out.println("This number will be added to your strength. This number subtracted from 8 will be added to dexterity.");
	    Scanner in = new Scanner(System.in);
	    int addToStrength = in.nextInt();
	    while (addToStrength>8 || addToStrength<0) {
		System.out.println("Please enter a value between 0 and 8.");
	    }
	    int addToDex = 8-addToStrength;
	    strength = strength + addToStrength;
	    dexterity = dexterity + addToDex;
	}
	else if (player == 2){
	    Warrior w = new Warrior(name);
	    System.out.println();
	    System.out.println("Hello Warrior " + name + "!");
	    System.out.println("You have 8 points to allot to either strength or dexterity. Please type and number between 0 and 8.");
	    System.out.println("This number will be added to your strength. This number subtracted from 8 will be added to dexterity.");
	    Scanner in = new Scanner(System.in);
	    int addToStrength = in.nextInt();
	    while (addToStrength>8 || addToStrength<0) {
		System.out.println("Please enter a value between 0 and 8.");
	    }
	    int addToDex = 8-addToStrength;
	    strength = strength + addToStrength;
	    dexterity = dexterity + addToDex;
	}
	else {
	    System.out.println("Silly " + name + ", that's not a choice! NOW YOU HAVE TO START OVER >:(");
	    CharacterS();
 	}
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

    public int getLevel() {
	return level;
    }

    public int roll() {
	Random r = new Random();
	int die1 = r.nextInt(6) + 1;
	int die2 = r.nextInt(6) + 1;
	int die3 = r.nextInt(6) + 1;
	return die1 + die2 + die3;
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



    // returns true if you succesfully flee, false otherwise
    public boolean flee() {
	int roll = this.roll();
	if (roll < this.dexterity && roll%2==0)
	    return true;
	else
	    return false;
    }

    /*
      this routine will decide first ask if other tries to flee. If
      so, and if it's succesful it should adjust experience and or
      gold as needed and return a 0.

      Then, it should decide if this character tries to flee. 
      If so and it's succesful, return a 1;
      
      Otherwise, call attack on both sides:
      this.attack(other);
      if (other.health>0) 
      other.attack(this);

      and then return 2 if this is dead, 3 if other is dead, 4 if both dead, 5 if none dead.

      (they would never be both dead.)
    */

    //Encounter: if other decides to flee, this gets experience, and encounter ends... if this decides to flee, other gets experience and encounter ends... otherwise, fight fight fight!! -A
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
		    if (this.health<0){
			System.out.println("Killed by thunder. Good job.");
			return 2;
		    }
		}
		else {
		    System.out.println("Killed by thunder. Good job.");
		    return 2;
		}
	    }
	    return 5;
	}
    }

    public void experience(){
	experience += 10;
    }

    //50 * 1.1 * 1.1 * 1.1 *1.1 * 1.1

    public void level(){
	if (experience >= expReq){
	    level ++;
	    expReq = (int)(Math.pow(1.1, level - 1) * expBase);
	    experience = 0;
	    strength += 2;
	    dexterity +=2;
	    maxhealth += 2;
	    health += 2;
	    
	}
    }

    public String getStatus() {
	String attrib1=String.format("Str: %d Dex: %d Int: %d",
				     strength, dexterity, intelligence);
	String attrib2=String.format("Exp: %d Health: %d of %d",
				     experience,health,maxhealth);
	String whole=String.format("%s\n%s\n%s\n",
				   name,attrib1,attrib2);
	return whole;
    }


    public String toString() {
	return name;
    }
    
}


//hey guys! finished Character and added attack() and combat(); these are generic methods so feel free to change them for specific classes! -Angela
