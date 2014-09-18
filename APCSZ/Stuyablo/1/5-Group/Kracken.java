import java.io.*;
import java.util.*;

public class Kracken extends NPC {
    private int intim;
    private Random rand = new Random();
    
    public Kracken (String name, int intim, int Pstr, int Pdex, int Pintl, int Pdef) {
	super(name, Pstr, Pdex, Pintl, Pdef);
	this.intim = intim;
    }

    public Kracken (String name, int lvl){
	super(name, 0.4, 0.5, 0.6, 1.0);
	this.intim = 12;
    }

    public void tentaSmack(playerCharacter other){
	int x = rand.nextInt(str)/2 + rand.nextInt(str)/2;
	x = x - other.def;
	if (x > 0){
	    other.hp = other.hp - x;
	    System.out.print(name + " used tentaSmack" + "\n");
	}
	else {
	    System.out.print(name + " missed!\n");
	}
    }

    public void glare (playerCharacter other) {
	int x = intim;
	x = x - (other.str + other.intl + other.dex + other.def) / 4;
	if (x <= 1){
	    x = 1;
	}
	other.dex = other.dex - x;
	System.out.print(name + " just used glare\n" +  other.name + "'s dex is now " + other.dex + "\n");
    }

    public void turn(playerCharacter other){
	if (r.nextDouble() < 0.5){
	    attack(other,"melee");
	}
	else if (r.nextDouble() < 0.8){
	    tentaSmack(other);
	}
	else {
	    glare(other);
	}
    }
}
