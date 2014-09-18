import java.util.*;
import java.io.*;

public class Player extends Character{

    public Player(String name){
	this.name = name;
	health = 8;
	dexterity = 8;
	strength = 8;
	experience = 0	
    }
    
    public boolean flee(){
	boolean result;
	Scanner sc = new Scanner(System.in);
	System.out.println("You have encountered a creature! Press 1 to flee, press 2 to attack");
	String response = sc.nextLine();
	if (response.equals("2")){
	    result = false;
	    System.out.println("You have decided to attack");
	} else{
	    result = true;
	    System.out.println("Your flight was successful");
	}
	return result;
    }
    
    public int encounter(Character other){
	if (other.flee() == true){
	    experience = experience + 1;
	    System.out.println(other.name + " has fled");
	    return 0;
	} 

	if (this.flee() == true){
	    System.out.println(this.name + " has fled");
	    return 1;
	} 

	this.attack(other);
	System.out.println("You have attacked " + other.name);

	if (other.health> 0){
	    other.attack(this);
	    System.out.println("You have been attacked by " + other.name);
	    if (this.health < 0){
		System.out.println("You have died");
		return 2;
	    }
	} else if (other.health < 0 && this.health < 0){
	    System.out.println("You and your opponent have died");
	    return 4;
	} else {
	    System.out.println(other.name + "has died");
	    experience = experience + 2;
	    return 3;
	}
	return 5;
    }

}

<<<<<<< HEAD
//Written by Rebecca
=======
>>>>>>> 7b32cf060ad09ac5aab6eef9c9a6f4add098b39d
