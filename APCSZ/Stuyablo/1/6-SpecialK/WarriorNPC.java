import java.io.*;
import java.util.*;

public class WarriorNPC extends Character {
    
    public WarriorNPC(){
	Random n = new Random();
	name = "Warren";
	charType = "Warrior";
	strength = 11 + n.nextInt(5);
	dexterity = 6+n.nextInt(5);
	defense = 9+n.nextInt(5);
	health = 10 + n.nextInt(5);
	maxhealth = strength;
	charm = 0;
	if (health>maxhealth){
		this.setHealth(this.getMaxHealth());
	}
    }
}
