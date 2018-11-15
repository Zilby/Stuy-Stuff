import java.io.*;
import java.util.*;

public class EdgeMatrix extends Matrix {

  private int lastCol;

  public EdgeMatrix() {
   super();
   lastCol = 0;
 }

 public EdgeMatrix( int c ) {
   super( c );
   lastCol = 0;
 }


    /*======== public static double distance() ==========
      Inputs:  double x0
               double y0
	       double x1
	       double y1 
      Returns: The distance between (x0, y0) and (x1, y1)

      03/09/12 17:57:57
      jonalf
      ====================*/
      public static double distance(double x0, double y0, 
        double x1, double y1) {
       return Math.sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1));
     }
	/**
	
	@param x x coord of the upper left front vertex
	**/
 public void addBox(double x, double y, double z, double w, double h, double d) {
  addEdge(x, y, z, x, y, z);
  addEdge(x + w, y, z, x + w, y ,z);
  addEdge(x, y-h, z, x, y-h, z);
  addEdge(x+w, y-h, z, x+w, y-h, z);
  addEdge(x, y, z+d, x, y, z+d);
  addEdge(x + w, y, z+d, x + w, y ,z+d);
  addEdge(x, y-h, z+d, x, y-h, z+d);
  addEdge(x+w, y-h, z+d, x+w, y-h, z+d);

}

public void addSphere(double cx, double cy, double radius) {
  int step = 1;
  for(int a = step; a <= 100; a+= step) {
    for(int t = step; t <= 100; t += step) { 
      double x = radius * Math.cos(2 * Math.PI * t/100.0) + cx;
      double y = radius * Math.sin(2 * Math.PI * t/100.0) * Math.cos(2 * Math.PI * a/100.0) + cy;
      double z = radius * Math.sin(2 * Math.PI * t/100.0) * Math.sin(2 * Math.PI * a/100.0);
      addEdge(x, y, z, x, y, z);
    }
  }
}

public void addTorus(double cx, double cy, double radiusSmall, double radiusLarge) {
  int step = 1;
  for(int a = step; a <= 100; a+= step) {
    for(int t = step; t <= 100; t += step) { 
      double x = (radiusSmall * Math.cos(2 * Math.PI * t/100.0) + radiusLarge) * Math.cos(2 * Math.PI * a/100) + cx;
      double y = radiusSmall * Math.sin(2 * Math.PI * t/100.0) + cy;
      double z = -1 * (radiusSmall * Math.cos(2 * Math.PI * t/100.0) + radiusLarge) * Math.sin(2 * Math.PI * a/100);
      addEdge(x, y, z, x, y, z);
    }
  }

} 
    /*======== public void addCircle() ==========
      Inputs:  int cx
               int cy
	       int rx
	       int ry 
      Returns: 
      
      Generates the edges required to make a circle and 
      adds them to the EdgeMatrix.

      The circle is centered at (cx, cy) and (rx, ry) is some
      point on the circumference.

      03/14/12 08:57:38
      jdyrlandweaver
      ====================*/
      public void addCircle(double cx, double cy, double rx, double ry) {
       double r = distance(cx, cy, rx, ry);
       int step = 1;
       double x0 = r * Math.cos(0) + cx;
       double y0 = r * Math.sin(0) + cy;
       for(int t = step; t <= 100; t += step) { 
        double x = r * Math.cos(2 * Math.PI * t/100.0) + cx;
        double y = r * Math.sin(2 * Math.PI * t/100.0) + cy;
        addEdge(x0, y0, 0, x, y, 0);
        x0 = x;
        y0 = y;
      }

    }


    /*======== public void addCurve() ==========
      Inputs:   double x0
                double y0
		double x1
		double y1
		double x2
		double y2
		double x3
		double y3 
      Returns: 
      
      Generates the edges required to create a curve
      and adds them to the edge matrix

      03/09/12 18:00:06
      jonalf
      ====================*/
      public void addCurve( double x0, double y0, 
       double x1, double y1, 
       double x2, double y2, 
       double x3, double y3, int type ) {
       Matrix coeffsX = new Matrix();
       Matrix coeffsY = new Matrix();
       if(type == gui.HERMITE_MODE) {
        double dy1, dx1, dy2, dx2;
        dy1 = y1 - y0;
        dx1 = x1- x0;
        dy2 = y3 - y2;
        dx2 = x3 - x2;

        coeffsY.generateHermiteCoefs(y0,y2,dy1,dy2);
        coeffsX.generateHermiteCoefs(x0,x2,dx2,dx2);
      } else {
        coeffsY.generateBezierCoefs(y0,y1,y2,y3);
        coeffsX.generateBezierCoefs(x0,x1,x2,x3);
      }

      int step = 1;
      double x00 = coeffsX.m[3][0];
      double y00 = coeffsY.m[3][0];
      for(int t = step; t <= 100; t += step) { 
        double x = coeffsX.m[0][0] * Math.pow(t/100.0,3) + coeffsX.m[1][0] * Math.pow(t/100.0,2) + coeffsX.m[2][0] * t/100.0 + coeffsX.m[3][0];
        double y = coeffsY.m[0][0] * Math.pow(t/100.0,3) + coeffsY.m[1][0] * Math.pow(t/100.0,2) + coeffsY.m[2][0] * t/100.0 + coeffsY.m[3][0];
        addEdge(x00, y00, 0, x, y, 0);
        x00 = x;
        y00 = y;
      }
    }

    /*======== public void addPoint() ==========
      Inputs:  int x
      int y
      int z 
      Returns: 
      adds (x, y, z) to the calling object
      if lastcol is the maxmium value for this current matrix, 
      call grow
      ====================*/
      public void addPoint(double x, double y, double z) {

       if ( lastCol == m[0].length ) 
         grow();

       m[0][lastCol] = x;
       m[1][lastCol] = y;
       m[2][lastCol] = z;
       m[3][lastCol] = 1;
       lastCol++;
     }

    /*======== public void addEdge() ==========
      Inputs:  int x0
      int y0
      int z0
      int x1
      int y1
      int z1 
      Returns: 
      adds the line connecting (x0, y0, z0) and (x1, y1, z1)
      to the calling object
      should use addPoint
      ====================*/
      public void addEdge(double x0, double y0, double z0, 
       double x1, double y1, double z1) {

       addPoint(x0, y0, z0);
       addPoint(x1, y1, z1);
     }



    /*======== accessors ==========
    ====================*/
    public int getLastCol() {
     return lastCol;
   }
   public double getX(int c) {
     return m[0][c];
   }
   public double getY(int c) {
     return m[1][c];
   }
   public double getZ(int c) {
     return m[2][c];
   }
   public double getD(int c) {
     return m[3][c];
   }

   public void clear() {
     super.clear();
     lastCol = 0;
   }
   
   public EdgeMatrix copy() {

     EdgeMatrix n = new EdgeMatrix( m[0].length );
     for (int r=0; r<m.length; r++)
       for (int c=0; c<m[r].length; c++)
        n.m[r][c] = m[r][c];
      n.lastCol = lastCol;
      return n;
    }
    interface Strategy {
     public void execute();	
   }
 }
