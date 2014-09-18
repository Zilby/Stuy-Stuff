import java.io.*;
import java.util.*;

public class Wizard extends Character{
	public Wizard(String name) {
		super(name, 6, 8, 10, true);
	}

	
    public void attack(Character other) {
		int cDex = 0, tempDex = 0, dist = 0;
		cDex = dexterity;
		Random r = new Random();
		Scanner sc = new Scanner(System.in);
		int dex = dexterity;
		int mult = 1;
		int x = r.nextInt(6) + 1, y = r.nextInt(6) + 1, z = r.nextInt(6) + 1;
		System.out.println("\nChoose your weapon:\n1 - Spell\n2 - Sword");
		System.out.print(">");
		int weapon = sc.nextInt();
		if (weapon == 1) {
			dist = (int)(getDistance(other));
			dexterity = dexterity - dist;
			mult = 2;
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
		dexterity = cDex;
    }
    public int damageDone(Character other, int multiplier){
        return this.intelligence * multiplier;
    }
}