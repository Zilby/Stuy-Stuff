import java.io.*;
import java.util.*;

public class Character {
    protected String Name;
    protected int Health,maxhealth;
    protected int Mana;
    protected int Strength;
    protected int Intelligence;
    protected int Dexterity;
    protected int Level;
    protected int experience,gold;
    protected double x,y;
    private Scanner sc1 = new Scanner(System.in);
    Random r = new Random();

    public Character() {
    }

    public String getStatus() {
        String attrib1=String.format("Str: %d Dex: %d Int: %d",
                                     Strength,Dexterity, Intelligence);
        String attrib2=String.format("Health: %d of %d",
				     Health,maxhealth);
	String attrib3=String.format("Exp: %d",
				     experience);
        String locale = String.format("x: %5.2f y: %5.2f",x,y);
        String whole=String.format("%s's Stats:\n%s\n%s\n%s\n",
                                   Name,attrib1,attrib2,attrib3,locale);
        return "\n" + whole;
    }

    public String toString() {
        return Name;
    }

    public int getHealth() {
        return Health;
    }

    public int encounter(Character other) {
       	if (this.getHealth() <= 0) 
	    return 2;
	else if (other.getHealth() <= 0)
	    return 3;
	else if (this.getHealth() <= 0 && other.Health <= 0) 
	    return 4;
	System.out.println("Your health: " + this.getHealth() + ", Opponent's health: " + other.getHealth());
	System.out.print("What would you like to do? (Attack/Flee): ");
	String ans = sc1.nextLine();
	while (ans.equals("Attack") == false && ans.equals("Flee") == false) {
	    System.out.println("Not an option! Try again (Attack/Flee): ");
	    ans = sc1.nextLine();
	}
        if (ans.equals("Attack")) {
	    System.out.println("You attack " + other.toString() + "!");
	    this.wait(1000);
	    if (r.nextInt(18) <= this.Dexterity) {
		this.attack(other);
		this.experience();
		this.wait(1000);
	        if (other.getHealth() > 0) {
		    System.out.println(other.toString() + " attacks you!");
		    this.wait(1000);
		    other.attack(this);
		}
	    } else {
		System.out.println("You missed!");
	    }	    
	} else {
	    System.out.println("You try to flee!");
	    this.wait(1000);
	    if (this.flee() == true)
		return 1;
	    else
		System.out.println("You can't escape!");
	}
	return this.encounter(other);
	    
    }

    public void attack(Character other) {
        int hit = r.nextInt(10);
        //this hit should take into account weapon choice
        boolean damage = true;
        int Dice = r.nextInt(6) + r.nextInt(6) + r.nextInt(6);
        if (Dice <= this.Dexterity) {
            damage = true;
            System.out.println(this.toString() + " did " + hit + " damage!");
        } else {
            damage = false;
            System.out.println(this.toString() + " missed!");
        }
        if (damage==true) {
            other.Health = other.Health - hit;
        }
    }

    public boolean flee() {
        int Dice = r.nextInt(36);
        if (Dice < this.Dexterity)
            return true;
        else
            return false;
    }

    public void experience() {
	if (Level == 10) {
	    experience = 0;
	} else {
	    experience = experience + 5;
	    if (experience == 100) {
		Level = Level + 1;            
		experience = 0;
		for (int i=2;i>0;i--) {
		    System.out.print("You have " + i + " points to distribute. Where would you like to upgrade? (enter s for Strength, i for Intelligence, d for Dexterity) ");
		    String pt = sc1.nextLine();
		    if (pt.equals("s")) {
			Strength = Strength + 1;
		    } else if (pt.equals("i")) {
			Intelligence = Intelligence + 1;
		    } else if (pt.equals("d")) {
			Dexterity = Dexterity + 1;
		    } else {
			System.out.print("You didn't enter a valid answer! Try again: ");
			i = i + 1;
		    }
		}
	    }
        }
    }

    public void wait(int n) {
	try {
            Thread.sleep(n);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }   
}

