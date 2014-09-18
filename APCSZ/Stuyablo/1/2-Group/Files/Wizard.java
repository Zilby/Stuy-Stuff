import java.util.*;

public class Wizard extends Character{

    protected int mana;
    
    public Wizard() {
	super();
	mana = 100;
	skills = 3;
	health = strength * 8;
    }

    public Wizard(int mana) {
	super();
 	this.mana = mana;
	skills = 3;
	health = strength * 8;
    }

    public Wizard(String name) {
	super(name, 8);
	mana = 100;
	skills = 3;
	health = strength * 8;
    }

    public Wizard(String name, int mana) {
	super(name, 8);
	this.mana = mana;
	skills = 3;
	health = strength * 8;
    }

    public int attack (int type, Character other) {
	while (true) {
	    switch(type) {
	    case 0:
		System.out.println(this.name + " swings at " + other.name + " with a staff");
		return super.attack(other,2,1,0);
	    case 1:
		System.out.println(this.name + " throws a fireball at " + other.name);
		mana = mana - 10;
		return super.attack(other,10,4,1);
	    case 2:
		System.out.println(this.name + " uses dark magic on " + other.name); //We can change spells later...
		mana = mana - 25;
		return super.attack(other,6,8,1);
	    case 3:
		System.out.println(this.name + " casts a spell on " + other.name);
		mana = mana - 50;
		return super.attack(other,3,14,1);
	    default:
		System.out.println("That is not an option");
		Scanner scan = new Scanner(System.in);
		type = scan.nextInt();
	    }
	}
    }

    public int test (int type, Character other) {
	switch(type) {
	case 0:
	    return super.test(other,2,1,0);
	case 1:
	    return super.test(other,10,4,1);
	case 2:
	    return super.test(other,6,8,1);
	case 3:
	    return super.test(other,3,14,1);
	default:
	    return super.test(0,other);
	}
    }
}
