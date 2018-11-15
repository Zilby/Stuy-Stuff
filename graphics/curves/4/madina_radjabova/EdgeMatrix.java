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

    public static double distance(double x0, double y0, 
				  double x1, double y1) {
		return Math.sqrt(Math.pow(x0-x1, 2) + Math.pow(y0-y1, 2));
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

       ====================*/
    public void addCircle(double cx, double cy, double rx, double ry) {

   		double radius = distance(cx, cy, rx, ry);

		double x = rx, y = ry, ix = cx + radius, iy = cy;
		double t;

		for (t=1; t<= 360; t++) {
	    	x = cx + radius * Math.cos(t);
	    	y = cy + radius * Math.sin(t);
	    	addEdge(rx, ry, 0, x, y, 0);
	    	ix = x;
	    	iy = y;
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
      ====================*/
    public void addCurve( double x0, double y0, 
			  double x1, double y1, 
			  double x2, double y2, 
			  double x3, double y3, int type )
    {
		if (type == 2) { //Hermite curve
	    	Matrix xx = new Matrix();
	    	xx.generateHermiteCoefs(x0, x1, x2, x3);
	    	Matrix yy = new Matrix();
	    	yy.generateHermiteCoefs(y0, y1, y2, y3);

	    	double t = 1, step = 2;
	    	double x = x0, y = y0, ix, iy;

	    	while (x != x3 && y != y3) {
				t = t * step;
				ix = xx.m[0][0] * t*t*t + xx.m[0][1] * t*t + xx.m[0][2] * t + xx.m[0][3];
				iy = yy.m[0][0] * t*t*t + yy.m[0][1] * t*t + yy.m[0][2] * t + yy.m[0][3];
				addEdge(x,y,0,ix,iy,0);
				x = ix;
        		y = iy;
        		t = t / step;
        		t += 1;
	    	}
		}
		if (type == 3) { //Bezier curve
	    	Matrix xx = new Matrix();
	    	xx.generateBezierCoefs(x0, x1, x2, x3);
	    	Matrix yy = new Matrix();
	    	yy.generateBezierCoefs(y0, y1, y2, y3);
		}        
        
    }

    public void addPoint(double x, double y, double z) {

	if ( lastCol == m[0].length ) 
	    grow();
	
	m[0][lastCol] = x;
	m[1][lastCol] = y;
	m[2][lastCol] = z;
	m[3][lastCol] = 1;
	lastCol++;
    }
    
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
