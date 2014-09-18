import java.io.*;
import java.util.*;

public class NPC extends Character{
    Random r = new Random();
    int x, y;

    public NPC (String name, double Pstr, double Pdex, double Pintl, double Pdef, int lvl){
	this.name = name;
	str = 8;
	maxhp = str;
	hp = maxhp;
	dex = 8;
	intl = 8;
	def = 8;
	this.lvl = lvl;
	for (int i = 0; i < (7+lvl); i++){
	    if (r.nextDouble()<Pstr){
		str = str + 1;
		maxhp = maxhp + 1;
		hp = maxhp;
	    }
	    else if (r.nextDouble()<Pdex){
		dex = dex + 1;
	    }
	    else if (r.nextDouble()<Pintl){
		intl = intl + 1;
	    }
	    else {
		def = def + 1;
	    }
	}
    }
    public NPC (String name, double Pstr, double Pdex, double Pintl, double Pdef){
	this.name = name;
	str = 8;
	dex = 8;
	intl = 8;
	def = 8;
	this.lvl = 1;
	for (int i = 0; i < 8; i++){
	    if (r.nextDouble()<Pstr){
		str = str + 1;
	    }
	    else if (r.nextDouble()<Pdex){
		dex = dex + 1;
	    }
	    else if (r.nextDouble()<Pintl){
		intl = intl + 1;
	    }
	    else {
		def = def + 1;
	    }
	}
	maxhp = str;
	hp = str;
    }
    public NPC (String Name){
	this.name = name;
	str = 10;
	dex = 10;
	intl = 10;
	def = 10;
    }
    
    public void attack (playerCharacter other, String type){
	int x = 0;
	if (type.equals("magic")){
	    x = intl - 2 - other.def;
	}
	else if (type.equals("melee")){
	    x = str - 2 - other.def;
	}
	if (x <= 1){
	    x = 1;
	}
	other.hp = other.hp - x;
	System.out.print(name + " attacked!\n");
    }
}
