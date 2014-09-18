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

    public Character(String n){
        name = n;
    }

    public void setAttributes(){
        int dex;
        int stren;
        int intell;
	int gold = 100;
        Random r=new Random();
        try{
            dex=r.nextInt(8)+1;
            stren=r.nextInt(8-dex)+1;
            intell=8-dex-stren;
        }
        catch (Exception e){
            dex=3;
            stren=3;
            intell=2;
        }
        dexterity=dex+8;
        strength=stren+8;
        health=50;
        maxhealth=50;
        intelligence=intell+8;
        x = r.nextInt(11);
        y = r.nextInt(11);
    }
    


    public void chooseClass(){
        Scanner sc=new Scanner(System.in);
        boolean answerChoice;
        answerChoice=false;
        while (!answerChoice){

            System.out.println("Press 1 to be a WARRIOR");
            System.out.println("Press 2 to be a WIZARD");
            System.out.println("Press 3 to be an OGRE ");
            System.out.println("Press 4 to be a THIEF");

            int answer=sc.nextInt();


            if (answer == 1){
                charClass="Warrior";
                answerChoice=true;
            }
            else if (answer == 2){
                charClass="Wizard";
                answerChoice=true;
            }
            else if (answer == 3){
                charClass="Ogre";
                answerChoice=true;
            }
            else if (answer == 4){
                charClass="Thief";
                answerChoice=true;
            }
            else {
                System.out.println("That is not a valid key.\n");
            }
        }
        System.out.println("----------------------");

    }

    public void randomClass(){
        Random rand=new Random();
        int c=rand.nextInt(4)+1;
        if (c == 1)
            charClass="Warrior";
        if (c == 2)
            charClass="Wizard";
        if (c == 3)
            charClass="Ogre";
        if (c == 4)
            charClass="Thief";


    }
 
    public int getHealth() {
        return health;
    }

    public String getName(){
        return name;
    }

    public String getCharClass(){
        return charClass;
    }

    /* You have to provide other needed get/set methods */

    public void delay (int x) {
	try {
            Thread.sleep(x);
        }
        catch(Exception e){
        
        } 
    }
    public void intimidate(Character other){
        Random r = new Random();
        if (intelligence >= other.intelligence){
	    say (this + " has intimidated " + other);
            int intdif = intelligence - other.intelligence;
            other.strength = other.strength - (r.nextInt(intdif) + 1);
            if (intdif >= 3)
                other.health = other.health - 2;
        }
        else {
            int intdif = other.intelligence - intelligence;
	     say (other + " has intimidated " + this);
            strength = strength - (r.nextInt(intdif) + 1);
            if (intdif >= 3)
                health = health - 2;
        }
    }

    public void talk(Character other){
            
        Scanner sc = new Scanner(System.in);
        Random y = new Random(); 
        
        say ("you have chosen to talk!");
        delay (2000);
        say ("type the number corresponding to your choice");
        say ("--------------------------------------------------");
        delay (2000); 
        say ("1. Hey big guy, you wanna go out for some drinks instead?\n");
        delay (1000); 
        say ("2. Please, don't you know who I am? I am the greatest swordsman in the East! " + 
             "I've been training since I was 3! You don't have any chance of defeating me!\n" );
        delay (1000);
        say ("3. Didn't you know that they're having a body building competition in the next town?" +
             " I bet you'd fit right in!\n");
        delay (1000);
        
        int answer = sc.nextInt(); 
        boolean x = y.nextBoolean ();
        
        if (answer == 1) {

            if (x) {
                delay (1000); 
                say ("Your enemy says:");
                say ("Sure");
                say ("you walk off into the sunset with your enemy");
            }        
            else {
                delay (1000);
                say ("Your enemy says:");
                say ("no way you freak!");
                intimidate(other);
                dexterity = dexterity + (y.nextInt(3) - 2);
                this.attack(other);
            }

        }
        if (answer == 2) {
            if (x) {
                delay (1000); 
                say ("Your enemy says:");
                say ("sh*t");
                other.flee(this);
            }
            else {
                delay (1000); 
                dexterity = dexterity + (y.nextInt(5) - 2);
                intimidate(other);
                say ("Your enemy says:");
                say ("bullsh*t"); 
                this.attack(other);
            }
        }
        if (answer == 3) {
            if (x) {
                delay (1000); 
                say ("Your enemy says:");
                say ("...you're a riot, kid. and an idiot");
                say("your enemy has left");
            }
            else {
                delay (1000);
                say ("Your enemy says:");
                say ("are you serious?");
                dexterity = dexterity + (y.nextInt(4) - 2);
                intimidate(other);
                this.attack(other);
            }
        }
        if (((answer != 1) && (answer != 2)) && (answer != 3)) {
                say ("That is not a valid input! Please choose one of the given responses.");
                delay (2000);
                this.talk(other); 
        }
    }

    public int roll(){
        
        Random x = new Random();
        int dice1 = x.nextInt(6) + 1;
        int dice2 = x.nextInt(6) + 1;
        int dice3 =  x.nextInt(6) + 1;
        return dice1+dice2+dice3;
    }
        
    public void takedamage(int k){
	if (health > k)
	    health = health-k;
        else 
	    health = 0;
    }                   
                        
    public void say(String s){
        System.out.println(s);
    }
    public void takegold( Character other){
        gold = gold + other.gold;
    }
    public void loosegold() {
        gold = 0;
    }
    public void die(){
        say( name + " has died");
    }

    public int attack (Character other){
	while (this.health>0 && other.health>0){
	    if (roll()<=this.dexterity){
		other.takedamage(this.strength);
		say (this + " has hit " + other);
		delay(2000);
		say (other + " has lost " + strength + " health points and has " + other.getHealth() + " health points left. ");
		delay(2000);
	    }
                        
	    if (roll()>this.dexterity){
		say(this + "'s attack missed!");
		delay(2000);
	    }
	    if (other.dexterity>=other.roll()){
		this.takedamage(other.strength);
		say( other + " has hit " + this); 
		say (this + " has lost " + other.strength + " health points and has " + this.getHealth() + " health points left. ");
		delay(2000);
	
	    }
	    if (other.dexterity > other.roll()){
		say(other + "'s attack missed!");
	        delay(2000);
	    }
	}
	if (other.health<=0){
	    other.die();
	    System.out.println("Congratulations! You defeated your opponent");
	    System.out.println("You earned 100 gold and "+ other.maxhealth + " experience points!");
	    this.takegold(other);
	    this.experience=experience + other.maxhealth;
	    delay(2000);
	    say("Another enemy approaches...");
	    this.encounter(other);
	    return 2;
	}
	else {
	    this.die();
	    System.out.println("GAME OVER");
	    return 3;
	}
    }
        
        public boolean flee (Character other){
                Random x = new Random();
                if (x.nextInt(intelligence) >= intelligence/2){
                        System.out.println(this + " has fled.");
                        delay(2000);
                        System.out.println("It's not over yet!");
                        this.encounter(other);
                        return true;
                }
                System.out.println("" + this + " could not flee successfully and must fight!");
                this.attack(other);
                return false;
        }
   
	public int encounter(Character other){
		Scanner sc = new Scanner (System.in);
		say ("type 1 if you wish to talk");
        delay(2000);
        say("type 2 if you wish to attempt to flee");
        delay(2000);
        say("type 3 if you wish to fight");
        
        int answer = sc.nextInt();
                
                if (answer == 1){
                        this.talk(other);
                }
                if (answer == 2){
                        if (this.flee(other)){
                                return 1;
                        }
                        else 
                                return 3;
                }
                if (answer == 3){
                        int i = this.attack(other);
                        if (i == 0){
                                return 1;
                        }
                        else if (i==1){
                                return 0;
                        }
                        else if (i==2){
                                return 2;
                        }
                        else 
                                return 3;
                }
                if (answer!=1 && answer!=2 && answer!=3){
                        say ("that is not a valid input. Please try again.");
                        this.encounter(other);
                }
                return 5;
        }

        public String getStatus() {
        setAttributes();
        chooseClass();
        String attrib1=String.format("Str: %d Dex: %d Int: %d",
                                     strength, dexterity, intelligence);
        String attrib2=String.format("Exp: %d Health: %d of %d",
                                     experience,health,maxhealth);
        String locale = String.format("x: %5.2f y: %5.2f",x,y);
        String whole=String.format("%s\n%s\n%s\n%s\n%s\n",
                                   name,charClass,attrib1,attrib2,locale);
        return whole;
    }

    public String getStatus2() {
        setAttributes();
        randomClass();
        String attrib1=String.format("Str: %d Dex: %d Int: %d",
                                     strength, dexterity, intelligence);
        String attrib2=String.format("Exp: %d Health: %d of %d",
                                     experience,health,maxhealth);
        String locale = String.format("x: %5.2f y: %5.2f",x,y);
        String whole=String.format("%s\n%s\n%s\n%s\n",
                                   name,charClass,attrib1,attrib2,locale);
        return whole;
    }


    public String toString() {
        return name;
    }
}        
