import java.util.*;
import java.io.*;
import java.math.*;

public class Character {
    protected int hp, mp, ep, level, dexterity, strength, intelligence;
    protected String name;

    public int getLevel() {
	return level;
    }

   public int getEp() {
	return ep;
    }

    public int getDexterity() {
	return dexterity;
    }
    
    public int getHp() {
	return hp;
    }

    public Character() {
	name = "Hans Gruber";
	dexterity = 8;
	strength = 8;
	intelligence = 8;
	level = 1;
	ep = 0;
	for (int i = 8; i > 0; i--) {
	    Random r = new Random();
	    int number = r.nextInt(2);
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

    public Character(String nm,int ST, int DX, int IQ) {
	name = nm;
	dexterity = DX;
	strength = ST;
	intelligence = IQ;
	level = 1;
	ep = 0;
	hp = strength;
	mp = strength;

    }

    public Character(String nm) {
	name = nm;
	dexterity = 8;
	strength = 8;
	intelligence = 8;
	level = 1;
	ep = 0;
	for (int i = 8; i > 0; i--) {
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

    public String getStats() {
	return "\n" + name+"'s Stats:\nLevel:"+level+"\nHealth:"+hp+"\nMana:"+mp+"\nExperience:"+ep+"\nDexterity:"+dexterity+"\nStrength:"+strength+"\nIntellegence:"+intelligence+"\n";
    }
    public boolean roll(){
	Random r1 = new Random();
	Random r2 = new Random();
	Random r3 = new Random();
	int die1=r1.nextInt(5)+1;
	int die2=r2.nextInt(5)+1;
	int die3=r3.nextInt(5)+1;
	int total = die1+die2+die3;
	if (dexterity>total){
	    return true;
	}
	else{
	    return false;
	}
    }

    public String toString() {
	return name;
    }

    public boolean encounter(Character other) {
	return attack(other);
    }
    
    
    public boolean die() {
	System.out.println(name + " is dead.");
	return false;
    }
    


    public boolean changeHP(int n) {
	if (hp > n) {
	    hp = hp - n;
	    return true;
	}
	else 
	    return die();
    }

    public void changeEP(int n) {
	ep = ep + n;
    }

    public boolean changeStrength(int n) {
        if (strength >= n) {
            strength = strength - n;
            return true;
		} else {
		    strength = 0;
		}
	return true;
    }
	

    public boolean attack(Character other) {
	try {
	    Thread.sleep(1000);
	} catch(InterruptedException ex) {
	    Thread.currentThread().interrupt();
	}
	if (roll()) {
	    System.out.println(name + " deals " + strength/3 + " damage!");
	    return other.changeHP(strength / 3);
	}
	else {
	    System.out.println(name + "'s attack misses!");
	    return true;
	}
    }

    public void levelup() {
	int stats = dexterity + intelligence + strength;
	boolean lv = false;
	if (stats <=36 && ep >= 125) {
	    ep -= 125;
	    lv = true;
	}
	else if (stats <=40 && ep >= 250) {
	    ep -= 250;
	    lv = true;
	}
	else if (stats <=45 && ep >= 1000) {
	    ep -= 1000;
	    lv = true;
	}
	else if (stats <=50 && ep >= 3000) {
	    ep -= 3000;
	    lv = true;
	}
	else if (stats <=55 && ep >= 5000) {
	    ep -= 5000;
	    lv = true;
	}
	if (lv == true) {
	    Scanner sc = new Scanner(System.in);
	    level +=1;
	    System.out.println("You have reached level " + level +". Congratulations!");
	    System.out.println("Select a stat to increase: 1 for strength, 2 for dexterity, 3 for intelligence.");
	    int stat = sc.nextInt();
	    if (stat == 1) {
		strength += 1;
	        System.out.println("Added 1 point to strength.");
	    }
	    if (stat == 2) {
		dexterity += 1;
		System.out.println("Added 1 point to dexterity.");
	    }
	    if (stat == 3) {
		intelligence += 1;
		System.out.println("Added 1 point to intelligence.");
	    }
	    if (stat != 1 && stat !=2 && stat != 3) {
		intelligence +=1;
		System.out.println("You obviously need more intelligence. Added 1 to intelligence.");
	    }
	    try {
		Thread.sleep(1000);
	    } catch(InterruptedException ex) {
		Thread.currentThread().interrupt();
	    }
	    
	}
    }
}
