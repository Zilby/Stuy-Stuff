import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxHealth;
    protected int dexterity, maxDex, strength, maxStr, intelligence, maxInt;
    protected int experience;
    protected int gold;
    protected double x,y,distance;
    protected String name;
    protected String charClass;
 
    public String toString() {
	return name;
    }

    public void wait(int millsecs) { //our dramatic pausing functionality.
	try {
	    Thread.sleep(millsecs); 
		}
	catch (Exception e){/*do nothing*/}
    }
    

    public String multStr(String str, int times){
	String ans;
	ans = "";
	for (int i = 0; i < times; i++) {
	    ans = ans + str;
	}
	return ans;
    }

    public void greet() {
	Scanner sc = new Scanner(System.in);
	System.out.println("What is your name, warrior?");
	String name = sc.nextLine();
	this.name = name;
    }
    //Get Methods
    public int getHP() {
	return health;
    }
    public int getDex() {
	return dexterity;
    }
    public int getStr() {
	return strength;
    }
    public int getInt() {
	return intelligence;
    }
    public int getExp() {
	return experience;
    }

    //Set Methods

    public void setDex(int x) {
	this.dexterity=x;
    }
    public void setStr(int x) {
	this.strength =x;
    }
    public void setInt(int x) {
	this.intelligence=x;
    }
    public void setExp(int x) {
	this.experience=x;
    }
    public void setHP(int x) {
	this.health = x;
    }
   

    public void getStatus() {
	System.out.println(this + "'s Stats:");

	System.out.print("Health: "+ this.getHP()); 
	// multStr("*",Math.round((this.getHP()/this.maxHealth)*100.0));  
	System.out.println("(" + (((this.getHP()*1.0)/(this.maxHealth*1.0))*100.0) + "%)");

	System.out.print("Strength: "+ this.getStr());
        //System.out.print(multStr("x",Math.round((this.getStr()/this.maxStr)*100)));
	System.out.println("(" + (((this.getStr()*1.0)/(this.maxStr*1.0))*100.0) + "%)");

	System.out.print("Dexterity: "+ this.getDex());
        //System.out.println(multStr("x",Math.round((this.getDex()/this.maxDex)*100))); 
	System.out.println("(" + (((this.getDex()*1.0)/(this.maxDex*1.0))*100) + "%)");
	System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~");
    }

    public void attack(Character other) {
        Random r = new Random();

	int dice1 = r.nextInt(6);
	int dice2 = r.nextInt(6);
	int dice3 = r.nextInt(6);

	if (dice1 + dice2 + dice3 > this.getDex()) {
	    System.out.println(this + " successfully strikes a blow on " + other + "!\n");
	    int damage = 1; //This may be changed later as we get into weapons and such.
	    other.health = other.getHP() - damage;
	}
	else {
	    System.out.println(this + " missed!!\n");
	}
    }

    public boolean flee(Character other) {
        Random r = new Random();
	if (r.nextDouble() < .1) {
	    return true;
	}
	else {
	    return false;
	}
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
      and then return 2 if this is dead, 3 if other is dead, 4 if both dead, 5 if none dead. */

    public int encounter(Character other) {
	Scanner sc = new Scanner(System.in);
	System.out.println("Beware, " + name + ", this forest is filled with monsters!");
	wait(400);
	System.out.println("You have encountered an " + other);
	wait(800);
	this.getStatus();
	wait(800);
	other.getStatus();
	wait(800);
	if (other.flee(this)) { 
	    System.out.println(other + " has escaped!");
	    return 0;
	}
	
	System.out.println("Do you want to try to escape?");
	System.out.println("y - yes \nn - no");
	String choice = sc.nextLine();
	if (choice.equals("y")) {
	    if (this.flee(other)) {
		System.out.println("You have escaped safely...this time");
		return 1;
	    }
	    else {
		System.out.println("Uh oh! " + other + " sees you! You can't get away!");
		wait(300);
		    }
	}
        return battle(other);
    }

    public int battle(Character other) {
	
	System.out.println("What do you want to do?");
	System.out.println("a - attack \nf - flee");

	Scanner sc = new Scanner(System.in);
	String move = sc.nextLine();
	
	if (move.equals("f")) {
	    if (this.flee(other)) {
		System.out.println("You successfully fled from the battle!");
		return 1;
	    }
	}

	if (move.equals("a")) {
	    this.attack(other);
	    wait(1500);
	    if (other.health > 0) {
		other.attack(this);
		wait(1500);
	    }
	}
	
	System.out.println("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n\n\n");
	this.getStatus();
	other.getStatus();

	if ((this.health == 0) && (other.health == 0)) {

	    System.out.println("Both you and " + other + " have died"); 
	    return 4;
	}
	else if (other.health == 0) {
	    System.out.println(other + " has died! \n You Win!! \n \n \n");
	    return 3;
	}
	else if (this.health == 0) {
	    System.out.println("You have died!");
	    return 2;
	}
	else {
	    return battle(other);
	}
    }
}
