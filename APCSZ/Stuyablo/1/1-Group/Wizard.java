import java.io.*;
import java.util.*;

public class Wizard extends Character {
    
    protected int mana;
    
    public Wizard (String name, boolean check){
	super(name, check);
	this.setAttributes();
	mana = 30;
    }

    public int attack(Character other){
	int answer = 0;
	String linebr = "--------------------------------";
	if (pc == true){
	    say(linebr);
	    System.out.println("Choose your attack:");
	    System.out.println("Press 1 to unleash FIREBALL");
	    System.out.println("Press 2 to unleash ICE STORM");
	    System.out.println("Press 3 to unleash EARTHSHAKER");
	    System.out.println("Press 4 to whack your opponent with your STAFF");
	    
	    Scanner sc = new Scanner(System.in);
	    answer = sc.nextInt();
	    System.out.println(linebr);
	}
	else if(pc == false){
	    Random r = new Random();
	    answer = r.nextInt(4) + 1;
	}
	delay(2000);
	System.out.println("Roll:" + roll() + " | Dexterity: " + this.dexterity); 
	if(roll() >= this.dexterity){
	    if (answer == 1){
		if (mana >= 8){
		    other.takedamage(11);
		    mana = mana - 8;
		    say (this.name + " has unleashed a FIREBALL upon " + other.name);
		    say (this.name + " has " + this.mana + " mana left.");
		    say (other + " has lost 11 health points and has "+other.getHealth()+" health points left");
		    //return super.attack(other);
		}		
		else{
		    System.out.println("You don't have enough mana!");
		}
	    }
	    else if (answer == 2){
		if (mana >= 3){
		    other.takedamage(6);
		    mana = mana - 3;
		    say (this.name + " has unleashed an ICESTORM upon " + other.name);
		    say (this.name + " has " + this.mana + " mana left.");
		    say (other + " has lost 6 health points and has "+other.getHealth()+" health points left");
		}
		else{
		    System.out.println("You don't have enough mana!");
		}
	    }
	    
	    else if (answer == 3){
		if (mana >= 5){
		    other.takedamage(8);
		    mana = mana - 5;
		    say (this.name + " has unleashed an EARTHSHAKER upon " + other.name);
		    say (this.name + " has " + this.mana + " mana left.");
		    say (other + " has lost 8 health points and has "+other.getHealth()+" health points left.");
		}
		else {
		    System.out.println("You don't have enough mana!");
		}
	    }
	    
	    else if (answer == 4){
		other.takedamage(3);
		say (this.name + " whacked " + other.name + " with a staff!");
		say (other + " has lost 3 health points and has " + other.getHealth() + " health points left.");
	    }
	    
	    else {
		say("I'm sorry. It does not seem you have this spell in your arsenal.");
	    }
	    say (linebr);
	}
	else{
	    say (this.name + "'s attack missed!");
	    if (answer == 1)
		mana = mana - 8;
	    else if (answer == 2)
		mana = mana - 3;
	    else if (answer == 3)
		mana = mana - 5;
	    say (this.name + " has " + this.mana + " mana left.");
	    say (linebr);
	    
	}	    
	    /*if (this.health <= 5){
	      if (this.flee(other)){
	      return 0;
	      }
	      }
	      if (other.health <= 5){
	      if (other.flee(this)){
		    return 1;
		    }
		    }
		    
		    if (this.health <= 0){
		    this.die();
		    return 2;
		    }
		    else{
		    other.die();
		    return 3;
		    }*/
	
	return 0;
    }

    public int encounter (Character other){
	say("You have encountered " + other);
	delay(2000);
	say("His status is:\n" + other.getStatus2());
	delay(2000);
     
	while (this.health > 0 && other.health > 0){
	    say("Press 1 if you wish to talk.");
	    say("Press 2 if you wish to attempt to flee.");
	    say("Press 3 if you wish to attack.");
	
	    Scanner sc = new Scanner(System.in);    
	    int answer = sc.nextInt();
	    
	    if (answer == 1)
		this.talk(other);
	    else if (answer == 2){
		if (this.flee(other))
		    return 1;
		else 
		    return 3;
	    }
	    else if (answer == 3){
		this.attack(other);
		delay(3000);
		other.attack(this);
		delay(3000);
	    }
	}
	return 5;
    }
}
