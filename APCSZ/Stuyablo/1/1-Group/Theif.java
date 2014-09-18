import java.io.*;
import java.util.*;

public class Theif extends Character{
    
    public Theif(String name){
        super(name);
    }

   
    
    public int attack (Character other){
        int[] dice1={1,2,3,4,5,6};
        int[] dice2={1,2,3,4,5,6};
        int[] dice3={1,2,3,4,5,6};
        //will add complicated x and y coor stuff later
        /*attacks include hitting with:
          hammer(close range)
          sword(med range)
          arrow(far range)*/

        System.out.println("Choose your attack:");
        System.out.println("Press 1 to use your pistol");
        System.out.println("Press 2 to use your dagger");
        System.out.println("Press 3 to use steal");

        Scanner sc=new Scanner(System.in);
        int answer=sc.nextInt();

        //Hammer time
        if (answer == 1) {
            int a=(dice1[new Random().nextInt(dice1.length)]);
            int b=(dice1[new Random().nextInt(dice1.length)]);
            int c=(dice1[new Random().nextInt(dice1.length)]);
            if ((a+b+c)<this.dexterity) {
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
            int a=(dice1[new Random().nextInt(dice1.length)]);
            int b=(dice1[new Random().nextInt(dice1.length)]);
            int c=(dice1[new Random().nextInt(dice1.length)]);
            if ((a+b+c)<this.dexterity) {
                System.out.println(this.name + " stabbed " + other.name + " with a dagger!");
                return super.attack(other);
            }
            else {
               System.out.println(this.name + "'s attack failed!");
            }
        }


	//*pew pew*
	else if (answer == 3){
	    int a=(dice1[new Random().nextInt(dice1.length)]);
	    int b=(dice1[new Random().nextInt(dice1.length)]);
	    int c=(dice1[new Random().nextInt(dice1.length)]);
	    if ((a+b+c)<this.dexterity) {
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
