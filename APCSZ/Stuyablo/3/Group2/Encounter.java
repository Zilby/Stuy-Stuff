import java.util.*;
import java.io.*;

public class Encounter {
    
    public boolean encounter (Character p1, Character p2) {
	boolean playmore = true;
        while (true) {
	    playmore =  p1.encounter(p2);
	    if (!playmore) {
		p1.changeEP(p2.getEp());
		p1.levelup();
		return playmore;
	    }
	    playmore = p2.encounter(p1);
	    if (!playmore) {
		p2.changeEP(p1.getEp());
		p2.levelup();
		return playmore;
	    }
	    System.out.println(p1 + "'s health: " + p1.getHp());
	    System.out.println(p2 + "'s health: " + p2.getHp());
	}
    }
}