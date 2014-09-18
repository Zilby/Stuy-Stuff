import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxhealth;
    protected int dexterity, strength, intelligence;
    protected int experience, level, experienceneeded; 
    protected int gold;      
    protected double x,y,distance;
    protected String name;
    protected String charClass;
 
    public int getHealth() {
	return health;
    }

    public int getLevel() {
	return level;
    }

public Character() {
	name = "DefaultName";
	dexterity = 8;
	strength = 8;
	intelligence = 8;
	Random r = new Random();
	x = r.nextInt(8);
	y = r.nextInt(14);
	//I think we are in a grid of 8x14?
	maxhealth = 4 * strength;
	health = maxhealth;
	experienceneeded = 10;
	level = 1;
}

public int[] getStat() {
	int[] stat = new int[3];
	stat[0] = dexterity;
	stat[1] = strength;
	stat[2] = intelligence;
	return stat;
}

public double[] getxy() {
	double[] d = new double[2];
	d[0] = x;
	d[1] = y;
	return d;
}

public void distance(Character other) {
	double[] d = other.getxy();
	//we will use taxicab distance
	double dist = x - d[0] + y - d[1];
	if (dist < 0)
	    distance = -1 * dist;
	else
	    distance = dist;
}

public void damage(int str) {  
	if (health >= str)
		health = health - str;
	else {
		health = 0;
		System.out.println(this + " died from this battle.");
	}
}

    /* You have to provide other needed get/set methods */


public void attack(Character other) {
	System.out.println(getStatus());
	System.out.println(other.getStatus());
	try {
	    Thread.sleep(2000);
	} catch(InterruptedException ex) {
	    Thread.currentThread().interrupt();
	}
	
/* do the attack:
	   print out the attempt and the result and update
	   all relavent variables
	*/
	Random r = new Random();
	int roll = r.nextInt(16) + 3;
	if (health == 0) {
		System.out.println(name + " died.");
	}
	else {
	if (dexterity >= roll) {
	    other.damage(strength);
	    System.out.println(name + " has dealt " + strength + " damage to the enemy!");
	    System.out.println("----------------------------------------------------------------");
	}
	else {
		System.out.println(name + " has missed!");
		System.out.println("----------------------------------------------------------------");
	}
	}
}

    // returns true if you succesfully flee, false otherwise
public boolean flee(Character other) {
	Scanner s = new Scanner(System.in);
	System.out.println("Will " + name +" fight? \n1. Yes\n2. No");
	int i = s.nextInt();
	if (i == 1) {
		System.out.println(name + " ran away! \n\n");
		System.out.println("----------------------------------------------------------------");
		return true;
	}
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

    */
    public int encounter(Character other) {
    	System.out.println(getStatus());
    	System.out.println(other.getStatus());
    	try {
    	    Thread.sleep(2000);
    	} catch(InterruptedException ex) {
    	    Thread.currentThread().interrupt();
    	}
    	boolean b1 = other.flee(this);
	if (b1 == true) {
		level(3);
		gold = gold + 10;
		return 0;
	}
	boolean b2 = flee(other);
	if (b2 == true) {
		return 1;
	}
	else {
		System.out.println("----------------------------------------------------------------");
		System.out.println("Engaging in a battle - distance = " + distance);
		while(health > 0 && other.getHealth() > 0) {
		this.attack(other);
		other.attack(this);
		}
		if (other.getHealth() <= 0 && health <= 0)
			return 4;
		if (health <= 0)
		return 2;
		if (other.getHealth() <= 0) {
			level(15);
			gold = gold + 100;
			return 3;
		}
		else
			return 5;
	}

}

public void level(int exp) {
	experience = experience + exp;
	if (experience > experienceneeded) {
		level = level + 1;
		System.out.println(name + " leveled up to level " + level + "! \nWhere would you like to spend your ability point? \n1. Dexterity \n2. Strength \n3. Intelligence");
		
	
	Scanner s = new Scanner(System.in);
	int i = s.nextInt();
	if (i == 1) {
		dexterity = dexterity + 1;
		experienceneeded = experienceneeded + 5 * (level - 1);
	} else {
	    if (i == 2) {
		strength = strength + 1;
		experienceneeded = experienceneeded + 5 * (level - 1);
	    }
	    else {
		intelligence = intelligence + 1;
		experienceneeded = experienceneeded + 5 * (level - 1); /*Increases exp needed to level up by 5 per level, so it's 10, 15, 25, 40, 60 Consider that you get 10 exp + enemies health per each kill.*/
	    }
	}
	maxhealth = 4 * strength;
	health = maxhealth; //health regeneration
	}
	

} 

    public String getStatus() {
    String slevel= "Level = " + level ;
	String attrib1=String.format("Str: %d Dex: %d Int: %d",
				     strength, dexterity, intelligence);
	String attrib2=String.format("Exp: %d Health: %d of %d",
				     experience,health,maxhealth);
	String locale = String.format("x: %5.2f y: %5.2f",x,y);
	String whole=String.format("%s\n%s\n%s\n%s\n%s\n",
				   name,slevel,attrib1,attrib2,locale);
	return whole;
    }


    public String toString() {
	return name;
    }
    
 
    public int play(Character other) {
    	distance(other);
        int playmore= -1;
        while (health>0) {
            playmore = encounter(other);
            if (playmore !=1 || playmore !=2 || playmore !=3 || playmore !=4 ||playmore !=5) {
            	return playmore;
            }
            if (playmore == 3 )
            	System.out.println(name + " won the battle!");
            if (playmore == 4 )
            	System.out.println("Both died.");
          
        }
    	try {
    	    Thread.sleep(2000);
    	} catch(InterruptedException ex) {
    	    Thread.currentThread().interrupt();
    	}
        return -1;
    }
    
}
