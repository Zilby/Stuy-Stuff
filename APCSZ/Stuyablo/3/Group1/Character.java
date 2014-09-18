import java.io.*;
import java.util.*;

/* st = Strength
   dx = Dexterity
   iq = Intelligence
*/

public class Character {
    protected int hp;
    protected int st,dx,iq;
    protected int exp;
    protected int statpt;
    protected int gold;
    protected double x,y,distance;
    protected String name;
    protected String charClass;
    protected Random rand = new Random();

    public int roll(int diceNumber, int diceSize){
        int i = 0;
        int diceSum = 0;
        while (i < diceNumber){
            diceSum = diceSum + 1 + rand.nextInt(diceSize);
            i++;
        }
        return diceSum;
    }

    public Character(String name){
        this.name = name;
        st = 8;
        dx = 8;
        iq = 8;
        hp=st;
    }

    public String toString() {return name;}
    public String getName() {return name;}
    public int getHp() {return hp;}
    public int getSt() {return st;}
    public int getDx() {return dx;}
    public int getIq() {return iq;}

    //placeholders until we actually have status effects and stuff
    public int getEffSt() {return st;}
    public int getEffDx() {return dx;}
    public int getEffIq() {return iq;}
	//again
    public void setEffSt(int St) {this.st = St;}
    public void setEffDx(int Dx) {this.dx = Dx;}
    public void setEffIq(int Iq) {this.iq = Iq;}

    public boolean alive() {return hp>0;}

    public void setHp(int hp){this.hp = hp;} //dunno if this will get used much
    public void hurt(int dam) {
        if (dam<0) 
            this.hp = this.hp - dam;
    }
    
    public void heal(int dam) {
        if (dam<0)
        this.hp = this.hp + dam;
    }

    // I put roll method here because roll method is necessary in many 
    // methods in this class such as attack methods            

    
    public void lightAttack(Character other) {
        /* do the attack:
           print out the attempt and the result and update
           all relavent variables
        */
        int hitroll = this.roll(3,6);
        System.out.println(this.getName() + " rolled " + hitroll);
        System.out.println(this.getName() + "'s effDex + 1: " + (getEffDx()-1));
        if (hitroll < this.getEffDx()+1){ //Plus 1 is to make this attack more accurate
            other.setHp(other.getHp()-1);
            System.out.println("Attack successful");
        } else {
            System.out.println("Attack missed");
        }
    }

    public void heavyAttack(Character other) {
        int roll = this.roll(3,6);
        System.out.println(this.getName() + " rolled " + roll);
        System.out.println(this.getName() + "'s effDex - 1: " + (getEffDx()-1));
        if (roll < this.getEffDx()-1){ //Minus 1 is to make this attack less accurate
            other.setHp(other.getHp()-2);
            System.out.println("Heavy attack successful");
        } else {
            System.out.println("Attack missed");
        }
    }
    public void specialAttack(Character other){

    }
    
    // returns true if you succesfully flee, false otherwise
    public boolean flee() { //I don't see why you need Character other in parameter
                boolean success = false;
                if (this.roll(2, dx/2) >= dx/2) {
                        success = true;
                }
        return success;
    }


    /*
      this routine will decide first ask if other tries to flee. If
      so, and if it's succesful it should adjust experience and or
      gold as needed and return a 0.

      Then, it should decide if this character tries to flee. 
      If so and it's succesful, return a 1;
      
      Otherwise, call attack on both sides:
      this.attack(other);
      if (other.health>0) 
        other.attack(this);

      and then return 2 if this is dead, 3 if other is dead, 4 if both dead, 5 if none dead.

    */
    public int encounter(Character other,String command) {
        boolean playerDied = false;
        boolean opponentDied = false;
        if (command.equals("Light Attack")){
            this.lightAttack(other);
            if (other.getHp() <= 0)
                opponentDied = true;
            other.lightAttack(this);
            if (this.getHp() <= 0)
                playerDied = true;
        }
        if (command.equals("Heavy Attack")){
            this.heavyAttack(other);
            if (other.getHp() <= 0)
                opponentDied = true;
            other.lightAttack(this);
            if (this.getHp() <= 0)
                playerDied = true;
        }
        if (command.equals("Special Attack")){
            specialAttack(other);
            if (other.getHp() <= 0)
                opponentDied = true;
            other.lightAttack(this);
            if (this.getHp() <= 0)
                playerDied = true;
            
        }
        if (command.equals("Flee")){
            if (this.flee())
                return 1;
        }
        System.out.println("This Character's status: ");
        System.out.println(this.getStatus());
        System.out.println("Other Character's status: ");
        System.out.println(other.getStatus());
                
        if (playerDied && opponentDied)
            return 4;
        else if (playerDied)
            return 2;
        else if (opponentDied)
            return 3;
        else
            return 5;
    }

    public String getStatus() {
        String attrib1=String.format("Name:%s St: %d Dx: %d Iq: %d",
                                     name, st, dx, iq);
        String attrib2=String.format("Exp: %d Health: %d of %d",
                                     exp,hp,st);
        String locale = String.format("x: %5.2f y: %5.2f",x,y);
        String whole=String.format("%s\n%s\n%s\n",
                                   attrib1,attrib2,locale);
        return whole;
    }
}
