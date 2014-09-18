//Class for 'Bad' missiles

import java.awt.Image;
import javax.swing.ImageIcon;
import java.awt.Rectangle;

public class MissileB extends Missile{

    private boolean visible;
    private boolean dead;
    private int w; //ie: width and height
    private int h;

    public MissileB(int x,int y) {
	super(x, y); //calls on Missile super class constructor
	visible = true; //if not visible ie: offscreen, it'll be removed
	dead = false; //if dead, it will be removed (similar to visible, but keeps in track with ship and enemy)
        ImageIcon ii = new ImageIcon(this.getClass().getResource("MissileB.png")); //sets image icon
        image = ii.getImage(); //sets image
	w = image.getWidth(null); //for ship's area
        h = image.getHeight(null);
    }
                   
    public boolean isVisible() {
        return visible;
    }

    public void move1() {
        y = y + Missile_Speed; //goes at the missile speed
        if (y > 600) //if it's offsceen it's not visible
            visible = false;
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