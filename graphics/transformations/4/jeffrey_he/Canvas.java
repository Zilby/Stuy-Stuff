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
        edges.matrixMult(transform);
        transform.clear();
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
        transform.makeScale(x,y,z);
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
        transform.makeTranslate(x,y,z);
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
        transform.makeRotX(theta);
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
        transform.makeRotY(theta);
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
        transform.makeRotZ(theta);
        apply();
    }

    /*======== public void setDrawing() ==========
      Inputs:  int x0
               int y0
	       int x1
	       int y1 
      Returns: 
      sets drawing to true and adds a line to the tmpLine PointMatrix

      ====================*/
    public void setDrawing(int x0, int y0, int x1, int y1) {
        tmpline.addEdge(x0, y0, 0, x1, y1, 0);
        drawing=true;
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

        if (drawing) {
            g2.setColor( TMP_COLOR );
            g2.drawLine((int)tmpline.getX(0),(int)tmpline.getY(0),
                    (int)tmpline.getX(1),(int)tmpline.getY(1));
        }

        int col = edges.getLastCol();

        g2.setColor(c);

        for (int i=0; i < col - 1; i+=2) {
            g2.drawLine( (int)edges.getX(i), (int)edges.getY(i),
                    (int)edges.getX(i+1), (int)edges.getY(i+1));
        }

        ((Graphics2D)g).drawImage(bi,null,0,0);
    }
}
