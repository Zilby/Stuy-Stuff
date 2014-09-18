import java.util.*;
import java.io.*;
import java.math.*;

public class Student extends Character {
    private int points;
    private Scanner sc = new Scanner(System.in);
    private boolean firstencounter = true;
    private boolean atk;
    private Random randGen;


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
    public Student() {
        System.out.println("Please enter your name:");
        name = sc.nextLine();
        points = 8;
        dexterity = 8;
        strength = 8;
        intelligence = 8;
        level = 1;
        ep = 0;
        System.out.println("You have 8 points to add to the following stats: Strength, Dexterity, Intelligence");
        strength = strength + addStat("strength");
        dexterity = dexterity + addStat("dexterity");
        intelligence = intelligence + addStat("intelligence");
        hp = strength;
        mp = strength;
        randGen = new Random();
    }

    public boolean heal() {
        if (mp >= 2) {
            mp = mp - 2;
            System.out.println("Attempt to heal self begins: 2 MP consumed.");
            System.out.println("You concentrate, exerting mental energy in addition to your mana as you struggle to recall Living Environment Regents material.");
            int attempt = randGen.nextInt(15);
            if (attempt < intelligence) { // Chance of success increases with greater INT; an INT of 15 grants a 100% success rate
                System.out.println("Success!");
                int amount = randGen.nextInt(5); // How much to heal for? 
                hp = hp + amount;
                System.out.println("Your HP has been healed by " + amount + "! Your HP is now " + hp + "!");
                return true;
            } else {
                System.out.println("You suck at healing. You should probably study more. Nothing happened.");
                return false;
            }
        } else {
            System.out.println("Not enough mana.");
            System.out.println("You had: " + mp + " MP; Required: 2 MP");
            return false;
        }
    }

    public boolean encounter(Character other) {        
        if (firstencounter == true) {
            System.out.println("A wild " + other + " appears!");
            firstencounter = false;
            try {
                Thread.sleep(1000);
            } catch(InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Study up? 1 -> Yes, 2 -> No");
            int response = sc.nextInt();
            if (response == 1) {
                this.changeHP(2);
                intelligence = intelligence + 4;
                System.out.println("Your passion for studying consumes you.");
                System.out.println("You lose 2HP.");
                System.out.println("INT increased by 4.");
            } else {
                System.out.println("Ignorance is bliss, anyway.");
            }
        }
        System.out.println("What would you like to do? Enter 1 for flee, 2 for attack, 3 for heal");
        int whatdo = sc.nextInt();
        if (whatdo == 1)
            return flee(other);
        if (whatdo == 2) {
            atk = attack(other);
            firstencounter = !atk;
            return atk;
        }
        if (whatdo == 3) {
            boolean healing = heal();
            firstencounter = false;
            return true;
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


    public boolean attack(Character other) {
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        int changeAmount;
        if (((strength/2) - (intelligence/4)) > 0) {
            changeAmount = intelligence/4;
        } else {
            changeAmount = 0; // avoid subtracting negative number later
        }

        if (roll()) {
            int damage = (strength/2) - changeAmount;
            System.out.println(name + " deals " + damage + " damage!");
            return other.changeHP(damage);
        }
        else {
            System.out.println(name + "'s attack misses!");
            return true;
        }
    }
}