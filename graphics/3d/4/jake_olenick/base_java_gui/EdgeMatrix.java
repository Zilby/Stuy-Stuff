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
	int r = (int)Math.sqrt( (rx-cx)*(rx-cx) + (ry-cy)*(ry-cy));
	int t = 0;
	double x0 = cx + r;
	double y0 = cy;
	t = 1;
	double x1;
	double y1;
	while (t <= (1.0 / step)){
	    x1 = cx + r*Math.cos(2*Math.PI*t*step);
	    y1 = cy + r*Math.sin(2*Math.PI*t*step);
	    add_edge(points,x0,y0,cz,x1,y1,cz);
	    x0 = x1;
	    y0 = y1;
	    t += 1;
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
	x_coefs = generate_curve_coefs(x0,x1,x2,x3,curve_type);
	y_coefs = generate_curve_coefs(y0,y1,y2,y3,curve_type);
	X0 = x0;
	Y0 = y0;
	t = 1;
	while (t <= (1.0/step)){
	    t = t * step;
	    X1 = x_coefs[0][0] * t**3 + x_coefs[0][1] * t**2 + x_coefs[0][2] * t + x_coefs[0][3];
	    Y1 = y_coefs[0][0] * t**3 + y_coefs[0][1] * t**2 + y_coefs[0][2] * t + y_coefs[0][3];
	    add_edge(points,X0,Y0,0,X1,Y1,0);
	    X0 = X1;
	    Y0 = Y1;
	    t = t / step;
	    t += 1;
	    print t;
	    t = t * step;
	    print x_coefs[0][0] * t**3  + x_coefs[0][1] * t**2 + x_coefs[0][2] * t + x_coefs[0][3];
	    print y_coefs[0][0] * t**3 + y_coefs[0][1] * t**2 + y_coefs[0][2] * t + y_coefs[0][3];
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

}
