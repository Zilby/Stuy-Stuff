import java.util.*;
import java.io.*;

public class Driver {
    public static void main(String[] args) {
	System.out.println("Mr. Moran begins strong, but quite slow due to his low dexterity. This makes it harder to run away from opponents. He also has the lowest possible charm, meaning you will probably go last");
        
        try {
            Thread.sleep(2000); // pauses for 2 seconds
        }
        catch (Exception a){
            // intentionally empty...nothing happens
        }

        System.out.println("A wizard can easily runaway, and its high maximum health means that health can reach (and starts at) a high level. However, low defense makes it harder to defend blows of strong opponents");

        try {
            Thread.sleep(2000); // pauses for 2 seconds
        }
        catch (Exception a){
            // intentionally empty...nothing happens
        }

        System.out.println("Ms. Zhang has very weak dexterity, but her defenses are top notch. She has a high charm, increasing the chances of going first in an attack bout");

        try {
            Thread.sleep(2000); // pauses for 2 seconds
        }
        catch (Exception a){
            // intentionally empty...nothing happens
        }
	System.out.println("Warriors have high strength and good defense, but low dexterity. As for students... you'll have to guess the stats.");
	PC n = new PC();
	System.out.println (n.getStatus());


	
	while ( n.getHealth()> 0 ){
	    System.out.println("What would you like to do next?...(a)fight the nearest enemy or (b)talk to the nearest NPC? or (c)See your stats? or (d) meditate? (e)Quit the game :(");
	    Scanner a = new Scanner(System.in);
	    String choice = a.nextLine();
	    if (choice.equalsIgnoreCase("a")){
		Random s = new Random();
		int x=s.nextInt(4);
		if (x == 1){
		    MoranNPC p = new MoranNPC();
		    n.encounter(p);
		}

		else if (x==2){
		    WizardNPC p = new WizardNPC();
		    n.encounter(p);
		}

		else if (x==3){
		    WarriorNPC p = new WarriorNPC();
		    n.encounter(p);
		}

		else if (x==0){
		    ZhangNPC p = new ZhangNPC();
		     n.encounter(p);
		}
		else{
		     BossMoranNPC p = new BossMoranNPC();
		     n.encounter(p);
		}
	    }
	    else if (choice.equalsIgnoreCase("b")){
		String[] chat = new String[8];
		chat[0] = "Get off the bridge.";
		chat[1] = "Make sure you get at least 24 hours of sleep daily.";
		chat[2] = "You're not allowed on floors 1-10.";
		chat[3] = "Should I confiscate that?...";
		chat[4] = "...";
		chat[5] = "This game is too easy, don't you think?";
		chat[6] = "I heard that you might heal if you meditate...";
		chat[7] = "Have you ever seen a cow before? I wish I could.";
		Random num = new Random();
		System.out.println("NPC: " + chat[num.nextInt(8)]);
	    }
	    else if (choice.equalsIgnoreCase("c")){
		System.out.println(n.getStatus());
	    }
	    else if (choice.equalsIgnoreCase("d")){
		System.out.println("You healed a little while resting.");
		Random tempr = new Random();
		n.setHealth(n.getHealth() + tempr.nextInt(4) + 1);
		if (n.getHealth() > n.getMaxHealth()) {
		    n.setHealth(n.getMaxHealth());
		}
	    }
	    else if (choice.equalsIgnoreCase("e")){
		System.out.println("Thanks for playing, fool");
		break;
	    }
	    else {
		System.out.println("You can't do that.");
	    }
	}
    }
}
