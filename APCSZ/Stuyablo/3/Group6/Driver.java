import java.io.*;
import java.util.*;

public class Driver {

    public static void main(String[] args) {

	Warrior w = new Warrior("Warrior");
	Ogre c = new Ogre();
	Thief t = new Thief();
	GoblinMage m = new GoblinMage();

	/*
	This driver has been separated into four main blocks of code. 
	The first three  blocks run PC vs. NPC battles.  The first is Warrior vs. Ogre,
        the next is Thief vs. Ogre, and the last is Warrior vs. GoblinMage.
	The last block runs an NPC vs NPC battle for GoblinMage vs Ogre.
	Uncomment the block you want to run, and
	comment out the blocks you don't want to run.
	*/

	
	c.setAttributes();
	w.Startup();
	System.out.println(w.name + " faces " + c.name + "\n" + "Status:\n" + c.getStatus());
	for (int i = 1, j = 0; w.getHealth() > 0 && c.getHealth() > 0 && j==0; i++) {
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("Round " + i);
	    int e1 = w.encounter(c);
	    if (e1 == 0)
		j = 1;
	    System.out.println(w.getStatus());
	    System.out.println(c.getStatus());
	    System.out.println();
	    if (j==0 && c.health > 0){
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("---Ogre's Response---\n");
	    int e2 = c.encounter(w);
	    if (e2 == 0)
		j = 1;
	    System.out.println(w.getStatus());
	    System.out.println(c.getStatus());
	    }
	    System.out.println("------------------------");
	}
	


	/*
	c.setAttributes();
	t.Startup();
	System.out.println(t.name + " faces " + c.name + "\n" + "Status:\n" + c.getStatus());
	for (int i = 1, j = 0; t.getHealth() > 0 && c.getHealth() > 0 && j==0; i++) {
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("Round " + i);
	    int e1 = t.encounter(c);
	    if (e1 == 0)
		j = 1;
	    System.out.println(t.getStatus());
	    System.out.println(c.getStatus());
	    System.out.println();
	    if (j==0 && c.health > 0){
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("---Ogre's Response---\n");
	    int e2 = c.encounter(t);
	    if (e2 == 0)
		j = 1;
	    System.out.println(t.getStatus());
	    System.out.println(c.getStatus());
	    }
	    System.out.println("------------------------");
	}
	*/


	/*
	w.Startup();
	System.out.println(w.name + " faces " + m.name + "\n" + "Status:\n" + m.getStatus());
	for (int i = 1, j = 0; w.getHealth() > 0 && m.getHealth() > 0 && j==0; i++) {
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("Round " + i);
	    int e1 = w.encounter(m);
	    if (e1 == 0)
		j = 1;
	    System.out.println(w.getStatus());
	    System.out.println(m.getStatus());
	    System.out.println();
	    if (j==0 && m.health > 0){
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("---Goblin Mage's Response---\n");
	    int e2 = m.encounter(w);
	    if (e2 == 0)
		j = 1;
	    System.out.println(w.getStatus());
	    System.out.println(m.getStatus());
	    }
	    System.out.println("------------------------");
	}
	*/

	/*
	c.setAttributes();
	System.out.println(m.name + " faces " + c.name + "\n" + "Status:\n" + m.getStatus()+"\n"+c.getStatus());
	for (int i = 1, j = 0; m.getHealth() > 0 && c.getHealth() > 0 && j==0; i++) {
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("Round " + i);
	    int e1 = m.encounter(c);
	    if (e1 == 0)
		j = 1;
	    System.out.println(m.getStatus());
	    System.out.println(c.getStatus());
	    System.out.println();
	    if (j==0 && c.health > 0){
	    try{Thread.sleep(2000);}catch(InterruptedException ex){}
	    System.out.println("---Ogre's Response---\n");
	    int e2 = c.encounter(m);
	    if (e2 == 0)
		j = 1;
	    System.out.println(m.getStatus());
	    System.out.println(c.getStatus());
	    }
	    System.out.println("------------------------");
	}
	*/


    }
}
