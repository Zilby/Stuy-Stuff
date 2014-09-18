//Class for first enemy

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Enemy1 {

    private String s = "Enemy.png";
    private int x; //ie xcor
    private int y; //ie ycor
    private int xinit; //x and y initial coordinates
    private int yinit;
    private int w; //width and height
    private int h;
    private Image image; 
    private String directh; //current direction horizontal and vertical
    private String directv;
    private int reload; //how long until next missile
    private Random r = new Random(); 
    private ArrayList missiles1; //holds all the missiles fired
    private boolean dead; //if dead will be removed
    private final int S_Size = 30; //for enemy's base size

    public Enemy1() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for Enemy's area
        h = image.getHeight(null);
	dead = false;
	missiles1 = new ArrayList(); //initializes missiles
	Random r1 = new Random();
	Random r2 = new Random();
        x = 80 + r1.nextInt(440); //sets starting coordinates
        y = 70 + r2.nextInt(120); 
	xinit = x; //ie: x initial, y initial
	yinit = y;
	if(r.nextInt(10)%2 == 0) { //sets starting direction horizontal
	    directh = "R";
	} else {
	    directh = "L";
	}
	if(r.nextInt(10)%2 == 0) { //sets starting direction vertical
	    directv = "U";
	} else {
	    directv = "D";
	}
	reload = 3 + r.nextInt(15); //sets time until first bullet (very short)
    }


    public void move() {
	//controls horizontal movement
	if(directh.equals("R") && x - xinit <= 70) {
	    x++;
	} else {
	    directh = "L";	     
	    x = x - r.nextInt(5); //slightly randomized
	}
	if(directh.equals("L") && x - xinit >= -70) {
	    x--;
	} else {
	    directh = "R";
	    x = x + r.nextInt(5);
	}
	//controls vertical movement
	if(directv.equals("U") && y - yinit <= 70) {
	    y++;
	} else {
	    directv = "D";	     
	}
	if(directv.equals("D") && y - yinit >= -70) {
	    y--;
	} else {
	    directv = "U";
	}

	//prevents from going offscreen horizontally from random
	if (x > 591) {
	    x = 9;
	}
	if (x < 6) { 
	    x = 588;
	}
	//controls firing
	if(reload == 0) {
	    fire();
	    reload = 50 + r.nextInt(100);
	} else {
	    reload--;
	}
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public Rectangle getArea() { //gives ship's area
        return new Rectangle(x, y, w, h);
    }

    public boolean deceased() {
	return dead;
    }

    public void setDead(boolean Q) {
	dead = Q;
    }

    public Image getImage() {
        return image;
    }

    public ArrayList getMissiles() {
        return missiles1;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles1.size();i++){
	    missiles1.remove(i);
	}
    }
    
    public void fire() {
	if(!deceased()){
	    missiles1.add(new MissileB(x + S_Size/2, y + S_Size)); //creates missile object and adds to arraylist
	}
    }
}