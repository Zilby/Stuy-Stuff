import java.io.*;
import java.util.*;


public class EdgeMatrix extends Matrix {

    /* TABLE OF CONTENTS

       int lastCol

       EdgeMatrix()
       EdgeMatrix(int)

       addPolygon
       addBox
       addSphere
       generateSphere
       addTorus
       generateTorus
       distance
       addCircle
       addCurve
       addPoint
       addEdge

       getNumPoints    \
       getLastCol      /these are the same, I just got confused
       getX
       getY
       getZ
       getD

       clear
       copy
       

    **/
    
    private int lastCol;

    public EdgeMatrix() {
	super();
	lastCol = 0;
    }

    public EdgeMatrix( int c ) {
	super( c );
	lastCol = 0;
    }

    /*======== public void addPolygon() ==========
      Inputs:   double x0
                double y0
		double z0
		double x1
		double y1
		double z2
		double x2
		double y2
		double z2 
      Returns: 
      Adds the vertices (x0, y0, z0), (x1, y1, z1)
      and (x2, y2, z2) to the polygon matrix. They
      define a single triangle surface.
      
      04/17/13 19:25:26
      jdyrlandweaver
      ====================*/
    public void addPolygon( double x0, double y0, double z0, 
			    double x1, double y1, double z1, 
			    double x2, double y2, double z2) {
	addPoint(x0,y0,z0);
	addPoint(x1,y1,z1);
	addPoint(x2,y2,z2);
    }

    /*======== public void addBox() ==========
      Inputs:   double x
                double y
                double z
                double width
		double height
		double depth  
      Returns: 

      adds all the edges required to make a wire frame mesh
      for a rectagular prism whose upper-left corner is
      (x, y, z) with width, height and depth dimensions.
      
      03/28/12 18:13:03
      jonalf
      ====================*/
    public void addBox( double x, double y, double z, 
			double width, double height, double depth ) {

	double x2, y2, z2;	
	x2 = x + width;
	y2 = y + height;
	z2 = z - depth;
	
	addPolygon( x,y,z,x,y2,z,x2,y,z);
	addPolygon( x2,y,z,x,y2,z,x2,y2,z);
	addPolygon( x,y,z2,x2,y,z2,x,y,z);
	addPolygon( x,y,z,x2,y,z,x2,y,z2);
	addPolygon( x,y,z,x,y,z2,x,y2,z2);
	addPolygon( x,y,z,x,y2,z2,x,y2,z);
	addPolygon( x,y2,z,x,y2,z2,x2,y2,z);
	addPolygon( x2,y2,z2,x2,y2,z,x,y2,z2);	
	addPolygon( x2,y2,z2,x2,y,z2,x2,y2,z);	
	addPolygon( x2,y,z,x2,y2,z,x2,y,z2);
	addPolygon( x2,y2,z2,x,y2,z2,x,y,z2);	
	addPolygon( x2,y2,z2,x,y,z2,x2,y,z2);
    }

    /*======== public void addSphere() ==========
      Inputs:   double cx
                double cy
		double r
		double step  
      Returns: 
      
      adds all the edges required to make a wire frame mesh
      for a sphere with center (cx, cy) and radius r.
      
      should call generateSphere to create the
      necessary points

      03/28/12 18:12:48
      jonalf
      ====================*/
    public void addSphere( double cx, double cy, double r ) {

	double step = 0.05;
	EdgeMatrix spherePoints = new EdgeMatrix();
	int index;
	int numSteps = 21; //default: 21
	int longStart, latStart, longStop, latStop;
	longStart = 0;
	latStart = 0;
	longStop = numSteps;
	latStop = numSteps;

	spherePoints.generateSphere( cx, cy, r, step );
	//points only
	
	int size = spherePoints.getNumPoints();

	for ( int longt = longStart; longt < longStop; longt++ ) {
	    for ( int lat = latStart; lat < latStop; lat++ ) {

		index = longt * numSteps + lat;
		

		if(lat == 0){
		    double x1 = spherePoints.getX(index);
		    double y1 = spherePoints.getY(index);
		    double z1 = spherePoints.getZ(index);
		    double x3 = spherePoints.getX((index+numSteps+1)%size);
		    double y3 = spherePoints.getY((index+numSteps+1)%size);
		    double z3 = spherePoints.getZ((index+numSteps+1)%size);
		    double x4 = spherePoints.getX((index+1)%size);
		    double y4 = spherePoints.getY((index+1)%size);
		    double z4 = spherePoints.getZ((index+1)%size);
		    addPolygon(x4,y4,z4,x3,y3,z3,x1,y1,z1);
		}
		else if(lat == latStop-1){}
		else{
		    double x1 = spherePoints.getX(index);
		    double y1 = spherePoints.getY(index);
		    double z1 = spherePoints.getZ(index);
		    double x2 = spherePoints.getX((index+numSteps)%size);
		    double y2 = spherePoints.getY((index+numSteps)%size);
		    double z2 = spherePoints.getZ((index+numSteps)%size);
		    double x3 = spherePoints.getX((index+numSteps+1)%size);
		    double y3 = spherePoints.getY((index+numSteps+1)%size);
		    double z3 = spherePoints.getZ((index+numSteps+1)%size);
		    double x4 = spherePoints.getX((index+1)%size);
		    double y4 = spherePoints.getY((index+1)%size);
		    double z4 = spherePoints.getZ((index+1)%size);
		    addPolygon(x3,y3,z3,x2,y2,z2,x1,y1,z1);
		    addPolygon(x4,y4,z4,x3,y3,z3,x1,y1,z1);
		}
		

	    }
	}
    }
    
