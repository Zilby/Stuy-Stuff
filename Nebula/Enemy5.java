//Class for Boss enemy

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Enemy5 {

    private String s = "Enemy5.png";
    private int x; //ie xcor
    private int y; //ie ycor
    private int xinit; //x and y initial coordinates
    private int yinit;
    private int w; //width and height
    private int h;
    private Image image; 
    private String directv; //initial direction
    private boolean up = true;
    private Random r = new Random(); 
    private ArrayList missiles51; //holds all the missileBs fired
    private ArrayList missiles53; //holds all the missileB3s fired
    private ArrayList missiles54; //holds all the missileB4s fired
    private boolean dead; //if dead will be removed
    private final int S_Size = 224; //for enemy's base size
    private int health = 60; 
    private int reload1a;
    private int reload1b;
    private int reload3a;
    private int reload3b;
    private int reload3c;
    private int reload3d;
    private int reload4;
    private int movecount;
    private Random r1;
    private Random r2;

    public Enemy5() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for Enemy's area
        h = image.getHeight(null);
	dead = false;
	missiles51 = new ArrayList(); //initializes missiles
	missiles53 = new ArrayList();
	missiles54 = new ArrayList();
	r1 = new Random();
	r2 = new Random();
        x = 180; //sets starting coordinates
        y = 50; 
	yinit = y;
	directv = "D"; //sets initial direction
	reload1a = 50 + r.nextInt(100);
	reload1b = 50 + r.nextInt(100);
	reload3a = 100 + r.nextInt(150);
	reload3b = 100 + r.nextInt(150);
	reload3c = 100 + r.nextInt(150);
	reload3d = 100 + r.nextInt(150);
	reload4 = 100 + r.nextInt(150);
	movecount = 2;
    }


    public void move() {
	//controls firing;
	//regular bullets
	if(reload1a == 0) {
	    fire1a();
	    reload1a = 50 + r.nextInt(100);
	} else {
	    reload1a--;
	}
	if(reload1b == 0) {
	    fire1b();
	    reload1b = 50 + r.nextInt(100);
	} else {
	    reload1b--;
	}
	//enemy3 bullets
	if(reload3a == 0) {
	    fire3a();
	    reload3a = 100 + r.nextInt(150);
	} else {
	    reload3a--;
	}
	if(reload3b == 0) {
	    fire3b();
	    reload3b = 100 + r.nextInt(150);
	} else {
	    reload3b--;
	}
	if(reload3c == 0) {
	    fire3c();
	    reload3c = 100 + r.nextInt(150);
	} else {
	    reload3c--;
	}
	if(reload3d == 0) {
	    fire3d();
	    reload3d = 100 + r.nextInt(150);
	} else {
	    reload3d--;
	}
	//enemy4 bullets
	if(reload4 == 0) {
	    fire4();
	    reload4 = 200 + r.nextInt(150);
	} else {
	    reload4--;
	}
	//controls vertical movement
	if(movecount == 0){
	    if(directv.equals("U") && y - yinit <= 20) {
		y = y + 1;
	    } else { 
		directv = "D";
	    }
	    if(directv.equals("D") && y - yinit >= -20) {
		y = y - 1;
	    } else { 
		directv = "U";
	    }
	    movecount = 10;
	} else { 
	    movecount--;
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
	    health = 100;
	}
    }

    public Image getImage() {
        return image;
    }

    public ArrayList getMissiles1() {
        return missiles51;
    }
    
    public ArrayList getMissiles3() {
        return missiles53;
    }

    public ArrayList getMissiles4() {
        return missiles54;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles51.size();i++){
	    missiles51.remove(i);
	}
	for (int j = 0;j<missiles53.size();j++){
	    missiles53.remove(j);
	}
	for (int k = 0;k<missiles54.size();k++){
	    missiles54.remove(k);
	}
    }
    
    public void fire1a() {
	if(!deceased()){
	    missiles51.add(new MissileB(x + 30, y + 50)); //creates missile object and adds to arraylist
	}
    }

    public void fire1b() {
	if(!deceased()){
	    missiles51.add(new MissileB(x + 190, y + 50)); //creates missile object and adds to arraylist
	}
    }

    public void fire3a() {
	if(!deceased()){
	    missiles53.add(new MissileB3(x + 10, y + 50)); //creates missile object and adds to arraylist
	}
    }

    public void fire3b() {
	if(!deceased()){
	    missiles53.add(new MissileB3(x + 80, y + 80)); //creates missile object and adds to arraylist
	}
    }

    public void fire3c() {
	if(!deceased()){
	    missiles53.add(new MissileB3(x + 150, y + 80)); //creates missile object and adds to arraylist
	}
    }

    public void fire3d() {
	if(!deceased()){
	    missiles53.add(new MissileB3(x + 220, y + 50)); //creates missile object and adds to arraylist
	}
    }

    public void fire4() {
	if(!deceased()){
	    missiles54.add(new MissileB4(x + S_Size/2 - 3, y + 65)); //creates missile object and adds to arraylist
	}
    }
}