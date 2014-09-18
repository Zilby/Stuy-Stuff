import java.io.*;
import java.util.*;

public class Driver {

    public static void main(String[] args) {
        Warrior w = new Warrior("Warrior");
	Wizard wi = new Wizard("Wizard");
	Elf e = new Elf();
	WallOfMeat wom = new WallOfMeat();
	
	wi.encounter(e);
	System.out.println("---------------------");
	w.encounter(wom);
	System.out.println("---------------------");
	wom.encounter(e);
	System.out.println("---------------------");
    }
}
