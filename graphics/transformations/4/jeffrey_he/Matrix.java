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
    public void scalarMult( int s ) {
        for(int row = 0; row < m.length; row++) {
            for(int col = 0; col <m[0].length; col++) {
                m[row][col] = m[row][col] * s;
            }
        }
    }

    /*===========matrixMult================
      Multply matrix n by the calling matrix, modify
      the calling matrix to store the result.
      
      eg.
      In the call m.matrixMult(n), n will remain the same
      and m will now be the product of n * m
    */
    public void matrixMult( Matrix n ) {
        m = matrixMult(n.m, m);
    }

    /**
     Multiplies matrix m by n
     @return Return matrix is m * n

     **/
    public static double[][] matrixMult(double[][] m, double[][] n) {
        double[][] newM = new double[m.length][n[0].length];
        for(int row = 0; row < m.length; row++) {
            for (int col2 = 0; col2 < n[0].length; col2++) {
                for(int col = 0; col < m[0].length; col++) {
                    newM[row][col2] += (m[row][col] * n[col][col2]);
                }
            }
        }
        return newM;
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
        /*
	  for(int row = 0; row < m.length; row++) {
	    for(int col = 0; col < m[0].length - 1; col++) {
		if(row==col) {
		    m[row][col] = 1;
		} else {
		    m[row][col] = 0;
		}
	    }
	    int col = m[0].length - 1;
	    switch(row) {
	    case 0:
		m[row][col] = x;
		break;
	    case 1:
		m[row][col] = y;
		break;
	    case 2:
		m[row][col] = z;
	    } 
	}
	 */
        m = new double[][]{ {1,0,0,x}, {0,1,0,y}, {0,0,1,z}, {0,0,0,1}};
    }

    /*===========MakeScale================
      Turns the calling matrix into the appropriate scale
      matrix using x, y and z as the scale factors.
     */
    public void makeScale(double x, double y, double z) {
        m = new double[][]{{x, 0, 0, 0}, {0, y, 0, 0}, {0, 0, z, 0}, {0, 0, 0, 1}};
    }

    /*=========== MakeRotX ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and X
      as the axis of rotation.
    */
    public void makeRotX(double theta) {
        m = new double[][]{{1, 0, 0, 0}, {0, Math.cos(theta), -1 * Math.sin(theta), 0}, {0, Math.sin(theta), Math.cos(theta), 0}, {0, 0, 0, 1}};
    }

    /*=========== MakeRotY ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and Y
      as the axis of rotation.
    */
    public void makeRotY(double theta) {
        m = new double[][]{{Math.cos(theta), 0, -1 * Math.sin(theta), 0}, {0, 1, 0, 0}, {Math.sin(theta), 0, Math.cos(theta), 0}, {0, 0, 0, 1}};
    }

    /*=========== MakeRotZ ================
      Turns the calling matrix into the appropriate rotation
      matrix using theta as the angle of rotation and axis
      as the axis of rotation.
    */
    public void makeRotZ(double theta) {
        m = new double[][]{{Math.cos(theta), -1 * Math.sin(theta), 0, 0},
                {Math.sin(theta), Math.cos(theta), 0, 0},
                {0, 0, 1, 0},
                {0, 0, 0, 1}};
    }

}
