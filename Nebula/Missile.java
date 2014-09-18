//Missile base class

import java.awt.Image;
import java.awt.Rectangle;
import javax.swing.ImageIcon;

public class Missile {

    protected int x, y;
    protected Image image;
    protected int Missile_Speed = 4;

    public Missile(int x, int y) {
        this.x = x; //sets private ints at beginning as this method's x and y values
        this.y = y;
    }

    public Image getImage() {
        return image;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}