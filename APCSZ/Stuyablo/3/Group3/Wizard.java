import java.util.*;

public class Wizard extends Character {

    protected int distance;
    protected int dieRoll;
    protected int attackRange;
    protected int intelligence;

    Random generator = new Random();
    public Wizard() {
	strength = 5;
	health = strength;
	dexterity = 10;
	intelligence = 10;
	attackRange = 10;
	experience = 0;
    }

    public void attack(Character other){
	int dice = DieRoll();
	if (attackRange < distance) {
	    distance = distance - 1;
	}
	else {
		if (dice <= dexterity) {
	    System.out.println("You strike your enemy with magic");
	    other.health = other.health -1;
	    experience = experience + 1;
		}
		else{
		    System.out.println("You missed!");
		}
	}
    }
}
	    



    


	