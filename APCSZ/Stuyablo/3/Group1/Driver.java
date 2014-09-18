import java.util.*;
import java.io.*;

public class Driver {
    public static void main(String[] args) {
        Game g = new Game();
        Character c = new Character("Character 1");   
        System.out.println(c.getStatus());
        Warrior w1 = new Warrior("Warrior");
        System.out.println(w1.getStatus());
        Game game = new Game();

        game.turn(w1,c);

    }
} 
