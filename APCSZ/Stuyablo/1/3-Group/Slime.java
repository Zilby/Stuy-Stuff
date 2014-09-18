import java.io.*;
import java.util.*;

public class Slime extends NPC {
    
    public Slime(){
	super();
	name = "Slime";
	strength = strength - 2;
	dexterity = dexterity + 2;
    }

    public void Talk(){
	System.out.println("The slime squelches.");
    }
}
