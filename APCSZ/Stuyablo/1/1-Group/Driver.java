import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        System.out.println("Please enter your name:");
        String name=sc.nextLine();
        System.out.println("Welcome "+name);
        System.out.println("-------------------------");

        Character c = new Character(name, true);
        Character c2 = new Character("Bob", false);

        System.out.println("Choose your character's class:\n");
        System.out.println(c.getStatus());
        System.out.println("you have encountered " + c2.getStatus2());    
        String a=c.getCharClass();
        String b=c2.getCharClass();
      	if (b.equals("Warrior")){
               c2= new Warrior(name);
	}

        if (a.equals("Wizard")){
	    c = new Wizard(name);
        }
        
    	if (b.equals("Wizard")){
	    c2 =  new Wizard(name);
        }
          if (a.equals("Ogre")){
	 c = new  Ogre(name);
       }

      	if (b.equals("Ogre")){
               c2= new Ogre(name);
	}

        if (a.equals("Thief")){
           c = new Thief(name);
        }
        
    	if (b.equals("Thief")){
    	   c2 =  new Thief(name);
        }
        c.encounter(c2);
    }
}
