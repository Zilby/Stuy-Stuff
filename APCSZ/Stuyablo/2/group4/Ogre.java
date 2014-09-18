import java.io.*;
import java.util.*;

public class Ogre extends Character {
    Random r = new Random();
    public Ogre() {
	name = "Ogre";
        // Strength, dexterity, and health will be a random number between 4 and 12
        strength = r.nextInt(8) + 4;
	maxStr = 16;
	dexterity = r.nextInt(8) + 4;
	maxDex = 16;
	health = r.nextInt(8) + 4;
	maxHealth = 16;
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
    // public string ASCIIOgre(){}
}
