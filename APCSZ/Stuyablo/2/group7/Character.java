import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxhealth;
    protected int dexterity, strength, intelligence;
    protected int experience;
    protected int gold;
    protected double x,y;
    protected String name;
    protected String charClass;
 
    public double getHealth() {
        return health;
    }
    public int getDex() {
        return dexterity;
    }
    public int getStr() {
        return strength;
    }
    public int getIntel() {
        return intelligence;
    }
    public int getEXP() {
        return experience;
    }
    public double getDistance(Character other) {
        double distance;
        double differX, differY;
        differX = this.x - other.x;
        differY = this.y - other.y;
        distance = Math.sqrt( (differX*differX) + (differY*differY) );
        return distance;
    }

	public Character(String name, int baseStr, int baseDex, int baseInt, boolean playable) {
		Random r = new Random();
		this.name = name;
        if (playable) {
            distributeStats(baseStr, baseDex, baseInt);
        }
        else {
    		int eStr = r.nextInt(9);
    		int eDex = r.nextInt(9 - eStr);
    		int eInt = 8 - eStr - eDex;
    		this.dexterity = baseDex + eDex;
    		this.strength = baseStr + eStr;
    		this.intelligence = baseInt + eInt;
        }
    	this.maxhealth = this.strength * 5;
    	this.health = this.maxhealth;
	}

    public void distributeStats(int baseStr, int baseDex, int baseInt) {
        Scanner sc = new Scanner(System.in);
        System.out.println(name + ", choose your stats:");
        System.out.println("\nStrength affects health and the damage done by melee characters.");
        System.out.println("Dexterity affects accuracy.");
        System.out.println("Intelligence affects the chance of fleeing and the damage done by magic users.");
        System.out.println("\nWarriors start off with 10 strength, 6 dexterity, and 8 intelligence.");
        System.out.println("Wizards start off with 6 strength, 8 dexterity, and 10 intelligence.");
        System.out.println("Thieves start off with 8 strength, 10 dexterity, and 6 intelligence.");
        System.out.println("\nYou have 8 more points to allocate.");
        System.out.println("\nHow many points do you want to add to strength?");
        System.out.print(">");
        int str = sc.nextInt();
        System.out.println("\nHow many points do you want to add to dexterity?");
        System.out.print(">");
        int dex = sc.nextInt();
        System.out.println("\nHow many points do you want to add to intelligence?");
        System.out.print(">");
        int intel = sc.nextInt();
        this.name = name;
        strength = baseStr + str;
        dexterity = baseDex + dex;
        intelligence = baseInt + intel;
        System.out.println(String.format("\nStr: %d Dex: %d Int: %d\n\n",
                                    strength, dexterity, intelligence));
        if (dexterity + strength + intelligence > 32) {
            System.out.println("You have added too many points, please try again.\n\n");
            distributeStats(baseStr, baseDex, baseInt);
        }
    }


    public void attack(Character other) {
        Random r = new Random();
        //the dice rolls
        int x = r.nextInt(6) + 1, y = r.nextInt(6) + 1, z = r.nextInt(6) + 1;
        System.out.println("\n" + this + " attacked!");
        pause();
        if (x+y+z <= dexterity) {
            //needs damage calculator!
            int dmg = this.strength * 2;
            other.loseHealth(dmg);
            System.out.println("\n" + name + " did " + dmg + " damage to " + other + "!");
        }
        else {
            System.out.println("\n" + name + " missed!");
        }
    }
    
    public int damageDone(Character other, int multiplier){
        return this.strength * multiplier;
    }
    
    // returns true if you succesfully flee, false otherwise
    public boolean flee(Character other) {
        Random r = new Random();
        boolean flee = false;
        int x = r.nextInt(6) + 1, y = r.nextInt(6) + 1, z = r.nextInt(6) + 1;
        int chance = this.intelligence - other.intelligence;
        if (chance <= 0) {
                //gives the character at least 1/18 chance of fleeing
                chance = 0;
        }
        flee = x+y+z <= chance + 3;
        if (flee) {
            health = 0;
        }
        return flee;
    }
    
    public void loseHealth(int hp) {
        health = health - hp;
    } 
    
    public int encounter(Character other) {
        Scanner sc = new Scanner(System.in);
        System.out.println("\n" + this + "\n1 - Attack \n2 - Flee");
        System.out.print("Enter your choice: ");
        int option = sc.nextInt();
        pause();
        if (option == 2) {
            if (this.flee(other)) {
                return 1;
            }
            else {
                System.out.println("\n" + this + " tried to flee, but failed."); 
                return 5;
            }
        }
        else {
            this.attack(other);
            if (other.health > 0) {
                return 5;
            }
            else {
                return 3;
            } 
        }
    }

    public String getStatus() {
        String attrib1=String.format("Str: %d Dex: %d Int: %d",
                                     strength, dexterity, intelligence);
        //String attrib2=String.format("Exp: %d Health: %d of %d",
        //                             experience,health,maxhealth);
        //String locale = String.format("x: %5.2f y: %5.2f",x,y);
        String whole=String.format("%s\n%s\n",
                                   name,attrib1);
        return whole;
    }
                   
    public String toString() {
        return name;
    }

    public void pause() {
            try {
            Thread.sleep(750); // pause for that many milliseconds
        } 
        catch (Exception e) {
                // do nothing here - it should never get run 
        }
    }

    public Character createNew() {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter a name: ");
        String name = sc.nextLine();
        System.out.println("\nChoose your class:\n\nWarrior\nWizard\nThief");
        System.out.print(">");
        String pClass = sc.nextLine();
        Character c1 = new Character(name,8,8,8,false);
        if (pClass.equals("Warrior")) {
                System.out.println("\nYou are now a warrior!\n");
                c1 = new Warrior(name);
        }
        else if (pClass.equals("Wizard")){
                System.out.println("\nYou are now a wizard!\n");
                c1 = new Wizard(name);
        }
        else if (pClass.equals("Thief")){
                System.out.println("\nYou are now a thief!\n");
                c1 = new Thief(name);
        }
        else {
                System.out.println("\nInvalid class, defaulting to Warrior.\n");
                c1 = new Warrior(name);
        }
        return c1;
    }
}
