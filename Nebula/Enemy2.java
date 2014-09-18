//Class for second enemy

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Enemy2 {

    private String s = "Enemy2.png";
    private int x; //ie xcor
    private int y; //ie ycor
    private int xinit; //x and y initial coordinates
    private int yinit;
    private int w; //width and height
    private int h;
    private Image image; 
    private String directh; //current direction horizontal
    private int jump; //how long until next jump
    private int airborn = 10; // how long airborn
    private boolean up = true;
    private Random r = new Random(); 
    private ArrayList missiles2; //holds all the missiles fired
    private boolean dead; //if dead will be removed
    private final int S_Size = 30; //for enemy's base size

    public Enemy2() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for Enemy's area
        h = image.getHeight(null);
	dead = false;
	missiles2 = new ArrayList(); //initializes missiles
	Random r1 = new Random();
	Random r2 = new Random();
        x = 80 + r1.nextInt(440); //sets starting coordinates
        y = 30 + r2.nextInt(80); 
	xinit = x; //ie: x initial, y initial
	yinit = y;
	if(r.nextInt(10)%2 == 0) { //sets starting direction horizontal
	    directh = "R";
	} else {
	    directh = "L";
	}
	jump = 100 + r.nextInt(120); //sets time until first jump
    }


    public void move() {
	//controls horizontal movement
	if(directh.equals("R")) {
	    x = x + 4;
	}
	if(directh.equals("L")) {
	    x = x - 4;
	}
	//prevents from going offscreen horizontally from random
	if (x > 591) {
	    x = 9;
	}
	if (x < 6) { 
	    x = 588;
	}
	//for jump
	if(jump == 0) {
	    fire();
	    if(airborn != 0 && up){
		y = y + airborn;
		airborn--;
	    } else if(airborn == 0 && up){
		up = false;
	    }
	    if(airborn <= 10 && !up){
		y = y - airborn;
		airborn++;
	    } else if(airborn > 10 && !up){
		airborn--;
		up = true;
		jump = 150 + r.nextInt(100);
	    }
	} else {
	    jump--;
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
        return missiles2;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles2.size();i++){
	    missiles2.remove(i);
	}
    }
    
    public void fire() {
	if(!deceased()){
	    missiles2.add(new MissileB(x + S_Size/2, y + S_Size)); //creates missile object and adds to arraylist
	}
    }
}