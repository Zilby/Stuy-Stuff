import java.io.*;
import java.util.*;

public class Warrior extends Character{
    public Warrior(String name){
        super(name);
        super.dx = 8;
        super.st  = 10;
        super.iq = 6;
        super.hp = super.st;
    }
    //Warrior special attack/spell. Does 4 damage
    public void specialAttack(Character other){
        System.out.println("Used special attack 'Power Strike'");
        int hitroll = this.roll(3,6);
        System.out.println(this.getName() + " rolled " + hitroll);
        System.out.println(this.getName() + "'s effDex: " + (getEffDx()));
        if (hitroll < this.getEffDx()){
            other.setHp(other.getHp()-4);
            System.out.println("Attack successful");
        } else {
            System.out.println("Attack missed");
        }
    }
}
