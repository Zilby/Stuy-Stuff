import java.io.*;
import java.util.*;

public class Player extends Character {
    public Player(String n) {
	name = n;
	health = 8;
	maxHealth = 8;
	dexterity = 8;
	maxDex = 8;
	strength = 8;
	maxStr = 8;
	intelligence = 8;
    }
    public void attack(Character other) {
        Random r = new Random();

	int dice1 = r.nextInt(6);
	int dice2 = r.nextInt(6);
	int dice3 = r.nextInt(6);

	if (dice1 + dice2 + dice3 > this.getDex()) {
	    System.out.println(this + " successfully strikes a blow on " + other + "!\n");
	    int damage = 1; //This may be changed later as we get into weapons and such.
	    other.health = other.getHP() - damage;
	}
	else {
	    System.out.println(this + " missed!!\n");
	}
    }
}

