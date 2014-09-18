import java.io.*;
import java.util.*;

public class ZhangNPC extends Character {
    
    public ZhangNPC(){
	Random n = new Random();
	name = "Jie";
	charType = "Zhang";
	strength = 9 + n.nextInt(5);
	dexterity = 6+n.nextInt(5);
	defense = 11+n.nextInt(5);
	maxhealth = strength;
	health = 10 + n.nextInt(5);
	charm = 0;
	if (health>maxhealth){
		this.setHealth(this.getMaxHealth());
	}
    }
}