    /*======== public void generateSphere() ==========
      Inputs:   double cx
                double cy
		double r
		double step
		Matrix mat
      Returns: 

      Generates all the points along the surface of a 
      sphere with center (cx, cy) and radius r

      Uses the rotation-of-a-semicircle method
      
      Adds these points to the calling matrix

      03/28/12 18:12:52
      jonalf
      ====================*/
    public void generateSphere( double cx, double cy, double r, double step) {
	
	double x, y, z;

	for ( double rotation = 0; rotation < 1.01; rotation+= step ) {
	    int j = 0;
	    for ( double circle = 0; circle < 1.01; circle+= step ) {
		j++;
		//x rotation		
		x = r * Math.cos( Math.PI * circle ) + cx;
		y = r * Math.sin( Math.PI * circle ) * 
		    Math.cos( 2 * Math.PI * rotation ) + cy;
		z = r * Math.sin( Math.PI * circle ) * 
		    Math.sin( 2 * Math.PI * rotation );
		addPoint(x,y,z);
	    }	    
	}

    }

    /*======== public void addTorus() ==========
      Inputs:   double cx
                double cy
		double r1
		double r2
		double step  
      Returns: 
      
      adds all the edges required to make a wire frame mesh
      for a torus with center (cx, cy) and radii r1 and r2.

      should call generateTorus to create the
      necessary points

      03/28/12 18:12:57
      jonalf
      ====================*/
    public void addTorus( double cx, double cy, double r1, double r2 ) {
	double step = 0.05;
	EdgeMatrix torPoints = new EdgeMatrix();
	
	int index;
	int numSteps = 21;
	int longStart, latStart, longStop, latStop;
	longStart = 0;
	latStart = 0;
	longStop = numSteps;
	latStop = numSteps;

	torPoints.generateTorus( cx, cy, r1, r2, step );
	int numPoints = torPoints.getNumPoints();
		
	//interpretation:
	//longt is the vertical line corresponding to extent of donut
	//lat is the horizontal line corresponding to extent of cross-section
	for ( int longt = longStart; longt < longStop; longt++ ) {
	    for ( int lat = latStart; lat < latStop; lat++ )  {
		index = longt * numSteps + lat;
		if (index == 419 || index == 440){
		    System.out.println("lat is:"+ lat);
		    System.out.println("longt is:" + longt);
		}
		else{
		    double x1 = torPoints.getX(index);
		    double y1 = torPoints.getY(index);
		    double z1 = torPoints.getZ(index);
		    double x2 = torPoints.getX((index+numSteps)%numPoints);
		    double y2 = torPoints.getY((index+numSteps)%numPoints);
		    double z2 = torPoints.getZ((index+numSteps)%numPoints);
		    double x3 = torPoints.getX((index+numSteps)%numPoints+1);
		    double y3 = torPoints.getY((index+numSteps)%numPoints+1);
		    double z3 = torPoints.getZ((index+numSteps)%numPoints+1);
		    double x4 = torPoints.getX((index)%numPoints+1);
		    double y4 = torPoints.getY((index)%numPoints+1);
		    double z4 = torPoints.getZ((index)%numPoints+1);
		    addPolygon(x3,y3,z3,x2,y2,z2,x1,y1,z1);
		    addPolygon(x4,y4,z4,x3,y3,z3,x1,y1,z1);
		    if((x1==0 || x2==0 || x3==0 || x4==0)&&
		       (y1==0 || y2==0 || y3==0 || y4==0)){
			System.out.println("\nthe following are the points:");
			System.out.println("(x1,y1): "+x1+","+y1);
			System.out.println("(x2,y2): "+x2+","+y2);
			System.out.println("(x3,y3): "+x3+","+y3);
			System.out.println("(x4,y4): "+x4+","+y4);
			System.out.println("the following are the indices: ");
			System.out.println("index: "+index);
			System.out.println("index+numSteps%numpoints: "+((index+numSteps)%numPoints));
			System.out.println("index+numSteps%numpoints+1: "+((index+numSteps)%numPoints+1));
			System.out.println("index%numPoints+1: "+(index%numPoints+1));
		    }
		}	    
	    }//end for longt
	}//end for lat
    }

