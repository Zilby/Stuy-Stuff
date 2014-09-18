import java.io.*;
import java.util.*;
public class Driver {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	NonPlayer n = new NonPlayer();
	NonPlayer n2 = new NonPlayer("Elmo");
	Wizard wi = new Wizard();
	Character c = new Character();
	System.out.print("Enter name:");
	String name = sc.next();
	System.out.println ( "Character Attributes \n" + "Warrior:\n  Strength:18\n   Health:18\n   Experience:1\n    Dexterity:8 \n   Intelligence:4\n" +"\nWizard:\n  Strength:16\n   Health:16\n   Experience:1\n    Dexterity:8 \n    Intelligence:7\n");
	
	System.out.print("Choose character (Warrior or Wizard): ");
	String charClass = sc.next().toUpperCase();
       
	if (charClass.equals("WARRIOR")){
	    c = new Warrior (name);
	}

	else if(charClass.equals ("WIZARD")){
	    System.out.print ("How much mana do you want?(enter a number)");
	    int s = sc.nextInt ();
	    c = new Wizard(name, s);
	}
	else{
	    System.out.print("Please Choose character (Warrior or Wizard): ");
	    charClass = sc.next().toUpperCase();
	    if (charClass. equals ("WARRIOR")){
		c = new Warrior (name);
	    }

	    else if(charClass.equals ( "WIZARD")){
		System.out.print ("How much mana do you want?(enter a number)");
		int s = sc.nextInt ();
		c = new Wizard(name, s);
	    }
	}
	System.out.println("---------------------------------/nPlayer vs. Player");
	c.Battle(30,wi);
	System.out.println("---------------------------------/nPlayer v. nonPlayer");
	c.Battle(30,n);
	System.out.println("---------------------------------/nNPC vs. NPC");
	n.Battle(30,n2);
    }
}
