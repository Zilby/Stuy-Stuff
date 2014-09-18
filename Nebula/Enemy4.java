//Class for fourth enemy

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Enemy4 {

    private String s = "Enemy4.png";
    private int x; //ie xcor
    private int y; //ie ycor
    private int xinit; //x and y initial coordinates
    private int yinit;
    private int w; //width and height
    private int h;
    private Image image; 
    private String directh; //current direction horizontal
    private String initdir; //initial horizontal direction
    private boolean up = true;
    private Random r = new Random(); 
    private ArrayList missiles4; //holds all the missiles fired
    private boolean dead; //if dead will be removed
    private final int S_Size = 52; //for enemy's base size
    private int health = 12; 
    private int reload;
    private int movecount;
    private Random r1;
    private Random r2;

    public Enemy4() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for Enemy's area
        h = image.getHeight(null);
	dead = false;
	missiles4 = new ArrayList(); //initializes missiles
	r1 = new Random();
	r2 = new Random();
        x = 100 + r1.nextInt(400); //sets starting coordinates
        y = 50 + r2.nextInt(100); 
	xinit = x; //ie: x initial, y initial
	yinit = y;
	if(r.nextInt(10)%2 == 0) { //sets starting direction horizontal
	    directh = "R";
	} else {
	    directh = "L";
	}
	initdir = directh; //sets initial direction
	reload = 100 + r.nextInt(150);
	movecount = 2;
    }


    public void move() {
	//controls firing;
	if(reload == 0) {
	    fire();
	    reload = 200 + r.nextInt(150);
	} else {
	    reload--;
	}
	//controls horizontal movement
	if(movecount == 0){
	    if(directh.equals("R")) {
		x = x + 1;
	    }
	    if(directh.equals("L")) {
		x = x - 1;
	    }
	    movecount = 10;
	} else { 
	    movecount--;
	}
	//prevents from going offscreen horizontally from random
	if (x > 591) {
	    x = 9;
	}
	if (x < 6) { 
	    x = 588;
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

    public int getHealth() {
	return health;
    }
    
    public void setHealth(int i){
	health = i;
    }

    public boolean deceased() {
	return dead;
    }

    public void setDead(boolean Q) {
	dead = Q;
	if(Q = false){
	    health = 5;
	}
    }

    public Image getImage() {
        return image;
    }

    public ArrayList getMissiles() {
        return missiles4;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles4.size();i++){
	    missiles4.remove(i);
	}
    }
    
    public void fire() {
	if(!deceased()){
	    missiles4.add(new MissileB4(x + S_Size/2 + 5, y + S_Size + 10)); //creates missile object and adds to arraylist
	}
    }
}