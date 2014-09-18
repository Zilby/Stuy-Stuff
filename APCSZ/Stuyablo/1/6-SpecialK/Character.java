import java.util.*;
import java.io.*;

public class Character {
    protected int health, maxhealth; // health will regenerate over time
    protected int defense; // effects ability to parry blows
    protected int dexterity; // effects ability to run away
    protected int strength; // effects strength of hits
    protected int charm; // effects who goes attempts to hit first in a battle
    protected int wins;
    protected String name;
    protected String charType;
    protected String winner;

    protected void init(String n, String c, int s, int dex, int def, int ch){
	name = n;
	charType = c;
	strength = s;
	dexterity = dex;
	defense = def;
	health = s;
	maxhealth = s;
	charm = ch;
	wins = 0;
    }
    

    public int getHealthPer(){
	return Math.round((health/maxhealth)*100);
    }

    public int getHealth(){
	return health;
    }

    public int getMaxHealth(){
	return maxhealth;
    }

    public int getDexterity(){
	return dexterity;
    }

    public int getStrength(){
	return strength;
    }

    public int getDefense(){
	return defense;
    }
    
    public String getType(){
	return charType;
    }

    public String getName(){
	return name;
    }

    public int getCharm () {
	return charm;
    }

    public int getWins(){
	return wins;
    }

    public void setWins(int w){
	wins = w;
    }

    public void setHealth(int h){
	health = h;
    }

    public void setDexterity(int d){
	dexterity = d;
    }
    public void setStrength(int s){
	strength = s;
    }
    public void setDefense(int d){
	defense = d;
    }

    public boolean flee(Character other){
	Random rand = new Random();
	if ((rand.nextInt(10) > 2) && (this.getDexterity() > other.getDexterity()) ){
	    this.setDexterity(this.getDexterity()+1);
	    return true;
	    // you are capable of running away, should cut out of current interaction
	    // leave your interaction with the current enemy
	}

	else {
	    this.setHealth(this.getHealth()-1);
	    return false;
	}
    }

    public void attack(Character other){
	int damage = (this.getStrength()/4 - other.getDefense()/4);
	Random r = new Random();
	int luck = (r.nextInt(6) + r.nextInt(6) + r.nextInt(6)); //3 6-sided die
 // can potentially give random bonuses
		if (luck > dexterity){
		    System.out.println("You missed.");
		}
		    else if (luck == dexterity -1){ 
		    damage = this.getStrength() - other.getDefense()/4;
		    if (damage > 0){
			    other.setHealth(other.getHealth()-damage);
			    System.out.println("You hit with a four times bonus, dealing " + damage + " damage to your opponent.");
			}
		    else {
			System.out.println("You hit but did not deal enough power to damage your opponent");
			    }
	   }

	   else if (luck == dexterity - 2){ // potential random bonus
		    damage = this.getStrength()*2 - other.getDefense()/4;
		    if (damage > 0){
			    other.setHealth(other.getHealth()-damage);
			    System.out.println("You hit with a eight times bonus, dealing " + damage + " damage to your opponent.");
			}
		    else {
			System.out.println("You hit but did not deal enough power to damage your opponent");
			    }
	   }

	   else if (luck == dexterity - 3) {
		    System.out.println("You missed your attack, and ended up accidently curing a disease your opponent had");
		    other.setHealth(other.getHealth()+1);
		}

	    else {
		    if (damage > 0) {
			other.setHealth(other.getHealth()-damage);
			System.out.println("You hit with a no bonus, dealing " + damage + " damage to your oponent.");
			}
		    else {
			System.out.println("You hit but did not have enough power to damage your opponent");
		    }
	    }
    }

    public void attackm(Character other){
	int damage = (this.getStrength()/4 - other.getDefense()/4);
	Random r = new Random();
	int luck = (r.nextInt(6) + r.nextInt(6) + r.nextInt(6)); //3 6-sided die
 // can potentially give random bonuses
		if (luck > dexterity){
		    System.out.println("Your opponent missed.");
		}
		    else if (luck == dexterity -1){ 
		    damage = this.getStrength() - other.getDefense()/4;
		    if (damage > 0){
			    other.setHealth(other.getHealth()-damage);
			    System.out.println("Your opponent hit you with a four times bonus, dealing " + damage + " damage to you.");
			}
		    else {
			System.out.println("Your opponent hit but did not deal enough power to damage you");
			    }
	   }

	   else if (luck == dexterity - 2){ // potential random bonus
		    damage = this.getStrength()*2 - other.getDefense()/4;
		    if (damage > 0){
			    other.setHealth(other.getHealth()-damage);
			    System.out.println("Your opponent hit with a eight times bonus, dealing " + damage + " damage to you.");
			}
		    else {
			System.out.println("Your oppponent hit but did not deal enough power to damage you");
			    }
	   }

	   else if (luck == dexterity - 3) {
		    System.out.println("Your opponent missed you, and ended up accidently curing a disease you had");
		    other.setHealth(other.getHealth()+1);
		}

	    else {
		    if (damage > 0) {
			other.setHealth(other.getHealth()-damage);
			System.out.println("Your opponent hit with  no bonus, dealing " + damage + " damage to you.");
			}
		    else {
			System.out.println("Your opponent hit but did not have enough power to damage you");
		    }
	    }
    }

