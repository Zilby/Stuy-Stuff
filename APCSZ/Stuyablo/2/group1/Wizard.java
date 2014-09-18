import java.io.*;
import java.util.*;

public class Wizard extends Character{
    protected int mana;
    protected Random r = new Random();

    public Wizard(String Name) {
	name = Name;
	setStat(8);
	health = maxHealth = strength;
	mana = intelligence;
	System.out.println("Strength: " + strength);
	System.out.println("Dexterity: " + dexterity);
	System.out.println("Intelligence: " + intelligence);
	System.out.println("-------------------------------");
    }

    public void basic(Character other) {
	System.out.println("-------------------------------");
	if(hit()==true) {
	    int tempStrength = strength - r.nextInt(5);
	    System.out.println("You hit the " + other + " for " + tempStrength + " damage!");
	    other.takeDamage(tempStrength);
	}
	else {
	    System.out.println("You swing at the " + other + " but miss!");
	}
    }
    
    public void throwFireball(Character other) {
	System.out.println("-------------------------------");
	if(mana >= 2) {
	    mana -= 2;
	    if(hit()==true) {
		int tempStrength = strength + r.nextInt(2);
		System.out.println("You cast an orb of flame at the " + other + " for " + tempStrength + " damage!");
		other.takeDamage(tempStrength);
	    }
	    else {
		System.out.println("Your fireball sputters out before you can throw it.");
	    }
	    System.out.printf("You have %d mana left",mana);
	}
	else
	    System.out.println("You don't have enough mana");
    }

    public void wHeal() {
	System.out.println("-------------------------------");
	if(mana >= 1) {
	    mana -= 1;
	    if(hit()==true) {
	        System.out.println("You heal yourself");
		health += 3;
		if(health > maxHealth) health = maxHealth;
		    System.out.println("You now have " + health + "health");
	    }
	    else
	        System.out.println("You try to heal yourself, but fail");
	}
	else
	    System.out.println("You have no mana");
    }

    public void attack(Character c) {
	/*Scanner s = new Scanner(System.in);	
	System.out.println("You can:\n  1:Whack it with your staff\n  2:Throw a fireball\n  3: Cast 'heal'\n  4:  Flee");
	switch(s.nextInt()){
			case 1:
				basic(c);
				
			case 2:
				throwFireball(c);
				
			case 3:
				heal();
			case 4:
				flee();
				
			default:
				System.out.println("Invalid command, try again");
	*/
	Scanner sc = new Scanner(System.in);  
	System.out.println("\nYou can:\n  1: Whack it with your staff\n  2: Throw a fireball\n  3: Cast 'heal'");
	String input = sc.nextLine();
	if (input.equals("1"))
	    basic(c);
	else if (input.equals("2"))
	    throwFireball(c);
	else if (input.equals("3"))
	    wHeal();
	else
	    System.out.println("Invalid command, try again");
    
    }
}
