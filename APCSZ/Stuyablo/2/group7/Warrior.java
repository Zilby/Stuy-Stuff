import java.io.*;
import java.util.*;

public class Warrior extends Character {
	public Warrior(String name) {
		super(name, 10, 6, 8, true);
    }
    public void attack(Character other) {
        Random r = new Random();
        Scanner sc = new Scanner(System.in);
        int dex = dexterity;
        int mult = 1;
        int x = r.nextInt(6) + 1, y = r.nextInt(6) + 1, z = r.nextInt(6) + 1;
        System.out.println("\nChoose your weapon:\n1 - Axe\n2 - Sword");
        System.out.print(">");
        int weapon = sc.nextInt();
        if (weapon == 1) {
        	dex = dexterity - 1;
        	mult = 3;
        }
        else if (weapon == 2) {
        	dex = dexterity + 2;
        	mult = 2;
        }
        System.out.println("\n" + this + " attacked!");
        pause();
        if (x+y+z <= dex) {
            int dmg = damageDone(other, mult);
            other.loseHealth(dmg);
            System.out.println("\n" + name + " did " + dmg + " damage to " + other + "!");
            }
        else {
            System.out.println("\n" + name + " missed!");
        }
    }
}