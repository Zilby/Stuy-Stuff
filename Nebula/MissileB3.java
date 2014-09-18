//Class for 'Bad' missiles for Enemy3s

import java.awt.Image;
import javax.swing.ImageIcon;
import java.awt.Rectangle;
import java.util.*;
import java.io.*;

public class MissileB3 extends Missile{

    private boolean visible;
    private boolean dead;
    private int w; //ie: width and height
    private int h;
    private int explosion;
    private Random r = new Random();

    public MissileB3(int x,int y) {
	super(x, y); //calls on Missile super class constructor
	visible = true; //if not visible ie: offscreen, it'll be removed
	dead = false; //if dead, it will be removed (similar to visible, but keeps in track with ship and enemy)
        ImageIcon ii = new ImageIcon(this.getClass().getResource("MissileB3.png")); //sets image icon
        image = ii.getImage(); //sets image
	explosion = 30;
	w = image.getWidth(null); //for ship's area
        h = image.getHeight(null);
    }
                   
    public boolean isVisible() {
        return visible;
    }

    public void move1() {
	int n = 400 + r.nextInt(160);
	if (y < n){
	    y = y + Missile_Speed; //goes at the missile speed
	    if (y > 600) {//if it's offsceen it's not visible
            visible = false;
	    }
	    if (y > n-50) {
		ImageIcon prior = new ImageIcon(this.getClass().getResource("Prior.png")); //sets image icon
		image = prior.getImage();
	    }
	} else {
	    if (explosion > 15){
		ImageIcon explode = new ImageIcon(this.getClass().getResource("Explode.png")); //sets image icon
		image = explode.getImage();
		w = image.getWidth(null); //for ship's area
		h = image.getHeight(null);
		explosion--;
	    } else if (explosion > 0){
	    ImageIcon post = new ImageIcon(this.getClass().getResource("Post.png")); //sets image icon
		image = post.getImage();
		w = image.getWidth(null); //for ship's area
		h = image.getHeight(null);
		explosion--;
	    } else {
		visible = false;
	    }
	}
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
}