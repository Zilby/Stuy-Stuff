import java.io.*;
import java.util.*;

public class BossMoranNPC extends Character {
    
    public BossMoranNPC(){
	Random n = new Random();
	name = "Boss Moron";
	charType = "Moran";
	strength = 15 + n.nextInt(5);
	dexterity = 10+n.nextInt(5);
	defense = 14+n.nextInt(5);
	maxhealth = strength;
	health = maxhealth;
	charm = 0;
    }
}
