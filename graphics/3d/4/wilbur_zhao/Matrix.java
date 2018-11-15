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

    /*===========Constructors================
      Default constructor creates a 4x4 matrix
      Second constructor creates a 4xN matrix
    */
    public Matrix() {
	m = new double[DEFAULT_SIZE][DEFAULT_SIZE];
    }
    public Matrix(int c) {
	m = new double[DEFAULT_SIZE][c];
    }

    /*===========grow================
      Increase the number of columns in a matrix by 10
      You can change the growth factor as you see fit
    */
    public void grow() {

	double[][] n = new double[m.length][m[0].length + 10];
	for (int r=0; r<m.length; r++)
	    for (int c=0; c<m[r].length; c++)
		n[r][c] = m[r][c];
	
	m = n;
    }

    /*======== public void clear() ==========
      Inputs:  
      Returns: 
      Sets every entry in the matrix to 0
      ====================*/
    public void clear() {

	for (int i=0; i<m.length; i++) 
	    for (int j=0; j<m[i].length; j++) 
		m[i][j] = 0;
    }		

    /*===========ident================
      Turns this matrix into the indentity matrix
      You may assume the calling Matrix is square
    */
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

    /*===========scalarMult================
      Inputs:  double x
      
      multiply each element of the calling matrix by x
    */
    public void scalarMult( double x ) {
       for (int i = 0; i <m.length; i++){
        for (int j = 0;j < m[i].length;j++){
          m[i][j] = m[i][j] * x;
       }
     }
    }		

    /*===========matrixMult================
      Multply matrix n by the calling matrix, modify
      the calling matrix to store the result.
      
      eg.
      In the call a.matrixMult(n), n will remain the same
      and a will now be the product of n * a
    */
    public void matrixMult( Matrix n ) {
      Matrix mcopy = this.copy();
     for (int i = 0; i < n.m.length; i++){
        for (int k = 0; k < mcopy.m[0].length; k++){
         int j = 0;
         m[i][k] = 0;
          while (j < n.m[i].length){
           m[i][k] += n.m[i][j] * mcopy.m[j][k]; 
           j++;
         }
       }
      }
    }
   
    /*===========copy================
      Create and return new matrix that is a duplicate 
      of the calling matrix
    */
    public Matrix copy() {

	Matrix n = new Matrix( m[0].length );
	for (int r=0; r<m.length; r++)
	    for (int c=0; c<m[r].length; c++)
		n.m[r][c] = m[r][c];

	return n;
    }

    /*===========toString================
      Crate a readable String representation of the 
      calling matrix.
    */
    public String toString() {

	String s = "";
	for (int i=0; i<m.length; i++) {
	    for (int j=0; j<m[i].length; j++)
		s = s + m[i][j] + " ";
	    s = s + "\n";
	}
	return s;
    }

    /*===========MakeTranslate================
      Turns the calling matrix into the appropriate
      translation matrix using x, y, and z as the translation
      offsets.
     */
    public void makeTranslate(double x, double y, double z) {
    this.ident();
    m[0][3] = x;
    m[1][3] = y;
    m[2][3] = z;
    }
    
    /*===========MakeScale================
      Turns the calling matrix into the appropriate scale
      matrix using x, y and z as the scale factors.
     */
    public void makeScale(double x, double y, double z) {
    this.ident();
    m[0][0] = x;
    m[1][1] = y;
    m[2][2] = z;
    }

    public double degToRad(double deg){
      return 2*Math.PI*deg/180;
   } 

    /*=========== MakeRotX ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and X
      as the axis of rotation.
    */
    public void makeRotX(double theta) {
      double rad = degToRad(theta);
    this.ident();
    double co = Math.cos(rad);
    double si = Math.sin(rad); 
    m[1][1] = co;
    m[1][2] = -si;
    m[2][1] = si;
    m[2][2] = co;
    }

    /*=========== MakeRotY ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and Y
      as the axis of rotation.
    */
    public void makeRotY(double theta) {
      double rad = degToRad(theta);
    this.ident();
    double co = Math.cos(rad);
    double si = Math.sin(rad); 
    m[0][0] = co;
    m[0][2] = -si;
    m[2][0] = si;
    m[2][2] = co;
    }

    /*=========== MakeRotZ ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and axis
      as the axis of rotation.
    */
    public void makeRotZ(double theta) {
      double rad = degToRad(theta);
    this.ident();
    double co = Math.cos(rad);
    double si = Math.sin(rad); 
    m[0][0] = co;
    m[0][1] = -si;
    m[1][0] = si;
    m[1][1] = co;
    }
/*
    [ 2 -2  1  1]
    [-3  3 -2 -1]
    [ 0  0  1  0]
    [ 1  0  0  0]

  */
	public void makeHermite(){
    this.ident();
    m[0][0] = 2;
    m[0][1] = -2;
    m[0][2] = 1;
    m[0][3] = 1;

    m[1][0] = -3;
    m[1][1] = 3;
    m[1][2] = -2;
    m[1][3] = -1;

    m[3][0] = 1;
    m[3][3] = 0;
	}

  /*
    [-1  3 -3  1]
    [ 3 -6  3  0]
    [-3  3  0  0]
    [ 1  0  0  0]
  */
	public void makeBezier(){
    this.ident();
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

    m[3][0] = 1;
    m[3][3] = 0;
	}
  
	public void generateHermiteCoefs(double p1, double p2,
									 double p3, double p4){
		Matrix herm = new Matrix();
		herm.makeHermite();
		m[0][0] = p1;
		m[1][0] = p3;
		m[2][0] = p2;
		m[3][0] = p4;

		this.matrixMult(herm);
	}

	public void generateBezierCoefs(double p1, double p2,
									double p3, double p4){
		Matrix bezi = new Matrix();
		bezi.makeBezier();

		m[0][0] = p1;
		m[1][0] = p2;
		m[2][0] = p3;
		m[3][0] = p4;

		this.matrixMult(bezi);	
	}
}
