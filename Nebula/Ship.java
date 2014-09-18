//Class for player controlled ship

import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.Rectangle;
import java.util.*;
import javax.swing.ImageIcon;

public class Ship {

    private String s = "Ship.png";
    private int dx;
    private int dy;
    private int x;
    private int y;
    private int w;
    private int h;
    private Image image;
    private boolean dead;

    private ArrayList missiles; //for the missile function
    private final int S_Size = 30; //for ship's size

    public Ship() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource(s));
        image = ii.getImage();
	w = image.getWidth(null); //for ship's area
        h = image.getHeight(null);
	dead = false;
	missiles = new ArrayList(); //initializes missiles
        x = 300;
        y = 500; 
	//all done before
    }


    public void move() {
        x = x + dx;
	if (y > 560 && dy > 0) { 
	} else if(y < 350 && dy < 0) {
	}else {
	    y = y + dy;
	}
	//so that it can't go off edge of board (ships horizontal movement is in 3's
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

    public void resetCoor() {
	x = 300;
        y = 500;
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
        return missiles;
    }

    public void resetMissiles() {
	for (int i = 0;i<missiles.size();i++){
	    missiles.remove(i);
	}
    }

    public void fire() {
        missiles.add(new MissileG(x + S_Size/2, y + S_Size/2)); //creates missile object and adds to arraylist
    }

    public void keyPressed(KeyEvent e) {

        int key = e.getKeyCode();

	if (key == KeyEvent.VK_SPACE) {
            fire();
        }

        if (key == KeyEvent.VK_LEFT) {
            dx = -4;
        }

        if (key == KeyEvent.VK_RIGHT) {
            dx = 4;
        }

        if (key == KeyEvent.VK_UP) {
		dy = -4;
        }

        if (key == KeyEvent.VK_DOWN) {
	    if (y > 0) {
		dy = 3;
	    }
        }
    }

    public void keyReleased(KeyEvent e) {
        int key = e.getKeyCode();

        if (key == KeyEvent.VK_LEFT) {
            dx = 0;
        }

        if (key == KeyEvent.VK_RIGHT) {
            dx = 0;
        }

        if (key == KeyEvent.VK_UP) {
            dy = 0;
        }

        if (key == KeyEvent.VK_DOWN) {
            dy = 0;
        }
    }
    //all pretty self explanatory
}