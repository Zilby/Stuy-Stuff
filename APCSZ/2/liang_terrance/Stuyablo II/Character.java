import java.io.*;
import java.util.*;

public class Character {
    protected int health=100, maxhealth=100;
    protected int dexterity=8 , strength=8 , intelligence=8;
    protected int experience = 0, level = 1;
    protected int gold = 100;
    protected String name;
    protected String charClass = "undecided";
 
    public Character(String n){
	name = n;
	//Starting game
    }

    public Character(){
    }

    public int getHealth() {
	return health;
    }

    public void loseHealth(int n){
	health = health - n;
    }

    public String toString() {
	return name;
    }

    public String getChar(){
	return charClass;
    }

    public String getStatus() {
	String cclass = "Character Class: " + charClass;
	String attrib1=String.format("Str: %d Dex: %d Int: %d",
				     strength, dexterity, intelligence);
	String attrib2=String.format("Health: %d of %d",
				     health,maxhealth);
	String attrib3=String.format("Gold: %d   Exp: %d",
				     gold, experience);
	String whole=String.format("%s\n%s\n%s\n%s\n%s\n",
				   name,cclass,attrib1,attrib2,attrib3);
	return whole;
    }

    public Character setClass(){
	Character p;
        Scanner s = new Scanner (System.in);
	System.out.print ("Are you a Wizard or a Warrior? Please type 'Wizard' or 'Warrior' ");
	String c = s.nextLine();
	if (c.equals("Wizard"))
	    p = new Wizard ();
	else if (c.equals("Warrior"))
	    p = new Warrior ();
	else {
	    System.out.print ("Silly player. That's not a choice. \n");
	    p = setClass();
	}
	return p;
    }

    public int  setStrength(int points){
	int p = points;
	Scanner s = new Scanner (System.in);
	System.out.print (" \n" + "Strength: + ");
	int strboost = s.nextInt();
	if ((strboost <= points)&&(strboost>=0)){
	    strength = strength + strboost;
	    p = points - strboost;
	}
	else if (strboost < 0)
	    System.out.print("I'm sorry, but you can't refund points");
	else {
	    System.out.print("Getting a little greedy now?");
	    p = this.setStrength(points);
	}
	return p;
    }

    public int  setDexterity(int points){
	int p = points;
	Scanner s = new Scanner (System.in);
	System.out.print (" \n" + "Dexterity: + ");
	int dexboost = s.nextInt();
	if ((dexboost <= points)&&(dexboost >=0)){
	    dexterity = dexterity + dexboost;
	    p = points - dexboost;
	}
	else if (dexboost < 0)
	    System.out.print("I'm sorry, but you can't refund points");
	else {
	    System.out.print("Getting a little greedy now?");
	    p = this.setDexterity(points);
	}
	return p;
    }
    public int  setIntelligence(int points){
	int p = points;
	Scanner s = new Scanner (System.in);
	System.out.print (" \n" + "Intelligence: + ");
	int intboost = s.nextInt();
	if ((intboost <= points)&&(intboost>=0)){
	    intelligence = intelligence + intboost;
	    p = points - intboost;
	}
	else if (intboost < 0)
	    System.out.print("I'm sorry, but you can't refund points");
	else {
	    System.out.print("Getting a little greedy now?");
	    p = this.setIntelligence(points);
	}
	return p;
    }


    public void setStat(){
	System.out.print ("\n" + "Here are eight stat points for you to add.");
	int points = 8;
	points = setStrength (points);
	System.out.print ("\n" + "There are " + points + " points left");
        if (points > 0){
	    points = setDexterity (points);
	    System.out.print ("\n" + "There are " + points + " points left");
	}
	if (points > 0){
	    points = setIntelligence (points);
	    System.out.print ("\n" + "There are " + points + " points left");
	}
	if (points > 0){
	    System.out.print ("\n" + "Due to failure to use all your points, they are now gone. -poof-" + "\n");
	}
    }


    public boolean hit(){
	Random r = new Random();
        int dice1, dice2, dice3;
	dice1 = r.nextInt(6)+ 1;
	dice2 = r.nextInt(6)+ 1;
	dice3 = r.nextInt(6)+ 1;
	int sum = dice1 + dice2 + dice3;
	return (sum <= dexterity);
    }

    public void action(){
    }
}
