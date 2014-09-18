import java.util.*;
import java.io.*;

public class Wizard extends playerCharacter {
    private Random rand = new Random();

    // public void turn (String a, Character other) {
    // 	a = a.toUpperCase();
    // 	Random r = new Random();
    // 	boolean correct = false;
    // 	while (!correct){
    // 	    if (a.equals("FLEE")) {
    // 		if ((r.nextInt(6) + r.nextInt(6) + r.nextInt(6)) < dex-1) {
    // 		    System.out.println("You have fled from combat");
    // 		}
    // 		else {
    // 		    System.out.println("You failed to flee");
    // 		}
    // 		correct = true;
    // 	    }
    // 	    else if (a.equals("ATTACK")) {
    // 		boolean correct2 = false;
    // 		Scanner s = new Scanner(System.in);
    // 		while (!correct2){
    // 		    System.out.println("1. Basic Attack ");
    // 		    System.out.println("2. Fireball ");
    // 		    System.out.println("3. Lightning Strike ");
    // 		    System.out.println("What do you want to do? ");
    // 		    int t = s.nextInt();

    // 		    if (t==1) {
    // 			basicAttack(other);
    // 		    }
    // 		    else if (t==2) {
    // 			Fireball(other);
    // 		    }
    // 		    else if (t==3) {
    // 			Lightning(other);
    // 		    }
    // 		    else {
    // 			System.out.println("please just say 1, 2, or 3");
    // 		    }
    // 		}	    
    // 		correct = true;
    // 	    }
    // 	    else {
    // 		System.out.println("please type in Attack or Flee, or some variation");
    // 	    }
    // 	}
    // }

    public void turn (Scanner S, Kracken other) {
	Random r = new Random();
	boolean correct = false;
	while (!correct){
	    String a = S.next().toUpperCase();
	    if (a.equals("FLEE")) {
		if ((r.nextInt(6) + r.nextInt(6) + r.nextInt(6)) < dex-1) {
		    System.out.println("You have fled from combat");
		}
		else {
		    System.out.println("You failed to flee");
		}
		correct = true;
	    }
	    else if (a.equals("ATTACK")) {
		boolean correct2 = false;
		Scanner s = new Scanner(System.in);
		while (!correct2){
		    System.out.println("1. Basic Attack ");
		    System.out.println("2. Fireball ");
		    System.out.println("3. Lightning Strike ");
		    System.out.print("What do you want to do? ");
		    int t = s.nextInt();

		    if (t==1) {
			basicAttack(other);
			correct2 = true;
		    }
		    else if (t==2) {
			Fireball(other);
			correct2 = true;
		    }
		    else if (t==3) {
			Lightning(other);
			correct2 = true;
		    }
		    else {
			System.out.println("please just say 1, 2, or 3");
		    }
		}	    
		correct = true;
	    }
	    else {
		System.out.println("please type in Attack or Flee, or some variation");
	    }
	}
    }
    
    public void basicAttack (Character c){
	int x = rand.nextInt(6) + rand.nextInt(6) + rand.nextInt(6);
	int dam = str - c.def;
	if (x < dex) {
	    if (dam > 0){
		c.hp = c.hp - dam;
	    }
	    else {
		System.out.println ("You did no damage");
	    }
	}
	else {
	    System.out.println("You missed!");
	}
    }
    

    public void Fireball (Character c) {
	int x = rand.nextInt(6) + rand.nextInt(6) + rand.nextInt(6);

	if (x < dex && str > 0) {
	    if (rand.nextInt(5)>0) {
		x = (intl - (((c.def+1)/2) + rand.nextInt(c.def/2)));//intelligence minus a number from half the guy's defense to all of it
		c.hp = c.hp - x;
		System.out.println("Successful fireball!");
	    }
	    else {
		str = str - 1;
		System.out.println("OH NO! Your spell backfired, so you lost 1 str permanently\n");
	    }
	}
	else if (str == 0){
	    System.out.println("OH NO! You've run out of str, no more spells for you\n");
	}
	else if (x >= dex){
	    System.out.println("Bad luck! You mispronounced the incantation, you need more dexterity\n");
	}
	else{
	    System.out.println("If you are seeing this message, you probably figured out how to get negative strength. I don't know what you did, but uhh...\n");
	}
    }

    public void Lightning (Character c) {
	int x = rand.nextInt(6) + rand.nextInt(6) + rand.nextInt(6);
	if (x <= dex && str > 0) {
	    if (rand.nextInt(2)>0) {
		x = (intl + (rand.nextInt(intl/2)) - (((c.def+1)/2) + rand.nextInt(c.def/2)));
		System.out.println("SUCCESSFUL LIGHTNING STRIKE");
	    }
	    else {
		str = str - 1;
		System.out.println("OH NO! Your risky lighting spell backfired and you lost 1 str permanently");
	    }
	}
	else if (str == 0){
	    System.out.println("OH NO! You've run out of str, no more spells for you\n");
	}
	else if (x >= dex){
	    System.out.println("Bad luck! You mispronounced the incantation, you need more dexterity\n");
	}
	else{
	    System.out.println("If you are seeing this message, you probably figured out how to get negative strength. I don't know what you did, but uhh...\n");
	}
    }
}
