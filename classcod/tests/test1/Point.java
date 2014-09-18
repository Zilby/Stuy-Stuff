import java.io.*;
import java.util.*;


public class Point {

    // Should be double
    private double x,y;
    
    /* An equivalent set method would have been ok */
    public Point(double x,double y) {
	this.x = x;
	this.y = y;
    }
    
    public void setXY(double x, double y) {
	this.x = x;
	this.y = y;
    }


    public double distance(Point other) {
	// Could use other.getX() if you wrote it instead of 
	// direct access

	// You could use this
	double apart = (other.x - this.x) * (other.x - this.x);

	// but you don't have to
	double bpart = (other.y - y) * (other.y - y);
	return Math.sqrt(apart+bpart);

    }

}

