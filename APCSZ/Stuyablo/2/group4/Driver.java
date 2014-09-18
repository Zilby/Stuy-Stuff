import java.io.*;
import java.util.*; 
public class Driver {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	System.out.println("What is your name, warrior?");
	String name = sc.nextLine();
	Player a = new Player(name);
        Ogre b = new Ogre();
        a.encounter(b);
    }
}
