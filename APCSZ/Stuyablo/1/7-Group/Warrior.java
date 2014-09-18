import java.io.*;
import java.util.*;

public class Warrior extends Character{
    private Random rand = new Random();
    Scanner sc = new Scanner(System.in);
    public Warrior(String name){
	this.name = name;
	strength = 18;
	health = 18;
	experience = 1;
	intelligence = 4;
	gold=100;
	x = 0;
	y=0;
	dexterity = 8;
    }
    public void attack(Character other){
	System.out.print("What is your weapon of choice: 1 for Sword, 2 for Arrow, 3 for Direct Combat");
	String weap = sc.next();
	
	if (weap == "1"){
	    if (this.distance(other) < 5){
		System.out.println(name + "chooses Sword");
		damage = 2;
		super.attack(other);
	    }
	    else{
		System.out.println("You're too far away!");
		System.out.println("Choose Weapon: 1 for Arrow");
		String weap2 = sc.next();
		while (weap2 != "1"){
		    System.out.println("Choose Weapon: 1 for Arrow");
		    weap2 = sc.next();
		}
		damage = 1;
		super.attack(other);
	    }
	}
	else{
	    damage = 1;
	    super.attack(other);
	}
    }
}
	    
		    
	    
