import java.io.*;
import java.util.*;

public class Wizard extends Character {
    
    public Wizard(){
	charType = "Wizard";
	Scanner sc = new Scanner (System.in);
	System.out.println("Enter your name:");
	name = sc.next();
        init(name, "Wizard", 11, 13, 8, 1);
	Scanner scanner = new Scanner (System.in);
	int i = 8;

        String inputs = "";
        
        while (i > 0){
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
