import java.util.*;

public class Stuyablo {
    public static void main(String[] args) {
	printLogo(); // Prints Sean Yip's logo
	System.out.print("Press Enter to begin: ");
	Scanner scanner = (new Scanner(System.in)).useDelimiter(" ");
	while (!(scanner.hasNext())) {} //waits for input	    
	System.out.println("Press Ctrl + C to quit at any time.");
	scanner = new Scanner(System.in); //intentional, to clear any input from the previous scanner instance
	Character player = new Character (); //base player
	Character opponent = new Character (); //base opponent
	//Name
	System.out.print("Enter name: ");
	boolean input = false; //method to check input here is slightly different when actually looking for a specific input, rather than simply any input at all. Is there a more efficient method to do this?
	String name = "";
	while (!input) {
	    name = (scanner.nextLine()).trim();
	    if (!(name.equals(""))) {input = true;}
	}
	System.out.println(player.setBoldText + "Your name is " + name + "!" + "\n" + player.setPlainText); //Makes it bold
	//Class
	System.out.print("Select a class (0 - Random, 1 - Warrior, 2 - Wizard, 3 - Thief): ");
	input = false;
	String _class = "";
	while (!input) {
	    _class = (scanner.nextLine()).trim();
	    if ((_class.equals("0")) || (_class.equals("1")) || (_class.equals("2")) || (_class.equals("3"))) {input = true;} //is there a more efficient method to do this line?
	}
	Random random = new Random();
	if (_class.equals("0")) {_class = String.valueOf(random.nextInt(3) + 1);} //keep forgetting that it's equals() and not ==, as in Python
	
	if (_class.equals("1")) {
	    _class = "Warrior";
	    player = new Warrior (name);
	}
	if (_class.equals("2")) {
	    _class = "Wizard";
	    player = new Wizard (name);
	}
	if (_class.equals("3")) {
	    _class = "Thief";
	    player = new Thief (name);
	}
	
	System.out.println(player);
	player.delay ();

	while (player.getHealth()>0) { 
	    int z = random.nextInt (3);
	    if (player.getExperience () % 100 == 0 && ! (player.getExperience() == 0) ) {

		boolean input4 = false;
		String attributer = "";
		System.out.println ("\n" + "Congratulations " + player.getCharacterClass() + "." + " You have leveled up!");
		player.delay ();
		System.out.println ("You now have 1 Attribute Point to Spend on whatever you want!");
		player.delay ();
		System.out.println ("Current Stats:");
		System.out.println ("Strength: " + player.getStrength ());
		System.out.println ("Intelligence: " + player.getIntelligence ());
		System.out.println ("Dexterity: " + player.getDexterity ());
		System.out.println ("Select an Attribute to raise (0 - Random, 1 - Strength, 2 - Intelligence, 3 - Dexterity): ");

		while (!input4) {

		    attributer = scanner.nextLine().trim();
		    	if ((attributer.equals("0")) || (attributer.equals("1")) || (attributer.equals("2")) || (attributer.equals("3"))) {input4 = true;} //is there a more efficient method to do this line?
	    }

	    if (attributer.equals("0")) {
		if (random.nextInt (3) == 0) {player.strength = player.strength + 1; attributer = "Strength"; }
		else {
		    if (random.nextInt (2) == 1) {player.intelligence= player.intelligence + 1; attributer = "Intelligence"; }
		    else {player.dexterity = player.dexterity + 1; attributer = "Dexterity"; }
		}
	    }
	    
	    
	    if (attributer.equals("1")) {player.strength = player.strength + 1; attributer = "Strength";}
	    if (attributer.equals("2")) {player.intelligence = player.intelligence + 1; attributer = "Intelligence";}
	    if (attributer.equals("3")) {player.dexterity = player.dexterity + 1; attributer = "Dexterity";}
	    
	    System.out.println ("\n" + player.setBoldText + "You have raised your " + attributer + "!" + player.setPlainText);
	    player.level = player.level + 1;
	    }

	    
	    
	    player.maxhealth = player.strength; //accounts for increases in strength;
	    player.health = player.maxhealth;


	    if (z== 0) {
		 opponent = new Wizard();
	        
	    }
	    
	    if (z== 1) {
		 opponent = new Warrior();
        
		
	    }
	    
	    if (z == 2) {
		 opponent = new Thief();
	        
		
	    }

	    	System.out.println ("\n" + player.setBoldText + "You have been challenged by " + opponent.getName() +  player.setPlainText );
	player.delay();

	System.out.println ("\n" + player);
	System.out.println ("\n" + opponent);

	    	player.attack(opponent);
		player.setOpponentsDefeated(player.getOpponentsDefeated() + 1);
	    
	}
	
	System.out.println ("\n" + player);
	System.out.println ("\n" + "You have killed " + player.getOpponentsDefeated() + " opponents!");
	
	
	System.out.println("\nProgram terminated.");
    }
    // Sean Yip's ASCII Logo thing. Made it into a separate static method to clean main method clean - EL
    public static void printLogo() {
	System.out.println("Welcome to");
	System.out.println("  _________ __                      ___.   .__          ");
	System.out.println(" /   _____//  |_ __ __ ___.__._____ \\_ |__ |  |   ____  ");
	System.out.println(" \\_____  \\\\   __\\  |  <   |  |\\__  \\ | __ \\|  |  /  _ \\ ");
	System.out.println(" /        \\|  | |  |  /\\___  | / __ \\| \\_\\ \\  |_(  <_> )");
	System.out.println("/_______  /|__| |____/ / ____|(____  /___  /____/\\____/ ");
	System.out.println("        \\/             \\/          \\/    \\/             "); //ASCII art doesn't exactly look right in code. Got to use "//" for every backslash (/) for the correct escape sequence
    }	
}
