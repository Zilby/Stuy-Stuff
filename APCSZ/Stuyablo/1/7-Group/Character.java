import java.io.*;
import java.util.*;

public class Character {
    protected int roll, health, maxhealth, dexterity, strength, intelligence,defense, experience, gold, damage;
    protected double x,y,distance;
    protected String name,charClass;
    Random r = new Random ();
    Scanner scc = new Scanner (System.in);
    public Character(){
	name = "name";
	health = 0;
	strength = 0;
    }
    /*	Scanner sc =new Scanner(System.in);
	System.out.print("Enter name: ");
	name = sc.next();
        System.out.print("Choose 1 to be a Warrior || Choose 2 to be a Wizard || Choose 3 to see the attributes given to each Character");
	String cl = sc.next();
	if (cl=="3"){
	    System.out.println("Character Attributes \n" + "Wizard:\n  Strength:18\n   Health:18\n   Experience:1\n   Intelligence:4\n" +"\nWizard:\n  Strength:16\n   Health:16\n   Experience:1\n   Intelligence:7\n");
	}
	else if (cl=="1"){
	    charClass="Warrior";
	    strength = 18;
	    health = 18;
	    experience = 1;
	    intelligence = 4;
	    dexterity = 8;
	    
	}
	else if (cl=="2"){
	    charClass="Wizard";
	    strength = 16;
	    health = 16;
	    experience = 1;
	    intelligence = 7;
	    dexterity = 8;
	}
	else{
	    System.out.println("Please Choose 1 to be a Warrior or 2 to be a Wizard");
	    if (cl=="1"){
		charClass="Warrior";
		strength = 18;
		health = 18;
		experience = 1;
		intelligence = 4;
		dexterity = 8;
	    }
	    else if (cl=="2"){
		charClass="Wizard";
		strength = 16;
		health = 16;
		experience = 1;
		intelligence = 7;
		dexterity = 8;
	    }
	}
	    
	x = 0;
	y= 0;
    */		
    
    public Character (String name, String charClass) {
	this.name = name;
	this.charClass = charClass;
	maxhealth = 20;
	dexterity = 10;
	strength = 10;
	intelligence = 10;
	experience = 1;
	gold = 100;
	health = strength;
	x = 0;
	y = 0;

    }

    public void initChar (int maxhealth,int dexterity, int  strength, int  intelligence, int  experience, int gold) {
	this.maxhealth = maxhealth;
	this.dexterity = dexterity;
	this.strength = strength;
	this.intelligence = intelligence;
	this.experience = experience;
	this.gold = gold;
	this.health = strength;
    }

    public double distance(Character other) {
	double a = (other.x - this.x) * (other.x - this.x);
	double b = (other.y - this.y) * (other.y - this.y);
	distance =  Math.sqrt(a+b);
	return distance;

    }
    public int getHealth() {
	return health;
    }

    public int getmaxHealth () {
	return maxhealth;
    }

    public int getDexterity () {
	return dexterity;
    }

    public int getStrength () {
	return strength;
    }
    public int getIntelligence () {
	return intelligence;
    }
    public int getExperience () {
	return experience;
    }
    public int getGold () {
	return gold;
    }
    public String getName () {
	return name;
    }

    public void setHealth(int health) {
	this.health = health;
    }
    public void setStrength(int Strength){
	this.strength = strength;
    }



    public void rolls(){
	Random rand = new Random();
	int ran = 0;
	for (int i = 0; i <3; i = i + 1){
	    ran = rand.nextInt(6);
	    if (ran == 0){
		ran = ran + 1;
	    }
	    roll = roll + ran;
	}
    }
    public void attack(Character other) {
	System.out.println(name + " tries to attack" + "\n");
	this.rolls();
	if (this.getDexterity() > roll){
	    System.out.println(name + " misses");
	    this.setStrength(this.getStrength()-1);
	    System.out.println(other.name);
	    System.out.println("   Health:" + other.getHealth());
	    System.out.println(this.name);
	    System.out.println("   Health:" + this.health);

	}
	       
	else {

	    System.out.println(name + " hits the enemy");
	    other.setHealth(other.getHealth()- damage);
	    this.setStrength(this.getStrength()+1);
	    this.experience = this.experience + 10;
	    System.out.println(other.name);
	    System.out.println("   Health:" + other.getHealth());
	    System.out.println(this.name);
	    System.out.println("   Health:" + this.health);

     
	}
       
	System.out.println("------------------");
		

    }

