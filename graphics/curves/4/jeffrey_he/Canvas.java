import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.image.*;
import javax.imageio.*;

public class Canvas extends JPanel {

  public static final int XRES = 500;
  public static final int YRES = 500;
  public static final Color REG_COLOR = Color.CYAN;
  public static final Color TMP_COLOR = Color.RED;


  private EdgeMatrix edges;
  private Matrix transform;
  private BufferedImage bi;
  private EdgeMatrix tmpline;
  private Color c;
  boolean drawing=false;    

  public Canvas() {
   edges = new EdgeMatrix();
   tmpline = new EdgeMatrix(2);
   transform = new Matrix();
   transform.ident();
   c = REG_COLOR;
 }

 public void setColor( Color n ) {
   c = n;
 }

    /*======== public void apply()) ==========
      Inputs:   
      Returns: 

      Apply the master transform matrix to the
      edge matrix
      Reset the master transform matrix after
      Update the drawing area
      
      03/09/12 09:10:15
      jdyrlandweaver
      ====================*/
      public void apply() {
       edges.matrixMult( transform );
       transform.ident();
       this.update(this.getGraphics());
     }	

    /*======== public void scale() ==========
      Inputs:  double x
               double y
               double z 
      Returns: 

      Turn the transform matrix into the appropriate
      scale matrix
      
      Apply the transformation

      03/09/12 09:12:31
      jdyrlandweaver
      ====================*/
      public void scale(double x, double y, double z) {
       transform.makeScale(x, y, z);
       apply();
     }

    /*======== public void translate() ==========
      Inputs:  double x
               double y
               double z 
      Returns: 

      Turn the transform matrix into the appropriate
      translation matrix
      
      Apply the transformation

      03/09/12 09:13:39
      jdyrlandweaver
      ====================*/
      public void translate(double x, double y, double z) {
       transform.makeTranslate(x, y, z);
       apply();
     }

    /*======== public void rotX() ==========
      Inputs:   double theta  
      Returns: 

      Turn the transform matrix into the appropriate
      rotation (x-axis)  matrix
      
      Users shoud be able to enter angles in degrees, 
      but they need to be translated into radians
      in order to work with java's math methods
      
      Apply the transformation

      03/09/12 09:14:53
      jdyrlandweaver
      ====================*/
      public void rotX( double theta ) {
       theta = theta * (Math.PI / 180);
       transform.makeRotX( theta );
       apply();
     }

    /*======== public void rotY() ==========
      Inputs:   double theta  
      Returns: 

      Turn the transform matrix into the appropriate
      rotation (y-axis)  matrix
      
      Users shoud be able to enter angles in degrees, 
      but they need to be translated into radians
      in order to work with java's math methods
      
      Apply the transformation

      03/09/12 09:15:02
      jdyrlandweaver
      ====================*/
      public void rotY( double theta ) {
       theta = theta * (Math.PI / 180);
       transform.makeRotY( theta );
       apply();
     }

    /*======== public void rotZ() ==========
      Inputs:   double theta  
      Returns: 

      Turn the transform matrix into the appropriate
      rotation (x-axis)  matrix
      
      Users shoud be able to enter angles in degrees, 
      but they need to be translated into radians
      in order to work with java's math methods
      
      Apply the transformation


      03/09/12 09:15:12
      jdyrlandweaver
      ====================*/
      public void rotZ( double theta ) {
       theta = theta * (Math.PI / 180);
       transform.makeRotZ( theta );
       apply();
     }

    /*======== public void setDrawing() ==========
      Inputs:  int x0
               int y0
	       int x1
	       int y1 
      Returns: 
      sets drawing to true 
      if mode == gui.LINE_MODE
          adds a line to the tmpLine EdgeMatrix
      if mode == CIRCLE_MODE
          adds the circle to the tmpline EdgeMatrix      
      if mode == gui.HERMITE_MODE or gui.BEZIER_MODE
          adds 2 lines to the tmpline EdgeMatrix, creating the
	  bounding lines for the cure
	  adds the actual curve to the tmpline EdgeMatrix

    ====================*/    
    public void setDrawing(int x0, int y0, int x1, int y1, int x2, int y2, int rx, int ry, int mode) {
     switch(mode) {
      case gui.CIRCLE_MODE:
        tmpline.addCircle(x0,y0,rx,ry);
        break;
      case gui.LINE_MODE:
        tmpline.addEdge(x0,y0,0,x1,y1,0);
        break;
      default:
        tmpline.addCurve(x0,y0,x1,y1,x2,y2,rx,ry, mode);
        break;

    }
    drawing = true;

  }