     public void Battle(Character other){
	int r = 20;
        while (r>0 && this.getHealth()>0 && other.getHealth()>0){
	    this.attack(other);
	    if (other.getHealth()>0){
		    other.attackm(this);}
	    r +=1;
		}
     }
    public void encounter(Character other) {
	System.out.println("" + other.getStatus());
	System.out.println("Enter 1 to flee, 2 to talk, any other number to fight");
            Scanner sc = new Scanner(System.in);
	int response = sc.nextInt();
	Random x = new Random();
            
	if (x.nextInt(100)>50 && other.flee(this)){ //randomizes if enemy tries to flee
	    System.out.println("Enemy fled.");}
        else if ((response==1) && (this.flee(other))){
	    System.out.println("You fled, and gained some dexterity.");}
	else if ((response==1) && ((this.flee(other))==false)){
	    System.out.println("You did not flee. You were caught, and damage was inflicted.");
	    System.out.println("Now you have no option but to fight \n");
	    this.Battle(other);
		if (this.getHealth()<=0){
		    System.out.println("You died.");
		}
		else{
		    System.out.println("You triumphed.");
		    this.setWins(this.getWins()+1);
		    Random a = new Random();
		    if (other.getStrength()>0){
			this.setStrength(this.getStrength() + ((other.getStrength()/20)+1));
		    }
		    if (other.getDexterity()>0)
		    {
			this.setDexterity(this.getDexterity()+((other.getDexterity()/20)+1));
		    }
		    if (other.getDefense()>0){
			this.setDefense(this.getDefense()+((other.getDefense()/10)+1));
		    }
		    this.setHealth(this.getHealth()+2);
		    if (this.getHealth()>this.getMaxHealth()){
			this.setHealth(this.getMaxHealth());
		    }
		    System.out.println(this.getStatus());
		}
	}
	else if (response == 2){
            System.out.println("Speak your mind: ");
            Scanner sc1 = new Scanner(System.in);
            String resp = sc1.nextLine();
            Random chrm = new Random();
            if (!(resp.equals("")) && this.getCharm() > other.getCharm() && chrm.nextInt(10)>5){
                System.out.println("Agh, I've been beguiled.. I will get you for this!");
                System.out.println("(the enemy has lost a little health)");
                other.setHealth(other.getHealth() - chrm.nextInt(3)+1);
                this.Battle(other);
                if (this.getHealth()<=0){
                    System.out.println("You died.");
                }
                else{
                    System.out.println("You triumphed.");
                    Random a = new Random();
                    this.setWins(this.getWins()+1);
                    if (other.getStrength()>0){
                        this.setStrength(this.getStrength() + ((other.getStrength()/20)+1));
                    }
                    if (other.getDexterity()>0)
                        {
                            this.setDexterity(this.getDexterity()+((other.getDexterity()/20)+1));
                        }
                    if (other.getDefense()>0){
                        this.setDefense(this.getDefense()+((other.getDefense()/20)+1));
                    }
                    this.setHealth(this.getHealth()+2);
                    if (this.getHealth()>this.getMaxHealth()){
                        this.setHealth(this.getMaxHealth());
                    }
                    System.out.println(this.getStatus());
                }
            }
            else if (resp.equals("")){
		System.out.println("What are your thoughts!");
	    }
	    else{
		System.out.println("Your words will be ignored! Don't even try.  How dare you try to negotiate, this is not the UN"); // this will be printed no matter what, because they have no time to enter something to say
		other.setHealth(other.getMaxHealth());
		this.encounter(other);
	    }
	
	}
        else{
	    this.Battle(other);
		if (this.getHealth()<=0){
		    System.out.println("You died.");
		}
		else{
		    System.out.println("You triumphed.");
		    this.setWins(this.getWins()+1);
		    Random a = new Random();
		    if (other.getStrength()>this.getStrength()){
			this.setStrength(this.getStrength() + ((other.getStrength()/10)+1));
		    }
		    if (other.getDexterity()>this.getDexterity())
		    {
			this.setDexterity(this.getDexterity()+((other.getDexterity()/10)+1));
		    }
		    if (other.getDefense()>this.getDefense()){
			this.setDefense(this.getDefense()+((other.getDefense()/10)+1));
		    }
		    this.setHealth(this.getHealth()+2);
		    if (this.getHealth()>this.getMaxHealth()){
			this.setHealth(this.getMaxHealth());
		    }
		    System.out.println(this.getStatus());
		}
	    }
    }   

     public String getStatus() {
        String attrib1=String.format("Str: %d Dex: %d Def: %d Chr: %d Wins: %d",
                                     strength, dexterity, defense, charm, wins);
        String attrib2=String.format("Health: %d of %d",
                                     health,maxhealth);
        String whole=String.format("%s\n%s\n%s\n",
                                   name,attrib1,attrib2);
        return whole;
    }

    public String toString() {
        return name;
    }
}
