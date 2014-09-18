import java.io.*;
import java.util.*;


public class Wizard extends Character{
    private Random rand = new Random();
    Scanner sc = new Scanner(System.in);
    protected int damage, mana;
    
   
    public Wizard(String name, int mana){
        this.name = name;
        strength = 16;
        health = 16;
        experience = 1;
        intelligence = 7;
        gold=100;
        x = 0;
        y=0;
        dexterity = 8;
	this.mana = mana;
	    }
    public Wizard(){
        name = "Phil";
        strength = 15;
        health = 15;
        experience = 1;
        intelligence = 7;
        gold=100;
        x = 0;
        y=0;
        dexterity = 8;
	mana = 10;
	    }



    public void staffattack (Character other) {
	 
	System.out.println(this.getName() + " chooses Staff");
	this.intelligence = intelligence + 4;
	System.out.println("What Staff Magic do you want to use : 1 for Inferno Fireball, 2 for Artic Ice Blizzard, 3 for Gust, 4 for Staff Slap");
        int magic = sc.nextInt();

	if (this.mana >= 5 && magic != 4) {
	    this.mana = this.mana - 5;

              
	    if (magic == 1) {
		damage = (this.intelligence) - rand.nextInt(6);
		System.out.println(other.getName() + " lost " + damage + " health from inferno fireball");
	        other.setHealth (other.health - damage);
		if (rand.nextInt (4) > 3) {
		    other.setHealth (other.health - 2);
		    System.out.println(other.getName() + " lost 3 health from being incinerated");
			
		}
	    }
		
                 
	    if (magic == 2) {
		damage = (this.intelligence) - rand.nextInt(6);
		System.out.println(other.getName() + " lost " + damage + " health from artic ice blizzard");
	        other.setHealth (other.health - damage);
		if (rand.nextInt (4) > 3) {
		    other.setHealth (other.health - 3);
		    System.out.println(other.getName() + " lost 3 health from being frozen");
			
		}
	    }

              
	    if (magic == 3) {
		damage = (this.intelligence) - rand.nextInt(4);
		System.out.println(other.getName() + " lost " + damage + " health from gust");
	        other.setHealth (other.health - damage);
	    }
	}

              
	else if (magic == 4) {
	    super.attack (other);
	    this.mana = this.mana + 1;
	}
	else if (mana < 5) {
	    System.out.println (this.getName() + " is out of mana");
	    mana = mana + 5;
	}
		
	else {
	    System.out.println ("Please enter either 1,2,3,or 4 only next time. You failed to listen to instructions so you don't deserve an attack");
	}
	this.intelligence = this.intelligence - 4;}



    public void attack(Character other){
        System.out.println("What is your weapon of choice: 1 for Wand, 2 for Staff");
        String weap = sc.next();
	while (! weap.equals ("1") && ! weap.equals ("2")){
	            System.out.println("What is your weapon of choice: 1 for Wand, 2 for Staff (please listen to the instructions)");
		    weap = sc.next();
	}
        
        if (weap.equals ("1")){
            if (this.distance(other) < 10){
		this.intelligence = this.intelligence + 2;
                System.out.println(name + " chooses Wand");
	        System.out.println("What Wand Magic do you want to use : 1 for Mini Fireball, 2 for Ice ball, 3 for Gust, 4 for Wand Slap");
                int magic = sc.nextInt();
		
		if (this.mana >= 5 && magic != 4) {
		    this.mana = this.mana - 5;

		    if (magic == 1) {
			damage = (this.intelligence) - rand.nextInt(5);
			System.out.println(other.getName() + " lost " + damage + " health from mini fireball");
			other.setHealth (other.health - damage);
			if (rand.nextInt (4) > 3) {
			    other.setHealth (other.health - 2);
			    System.out.println(other.getName() + " lost 2 health from being burnt");
			
			}
		    }
		
                 
		    if (magic == 2) {
			damage = (this.intelligence) - rand.nextInt(6);
			System.out.println(other.getName() + " lost " + damage + " health from iceball");
		        other.setHealth (other.health - damage);
			if (rand.nextInt (4) > 3) {
			    other.setHealth (other.health - 3);
			    System.out.println(other.getName() + " lost 3 health from being frozen");
			
			}
		    }

              
		    if (magic == 3) {
			damage = (this.intelligence) - rand.nextInt(4);
			System.out.println(other.getName() + " lost " + damage + " health from gust");
		        other.setHealth (other.health - damage);
		    }
		}
              
		else if (magic == 4) {
		    System.out.println(this.getName() + " uses Wand Slap because you do not have enough mana.");
		    super.attack (other);
		}
		else if (mana < 5) {
		    System.out.println (this.getName() + " is out of mana");
		    mana = mana + 5;
		}
		else {
		    System.out.println ("Please enter either 1,2,3,or 4 only next time. You failed to listen to instructions so you don't deserve an attack");
			}
		this.intelligence = this.intelligence - 2;

            }
	
	    else{
		System.out.println("You're too far away!You must use your staff for your long range magic");
		System.out.println("Choose Weapon: 2 for Staff");
		String ans = sc.next();
		while (!ans.equals("2")){
		    System.out.println("Choose Weapon: 2 for Staff");
		    ans = sc.next();
		}
		this.staffattack(other);
	}
    }
    else{
        this.staffattack(other);
    }
    }
}
