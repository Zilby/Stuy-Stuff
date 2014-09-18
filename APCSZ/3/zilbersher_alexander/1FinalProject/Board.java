import java.io.*;
import java.util.*;
import javax.swing.JPanel; //imports tools to make board
import java.awt.Graphics;  //  \
import java.awt.Graphics2D;//   } All used to add images to board
import java.awt.Image;//        }
import javax.swing.ImageIcon;///

public class Board extends JPanel{

    //public Board() {
    //}

    //up to here just creates the board
    
    Image i; //new Image variable
    public Board() {
        ImageIcon ii = new ImageIcon(this.getClass().getResource("face.png"));//creates Image Icon
        i = ii.getImage(); //gets image out of Image Icon
    }

    public void paint(Graphics g) {
	Graphics2D g2d = (Graphics2D) g; //creates graphics method?
        //g2d.drawImage(i, 10, 10, null);  draws image on screen with coordinates 10,10
	
	//g2d.drawImage(image i, int dstx1, int dsty1, int dstx2, int dsty2,
	// int srcx1, int srcy1, int srcx2, int srcy2, ImageObserver observer);

	/* The src parameters represent the area of the image to copy and draw. 
	   The dst parameters display the area of the destination to cover by 
	   the the source area. The dstx1, dsty1 coordinates define the location 
	   to draw the image. The width and height dimensions on the destination 
	   area are calculated by the following expressions: (dstx2-dstx1), (dsty2-dsty1). 
	   If the dimensions of the source and destinations areas are different, 
	   the Java 2D API will scale up or scale down, as needed.
	   ImageObserver can be substituted for null, but otherwise will notify the 
	   application of updates to an image that is loaded asynchronously.
	*/

	g2d.drawImage(i,10,10,100,100,null);
    }
}
    