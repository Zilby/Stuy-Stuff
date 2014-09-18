import java.io.*;
import java.util.*;

public class Character {
    protected int health, maxhealth;
    protected int dexterity, strength, intelligence;
    protected int experience;
    protected int gold;
    protected double x,y,distance;
    protected String name;
    protected String charClass;
    protected int damage;//Richard added
    Helper h = new Helper();
    public Character(){
	experience = 0;
	gold = 0;
    }
    public int getHealth() {
	return health;
    }
    public int getMaxHealth(){
	return maxhealth;
    }
    public String getName() {
	return name;
    }
    public void setName(String n){
	name = n;
    }
    public void setHealth(int n) { 
	health=n; 
    }

    public void loseHealth(Character other, int i){//Richard added
	if (i > other.getHealth()){//make it so that i will print appropriately
	    i = other.getHealth();
	}
	other.setHealth( other.getHealth() - i);
	System.out.println(other.getName()+ " has lost " + i + " health");
	System.out.println(other.getName()+ " has " + other.getHealth() + " health left.");
	System.out.println("---------------------------------------------------------------");
    }
    public int getStr(){
	return strength;
    }
    public int getDex(){
	return dexterity;
    }
    public int getInt(){
	return intelligence;
    }
    public int getGold(){
	return gold;
    }
    public int getExp(){
	return experience;
    }
    public void setStr(int i){
	strength = strength + i;
    }
    public void setDex(int i){
	dexterity = dexterity + i;
    }
    public void setInt(int i){
	intelligence = intelligence + i;
    }
    public void setGold(int i){
	gold = gold + i;
    }
    public void setExp(int i){
	experience = experience + i;
    }
    public void setDamage(){
	damage = strength;
    }
    /* You have to provide other needed get/set methods */


    public void attack(Character other) {
	h.pause();
	Random r= new Random();
	int roll=r.nextInt(6) + r.nextInt(6)+ r.nextInt(6); /*three six-sided die roll implementation by Matthew*/
	if (roll < this.getDex()) {
	    System.out.println(this.getName() + " hit!");
	    loseHealth(other,damage);
	    /* do the attack:
	       print out the attempt and the result and update
	       all relavent variables
	    */
	}
	else {
	    System.out.println(this.getName() + " missed!\n---------------------------------------------------------------");
	}
    }

    // returns true if you succesfully flee, false otherwise
    public boolean flee(Character other){
	h.pause();
	Random r= new Random();
	if (r.nextInt(6) + r.nextInt(6)+ r.nextInt(6) +r.nextInt(6) < other.getDex()){       // if the sum of the outcomes of four dice is less than your dexterity, then you escape.
	    return true;
	}
	else { 
	    return false;
	}
    }

    /*
      this routine will decide first ask if other tries to flee. If
      so, and if it's succesful it should adjust experience and or
      gold as needed and return a 0.

      Then, it should decide if this character tries to flee. 
      If so and it's succesful, return a 1;
      
      Otherwise, call attack on both sides:
      this.attack(other);
      if (other.health>0) 
        other.attack(this);

      and then return 2 if this is dead, 3 if other is dead, 4 if both dead, 5 if none dead.
    */
    
    public int encounter(Character other, String fightInput) {
	boolean failFlee = false;
        if (other.getHealth() < other.getMaxHealth()/2){
	    if (other.flee(this)){
		System.out.println("The ogre has fled!");
		this.setExp(other.getExp());
		this.setGold(other.getGold());
		return 0;
	    }
	    else{
		System.out.println("The ogre failed to flee!\n---------------------------------------------------------------");
		failFlee = true;
	    }
	}
	if (fightInput.equals("Flee")){
	    if (this.flee(other)){
		System.out.println("You have fled");
		return 1;
	    }
	    else{
		System.out.println("You failed to flee\n---------------------------------------------------------------");
		other.attack(this);
		if (this.getHealth() == 0){
		    System.out.println("Your adventure ends here...");
		}
	    }
	}
	if (fightInput.equals("Attack")){
	    this.attack(other);
	    if (other.getHealth()>0 && !failFlee)
		other.attack(this);
	    if (this.getHealth()==0)
		return 2;
	    if (other.getHealth()==0){
		this.setExp(other.getExp());
		return 3;
	    }
	}
	return 5;    
    }
    
    public String getStatus() {
	String attrib1=String.format("Str: %d Dex: %d Int: %d",
				     strength, dexterity, intelligence);
	String attrib2=String.format("Exp: %d Health: %d of %d",
				     experience,health,maxhealth);
	String locale = String.format("x: %5.2f y: %5.2f",x,y);
	String whole=String.format("%s\n%s\n%s\n%s\n",
				   name,attrib1,attrib2,locale);
	return whole;
    }
    
    public String toString() {
	return name + charClass;
    }
    
}
