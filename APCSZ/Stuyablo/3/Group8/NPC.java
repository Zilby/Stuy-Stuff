import java.io.*;
import java.util.*;

public class NPC extends Character {
    Random r = new Random();
    public NPC() {
	Name = "Enemy";
	Level = 1;
	Health = 50;
	maxhealth = 50;
	Intelligence = 8;
	Strength = 8;
	Dexterity = 8;
	Mana = Intelligence * 2;
	experience = 0;
	gold = r.nextInt(1000);
	for (int i=8 ; i>0; i--) {
	    int pt = r.nextInt(3);
	    if (pt == 0) {
		Strength = Strength + 1;
	    } else if (pt == 1) {
		Intelligence = Intelligence + 1;
	    } else {
		Dexterity = Dexterity + 1;
	    }
	}
    }
}