    /*======== public void addCircle() ==========
      Inputs:  int cx
               int cy
	       int rx
	       int ry 
      Returns: 

      Calls addCircle on the permanent EdgeMatrix
      03/14/12 08:56:51
      jdyrlandweaver
      ====================*/
      public void addCircle(int cx, int cy, int rx, int ry) {
       edges.addCircle(cx,cy,rx,ry);
     }

    /*======== public void addCurve() ==========
      Inputs:   int x0
                int y0
		int x1
		int y1
		int x2
		int y2
		int x3
		int y3
		int mode  
      Returns: 

      Calls the renderCurve method on the edges EdgeMatrix and updates
      the drawing area

      03/12/12 13:16:16
      jdyrlandweaver
      ====================*/
      public void addCurve( int x0, int y0, int x1, int y1, int x2, int y2, int x3, int y3, int mode ) {
        edges.addCurve(x0,y0,x1,y1,x2,y2,x3,y3,mode);
     }

     public void stopDrawing() {
       drawing=false;
     }

     public BufferedImage getBufferedImage() {
       return bi;
     }

     public Dimension getPreferredSize() {
       return new Dimension(XRES, YRES);
     }

    /*======== public void addLine() ==========
      Inputs:  int x0
               int y0
	       int z0
	       int x1
	       int y1
	       int z1 
      Returns: 
      Adds the specified line to the edges PointMatrix
      ====================*/
      public void addLine(int x0, int y0, int z0, 
       int x1, int y1, int z1) {
       edges.addEdge(x0,y0,z0,x1,y1,z1);
       this.update(this.getGraphics());
     }

    /*======== public void addPoint() ==========
      Inputs:  int x0
         int y0
         int z0 
      Returns: 
      add a single point to the edges PointMatrix
      ====================*/
      public void addPoint(int x0, int y0, int z0) {

       edges.addPoint(x0,y0,z0);
       this.update(this.getGraphics());
     }


    /*======== public void clearTmp()) ==========
      Inputs:   
      Returns: 

      Clear the temporary edge matrix

      03/05/12 11:17:10
      jdyrlandweaver
      ====================*/
      public void clearTmp() {
       tmpline.clear();
     }

    /*======== public void clearPoints()) ==========
      Inputs:   
      Returns: 

      Clear the permanent edge matrix

      03/05/12 11:17:10
      jdyrlandweaver
      ====================*/
      public void clearPoints() {
       edges.clear();
       this.update(this.getGraphics());
     }

    /*======== public void paintComponent() ==========
      Inputs:  Graphics g 
      Returns: 
      draws the edges stored in tmpLine or edges to the canvas
      depending on the value of drawing
      ====================*/
      public void paintComponent(Graphics g) {

       super.paintComponent(g);
       bi = (BufferedImage)this.createImage(XRES, YRES);
       Graphics2D g2 = bi.createGraphics();

       int col;

       if (drawing) {
         g2.setColor(TMP_COLOR );

         col = tmpline.getLastCol();
         for (int i=0; i < col - 1; i+=2)
          g2.drawLine( (int)tmpline.getX(i), (int)tmpline.getY(i), 
            (int)tmpline.getX(i+1), (int)tmpline.getY(i+1));	
      }

      col = edges.getLastCol();
      g2.setColor(c);

      for (int i=0; i < col - 1; i+=2) {
       g2.drawLine( (int)edges.getX(i), (int)edges.getY(i), 
        (int)edges.getX(i+1), (int)edges.getY(i+1));	    
     }	

     ((Graphics2D)g).drawImage(bi,null,0,0);
   }
 }
