import java.util.*;

public class Driver {
    public static void main(String[] args) {

	Scanner sc = new Scanner(System.in);
	boolean valid = false;
	String game;
	String type;
	Character ch1 = new Character("placeholder",0);
	Character ch2 = new Character("placeholder",0);

	while (!valid) {
	System.out.print("Choose a game mode. PvP or PvE:  ");
	game = sc.next();
	if (game.equals("PvE")) {
	while (!valid) {
	System.out.println("Choose your class. Warrior or Wizard?");
	type = sc.next();
	if (type.equals("Warrior")) {
	ch1 = new Warrior();
	valid = true; }
	else if (type.equals("Wizard")) {
	ch1 = new Wizard();
	valid = true; }
	else
	System.out.println("Please choose a 'Warrior' or 'Wizard' class."); }
	valid = true;
	ch1.getInfo();
	System.out.println("_________________");
	try {
	    Thread.sleep(2000); // how many milliseconds to pause
	} catch (Exception e) {
	    // do nothing here 
	}
        ch1.play(); }

	else if (game.equals("PvP")) {
	while (!valid) {
	System.out.println("Choose your class. Warrior or Wizard?");
	type = sc.next();
	if (type.equals("Warrior")) {
	ch1 = new Warrior();
	valid = true; }
	else if (type.equals("Wizard")) {
	ch1 = new Wizard();
	valid = true; }
	else
	System.out.println("Please choose a 'Warrior' or 'Wizard' class."); }
	valid = true;
	ch1.getInfo();
	System.out.println("_________________");
	try {
	    Thread.sleep(2000); // how many milliseconds to pause
	} catch (Exception e) {
	    // do nothing here 
	}

	valid = false;
	while (!valid) {
	System.out.println("Choose your class. Warrior or Wizard?");
	type = sc.next();
	if (type.equals("Warrior")) {
	ch2 = new Warrior();
	valid = true; }
	else if (type.equals("Wizard")) {
	ch2 = new Wizard();
	valid = true; }
	else
	System.out.println("Please choose a 'Warrior' or 'Wizard' class."); }
	valid = true;
	ch2.getInfo();
	System.out.println("_________________");
	try {
	    Thread.sleep(2000); // how many milliseconds to pause
	} catch (Exception e) {
	    // do nothing here 
	}
        ch1.battle(ch2,ch1); }
	else
	System.out.println("That is not a valid game mode. Choose 'PvP' or 'PvE'"); }
	
 // Warrior wa1 = new Warrior(); //Player
//	wa1.getInfo();
//	System.out.println("_________________");
//	try {
//	    Thread.sleep(2000); // how many milliseconds to pause
//	} catch (Exception e) {
//	    // do nothing here 
//	}
  //      wa1.play();

	//Wizard wi = new Wizard("tom", 8);
//	System.out.println(wi.strength);

//	Wizard wi2 = new Wizard("Barry", 8);
//	System.out.println(wi2);

//	System.out.println(wi.distance(wi2));
//	c1.battle(wi);
//	System.out.println("_________________");
//	ch1.play();
    }
}


