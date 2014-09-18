//Class for third enemy

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Enemy3 {

    private String s = "Enemy3.png";
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
    private ArrayList missiles3; //holds all the missiles fired
    private boolean dead; //if dead will be removed
    private final int S_Size = 30; //for enemy's base size
    private int health = 5; 
    private int reload;

    public Enemy3() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for Enemy's area
        h = image.getHeight(null);
	dead = false;
	missiles3 = new ArrayList(); //initializes missiles
	Random r1 = new Random();
	Random r2 = new Random();
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
	reload = 50+r.nextInt(100);
    }


    public void move() {
	//controls firing;
	if(reload == 0) {
	    fire();
	    reload = 100 + r.nextInt(150);
	} else {
	    reload--;
	}
	//controls horizontal movement
	if(directh.equals("R")) {
	    x = x + 2;
	    if(x > 500){ //turns around at 500
		directh = "L";
	    }
	}
	if(directh.equals("L")) {
	    x = x - 2;
	    if(x < 100){ //and 100
		directh = "R";
	    }
	}
	//prevents from going offscreen horizontally from random
	if (x > 591) {
	    x = 9;
	}
	if (x < 6) { 
	    x = 588;
	}
	//for vertical movement
	if(initdir.equals("R")){ //note that this is initdir not directh
	    if(x > 460){ //will go up at endpoints and down again
		y++;
	    }
	    if(x < 140){
		y--;
	    }
	} else {
	    if(x > 460){
		y--;
	    }
	    if(x < 140){
		y++;
	    }
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
        return missiles3;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles3.size();i++){
	    missiles3.remove(i);
	}
    }
    
    public void fire() {
	if(!deceased()){
	    missiles3.add(new MissileB3(x + S_Size/2, y + S_Size)); //creates missile object and adds to arraylist
	}
    }
}