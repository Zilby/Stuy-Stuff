import java.io.*;
import java.util.*;

public class Thief extends Character{
    
    public Thief(String name){
        super(name);
    }

   
    
    public int attack (Character other){
	int roll = roll();
	double xchange = this.x - other.x;
	double ychange = this.y - other.y;
	double d = Math.sqrt(xchange*xchange + ychange*ychange);
        System.out.println("Choose your attack:");
        System.out.println("Press 1 to use your pistol");
        System.out.println("Press 2 to use your dagger");
        System.out.println("Press 3 to steal");

        Scanner sc=new Scanner(System.in);
        int answer=sc.nextInt();

        //pistole time
        if (answer == 1) {
            if (roll<this.dexterity) {
            //if x,y coors are <2 or something (something small)
                System.out.println(this.name + " shot " + other.name +" with a pistol!");
		return super.attack(other);
            }
            else {
                System.out.println(this.name + "'s attack failed!");
		return super.attack(other);
            }
        }
     
        //Swords at the ready!
        else if (answer == 2){
            if (roll<this.dexterity) {
                System.out.println(this.name + " stabbed " + other.name + " with a dagger!");
                return super.attack(other);
            }
            else {
               System.out.println(this.name + "'s attack failed!");
            }
        }


	//*pew pew*
	else if (answer == 3){
	    if (roll<this.dexterity) {
		System.out.println(this.name + " stole " + other.name + "'s health!");
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
