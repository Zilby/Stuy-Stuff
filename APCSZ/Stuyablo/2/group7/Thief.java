import java.io.*;
import java.util.*;

public class Thief extends Character {
	public Thief(String name) {
		super(name, 8, 10, 6, true);
    }
    public void attack(Character other) {
        Random r = new Random();
        Scanner sc = new Scanner(System.in);
        int dex = dexterity;
        int mult = 1;
        int x = r.nextInt(6) + 1, y = r.nextInt(6) + 1, z = r.nextInt(6) + 1;
        System.out.println("\nChoose your weapon:\n1 - Dagger\n2 - Short sword");
        System.out.print(">");
        int weapon = sc.nextInt();
        if (weapon == 1) {
        	dex = dexterity + 3;
        	mult = 2;
        }
        else if (weapon == 2) {
        	dex = dexterity + 1;
        	mult = 3;
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