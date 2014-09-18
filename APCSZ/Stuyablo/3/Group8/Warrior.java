import java.util.*;
import java.io.*;

public class Warrior extends Character {

    private Scanner sc = new Scanner(System.in);
    
    public Warrior() {
	System.out.print("What's your name? ");
	Name = sc.nextLine();
	Level = 1;
	Health = 50;
	maxhealth = 50;
	Intelligence = 8;
	Strength = 8;
	Dexterity = 8;
	Mana = Intelligence * 2;
	experience = 0;
	gold = 0;
	for (int i=8 ; i>0; i--) {
	    System.out.print("You have " + i + " points to distribute. Where would you like to upgrade? (enter s for Strength, i for Intelligence, d for Dexterity) ");
	    String pt = sc.nextLine();
	    if (pt.equals("s")) {
		Strength = Strength + 1;
	    } else if (pt.equals("i")) {
		Intelligence = Intelligence + 1;
	    } else if (pt.equals("d")) {
		Dexterity = Dexterity + 1;
	    } else {
		System.out.println("You didn't enter a valid answer! Try again: ");
		i = i + 1;
	    }
	}
    }
}

