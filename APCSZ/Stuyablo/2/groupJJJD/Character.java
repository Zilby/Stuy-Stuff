import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxhealth;
    protected int dexterity, strength, intelligence; 
    //dexterity will be our accuracy, intelligence will be bonus hit (crit) and flee factor - jamesc
    protected int experience;
    protected int gold;
    protected double x,y,distance;
    protected String name;
    protected String charClass;
    protected int roll;

    protected int level;
	protected double dmg; 

 
    public void rollDice() { //a method to use roll the dice -jamesc
	Random r = new Random();
	roll = r.nextInt(18);
	
	}
	
	public Character(String name, int strClass, int dexClass, int intClass) {
	//this will be our base but all the parameters will be specific to each race/class - jamesc
	this.name = name;
	this.strength = 8 + strClass;
	this.dexterity = 8 + dexClass;
	this.intelligence = 8 + intClass; 
	this.health = this.strength;
	this.maxhealth = this.strength;
	this.experience = 0;
	this.level = 1;
	
	
    }
	
	
	
    public int getHealth() {
	return health;
    }

    /* You have to provide other needed get/set methods */

	public void calcDmg() {
	
	dmg = (((2 * this.level / 5 + 2) * (this.intelligence/2) * this.strength) / 50);
	
	
	}

    public void attack(Character other) {
    rollDice();
    if (roll > this.dexterity) {
    
    other.health = other.health - (int)this.dmg;
    /*System.out.println(this.toString() + "'s Health: " + this.health);
    System.out.println(other.toString() + "'s Health: " + other.health);
    System.out.println(this.toString() + "'s Damage: " + this.dmg);
    System.out.println(other.toString() + "'s Damage: " + other.dmg);*/
    }
    
    }
	/* do the attack:
	   print out the attempt and the result and update
	   all relavent variables
	*/
    

    // returns true if you succesfully flee, false otherwise
    public boolean flee(Character other) {
   
   if (this.intelligence >= other.intelligence) {
    return true;
    }
    
    else return false;
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

    */
   public int encounter(Character other) {
    //random if other flees, for now, other never flees
	
	Scanner sc = new Scanner(System.in);
	System.out.println("Do you want to flee? y/n");
	String flee = sc.nextLine();
	if (flee.equals("y")) {
	    if (flee(other) == true) {
		System.out.print("You have fled"); 
		return 1;   	
	    }
	}
    Scanner at= new Scanner(System.in);
    while (health>0 && other.health>0){
	System.out.println("Choose your attack ( Press 1 Its all you know) ");
	String att= sc.nextLine();
	    if (att.equals("1")){
		this.attack(other);
		if (other.health > 0) {
		    other.attack(this);
		}	
  	    }	
   	    	    System.out.println("Your current Health : " +this.health);
	    System.out.println("His current Health : " + other.health);}
    return 0;
    }
    


    public String getStatus() {
	String attrib1=String.format("Str: %d Dex: %d Int: %d",
				     strength, dexterity, intelligence);
	String attrib2=String.format("Exp: %d Health: %d of %d",
				     experience,health,maxhealth);
	String locale = String.format("x: %5.2f y: %5.2f",x,y);
	String whole=String.format("%s\n%s\n%s\n%s\n",
				   name,attrib1,attrib2,locale);
	return whole;
    }


    public String toString() {
	return name;
    }
    
    }
    

