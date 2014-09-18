import java.io.*;
import java.util.*;

public class Warrior extends Character{
    
    public Warrior(String name){
        super(name);
                setAttributes();
    }

    public int attack (Character other){
	while (this.health>0 && other.health>0){
	    int roll = roll();
	    double xchange,ychange;
	    xchange = this.x-other.x;
	    ychange = this.y-other.y;
	    double d = Math.sqrt(xchange*xchange + ychange*ychange);
	    
	    System.out.println("Choose your attack:");
	    System.out.println("Press 1 to use your hammer");
	    System.out.println("Press 2 to use your sword");
	    System.out.println("Press 3 to use your bow and arrow");
	    
	    Scanner sc=new Scanner(System.in);
	    int answer=sc.nextInt();
	    
	    //Hammer time
	    if (answer == 1) {
		if (roll<this.dexterity) {
		    if (d<3) { 
			System.out.println(this.name + " whacked " + other.name +" with a hammer!");
               return  super.attack(other);
		    }
		    else { 
			System.out.println(this.name + " is too far away! You missed and " + other.name + " knows your fighting strategies");
			other.intelligence = other.intelligence + 2;
			other.dexterity = other.dexterity + 1;
			this.dexterity = this.dexterity - 1;
		    }
		}
	    }
	    
	    //Swords at the ready!
	    else if (answer == 2){
		if (roll<this.dexterity) {
		    if (d<2) {
			System.out.println(other.name + " has been stabbed in the heart");
			other.health = other.health - 3;
		    }
		    else if (d<5) { 
			System.out.println(other.name + " has been stabbed in the arm");
                    other.health = other.health - 2;
		    }
		    else {
			System.out.println(other.name + " has been slashed. He's angry and his adrenaline is pumping!");
			other.health = other.health - 2;
			other.strength = other.strength + 1;
		    }
		}
		else {
		    System.out.println(this.name + "'s attack failed!");
		}
	    }

	    //*pew pew*
	    else if (answer == 3){
		if (roll<this.dexterity) {
		    if (d<3) { 
			System.out.println(this.name + " shot " + other.name + " with a bow and arrow!");
			this.dexterity = this.dexterity + 1;
			other.health = other.health - 1;
		    }
		    else {
			System.out.println(this.name + " missed!");
                    this.dexterity = this.dexterity - 1;
		    }     
		}
		else { 
		    System.out.println(this.name + "'s attack failed!");
		}
	    }
	    else {
		System.out.println(this.name + "you, made a typo!");
	    }
	}
	return 5;
    }
}
