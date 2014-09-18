import java.util.*;
import java.io.*;

public class PC extends Character {
    protected int s, dex, def, mh, ch;
    public PC () {
	Scanner sc = new Scanner (System.in);
	System.out.println("Enter your name: ");
	name = sc.next();
	System.out.println("Choose your class. 1-Moran, 2-Wizard, 3-Zhang, 4- Warrior, Any other number- Student...Caution, a non number character will crash the program ");
	int cl = sc.nextInt();
	if (cl == 1){
	    charType="Moran";
	    s = 12;
	    dex = 8;
	    def = 12;
	    mh = s;
	    ch = 0;
	}
	else if (cl == 2){
	    charType="Wizard";
	    s = 11;
	    dex = 13;
	    def = 8;
	    mh = s;
	    ch = 1;
	}
	else if (cl == 3){
	    charType="Zhang";
	    s = 11;
	    dex = 8;
	    def = 13;
	    mh = s;
	    ch = 2;
	}
	else if (cl == 3){
	    charType="Warrior";
	    s = 13;
	    dex = 8;
	    def = 11;
	    mh = s;
	    ch = 1;
	}
	else {
	    charType="Student";
	    s = 10;
	    dex = 12;
	    def = 12;
	    mh = s;
	    ch = 2;
	}
	init(name, charType, s, dex, def, ch);
	distributePoints();
    }

    public void distributePoints() {
	Scanner scanner = new Scanner (System.in);
	int i = 8;
	String inputs = "";
	while (i>0){
	    System.out.println("\n Right now you have:");
	    System.out.println("\n Strength: " + strength);
	    System.out.println("\n Dexterity: " + dexterity);
	    System.out.println("\n Defense: " + defense);
	    System.out.println("\n Maximum Health: " + strength);
	    System.out.println("\n Charm: " + charm);

	    System.out.println("Select one to increment: 0 - Strength, 1 - Dexterity, 2 - Defense, 3 - Charm, 4 - Random");

	    inputs = (scanner.nextLine());

            if (inputs.equals("0")){
                    strength += 1;
                    maxhealth += 1;
                    health += 1;
                }

            else if (inputs.equals("1")){
                    dexterity += 1;
                }

            else if (inputs.equals("2")){
                    defense += 1;
                }

            else if (inputs.equals("3")){
                    charm += 1;
                }

            else if (inputs.equals("4")){
                 Random r1 = new Random();
                 int k = r1.nextInt(4);
                 if (k==0){
                     strength += 1;
                     maxhealth += 1;
                     health += 1;
                 }

                 else if (k == 1){
                     dexterity += 1;
                 }

                 else if (k==2){
                     defense += 1;
                 }
                 else{
                     charm += 1;
                 }
            }
             else {
                 System.out.println("You can't do that.");
                 i = i + 1;
            }
              i = i - 1;
        }
    }
}
