import java.util.*;
import java.io.*;

public class MrMoran extends Character{
    public MrMoran(){
	name = "Mr.Moran";
	charClass = "Mr.Moran";
    }
    Random s = new Random();
    private int cooldown;

    public void setStrength(){
	strength = 8+level;
    }

    public void setDexterity(){
	dexterity = 8+level;
    }

    public void setIntelligence(){
	intelligence = 8 + level;
    }

    public void attack(Character c){
	if (cooldown != 0){
	    basicattack(c);
	}
	else{
	    if ((s.nextInt(10))<3)
		specialattack2(c);
	    else if ((s.nextInt(10))<5)
		specialattack1(c);
	    else
		basicattack(c);
	}
    }

    public void basicattack(Character c){
	Random r = new Random();
	int damage = 0;
	String aname = "Basic Attack";
	damage = intelligence + 2 + r.nextInt(3);
        if (cooldown > 0)
            cooldown = cooldown - 1;	
	if (hit()){
            c.loseHealth(damage);
            System.out.println (name + " has attacked " + c + " with " + aname + " and did " + damage + " damage!\n");
        }
        else {
            System.out.println ("Oooh! What a shame! " + name+ " has used " + aname + ", but missed!\n");
        }
    }
    public void specialattack1(Character c){
	int damage = 0;
	String aname = "";
        if (cooldown == 0){
	    damage = intelligence + 13;
	    aname = "Call Parent";
            cooldown = 3;
        }
	if (hit()){
            c.loseHealth(damage);
            System.out.println (name + " has attacked " + c + " with " + aname + " and did " + damage + " damage!\n");
        }
        else {
            System.out.println ("Oooh! What a shame! " + name+ " has used " + aname + ", but missed!\n");
        }
    }
    public void specialattack2(Character c){
	String aname = "";
	int damage = 0;
        if (cooldown == 0){
	    damage = intelligence + 25;
	    aname = "Confiscate Phone";
            cooldown = 5;
        }
	if (hit()){
            c.loseHealth(damage);
            System.out.println (name + " has attacked " + c + " with " + aname + " and did " + damage + " damage!\n");
        }
        else {
            System.out.println ("Oooh! What a shame! " + name+ " has used " + aname + ", but missed!\n");
        }
    }

}
