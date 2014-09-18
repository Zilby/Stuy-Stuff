import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	Character c;
	Random rand = new Random();
	Scanner sc = new Scanner(System.in);
	System.out.println("What class would you like to be?(o for ogre, w for wizard)");
	String character = sc.nextLine();
	System.out.println(character);
	if (character.equals("o")){
            c = new OgrePC();
	    System.out.println("You have chosen to be an ogre");
	}
	else{ /*(character == "w"){*/
	    c = new Wizard();
	    System.out.println("You have chosen to be a wizard");
	}
	WarriorNPC w = new WarriorNPC();
	ThiefNPC t = new ThiefNPC();
	System.out.println(c.getStatus());
	int choice = rand.nextInt(2);
	if (choice == 0)
	    c.startEncounter(w);
	else
	    c.startEncounter(t);
    }
}
