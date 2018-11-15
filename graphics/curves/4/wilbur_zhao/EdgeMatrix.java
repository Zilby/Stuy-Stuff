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
								  double x1, double y1){
		return Math.sqrt(Math.pow(x0 - x1,2) +
						 Math.pow(y0 - y1,2));
	}

	public void addCircle(double cx, double cy, double r){
		int step = 1;
		int maxSteps = 100;

		double x0 = cx + r;
		double y0 = cy;
		double z0 = 0;
		double x = 0;
		double y = 0;
		double z = 0;
		for (int t = 0; t <= maxSteps + step;t+=step){
			x = cx + r*Math.cos(2*Math.PI*t/maxSteps);
			y = cy + r*Math.sin(2*Math.PI*t/maxSteps);
			addEdge(x0,y0,z0,x,y,z);
			x0 = x;
			y0 = y;
		}
		
	}

	public void addCurve(double x0, double y0,
						 double x1, double y1,
						 double x2, double y2,
						 double x3, double y3, int type){
		int step = 1;
		int maxSteps = 100;

		double x = 0;
		double y = 0;
		double z = 0;
		
		double xx = 0;
		double yy = 0;
		double zz = 0;
		Matrix curveMatrixX = new Matrix(1);
		Matrix curveMatrixY = new Matrix(1);
		if (type == 0 || type == 1){
			//setting the original values 
			if (type == 0){
				curveMatrixX.generateHermiteCoefs(x0,x1-x0,x2,x3-x2);
				curveMatrixY.generateHermiteCoefs(y0,y1-y0,y2,y3-y2);
			} else if (type == 1){
				curveMatrixX.generateBezierCoefs(x0,x1,x2,x3);
				curveMatrixY.generateBezierCoefs(y0,y1,y2,y3);		
			}
			xx = curveMatrixX.m[3][0];
			yy = curveMatrixY.m[3][0];
			for (int t = 1; t <= maxSteps + step;t+=step){
				x = curveMatrixX.m[0][0]*Math.pow(((double)t)/maxSteps,3) +
					curveMatrixX.m[1][0]*Math.pow(((double)t)/maxSteps,2) +
					curveMatrixX.m[2][0]*((double)t)/maxSteps +
					curveMatrixX.m[3][0];
				y = curveMatrixY.m[0][0]*Math.pow(((double)t)/maxSteps,3) +
					curveMatrixY.m[1][0]*Math.pow(((double)t)/maxSteps,2) +
					curveMatrixY.m[2][0]*((double)t)/maxSteps +
					curveMatrixY.m[3][0];
				addEdge(xx,yy,zz,x,y,z);
				xx = x;
				yy = y;
			}   			
		} else {
			System.out.println("type " + type + " is not a recognized curve type.");
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
