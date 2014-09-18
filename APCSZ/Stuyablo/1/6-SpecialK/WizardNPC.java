import java.io.*;
import java.util.*;

public class WizardNPC extends Character {
    
    public WizardNPC(){
	Random n = new Random();
	name = "Gandolf";
	charType = "Wizard";
	strength = 10 + n.nextInt(5);
	dexterity = 11+n.nextInt(5);
	defense = 6+n.nextInt(5);
	maxhealth = strength;
	health = 10 + n.nextInt(5);
	charm = 0;
	if (health>maxhealth){
		this.setHealth(this.getMaxHealth());
	}
    }
}
