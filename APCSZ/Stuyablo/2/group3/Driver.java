import java.io.*;
import java.util.*;

public class Driver {

    public static void main (String[] args) {

        Character[] npc = null;
        Random r = new Random();
        Scanner sc = new Scanner(System.in);
     
        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        String type = new String();
        Character player = new Character(name);
        int x = 0;

        while ( x == 0 ) {
            System.out.print("Which type of character do you want to be? (Warrior, Wizard, or Rogue): ");
            type = sc.nextLine();
            if ( type.equalsIgnoreCase ( "Warrior" ) ) {
                player = new Warrior ( name );
                x = 1;
            }
            else if ( type.equalsIgnoreCase ( "Wizard" ) ) {
                player = new Wizard ( name );
                x = 1;
            }
            else if ( type.equalsIgnoreCase ( "Rogue" ) ) {
                player = new Rogue ( name );
                x = 1;
            }
            else
                System.out.println ("Misspelled character type");
        }

        // GOD Mode
        if (args.length != 0) {
            player.health = player.str = player.dex = player.iq = Integer.MAX_VALUE / 2;
            System.out.println("\nGOD MODE ENABLED: RUNNING GAME LIKE YOU'RE GOD");
        }

        while (player.health > 0) {

            if (npc == null || npc.length <= 1) {
                npc = new Character[r.nextInt(26) + 15];
                for (int i=1; i<npc.length; i++) {
                    npc[i] = new Ogre("Ogre " + i, player);
                }
                npc[0] = new Moran("BOSS: MR.MORAN", player);
            }

            System.out.println(String.format("\nWhat would you line to do? (Attack nearest enemy(a), move(m), status(s), or distribue %d skills(d) ): ", player.skills));
            String choice = sc.nextLine();

            int[] xArray = new int [ npc.length - 1 ];
            int[] yArray = new int [ npc.length - 1 ];
            for ( int j = 0 ; j < npc.length - 1; j++ ) {
                xArray [ j ] = npc [ j ].xcor;
                yArray [ j ] = npc [ j ].ycor;
            }
            String map = new String();
            containsI p = new containsI();
            //System.out.println( Arrays.toString ( xArray ) + "\n" + Arrays.toString ( yArray ) + "\n" + p.count ( yArray , 9 ) );
            for ( int i = 0 ; i < xArray.length ; i++ )
                System.out.println ( npc[i] + ": " + xArray[i] + ", " + yArray [ i ] );
	    /*
            for ( int k = player.gridRange ; k >= (-1 * player.gridRange) ; k-- ) {
                if ( p.containsInt ( yArray, k ) ) {
                    int index = p.findInt ( yArray ,k );
                    int other = xArray [ index ];
                    for ( int l = (-1 * player.gridRange) ; l < other ; l++ ) {
                        map = map + "-";
                    }
                    map = map + "E";
                    for ( int m = other + 1 ; m <= player.gridRange ; m++ ) {
                        map = map + "-";
                    }
                }
                else {
                    for ( int i = (-1 * player.gridRange) ; i <= player.gridRange ; i++ ) {
                        map = map + "-";
                    }
                }
                map = map + "\n";
		}*/
            for ( int k = player.gridRange ; k >= ( -1 * player.gridRange ) ; k-- ) {
                map = map + p.mapRow ( xArray , yArray , k , player.gridRange );
            }
            System.out.println ( "Your coordinates: " + player.xcor + ", " + player.ycor );
            int row = player.gridRange - player.ycor;
            int column = player.gridRange + 1 + player.xcor;
            String map1 = map.substring ( 0 , row * (player.gridRange * 2 + 2) + column - 1 );
            String map2 = map.substring ( row * (player.gridRange * 2 + 2) + column );
            System.out.println ( map1 + "Y" + map2 );

            if (choice.equalsIgnoreCase("m")) {
                boolean badChoice = true;
                System.out.println("Which direction would you like to go? ((u)p, (d)own, (l)eft, (r)ight)");
                while (badChoice) {
                    badChoice = false;
                    String dir = sc.nextLine();
                    if (dir.equalsIgnoreCase("u")) {
                        if ( player.ycor < player.gridRange )
                            player.ycor = player.ycor + 1;
                        else
                            System.out.println ( "Out of bounds" );
                    }
                    else if (dir.equalsIgnoreCase("d")) {
                        if ( player.ycor > (-1 * player.gridRange ))
                            player.ycor = player.ycor - 1;
                        else
                            System.out.println ( "Out of bounds" );
                    }
                    else if (dir.equalsIgnoreCase("l")) {
                        if ( player.xcor > (-1 * player.gridRange ))
                            player.xcor = player.xcor - 1;
                        else
                            System.out.println ( "Out of bounds" );
                    }
                    else if (dir.equalsIgnoreCase("r")) {
                        if ( player.xcor < player.gridRange )
                            player.xcor = player.xcor + 1;
                        else
                            System.out.println ( "Out of bounds" );
                    }
                    else {
                        badChoice = true;
                        System.out.println ( "Misspelled direction" );
                    }
                }
                if (Math.random() < 1/4.)
                    player.health++;
            }

            else if (choice.equalsIgnoreCase("a")) {
                if (player.encounter(npc)) {
                    int healthLeft = player.health;
                    boolean fleeSuccess = true;
                    battle: // Label for battle loop, used in nested loops to break out of this one
                    while (player.getEnemy().health > 0 && player.health > 0) {
                        player.attack();
                        if (player.getEnemy().health > 0) {
                            player.getEnemy().attack();
                            if (player.health <= 0) {
                                player.die(player.getEnemy());
                                break battle;
                            }
                            else if ((player.health < 8 && player.health != healthLeft) || !fleeSuccess) {
                                boolean badChoice = true;
                                System.out.println("You're almost about to die with your " + player.health + " health remaining! But your enemy has " + player.getEnemy().health + " health remaining!\nWould you like to continue attacking(a) or would you rather flee for your life(f)?");
                                while (badChoice) {
                                    badChoice = false;
                                    choice = sc.nextLine();
                                    if (choice.equalsIgnoreCase("a"))
                                        healthLeft = player.health;
                                    else if (choice.equalsIgnoreCase("f")) {
                                        if (player.flee()) {
                                            player.setEnemy(null);
                                            System.out.println("\nYou have succesfully ran away from the battle! Move around to get more life :)\nTip: Increase your dexterity if you are missing a lot.");
                                            break battle;
                                        }
                                        else {
                                            fleeSuccess = false;
                                            System.out.println("\nYou tried to run away, but " + player.getEnemy() + " has caught up to you!");
                                        }
                                    }
                                    else {
                                        badChoice = true;
                                        System.out.println("Not sure if you want to continue attacking(a) or flee(f): ");
                                    }
                                }
                            }
                            try {
                                Thread.sleep(50);
                            }
                            catch (Exception e) {
                            }
                        }
                        else {
                            player.getEnemy().die(player);
                            break battle;
                        }
                    }
                    Character[] tempNpc = new Character[npc.length - 1];
                    int offset = 0;
                    for (int i=0; i<tempNpc.length; i++) {
                        if (npc[i].equals(player.getEnemy())){
                            offset -= 1;
                        }
                        else {
                            tempNpc[i + offset] = npc[i];
                       }
                    }
                    npc = tempNpc;
                }
            }

            else if (choice.equalsIgnoreCase("s")) {
                System.out.println(String.format("Class: %s\nLevel: %d\nExperience: %d/%d\nHealth: %d\nStrength: %d\nDexterity: %d\nIntelligence %d\n", player.charClass, player.level, player.exp, (int) (50 + Math.pow(2, player.level)), player.health, player.str, player.dex, player.iq));
            }

            else if (choice.equalsIgnoreCase("d")) {
                int add;
                System.out.println(String.format("You have %d skill points to distribute amongst your strength, dexterity, and intelligence.", player.skills));
                System.out.println(String.format("How much would you like to add to your %d strength? %d skill points remaining.", player.str, player.skills));
                while (!(sc.hasNextInt())) {
                    System.out.println("Please input a number!");
                    sc = new Scanner(System.in);
                }
                add = sc.nextInt();
                while (add > player.skills) {
                    System.out.println(String.format("You don't have %d skill points to spend! Choose again.", add));
                    add = sc.nextInt();
                }
                player.skills -= add;
                player.str += add;
                System.out.println(String.format("How much would you like to add to your %d dexterity? %d skill points remaining.", player.dex, player.skills));
                while (!(sc.hasNextInt())) {
                    System.out.println("Please input a number!");
                    sc = new Scanner(System.in);
                }
                add = sc.nextInt();
                while (add > player.skills) {
                    System.out.println(String.format("You don't have %d skill points to spend! Choose again", add));
                    add = sc.nextInt();
                }
                player.skills -= add;
                player.dex += add;
                System.out.println(String.format("How much would you like to add to your %d intelligence? %d skill points remaining.", player.iq, player.skills));
                while (!(sc.hasNextInt())) {
                    System.out.println("Please input a number!");
                    sc = new Scanner(System.in);
                }
                add = sc.nextInt();
                while (add > player.skills) {
                    System.out.println(String.format("You don't have %d skill points to spend! Choose again", add));
                    add = sc.nextInt();
                }
                player.skills -= add;
                player.iq += add;
            }

            else
                System.out.println ( "Please enter a valid command" );

            if (player.exp >= (50 + Math.pow(2, player.level))) {
                player.level = player.level + 1;
                player.exp = 0;
                player.str++;
                player.dex++;
                player.iq++;
                player.skills += 2;
                System.out.println ( "Congratulations! You have leveled up to level " + player.level );
                player.health = player.str;
            }
        }
        System.out.println(String.format("\nOH NOES! YOU HAVE DIED! :(\nYour legacy as a level %d %s will stay in our hearts. <3", player.level, player.charClass));
    }
}
