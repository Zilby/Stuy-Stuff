import java.io.*;
import java.util.*;

public class Thief extends Character{
    Scanner sc1 = new Scanner (System.in);
    public Thief (){
	Random r = new Random();
	int extrapts = 8;
	int str = r.nextInt(extrapts+1);
	extrapts = extrapts - str;
	int dex = r.nextInt(extrapts+1);
	extrapts = extrapts - dex;
	int intel = r.nextInt (extrapts + 1);
	setDexterity(12+dex);
	setIntelligence(8+intel);
	setStrength(4+str);
	setName("Dovah the Sly");
	setCharClass("Thief");
	setMaxHealth(strength);
	setHealth(strength);
    }

    public String toString(){
	return name;
    }

    public boolean flee (Character other){
	if(this.dexterity > other.dexterity){
	    return true;
	}else{
	    return false;
	}
    }

    public void Startup(){
	System.out.println("Created " + this + "(Thief).\nStatus:\n" + getStatus());
    }

    public void attack(Character other) {
	System.out.println(this + " tried to attack " + other + ".");
	boolean hitsuccess = this.roll();
	if (hitsuccess == false) {
	    System.out.println("Attack failed.");
	    System.out.println();
	}
	if (hitsuccess == true) {
	    int damage = strength * 2 / 3; // damage is approximately 2/3 that of strength
	    System.out.println("Attack succeeded.");
	    if (other.health <= damage) {
		other.health = 0;
		this.experience += other.experience;
		System.out.println(other + " defeated.  " + this + "'s experience increased by " + other.experience + " points.");
		System.out.println();
	    }
	    else
		other.setHealth(other.health - damage);
	    System.out.println(other + "'s health has decreased to " + other.getHealth());
	    this.experience += 1;
	    System.out.println(this + "'s experience increased by 1 point.");
	    System.out.println();	    
	}
    }

    public int encounter(Character other) {
        Scanner scan1 = new Scanner(System.in);
        System.out.print("Do you want to flee? (enter 'true' or 'false'): ");
        boolean b = scan1.nextBoolean();
        if (b) {
            System.out.println(this + " tried to flee.");
            boolean fleesuccess = this.flee(other);
            if (fleesuccess == true) {
                this.experience += 1;
                this.gold += 1;
                System.out.println("Fleed successfully.  " + this + "'s experience and gold each increased by 1.");
                System.out.println();
                return 0;
            }
            if (fleesuccess == false) {
                System.out.println("Failed to flee.");
                System.out.println();
                return 1;
            }
        }
        else{
            System.out.println("In that case, it looks likes you're going to attempt an attack.");
            this.attack(other);
        }
	/*
        if (this.health == 0 && other.health == 0) {
            System.out.println(this + " and " + other + " died.");
            System.out.println();
            return 4;
        }
	*/
        if (this.health == 0) {
            System.out.println(this + " died.");
            System.out.println();
            return 2;
        }
        else if (other.health == 0) {
            //this.gold += other.gold; //potential incorporation of gold
            //other.gold = 0;
            System.out.println();
            return 3;
        }
        else {
            System.out.println("No characters killed.  Battle continues.");
            System.out.println();
            return 5;
        }
    }
}
