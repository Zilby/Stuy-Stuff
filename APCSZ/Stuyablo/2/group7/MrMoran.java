import java.io.*;
import java.util.*;

public class MrMoran extends Character {
    public MrMoran() {
    	super("Mr. Moran", 10, 4, 7, false);
    }
    public int encounter(Character other) {
    	Random r = new Random();
    	int option = r.nextInt(5);
    	pause();
    	if (option == 0) {
            if (this.flee(other)) {
                return 1;
            }
            else {
                System.out.println("\n" + this + " tried to flee, but failed."); 
                return 5;
            }
        }
        else {
            this.attack(other);
            if (other.health > 0) {
                return 5;
            }
            else {
                return 3;
            } 
        }
    }
}