    public boolean hit (Character other) {
	return (this.dexterity > r.nextInt (18));
 
    }



    public void Battle(int n, Character other){
	int stat = 0;
	System.out.print ("Do you want to flee? (Y or N)");
	String s = scc.next ();
	if (! s.equals ("Y") && ! s.equals ("N")) {
	    System.out.print ("Do you want to flee? (Y or N)");
	    s = scc.next ();
	}
	
	if (s.equals ("Y")) {
	    if (other.hit(this)) {
		System.out.println (other.getName() + " has successfully fled.");
	    }
	    else {
		System.out.println (other.getName() + " has failed at fled.");
		other.Battle (n , this);
	    }
	}
	else {
	    while (n>=0){
		if (n==0){
		    System.out.println("Game Over");

		    break;
		}
		else {
		    if (this.dexterity > other.dexterity){
			stat=this.encounter(other);
			if (stat > 1 && stat < 5){
			    if (stat == 2){
				System.out.println("You have died");
			    
			    }
			    else if (stat == 3){
				System.out.println("Your opponent has died");
			    }
			    else if (stat == 4){
				System.out.println("You and your opponent have both died");
			    }
			    break;
			}
			else{
			    n = n-1;
			}
		    }
		    else {
			stat = other.encounter(this);
			if (stat > 1 && stat < 5){
			    if (stat == 2){
				System.out.println("Your opponent has died");
			 
			    }
			    else if (stat == 3){

				System.out.println("You have died");
	        
			    }
			    else if (stat == 4){

				System.out.println("You and your opponent have both died");
	       
			    }
			    break;
			}
			else{
			    n = n-1;
			}
		    }
		}
	    }
	}
    }

		    
    public int encounter(Character other) {
	int ex = 0;
	if (this.getHealth() > 0 && other.getHealth() > 0){
	    if (other.hit(this)) {
		System.out.println(other.name + " says hi");
		System.out.println(other.name);
		System.out.println("   Health:" + other.getHealth());
		System.out.println(this.name);
		System.out.println("   Health:" + this.health);
		System.out.println("------------------- \n");
		ex= 0;
	    }
     
	    else if (this.hit(other)) {
		ex = 1;
		System.out.println(this.name + " says hi");
		System.out.println(other.name);
		System.out.println("   Health:" + other.getHealth());
		System.out.println(this.name);
		System.out.println("   Health:" + this.health);
		System.out.println("------------------- \n");

	    }
	    else {
		this.attack (other);
		other.attack(this);
		
		if (this.health <= 0){
		    if(other.health <= 0) {
			ex= 4;
		    }
		    ex = 2;
		}
		else if (other.health <= 0) {
		    ex= 3;
		}
	
		else {
		    ex= 5;
		}
	    }
	}
	else{
	    ex = 5;
	}
	     
	return ex;
    }

    /*
      public String levelUp(String stat) {
      String result = "Congratulations!";
      if (stat == "maxhealth") {
      maxhealth = maxhealth + 1;
      result = "Leveled up maxhp. maxhp = " + maxhp;
      }
      else if (stat == "strength") {
      strength = strength + 1;
      result  = "Leveled up str. str = " + str;
      }
      else if (stat == "dexterity") {
      dexterity = dexterity + 1;
      result  = "Leveled up dex. dex= " + dex;
      }
      else if (stat == "intelligence"){
      intelligence = intelligence+ 1;
      result  = "Leveled up intl. intl = " + intl;
      }
      else if (stat == "defense") {
      defense = defense + 1;
      result  = "Leveled up def. def = " + def;
      }
      else {
      result = "Unable to level up a stat. Please input one of the following stats to level up: 'maxhp','str', 'dex', 'intl', or 'def'."; }
      return result;
      }

   `public String  equipWeapon(String weapon) {
      String result = "";
      if( weapon == "Hammer"){
      strength = strength + 2;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else if( weapon == "Sword:"){
      strength = strength + 6;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else {
      result =  "Unable to equip weapon. Please select a weapon from the list.";
      }
      return result;
      }
    */

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
	return name;
    }
    
}
