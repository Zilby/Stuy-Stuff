import java.io.*;
import java.util.*;

public class Ogre extends Character{
    
    public Ogre(String name){
        super(name);
    }

   
    
    public int attack (Character other){
        int roll = roll();
	double xchange,ychange;
       	xchange = this.x-other.x;
	ychange = this.y-other.y;
	double d = Math.sqrt(xchange*xchange + ychange*ychange);

        System.out.println("Choose your attack:");
        System.out.println("Press 1 to use your morning spike");
        System.out.println("Press 2 to use your cleaver");
        System.out.println("Press 3 to use your donkey");

        Scanner sc=new Scanner(System.in);
        int answer=sc.nextInt();

        //
        if (answer == 1) {
            if (roll<this.dexterity && d<5) {
                System.out.println(this.name + " hit " + other.name +" with a morning spike - OUCH!");
		System.out.println("Using a morning spike is hard work! " + this.name + " is quite tired.");
		this.dexterity = this.dexterity -1;
		other.health = other.health - 3;
		other.dexterity = other.dexterity - 1;
		return super.attack(other);
            }
            else {
                System.out.println(this.name + "'s attack failed!" + this.name + " was too far away!");
		System.out.println(other.name + " has learned about your fighting strategies!");
		other.intelligence = other.intelligence + 1;
		other.dexterity = other.dexterity + 1;
		return super.attack(other);
            }
        }
     
        //Swords at the ready!
        else if (answer == 2){
            if (roll<this.dexterity && d<3) {
                System.out.println(this.name + " chopped " + other.name + " with a cleaver!");
		other.health = other.health - 2;
		other.dexterity = other.dexterity - 1;
		this.dexterity = this.dexterity + 1;
                return super.attack(other);
            }
            else {
		System.out.println(this.name + "'s attack failed!");
		System.out.println(this.name + "dropped his cleaver!");
		this.dexterity = this.dexterity - 1;
            }
        }


	//*pew pew*
	else if (answer == 3){
	    if (roll<this.dexterity) {
		System.out.println(this.name + " used Donkey against " + other.name);
		
		System.out.println(other.name + " is stunned and very confused!");
		other.health = other.health - 1;
		other.intelligence = other.intelligence - 1;
		other.dexterity = other.dexterity -1;
		return super.attack(other);
	    }
	    else {
		System.out.println(this.name + "'s attack failed!");
	    }
	}
	else {
	    System.out.println(this.name + "you, made a typo!");
	    return this.attack(other); 
	}
	return 5;

        
    }
}
