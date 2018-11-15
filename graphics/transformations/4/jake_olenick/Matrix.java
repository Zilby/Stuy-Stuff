/*========== Matrix.java ==========
  Matrix will hold a 2-d array of doubles and have a default size of 4x4.
  Handles basic matrix maintenence and math.
  Creates transformation matrices for translation, scaling, and rotation
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
    public void scalarMult( int s ) {
	for(int i = 0; i < m.length; i++)
	    for(int j = 0; j < m[0].length; j++)
		m[i][j] = s * m[i][j];
    }		

    /*===========matrixMult================
      Multply matrix n by the calling matrix, modify
      the calling matrix to store the result.
      
      eg.
      In the call m.matrixMult(n), n will remain the same
      and m will now be the product of n * m
    */
    public void matrixMult( Matrix n ) {
	Matrix temp = this.copy();
	for(int mCol = 0; mCol<m[0].length; mCol++){
	    for(int mRow = 0; mRow<m.length; mRow++){
		double sum = 0;
		for(int j = 0; j<m.length; j++){
		    sum += n.m[mRow][j] * temp.m[j][mCol];
		}
		m[mRow][mCol] = sum;
		sum = 0;
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
	if (m.length == m[0].length){
	    m[0][3] = x;
	    m[1][3] = y;
	    m[2][3] = z;
	}
	else
	    System.out.println("NO STOP, WRONG MATRIX!!! (translate)");
    }
    
    /*===========MakeScale================
      Turns the calling matrix into the appropriate scale
      matrix using x, y and z as the scale factors.
     */
    public void makeScale(double x, double y, double z) {
	if (m.length == m[0].length){
	    m[0][0] = x;
	    m[1][1] = y;
	    m[2][2] = z;
	}
	else
	    System.out.println("NO STOP, WRONG MATRIX!!! (scale)");
    }

    /*=========== MakeRotX ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and X
      as the axis of rotation.
    */
    public void makeRotX(double theta) {
	if (m.length == m[0].length){
	    theta = theta / (180.0 / Math.PI);
	    
	    m[1][1] = Math.cos(theta);
	    m[1][2] = 0 - Math.sin(theta);
	    m[2][1] = Math.sin(theta);
	    m[2][2] = Math.cos(theta);
	}
	else
	    System.out.println("NO STOP, WRONG MATRIX!!! (rotX)");
	
    }

    /*=========== MakeRotY ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and Y
      as the axis of rotation.
    */
    public void makeRotY(double theta) {
	if (m.length == m[0].length){
	    theta /= (180.0 / Math.PI);
	    
	    m[0][0] = Math.cos(theta);
	    m[0][2] = 0 - Math.sin(theta);
	    m[2][0] = Math.sin(theta);
	    m[2][2] = Math.cos(theta);
	}
	else
	    System.out.println("NO STOP, WRONG MATRIX!!! (rotY)");
    }

    /*=========== MakeRotZ ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and axis
      as the axis of rotation.
    */
    public void makeRotZ(double theta) {
	if (m.length == m[0].length){
	    theta /= (180.0 / Math.PI);
	    
	    m[0][0] = Math.cos(theta);
	    m[0][1] = 0 - Math.sin(theta);
	    m[1][0] = Math.sin(theta);
	    m[1][1] = Math.cos(theta);
	}
	else
	    System.out.println("NO STOP, WRONG MATRIX!!! (rotZ)");
    }
}
