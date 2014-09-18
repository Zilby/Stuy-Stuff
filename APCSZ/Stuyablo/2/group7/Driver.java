import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stuyablo s = new Stuyablo();
        System.out.println("What kind of game would you like?\n1 - Player vs Player\n2 - Player vs NPC\n3 - NPC vs NPC");
        System.out.print(">");
        Character c1 = new Character("name",8,8,8,false);
        Character c2 = new Character("name",8,8,8,false);
        int option = sc.nextInt();
        if (option == 1){
            c1 = c1.createNew();
            c2 = c2.createNew();
        }
        else if (option == 2) {
            System.out.println("Who would you like to play against?\n1 - Ogre\n2 - Mr. Moran");
            System.out.print(">");
            int enemy = sc.nextInt();
            c1 = c1.createNew();
            if (enemy == 2) {
                c2 = new MrMoran();
            }
            else {
                c2 = new Ogre("Ogre");
            }
        }
        else if (option == 3) {
            c1 = new Ogre("Ogre");
            c2 = new MrMoran();
        }
        else {
            System.out.println("You can't follow directions, so I'll make you watch Mr.Moran fight an ogre.");
            c1 = new Ogre("Ogre");
            c2 = new MrMoran();        
        }
        System.out.println("\n" + c1.getStatus() + "\n" + c2.getStatus());
        s.fight(c1, c2);    
    }
}