    /*======== public void generateTorus() ==========
      Inputs:   double cx
                double cy
		double r1
		double r2
		double step  
      Returns: 

      Generates all the points along the surface of a 
      tarus with center (cx, cy) and radii r1 and r2

      Adds these points to the matrix parameter
      
      03/28/12 18:13:00
      jonalf
      ====================*/
    public void generateTorus( double cx, double cy, double r1, double r2, double step ) {
	double x, y, z;

	for ( double rotation = 0; rotation < 1.01; rotation+= step )
	    for ( double circle = 0; circle < 1.01; circle+= step ) {

		//y rotation
		x = Math.cos( 2 * Math.PI * rotation ) *
		    ( r1 * Math.cos( 2 * Math.PI * circle ) + r2 ) + cx;
		y = r1 * Math.sin( 2 * Math.PI * circle ) + cy;
		z = Math.sin( 2 * Math.PI * rotation ) *
		    ( r1 * Math.cos( 2 * Math.PI * circle ) + r2 );
		/*
		  // x rotation
		x = r1 * Math.cos( 2 * Math.PI * circle ) + cx;
		y = Math.cos( 2 * Math.PI * rotation ) * 
		    ( r1 * Math.sin( 2 * Math.PI * circle ) + r2 ) + cy;
		z = Math.sin( 2 * Math.PI * rotation ) *
		    ( r1 * Math.sin( 2 * Math.PI * circle ) + r2 );
		*/
		addPoint(x, y, z);
	    }	
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
	return Math.sqrt( (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0) );
    }
	   

    /*======== public void addCircle() ==========
      Inputs:  int cx
               int cy
	       double r
      Returns: 
      
      Generates the edges required to make a circle and 
      adds them to the EdgeMatrix.

      The circle is centered at (cx, cy) with radius r

      03/14/12 08:57:38
      jdyrlandweaver
      ====================*/
    public void addCircle(double cx, double cy, double r) {
	
	double x0, y0, x, y, step;
	
	step = 0.01;

	x0 = r + cx;
	y0 = cy;

	for( double t= step; t <= 1; t+= step) {
	    
	    x = r * Math.cos( 2 * Math.PI * t) + cx;
	    y = r * Math.sin( 2 * Math.PI * t) + cy;

	    addEdge(x0, y0, 0, x, y, 0);
	    x0 = x;
	    y0 = y;
	}

	addEdge(x0, y0, 0, r + cx, cy, 0);
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
	
	EdgeMatrix xcoefs = new EdgeMatrix(1);
	EdgeMatrix ycoefs = new EdgeMatrix(1);

	//a lower step value makes a more precise curve
	double step = 0.01;

	double x, y, z, ax, ay, bx, by, cx, cy, dx, dy;
	
	if ( type == gui.HERMITE_MODE ) {
	    xcoefs.generateHermiteCoefs(x0, x1, x2, x3);
	    ycoefs.generateHermiteCoefs(y0, y1, y2, y3);
	}
	else {
	    xcoefs.generateBezierCoefs(x0, x1, x2, x3);
	    ycoefs.generateBezierCoefs(y0, y1, y2, y3);
	}

	ax = xcoefs.getX(0);
	bx = xcoefs.getY(0);
	cx = xcoefs.getZ(0);
	dx = xcoefs.getD(0);

	ay = ycoefs.getX(0);
	by = ycoefs.getY(0);
	cy = ycoefs.getZ(0);
	dy = ycoefs.getD(0);

	double startx = x0;
	double starty = y0;

	for (double t = step; t <= 1; t+= step ) {
	    
	    x = ax * t * t * t + bx * t * t + cx * t + dx;
	    y = ay * t * t * t + by * t * t + cy * t + dy;

	    addEdge( startx, starty, 0, x, y, 0 );
	    startx = x;
	    starty = y;
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
    public int getNumPoints() {
	return lastCol;
    }
    public int getLastCol(){
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
