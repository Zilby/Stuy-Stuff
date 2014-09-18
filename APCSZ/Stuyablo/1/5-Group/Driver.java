import java.util.*;
import java.io.*;

public class Driver {

    public static Boolean play = true;

    public static void main(String[] args) {

	Scanner s = new Scanner(System.in);

	////STARTUP:
	playerCharacter p1 = Startup(s);
	Kracken A = new Kracken("Agbol",p1.lvl);
	Kracken B = new Kracken("Blib",p1.lvl);
	Kracken C = new Kracken("Chogg'du",p1.lvl);
	Kracken D = new Kracken("Dlo",p1.lvl);
	Kracken E = new Kracken("Eggbutt",p1.lvl);
	Kracken[] K = {A,B,C,D,E};
	A.x = 3;
	B.x = 1; B.y = 3;
	C.x = 3; C.y = 5;
	D.y = 7;
	E.x = 7; E.y = 7;
	////GAMEPLAY
	while (play){
	    for (int i = 0; i<5; i++){
		if (Math.abs(p1.x - K[i].x) <= 1 && Math.abs(p1.y -K[i].y) <= 1){
		    System.out.print("ENCOUNTER!" + "\n");
		    System.out.print("It's the notorious Kracken "+K[i].name + "\n");
		    while (K[i].hp >= 0 && p1.hp >=0){
			EncounterTurn(p1,K[i],s);
		    }
		}
	    }
	    //moving around
	    if (s.hasNext()){
		String in = s.next().toUpperCase();
		if (in.equals("W") && p1.y<7){
		    p1.y = p1.y + 1;
		    System.out.println (p1.x + ", " + p1.y);
		}
		else if (in.equals("A") && p1.x>0){
		    p1.x = p1.x - 1;
		    System.out.println (p1.x + ", " + p1.y);
		}
		else if (in.equals("S") && p1.y>0){
		    p1.y = p1.y - 1;
		    System.out.println (p1.x + ", " + p1.y);
		}
		else if (in.equals("D") && p1.x<7){
		    p1.x = p1.x + 1;
		    System.out.println (p1.x + ", " + p1.y);
		}
		else if (p1.x==7 || p1.y==7){
		    System.out.println("This game takes place on a square grid extending from (0,0) to (7,7). Sorry, but you may not go beyond this grid");
		}
		else if (in.equals("QUIT")){
		    play = false;
		}
		else if (in.equals("HELP")){
		    System.out.println("Press W to go up");
		    System.out.println("Press A to go left");
		    System.out.println("Press S to go down");
		    System.out.println("Press D to go right");
		    System.out.println("Type QUIT to stop playing");
		    System.out.println("Type HELP to see this message again");
		}
		else {
		    System.out.println("not a valid input, type HELP for valid inputs");
		}
	    }
	    if (K[0].x == 10 && K[1].x == 10 && K[2].x == 10 && K[3].x == 10 && K[4].x == 10) {
		System.out.println("YOU DID IT! YOU KILLED THEM ALL!");
		play = false;
	    }
	}
	s.close();
    }

    public static playerCharacter Startup(Scanner s) {
	playerCharacter c;
	System.out.print("\nWELCOME TO THE GAME!\n\n");
	//character type
	System.out.println("-Warrior");
	System.out.println("-Wizard");
	System.out.print("Which class would you like to be? ");
	int n = 1;
	String a = s.next();
	c = new Wizard();
	while (n>0){
	    if (a.toUpperCase().equals("WARRIOR")) {
		c = new Warrior();
		n = n-1;
	    }
	    else if (a.toUpperCase().equals("WIZARD")){
		c = new Wizard();
		n = n-1;
	    }
	    else{
		System.out.println("The computer doesn't understand, please type something that looks like 'warrior' or 'wizard'");
	    }
	}
	//name
	System.out.print("Please enter your Desired Name: ");
	c.name = s.next();
	System.out.println("");
	System.out.println("Greetings, young " + a + " named " + c.name  + "\n");
	//stats
	System.out.print("Do you wish to allocate your skill points Manually or Randomly? ");
	System.out.println("");
	Boolean done = false;
	while (!done){
	    a = s.next();
	    if (a.toUpperCase().equals("MANUALLY")) {
		int x = 8;
		while (x>0){
		    System.out.println("");
		    System.out.println("You have " + x + " attribute points left");
		
		    System.out.println("1. Strength");
		    System.out.println("2. Dexterity");
		    System.out.println("3. Intelligence");
		    System.out.println("4. Defense");
		    System.out.print("Select the number of the Attribute you would like to increase: ");
		    int attIncrease = s.nextInt();
		    if (attIncrease == 1) {
			c.str = c.str + 1;
			c.maxhp = c.maxhp + 1;
			c.hp = c.maxhp;
		    }
		    else if (attIncrease == 2) {
			c.dex = c.dex + 1;
		    }
		    else if (attIncrease == 3) {
			c.intl = c.intl + 1;
		    }
		    else if (attIncrease == 4){
			c.def = c.def + 1;
		    }
		    else {
			System.out.println("please just type 1, 2, 3, or 4");
		    }

		    x = x - 1;
		}
		done = true;
	    }
	    else if (a.toUpperCase().equals("RANDOMLY")){
		Random f = new Random();
		for(int x=8; x>0; x--) {
		    int y = f.nextInt(3);
		    if (y==1) {
			c.str = c.str + 1;
			c.maxhp = c.maxhp + 1;
		    }
		    else if (y==2) {
			c.dex = c.dex + 1;
		    }
		    else if (y==3) {
			c.intl = c.intl + 1;
		    }
		    else {
			c.def = c.def + 1;
		    }
		}
		done = true;
	    }
	    else if (s.hasNext()){
		System.out.println("Please input either 'Manually' or 'Randomly'");
	    }
	}
	System.out.println("\n You are on an 8 by 8 grid with 5 Krackens, defeat them all in a doomed attempt to win, type 'help' for help\n");
	System.out.println(c.x + ", " + c.y);
	return c;
    }

    public static void EncounterTurn (playerCharacter m, Kracken n, Scanner S){
	System.out.println(mult("|",n.hp) + n.name);
	System.out.println(mult("|",m.hp) + m.name);
	System.out.println("your turn");
	System.out.print("-attack\n-flee\n");
	m.turn(S,n);
	if (n.hp <= 0){
	    System.out.println("You defeated " + n.name + "!");
	    n.x = 10; n.y = 10;
	    System.out.println("You have gained 50 XP and regained all your health");
	    m.xp += 50;
	    m.hp = m.maxhp;
	    if (m.xp == 100) {
		m.levelUp();
	    }
	}
	else {
	    n.turn(m);
	    if (m.hp <= 0){
		System.out.println("You have died.");
		play = false;
	    }
	}
    }
    
    public static String mult(String s, int n){
	String result = s;
	for (n = n; n > 0; n--){
	    result = result + s;
	}
	return result;
    }
}

