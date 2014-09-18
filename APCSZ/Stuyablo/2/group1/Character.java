import java.io.*;
import java.util.*;

public class Character {
   
    protected String name;
    protected String charclass="none";
    protected int health,maxHealth;
    protected int dexterity=8,strength=8,intelligence;
    protected int points;
    protected int exp=0,lvl=1;
    protected int x,y;
    protected Character current;

    public void setChar() {
	Scanner sc = new Scanner(System.in);
	System.out.print("Welcome to StuyabloII. \nEnter your name: ");
	name = sc.nextLine();
	System.out.println("Hello " + name);
	System.out.println("-------------------------------");

	System.out.println("What would you like to be?");
	System.out.println("(1) Warrior or (2) Wizard");
	String num = sc.nextLine();
	System.out.println("-------------------------------");

	if (num.equals("1")) {
	    System.out.println("Woo, You're a warrior");
	    Warrior w = new Warrior(name);
	    current = w;
	    charclass = "Warrior";
	    /* this.health = w.health;
	    this.maxHealth = w.maxHealth;
	    this.strength = w.strength;
	    this.dexterity = w.dexterity;
	    this.intelligence = w.intelligence;
	    */
	    }
	else if (num.equals("2")) {
	    System.out.println("Woo, you're a Wizard");
	    Wizard w = new Wizard(name);
	    current = w;
	    charclass = "Wizard";
	    /*this.health = w.health;
	    this.maxHealth = w.maxHealth;
	    this.strength = w.strength;
	    this.dexterity = w.dexterity;
	    this.intelligence = w.intelligence;
	    */
	    }
	else {
	    System.out.println("Silly you, ponies aren't a choice");
	    setChar();
	}
    }

    public void setStat(int n) {
	points = n;
	Scanner sc = new Scanner(System.in);

	System.out.println("You have " + points + " skill points available.");
	System.out.print("Strength = " + this.strength + "+ ");
	int add = sc.nextInt();
	if (add > points){
	    add = points;
	    System.out.printf("Only able to add %d points\n",add);
	}
        this.strength = this.strength + add;
	this.maxHealth = this.strength * 2;
	this.health = this.strength;
        points = points - add;

	System.out.println("-------------------------------");

        System.out.println("You still have " + points + " skill points available");
	System.out.print("Dexterity = " + this.dexterity + "+ ");
	add = sc.nextInt();
	if (add > points) {
	    add = points;
	    System.out.printf("Only able to add %d points\n",add);
	}

	this.dexterity = this.dexterity + add;
	points = points - add;
	
	System.out.println("-------------------------------");

	System.out.printf("Remaining %d points put into intelligence\n",points);
	this.intelligence += points;

	System.out.println("-------------------------------");
    }
  
    public boolean turn() {
	if (current.health <= 0)
	    return false;

	if (exp > 100) {
	    levelUp();
	    turn();
	}

	Scanner sc = new Scanner(System.in);
	System.out.println("Hey you, what does your heart desire?");
	System.out.println("(1) Fight or (2) Heal or (3) Get Status (4) Quit");
	String ans = sc.nextLine();
	System.out.println("-------------------------------");

	if (ans.equals("1")) {
	    encounter();
		//turn();
	}
	else if (ans.equals("2")) {
	    current.heal();
	    //turn();
	}
	else if (ans.equals("3")) {
	    current.getStatus(); 
	}
	else if (ans.equals("4")) {
	    System.out.println("You are a disgrace.");
	    return false;
	}
	else {
	    System.out.println("Silly " + name + " that's not a choice.");
	    //turn();
	}
	return true;
    }

    public boolean encounter() {
	Character enemy = new Character();
	Random r = new Random();
	if (r.nextDouble() > 0.5){
	    enemy = new Ogre();
	}
	else{
	    enemy = new Undead();
	}
	
	while ((current.alive()) && (enemy.alive())){
	    System.out.println("It's "+ enemy +"! \n What will you do?: ");	    
	    System.out.print("(1)Fight or (2)Flee\n");
	    Scanner sc = new Scanner(System.in);
	    String input = sc.nextLine();
	    System.out.println("-------------------------------");
	    if (input.equals("1")){
		current.attack(enemy);
		enemy.attack(current);
		}
	    else if (input.equals("2")){
		current.flee();
	    }
	    else {
		System.out.println("Invalid choice");
	    }
	    System.out.println("Your Health: " + current.getHealth());
	    System.out.println("Enemy Health: " + enemy.getHealth());
	    System.out.println("-------------------------------");
	}
	if (current.alive()) {
	    System.out.println("You have successfully defeated the " + enemy + ".");
	    System.out.println("-------------------------------");
	    current.reward(enemy.getExp());
	    exp = current.exp;
	}
	else {
	    System.out.println("What a shame, you have died.");
	    return false;
	}
	return true;
    }

    public void heal() {
	if (health == maxHealth) {
	    System.out.println("You don't need a rest...");
	    // turn();
	}
	else {
	    int add = (int)(maxHealth * .1);
	    health = health + add;
	    if (health > maxHealth) {
		health = maxHealth;
	    }
	    System.out.println("You have been healed.");
	}
    }

    public void levelUp() {
	exp = 0;
	lvl = lvl + 1;
	System.out.println("Congratulations, you have grown so much wiser.");
	System.out.println("As your reward, you have three skill points to add.");
	setStat(3);
	health = maxHealth = strength;
    }

    public int getExp() {
	return exp;
    }

    public void reward(int n) {
	exp = exp + n;
    }

    public void attack(Character other) {
        System.out.println("Sissy Slap!");
    }
    
    public void takeDamage(int amount) {
	health -= amount;
	if(health < 0)
	    health = 0;
    }

    public boolean flee() {
	Random r = new Random();
	if(r.nextFloat() > 0.35){
	    System.out.println("Got away safely");
	    return true;
	}
	System.out.println("Failed to escape");
	return false;
    }

    public boolean hit() {
	Random r = new Random();
	int d1,d2,d3,sum;
	d1 = r.nextInt(6) + 1;
	d2 = r.nextInt(6) + 1;
	d3 = r.nextInt(6) + 1;
	sum = d1 + d2 + d3;
	return (sum <= dexterity);
    }


    public void getStatus() {
	System.out.println("Name: " + name);
	System.out.println("Class: " + this.charclass);
	System.out.println("Health: " + health);
	System.out.println("Strength: " + strength);
	System.out.println("Dexterity: " + dexterity);
	System.out.println("Intelligence: " + intelligence);
	System.out.println("Experience: " + exp);
	System.out.println("-------------------------------");
    }



    public String toString() {
        return name;
    }

    public int getHealth() {
	return health;
    }

    public boolean alive()
    {
	    return health > 0;
    }

}

