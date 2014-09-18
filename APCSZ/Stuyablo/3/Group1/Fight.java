import java.util.*;
import java.io.*;

public class Fight {
    Player plr;
    Enemy foe;
    int round;
    Scanner input = new Scanner(System.in);

    public Fight(Player p, Enemy e) {
        plr=p;
        foe=e;
        round=1;
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
    public int swing() {
        int select;
        printStatus();
        while (plr.alive() && foe.alive()) {
            printCommands();
            //keep asking for input until get something valid
            select=-1;
            while (select<0 || select>4) {
                select = input.nextInt();
            }
            if (select==4) {
                if (playerturn(select)==1) {
                    System.out.println("You got away");
                    return 1;}
            } else {
                playerturn(select);
            }
            foe.lightAttack(plr);
            printStatus();

            if (!plr.alive() && !foe.alive()) {
                System.out.println("You both died");
                return 4;
            } else if (!plr.alive()) {
                System.out.println("You died");
                return 2;
            } else if (!foe.alive()) {
                System.out.println("You won the fight");
                return 3;
            }
        }
        System.out.println("DEBUG: Something broke.");
        return -1;
    }

    public void printStatus() {
        System.out.println("");
        System.out.println(plr.getStatus());
        System.out.println(foe.getStatus());
    }

    public void printCommands() {
        System.out.println("===(ROUND "+round+")===");
        System.out.println("Commands:");
        System.out.println("0. Light Attack");
        System.out.println("1. Heavy Attack");
        System.out.println("2. Spell NOT IMPLEMENTED");
        System.out.println("3. Item NOT IMPLEMENTED");
        System.out.println("4. Flee");
    }

    public int playerturn(int select) {
        System.out.println("");
        System.out.println("");
        System.out.println("");
        if (select == 0) {
            plr.lightAttack(foe);
        } else if (select == 1) {
            plr.heavyAttack(foe);
        } else if (select == 4) {
            if (plr.flee()) {return 1;}
        } else {
            System.out.println("Nope");
            return -1;
        }
        round=round+1;
        return 0;
    }
}