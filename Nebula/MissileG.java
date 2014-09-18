//Class for 'Good' missiles
//See MissileB for details, they're all the same
import java.awt.Image;
import javax.swing.ImageIcon;
import java.awt.Rectangle;

public class MissileG extends Missile{

    private boolean visible;
    private boolean dead;
    private int w;
    private int h;

    public MissileG(int x,int y) {
	super(x, y);
	visible = true;
	dead = false;
        ImageIcon ii =
            new ImageIcon(this.getClass().getResource("MissileG.png"));
        image = ii.getImage();
	w = image.getWidth(null); //for ship's area
        h = image.getHeight(null);
    }

    public boolean isVisible() {
        return visible;
    }

    public void move() {
        y = y - Missile_Speed;
        if (y < 0)
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