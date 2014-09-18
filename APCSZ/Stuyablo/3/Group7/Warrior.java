import java.util.*;
import java.io.*;

public class Warrior extends Character {
    String name = new String();
    Scanner sc = new Scanner(System.in);

    public Warrior(String n){
	name = n;
	dexterity = 10;
	strength = 15;
	maxhealth = 50;
	experience = 10;

    }

    public void attack(Character other){
	Random r = new Random();
	int rollDie = r.nextInt(18)+1;


	if (rollDie <= dexterity){
	  
	    System.out.println(name + " attacked and hit the enemy!");
	    experience = experience + 1;
	    other.health = other.health -1;
	    if (experience == 15){
		maxhealth = maxhealth + 5;
		experience = 10;
		strength = strength +1;
		dexterity = dexterity +1;
        
	    }
	}
	else {
	    System.out.println(name + " missed!");
	
		}
    }

    public boolean flee(Character other){
	Random r = new Random();
	int rollDie = r.nextInt(18) +1;
	if(rollDie <= dexterity){
	    
	    experience = experience - 1;
	    maxhealth = maxhealth -5;
	    System.out.println(name + " fled. Cowardly actions have decreased EXP.");
	    return true;

	}
	else {
	    System.out.println(name + " failed to flee.");
	    return false;
	}
    }


    public int encounter(Character other){
	if (other.flee(this)){
	    experience = experience -1;
	    if(experience == 15){
		maxhealth = maxhealth + 5;
		experience = 10;
		strength = strength +1;
		dexterity = dexterity +1;
	    }
	}
	else if (other.strength>=this.strength || other.health>=this.health) {
            if (flee(other))
                return 1;
                    }
        this.attack(other);
        if (other.health > 0)
            other.attack(this);
        if (health == 0)
            return 2;
        else if (other.health == 0)
            return 3;
        else if (health == 0 && other.health == 0)
            return 4;
        else
            return 5;
	
    }
    
    public int getHealth() {
	return health;
    }
}
