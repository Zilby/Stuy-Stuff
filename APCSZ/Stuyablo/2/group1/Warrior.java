import java.io.*;
import java.util.*;

public class Warrior extends Character {
    private int exp=0,lvl=1;
    private int wait;

    public Warrior(String Name) {
	name = Name;
	setStat(8);
	health = maxHealth = strength;
	System.out.println("Strength: " + strength);
	System.out.println("Dexterity: " + dexterity);
	System.out.println("Intelligence: " + intelligence);
	System.out.println("-------------------------------");
    }

    public void attack(Character c) {
	Scanner sc = new Scanner(System.in);
	System.out.print("\nChoose your attack!\n" + "(1) Poke, (2) Stab, (3) SUPERSLASH\n");
	String atk = sc.nextLine();

	if (atk.equals("1")) {
	    poke(c);
	}
	else if (atk.equals("2")) {
	    stab(c);
	}
	else if (atk.equals("3")) {
	    superslash(c);
	}
	else {
	    System.out.println("\nSilly " + name + ", you can't kiss them");
	    attack(c);
	}
    }
		

    public void poke(Character c) {
	Random r = new Random();
	String atk = "poke";
	int dmg = (int)(strength*r.nextDouble());
	try {
                Thread.sleep(1000);
            } catch (Exception e) {
            }
	if (hit() == true) {
	    c.health = c.health - dmg;
	    System.out.println("\n" + name + " has hurt " + c + " with a " + atk + ".");
	}
	else {
	    System.out.println("\n" + name + " missed " + c + ".");
	}

	if (wait > 0) {
	    wait = wait - 1;
	}
    }

    public void stab(Character c) {
	Random r = new Random();
	String atk = "stab";
	try {
                Thread.sleep(1000);
            } catch (Exception e) {
            }
	if (wait == 0) {
	    int dmg = (int)(strength*(0.5 + r.nextDouble()));
	    if (hit()) {
		c.health = c.health - dmg;
		System.out.println("\n" + name + " has hurt " + c + " with a " + atk + ".");
	    }
	    else {
		System.out.println("\n" + name + " missed " + c + ".");
	    }
	    wait = 1;
	}
	else {
	    System.out.println("\nSorry, you're too tired to " + atk + ".");
	}
    }

    public void superslash(Character c) {
	Random r = new Random();
	String atk = "superslash";
		try {
                Thread.sleep(1000);
            } catch (Exception e) {
            }
	if (wait == 0) {
	    int dmg = (int)(strength*(1 + r.nextDouble()));
	    if (hit() == true) {
		c.health = c.health - dmg;
		System.out.println("\n" + name + " has hurt " + c + " with a " + atk + ".");
		    }
	    else {
		System.out.println("\n" + name + " missed " + c + ".");
	    }
	    wait = 2;
	}
	else {
	    System.out.println("\nSorry, you're too tired to " + atk + ".");
	}

    }	    


    public void defend(int dmg) {
	health = health - dmg;
    }

}
