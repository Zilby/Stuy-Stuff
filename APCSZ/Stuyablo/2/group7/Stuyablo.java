import java.io.*;
import java.util.*;

public class Stuyablo {
    public void fight(Character one, Character two) {
        pause();
        pause();
        boolean oneHasMoreDex = one.dexterity >= two.dexterity;
        int turn = 1;
        int options1 = 5, options2 = 5;
        if (!(oneHasMoreDex)) {    
            fight(two, one);
        }
        while (options1 == 5 && options2 == 5) {
            if (options1 != 5 || options2 != 5 || one.getHealth() <= 0 || two.getHealth() <= 0) {
                break;
            }
            pause();
            System.out.println("\n~~~\nTurn: "+ turn+ "\n\n" + one + "'s health: " + one.getHealth());
            turn = turn + 1;
            System.out.println(two + "'s health: " + two.getHealth());
            options1 = one.encounter(two);
            if (options1 == 5) {
                options2 = two.encounter(one);
            }
            else if (options1 == 1) {
                System.out.println("\n" + one + " fled!");
            }
            else if (options1 == 3) {
                System.out.println("\n" + two + " died!");
            }
            if (options2 == 1) {
                System.out.println("\n" + two + " fled!");
            }         
            else if (options2 == 3) {
                System.out.println("\n" + one + " died!");
            } 
        }           
    }

    public void pause() {
        try {
            Thread.sleep(500); // pause for that many milliseconds
        } 
        catch (Exception e) {
                // do nothing here - it should never get run 
        }
    }   
}