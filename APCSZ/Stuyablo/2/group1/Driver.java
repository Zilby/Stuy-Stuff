import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	Character player;
	player = new Character();

	player.setChar();

	while (player.turn()) {
	    player.turn();
	}
    }
}
	       
	
