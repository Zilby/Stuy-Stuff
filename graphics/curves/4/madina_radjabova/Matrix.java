/*========== Matrix.java ==========
  Matrix will hold a 2-d array of doubles and have a default size of 4x4.
  Handles basic matrix maintenence and math.
  Creates transformation matricies for tralation, scale and rotate
=========================*/

import java.io.*;
import java.util.*;

public class Matrix {

    public static final int DEFAULT_SIZE = 4;
    protected double[][] m;

    public Matrix() {
	m = new double[DEFAULT_SIZE][DEFAULT_SIZE];
    }
    public Matrix(int c) {
	m = new double[DEFAULT_SIZE][c];
    }

    public void grow() {
	double[][] n = new double[m.length][m[0].length + 10];
	for (int r=0; r<m.length; r++)
	    for (int c=0; c<m[r].length; c++)
		n[r][c] = m[r][c];
	
	m = n;
    }

    public void clear() {

	for (int i=0; i<m.length; i++) 
	    for (int j=0; j<m[i].length; j++) 
		m[i][j] = 0;
    }		

    public void ident() {	
	for (int i=0; i<m.length; i++) {
	    for (int j=0; j<m[i].length; j++) {	
		if (i==j)
		    m[i][j] = 1;
		else
		    m[i][j] = 0;
	    }
	}
    }

    public void scalarMult( int s ) {
	for (int i=0; i<m.length; i++) 
	    for (int j=0; j<m[i].length; j++) 
		m[i][j] = m[i][j] * s;
    }		

    public void matrixMult( Matrix n ) {
	double[][] tmp = new double[4][1];

	for (int c=0; c<m[0].length; c++) {
	    for (int r=0; r<4; r++) 
		tmp[r][0] = m[r][c];

	    for (int r=0; r<4; r++)
		m[r][c] = n.m[r][0] * tmp[0][0] +
		    n.m[r][1] * tmp[1][0] +
		    n.m[r][2] * tmp[2][0] +
		    n.m[r][3] * tmp[3][0];
	}
    }

    public Matrix copy() {
	Matrix n = new Matrix( m[0].length );
	for (int r=0; r<m.length; r++)
	    for (int c=0; c<m[r].length; c++)
		n.m[r][c] = m[r][c];

	return n;
    }

    public String toString() {
	String s = "";
	for (int i=0; i<m.length; i++) {
	    for (int j=0; j<m[i].length; j++)
		s = s + m[i][j] + " ";
	    s = s + "\n";
	}
	return s;
    }

    public void makeTranslate(double x, double y, double z) {
	ident();
	m[0][3] = x;
	m[1][3] = y;
	m[2][3] = z;
    }
    
    public void makeScale(double x, double y, double z) {
	ident();
	m[0][0] = x;
	m[1][1] = y;
	m[2][2] = z;
    }

    public void makeRotX(double theta) {	
	ident();
	m[1][1] = Math.cos( theta );
	m[1][2] = -1 * Math.sin( theta );
	m[2][1] = Math.sin( theta );
	m[2][2] = Math.cos( theta );
    }

    public void makeRotY(double theta) {
	ident();
	m[0][0] = Math.cos( theta );
	m[0][2] = -1 * Math.sin( theta );
	m[2][0] = Math.sin( theta );
	m[2][2] = Math.cos( theta );
    }

    public void makeRotZ(double theta) {
	ident();
	m[0][0] = Math.cos( theta );
	m[0][1] = -1 * Math.sin( theta );
	m[1][0] = Math.sin( theta );
	m[1][1] = Math.cos( theta );
    }
    
    public void makeHermite() {
	ident();
	m[0][0] = 2;
	m[1][1] = -2;
	m[2][0] = 1;
	m[3][0] = 1;
	m[0][0] = -3;
	m[1][0] = 3;
	m[2][0] = -2;
	m[3][0] = -1;
	m[2][2] = 1;
	m[0][3] = 1;	
    }

    public void makeBezier() {
	ident();
	m[0][0] = -1;
	m[0][1] = 3;
	m[0][2] = -3;
	m[0][3] = 1;

	m[1][0] = 3;
	m[1][1] = -6;
	m[1][2] = 3;
	m[1][3] = 0;

	m[2][0] = -3;
	m[2][1] = 3;
	m[2][2] = 0;
	m[2][3] = 0;

	m[3][0] = 1;
	m[3][1] = 0;
	m[3][2] = 0;
	m[3][3] = 0;
    }

    /*======== public void generateHermiteCoefs() ==========
      Inputs:  double p1
               double p2
	       double p3
	       double p4 
      Returns: 
      
      Turns the calling matrix into a matrix that provides the 
      coefiecients required to generate a Hermite curve given 
      the values of the 4 parameter coordinates.
      ====================*/
    public void generateHermiteCoefs(double p1, double p2, 
				     double p3, double p4) {
	makeHermite();
	double r1 = p2 - p1;
	double r2 = p4 - p3;
	Matrix p = new Matrix(1);
	p.m[0][0] = p1;
	p.m[1][0] = p2;
	p.m[2][0] = r1;
	p.m[3][0] = r2;
	matrixMult(p);
	
    }

    /*======== public void generateBezierCoefs() ==========
      Inputs:  double p1
               double p2
	       double p3
	       double p4 
      Returns: 
      
      Turns the calling matrix into a matrix that provides the 
      coefiecients required to generate a Bezier curve given 
      the values of the 4 parameter coordinates.
      ====================*/
    public void generateBezierCoefs(double p1, double p2, 
				    double p3, double p4) {
	makeBezier();
	Matrix p = new Matrix(1);
	p.m[0][0] = p1;
	p.m[1][0] = p2;
	p.m[2][0] = p3;
	p.m[3][0] = p4;
	matrixMult(p);
    } 

}
