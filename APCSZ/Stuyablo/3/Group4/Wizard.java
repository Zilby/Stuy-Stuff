import java.io.*;
import java.util.*;

public class Wizard extends Character {
	//Wonder if this constructor will work in asking to initialize character.
	public Wizard() {
		charClass = "Wizard";
		Scanner s = new Scanner(System.in);
		Random r = new Random();
		x = r.nextInt(8);
		y = r.nextInt(14);

		System.out.println("Enter your Character name: ");
		name = s.nextLine();
		//inputs character name

		System.out.println("Would you like to distribute ability points? \n1. Yes \n2. I will let the machine decide");
		int i = s.nextInt();
		if (i !=1) {
			int a = r.nextInt(8);
			int b = r.nextInt(8-a);
			int c = 8-a-b;
			strength = strength + a;
			dexterity = dexterity + b;
			intelligence = intelligence + c;
		} else {
			System.out.println("Strength? 8 point(s) left");
			int x = s.nextInt();
			if (x < 8 && x > -1) {
				strength = strength + x;
				int x1 = 8 - x;
				System.out.println("Dex? " + x1 + " point(s) left");
				int y = s.nextInt();
				if (y < x1 && x1 > -1) {
					dexterity = dexterity + y;
					intelligence = intelligence + x1 - y;
				}
				else
					dexterity = dexterity + x1;
			}
			else
			    strength = strength + 8;

		}
		maxhealth = 10*strength;
		health = maxhealth;
	}
	
	public void level(int exp) {
		experience = experience + exp;
		if (experience > experienceneeded) {
			level = level + 1;
			System.out.println(name + " leveled up to level " + level + "! \nWhere would you like to spend your ability point? \n1. Dexterity \n2. Strength \n3. Intelligence");
			
		
		Scanner s = new Scanner(System.in);
		int i = s.nextInt();
		if (i == 1) {
			dexterity = dexterity + 1;
			experienceneeded = experienceneeded + 5 * (level - 1);
		} else {
		    if (i == 2) {
			strength = strength + 1;
			experienceneeded = experienceneeded + 5 * (level - 1);
		    }
		    else {
			intelligence = intelligence + 1;
			experienceneeded = experienceneeded + 5 * (level - 1); /*Increases exp needed to level up by 5 per level, so its 10, 15, 25, 40, 60 Consider that you get 10 exp + enemies health per each kill.*/
		    }
		}
		maxhealth = 10 * strength;
		health = maxhealth; //health regeneration
		}
		

	} 
	public boolean flee(Character other) {
		Scanner s = new Scanner(System.in);
		System.out.println("Will " + name +" fight? \n1. Yes\n2. No");
		int i = s.nextInt();
		if (i != 1) {
			System.out.println(name + " ran away! \n\n");
			System.out.println("----------------------------------------------------------------");
			return true;
		}
		else
			return false;
			
		}
	
	public void attack(Character other) {
		System.out.println(getStatus());
		System.out.println(other.getStatus());
		try {
		    Thread.sleep(2000);
		} catch(InterruptedException ex) {
		    Thread.currentThread().interrupt();
		}
		
	/* do the attack:
		   print out the attempt and the result and update
		   all relavent variables
		*/
		Random r = new Random();
		int roll = r.nextInt(16) + 3;
		if (health == 0) {
			System.out.println(name + " died.");
		}
		else {
		    if ((dexterity + (intelligence /2)) >= roll) {
			other.damage(intelligence + 3);
			System.out.println(name + " has dealt " + (intelligence + 3) + " damage to its enemy!");
			System.out.println("----------------------------------------------------------------");
		}
		else {
			System.out.println(name + " missed!");
			System.out.println("----------------------------------------------------------------");
		}
		}
	}
}
