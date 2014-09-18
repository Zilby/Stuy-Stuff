import java.util.*;
import java.io.*;

public class Gnome extends Character {

    public Gnome (String name) {
	super(name);
    }

     public boolean flee() {
	 boolean result = true;
	 Random r = new Random();
	 String response = "";
	 int random = r.nextInt(100);
	 if (random > 50) {
	     response = "YES";
	 }
	 else {
	     response = "NO";
	 }
	 if (response == "YES") {
	     int roll = this.roll();
	     if (roll < this.dexterity && roll%2==0) {
		     result = true;
	     }
	     else {
		     result = false;
	     }
	 }
	 else if (response == "NO") {
	     result = false;
	 }
	 return result;
    }

    public void attack (Character other) {
	Random r = new Random();
	int random = r.nextInt(100);
	if (random > 50) {
	    other.health = other.health - 1;
	}
    }
}



	

    
