/*========== Frame.java ==========
  Wrapper class for java's built in BufferedImage class.
  Allows use of java's DrawLine and image saving methods

  =========================*/

import java.io.*;
import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import javax.imageio.*;

public class Frame {

    public static final int XRES = 1024;
    public static final int YRES = 1024;
    public static final int COLOR_VALUE = 255;

    private int maxx, maxy, maxcolor;
    private BufferedImage bi;

    public Frame() {
	maxx = XRES;
	maxy = YRES;
	maxcolor = COLOR_VALUE;
	bi = new BufferedImage(maxx,maxy,BufferedImage.TYPE_BYTE_INDEXED);
    }

    public void clearScreen() {
	bi = new BufferedImage(maxx,maxy,BufferedImage.TYPE_BYTE_INDEXED);
    }	

    /*======== public void drawLines() ==========
      Inputs:  PointMatrix pm
      Color c 
      Returns: 
      calls drawLine so that it draws all the lines within PointMatrix pm
      ====================*/
    public void drawLines(EdgeMatrix pm, Color c) {
	
		for (int i=0; i < pm.getLastCol() - 1; i+=2){ 
		   
			drawLine( (int)pm.getX(i), (int)pm.getY(i),
				  (int)pm.getX(i+1), (int)pm.getY(i+1), c);
		}
    }	

    public void drawPolygons(EdgeMatrix pm, Color c){
      
      for (int i=0; i < pm.getLastCol() - 1; i+=3){ 
        double[] view = {0,0,-1};
        double x0 = pm.getX(i);
        double y0 = pm.getY(i);
        double z0 = pm.getZ(i);

        double x1 = pm.getX(i+1);
        double y1 = pm.getY(i+1);
        double z1 = pm.getZ(i+1);

        double x2 = pm.getX(i+2);
        double y2 = pm.getY(i+2);
        double z2 = pm.getZ(i+2);

        double ax = x1-x0;
        double ay = y1-y0;
        double az = z1-z0;

        double bx = x2-x0;
        double by = y2-y0;
        double bz = z2-z0;

        double[] norm = pm.crossProduct(ax,ay,az,bx,by,bz);
        
        //if(pm.calculateDot(norm,view) <= 0){
          drawLine( (int)pm.getX(i), (int)pm.getY(i),
            (int)pm.getX(i+1), (int)pm.getY(i+1), c);
          drawLine( (int)pm.getX(i+1), (int)pm.getY(i+1),
            (int)pm.getX(i+2), (int)pm.getY(i+2), c);
          drawLine( (int)pm.getX(i+2), (int)pm.getY(i+2),
            (int)pm.getX(i), (int)pm.getY(i), c);
        //}

      }
      

    }


    /*======== public void drawLine() ==========
      Inputs:  int x0
      int y0
      int x1
      int y1
      Color c 
      Returns: 
      Wrapper for java's built in drawLine routine
      ====================*/
    public void drawLine(int x0, int y0, int x1, int y1, Color c) {
	Graphics2D g = bi.createGraphics();
	g.setColor(c);
	g.drawLine(x0,y0,x1,y1);
    }	
 
   
    /*======== public void save() ==========
      Inputs:  String filename 
      Returns: 
      saves the bufferedImage as a png file with the given filename
      ====================*/
    public void save(String filename) {
	try {
	    File fn = new File(filename);
	    ImageIO.write(bi,"png",fn);
	}
	catch (IOException e) {}
    }

}
