import java.util.*;

public class Troll  extends Character {

    public Troll(String name, int limit) {
	super(name,limit);
	health = strength * 10;
	skills = 3;
	movement = 5;
    }
    public Troll() {
	super();
	health = strength * 10;
	skills = 3;
	movement = 5;
	}

    public int attack (int type, Character other) {
	while (true) {
	    if (type == 1) {
		System.out.println(this.name + " hits " + other.name + " with a haymaker");
		return super.attack(other,1,strength,0);
	    }
	    else if (type == 2) {
		System.out.println(this.name + " swings his club at " + other.name);
		return super.attack(other,2,8,0);
	    }
	    else if (type == 3) {
		System.out.println(this.name + " starts a flame war with " + other.name);
		return super.attack(other,6,2,1);
	    }
	    else
		System.out.println("That is not an option");
		Scanner scan = new Scanner(System.in);
		type = scan.nextInt();
	}
    }

    public int test (int type, Character other){
	if (type == 1) {
	    return super.test(other,1,strength,0); }
	else if (type == 2) {
	    return super.test(other,2,8,0); }
	else if (type == 3) {
	    return super.test(other,6,2,1); }
	else
		return super.test(0,other);
	}

}
