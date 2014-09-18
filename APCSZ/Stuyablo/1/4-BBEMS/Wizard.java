import java.io.*;
import java.util.*;


public class Wizard extends Character {
    protected int spelldamage;
    protected int boostcount;


    public Wizard () {
	super.setCharacterClass ("Wizard");
	spelldamage = 0;
	boostcount = 0;
    }

    public Wizard (String name) {
	super (name, "Wizard");
	boostcount = 0;
	spelldamage = 0;
    }

    /* Sorry man, I'm not sure how to deal with this at the moment. 

    public void attack (Character other){
	if (freezecount == 0) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Do You Want To");
	    System.out.println("Cast");
	    System.out.println("Attack");
	    String option = sc.next();
	    if (option.equals("Cast") || option.equals("cast")) {
		System.out.println("Select the spell you want to use");
		System.out.println("1. Fireball");
		System.out.println("2. Heal");
		System.out.println("3. Ice Storm");
		System.out.println("4. Power boost");
		System.out.println("5. Sleep");
		System.out.println("6. Final Flame");
		int spell = sc.nextInt();
		if (spell == 1) {
		    spelldamage = (this.intelligence + 7) - random.nextInt(4);
		    System.out.println(other.getName() + "was hit by a fireball");
		}
		else if (spell == 2) {
		    this.health = this.health + 30;
		    System.out.println(super.getName() + "cast heal");
		}
		else if (spell == 3) {
		    spelldamage = (this.intelligence) - random.nextInt(3);
		    System.out.println(other.getName() + "was hit by ice");
		    if (Math.random() < 0.4) {
			other.freezecount  = 2;
			System.out.println (other.getName() + "was frozen");
		    }
		}
		else if (spell == 4) {
		    this.intelligence = this.intelligence * 2;
		    this.boostcount = 2;
		    System.out.println(this.getName() + "has increased their intelligence");
		}
		else if (spell == 5) {
		    other.freezecount = 3;
		    System.out.println (other.getName() + "is asleep");
		}
		
		else if (spell == 6) {
		    spelldamage = this.intelligence * 3 - random.nextInt(10);
		    System.out.println (other.getName() + "has been hit by the final flame");
		}
		else {
		    System.out.println(spell);
		    System.out.println("Invalid spell, you will now perform a basic attack");
		}
	    }
	    else {
		spelldamage = this.strength;
	    }
	    other.health = other.health - spelldamage;
	}
	else {
	    System.out.println ("Your character is immobilized");
	}
	if (freezecount > 0) {
	    freezecount = freezecount - 1;
	}
	if (boostcount > 0) {
	    boostcount = boostcount - 1;
	}
	if (boostcount == 0) {
	    this.intelligence = this.intelligence / 2;
	    boostcount = boostcount - 1;
	}
    }

    */
}




