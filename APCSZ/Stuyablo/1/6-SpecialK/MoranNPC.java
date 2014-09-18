import java.io.*;
import java.util.*;

public class MoranNPC extends Character {
    
    public MoranNPC(){
	Random n = new Random();
	charType = "Moran";
	name = "Enemy";
	strength = 12+n.nextInt(4);
	dexterity = 8+n.nextInt(2);
	defense = 12+n.nextInt(3);
	maxhealth = strength;
	health = 10 +n. nextInt(5);
	charm = 0;
	if (health>maxhealth){
		this.setHealth(this.getMaxHealth());
	}
    }
}
