import java.util.*;
import java.io.*;

public class GameDriver {
    public static void main (String[] args) {
        Human h = new Human("Jerry the Human");
	Gnome g = new Gnome("Fred the Gnome");
	System.out.println(h.encounter(g));
    }
}

