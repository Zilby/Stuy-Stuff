import java.util.*;
import java.io.*;

public class Elf extends Character{
	
	public Elf() {
		strength = 10;
		dexterity = 16;
		intelligence = 11;
		maxhealth = 10;
		health = 10;
	}

	public void attack(Character other) {
		int damage = strength; //this can change when range is dealt with
		Random r = new Random();
		int rollDie = r.nextInt(18) + 1;
		if (rollDie <= dexterity) {
			System.out.println("Elf successfully hit the attacker");
			//enemy loses health
		}
		else
			System.out.println("Elf missed!");
	}

    public boolean flee(Character other){
	Random r = new Random();
	int rollDie = r.nextInt(18) + 1;
	if (rollDie <= other.dexterity)
		return false;
	else
		return true;
	}

	public int encounter(Character other) {
		//need to figure out if other wants flee
		if (other.strength + other.dexterity > strength + dexterity) {
			if (flee(other))
				return 1;
		}
		this.attack(other);
		if (other.health > 0)
			other.attack(this);
		if (health <= 0 || other.health <= 0) {
			if (other.health > 0)
				return 2;
			else if (health > 0)
				return 3;
			else
				return 4;
		}
		else
			return 5;
	}
		

    public int getHealth(){
	return health;
    }



	


}