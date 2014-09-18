import java.io.*;
import java.util.*;
public class Warrior extends Character{
    public Warrior(){//Richard added
        health = 20;
        maxhealth = 20;
        dexterity = 8;
        strength = 8;
        intelligence = 8;
        name = "Arthur";
        charClass = "Warrior";
        damage = strength;
    }
    /*
public void attack(Character other) {
        Random r=new Random();
        int roll=r.nextInt(18); //three six-sided die roll implementation by Matthew
if (roll < dexterity) {
System.out.println("A hit!");
loseHealth(other,(damage*3)/2);
}
else {
System.out.println("A miss...");
}
}
*/
    

}