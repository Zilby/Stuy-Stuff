import java.io.*;
import java.util.*;

public class playerCharacter extends Character {

    public playerCharacter () {
	str = 8;
	maxhp = str;
	hp = maxhp;
	dex = 8;
	intl = 8;
	def = 8;
    }
 
    public void turn (Scanner a, Kracken c) {
    // 	a = a.toUpperCase();
    // 	Random r = new Random();
    // 	boolean correct = false;
    // 	while (!correct){
    // 	    if (a.equals("FLEE")) {
    // 		if ((r.nextInt(6) + r.nextInt(6) + r.nextInt(6)) < dex-1) {
    // 		    System.out.println("You have fled from combat");
    // 		    x = x-1;
    // 		}
    // 		else {
    // 		    System.out.println("You failed to flee");
    // 		}
    // 		correct = true;
    // 	    }
    // 	    else if (a.equals("ATTACK")) {
    // 		int x = r.nextInt(6) + r.nextInt(6) + r.nextInt(6);
    // 		int dam = str + 1 - c.def;
    // 		if (x < dex) {
    // 		    if (dam > 0){
    // 			c.hp = c.hp - dam;
    // 			System.out.println ("You did " + dam + " damage!");
    // 		    }
    // 		    else {
    // 			System.out.println ("You did no damage");
    // 		    }
    // 		}
    // 		else {
    // 		    System.out.println("You missed!");
    // 		}
    // 		correct = true;
    // 	    }
    // 	}
    // }
    }

    public String getStr() {
	return "Your Strength (and max HP) is " + str;
    }
    public String getDex() {
	return "Your Dexterity is " + dex;
    }
    public String getInt() {
	return "Your Intelligence is " + intl;
    }
    public String getHP() {
	return "Your current Health is " + hp;
    }

}
