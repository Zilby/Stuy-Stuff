import java.io.*;
import java.util.*;

public class Warrior extends playerCharacter{
    private Random rand = new Random();

    public void turn (Scanner S, Character other) {
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
		    System.out.println("2. Triple Strike ");
		    System.out.println("3. Critical Hit ");
		    System.out.println("What do you want to do? ");
		    int t = s.nextInt();
		    
		    if (t==1) {
			basicAttack(other);
			correct2 = true;
		    }
		    else if (t==2) {
			tripleStrike(other);
			correct2 = true;
		    }
		    else if (t==3) {
			critHit(other);
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
		    System.out.println("2. Triple Strike ");
		    System.out.println("3. Critical Hit ");
		    System.out.println("What do you want to do? ");
		    int t = s.nextInt();
		    
		    if (t==1) {
			basicAttack(other);
			correct2 = true;
		    }
		    else if (t==2) {
			tripleStrike(other);
			correct2 = true;
		    }
		    else if (t==3) {
			critHit(other);
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
		System.out.println ("You did " + dam + " damage!");
	    }
	    else {
		System.out.println ("You did no damage");
	    }
	}
	else {
	    System.out.println("You missed!");
	}
    }

    public void critHit (Character c){
	int y = rand.nextInt(6) + rand.nextInt(6) + rand.nextInt(6);
	if (y < dex - 5) {
	    c.hp = c.hp - 2;
	    System.out.println ("Critical hit! + 1 damage");
	}
	else {
	    System.out.println ("You flung your sword so hard that it got stuck in the ground, what a dingus!");
	}
    }

    public void tripleStrike (Character c){
	int z = rand.nextInt(6) + rand.nextInt(6) + rand.nextInt(6);
	if (z < dex) {
	    if (rand.nextInt(2) > 0){
		System.out.println ("Hit!");
		c.subHealth(rand.nextInt(2)+1);
	    }
	    else {
		System.out.println("Miss!");
	    }
	    if (rand.nextInt(2) > 0){
		System.out.println ("Hit!");
		c.subHealth(rand.nextInt(2)+1);
	    }
	    else {
		System.out.println("Miss!");
	    }
	    if (rand.nextInt(2) > 0){
		System.out.println ("Hit!");
		c.subHealth(rand.nextInt(2)+1);
	    }
	    else {
		System.out.println("Miss!");
	    }
	}
	else {
	    System.out.println("You tripped and fell before your first strike, get more dexterity you lump!");
	}
    }
}
