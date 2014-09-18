import java.io.*;
import java.util.*;

public class Character {
    protected int hp, maxhp, xp, lvl, str, dex, intl, def;
    protected int x, y;
    protected String name;
    private Random r = new Random();

    protected void init(String name) {
	this.name = name;
	this.hp = maxhp;
	this.lvl = 1;
    }

    public Character () {
	init("No Name");
    }
    
    public Character (String name) {
	init(name);
    }

    public String attack () {
	return "Generic attack";
    }

    // public String toString () {
    // 	return name;
    // }
    
    public void subHealth (int x) {
	hp = hp - x;
    }

    public void levelUp() {
	Scanner S = new Scanner(System.in);
	Boolean a = false;
	System.out.println("Congratulations, you've leveled up! Please input str, dex, intl, or def to level up a stat");
	while (!a){
	    String stat = S.next();
	    String result;
	    if (stat == "str") {
		str = str + 1;
		hp = hp + 1;
		result  = "Leveled up str and hp. str and hp = " + str;
		a = true;
	    }
	    else if (stat == "dex") {
		dex = dex + 1;
		result  = "Leveled up dex. dex= " + dex;
		a = true;
	    }
	    else if (stat == "intl"){
		intl = intl+ 1;
		result  = "Leveled up intl. intl = " + intl;
		a = true;
	    }
	    else if (stat == "def") {
		def = def + 1;
		result  = "Leveled up def. def = " + def;
		a = true;
	    }
	    else {
		result = "Unable to level up a stat. Please input one of the following stats to level up: 'str', 'dex', 'intl', or 'def'."; 
	    }
	    System.out.println(result);
	}
    }
    /*
      public String  equipWeapon(String weapon) {
      String result = "";
      if( weapon.equals("Hammer")){
      str = str + 5;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else if( weapon.equals("Sword")){
      str = str + 20;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else if( weapon.equals("Wand")){
      intl = intl + 5;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else if( weapon.equals("Staff")){
      intl = intl + 20;
      result = name + " has sucessfully equipped a " + weapon + ".";
      }
      else {
      result =  "Unable to equip weapon. Please select a weapon from the list.";
      }
      return result;
      }
    */
}
