import java.util.*;
import java.io.*;
import java.math.*;

public class Player extends Character {
    private int points;
    private Scanner sc = new Scanner(System.in);
    private boolean firstencounter = true;
    private boolean atk;

    public int addStat(String stat) {
        System.out.println("Add how many points to " + stat + " (0-" + points + ")");
        int number = sc.nextInt();
        if (number > points) {
            System.out.println("You do not have that many points to add. Added all your points to " + stat + ".");
            int result = points;
            points = 0;
            return result;
        }
        else {
            System.out.println("Added " + number + " points to " + stat + ".");
            points -= number;
            return number;
        }
    }
    public Player() {
        System.out.println("Please enter your name:");
        name = sc.nextLine();
        points = 8;
        dexterity = 8;
        strength = 8;
        intelligence = 8;
        level = 1;
        ep = 0;
        System.out.println("You have 8 points to add to the following stats: Strength, Dexterity, Intellegence");
        strength = strength + addStat("strength");
        dexterity = dexterity + addStat("dexterity");
        intelligence = intelligence + addStat("intelligence");
        hp = strength;
        mp = strength;
    }

    public boolean encounter(Character other) {        
        if (firstencounter == true)
        System.out.println("A wild " + other + " Appeared!");
        firstencounter = false;
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        System.out.println("What would you like to do? Enter 1 for flee, 2 for attack");
        int whatdo = sc.nextInt();
        if (whatdo == 1)
            return flee(other);
        if (whatdo == 2) {
            atk = attack(other);
            firstencounter = !atk;
            return atk;
        }
        return encounter(other);
    }

    public boolean flee(Character other) {
        System.out.println("You attempt to flee...");
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        if (dexterity > other.getDexterity()) {
            System.out.println("You got away safely!");
            firstencounter = true;
	    ep -= other.getEp();
            return false;
        }
        System.out.println("You cannot escape!");
        return true;
    }

    public boolean die() {
        System.out.println("you are dead.");
        firstencounter = true;
        return false;
    }
}
