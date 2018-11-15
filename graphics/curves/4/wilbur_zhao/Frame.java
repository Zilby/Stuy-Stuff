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
	
	for (int i=0; i < pm.getLastCol() - 1; i+=2) 
	    drawLine( (int)pm.getX(i), (int)pm.getY(i),
		      (int)pm.getX(i+1), (int)pm.getY(i+1), c);
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