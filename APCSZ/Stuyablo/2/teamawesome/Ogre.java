import java.io.*;
import java.util.*;
public class Ogre extends Character{
    Random r = new Random();
    public Ogre(){
	maxhealth = 14 + (r.nextInt(6) - 2);
	health = maxhealth;
	strength = 8 + (r.nextInt(6) - 2);
	dexterity = 10 + (r.nextInt(6) - 2);
	intelligence = 5 + (r.nextInt(6) - 2);
	damage = strength;
	experience = 10;
	gold = 10;
	name = "Steve the Ogre";
    }
}

