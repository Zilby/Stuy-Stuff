import java.util.*;
import java.io.*;
import java.math.*;

public class Homework extends Character {

    private Random randGen = new Random();

    public void changeEP(int n) {
        ep = ep;
    }

    public Homework(String nm, int lv) {
        name = nm;
        dexterity = 8;
        strength = 4;
        intelligence = 4;
        level = lv;
        ep = 30 + 20*lv;
        for (int i = 3 + lv; i > 0; i--) {
            Random r = new Random();
            int number = r.nextInt(3);
            if (number == 2)
                dexterity++;
            else if (number == 1)
                strength++;
            else
                intelligence++;
                }
        hp = strength;
        mp = strength;                
    }

    public boolean die() {
        System.out.println(name + " is dead.");
        return false;
    }

    public boolean encounter(Character other) {
        int randomSelection = randGen.nextInt(4);
        if (randomSelection < 2) {
            return attack(other);
        } else if (randomSelection == 3) {
            return overwhelm(other);
        } else {
            return grow();
        }
    }

    public boolean grow() {
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        boolean death = false;

        if (hp - 1 > 0) { // If it's not going to die...
            hp = hp - 1; // sacrifice 1 hp.
        } else {
            return false; // Otherwise, die! 
        }
        System.out.println("You finish one homework...");
        System.out.println("[" + name + " sacrifices 1HP.]");
        hp = hp * 2; 
        System.out.println("But your teachers simply assign more! The swarm grows.");
        System.out.println("[" + name + " has doubled its HP to " + hp + "]");
        return true;        
    }

    public boolean overwhelm(Character other) {
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        if (roll()) {
                int amount = randGen.nextInt(3);
                other.changeStrength(amount);
                System.out.println("Homework overwhelms " + other + ", lowering their Strength by " + amount + ".");
                System.out.println(name + " deals " + strength/6 + " damage!");
                return other.changeHP(strength / 6);

        }
        else {
            System.out.println(name + "'s attempt to overwhelm fails!");
            return true;
        }
    }
}