import java.io.*;
import java.util.*;

public class NPC extends Character{
    
    public NPC(){
	dexterity = 6;
	strength = 6;
	intelligence = 6;
	Random r = new Random();
	strength = strength + r.nextInt(3);
	dexterity = dexterity + r.nextInt(3);
	intelligence = intelligence + r.nextInt(3);
	health = 50 + ((strength - 8)*4);
    }
    
   

}

