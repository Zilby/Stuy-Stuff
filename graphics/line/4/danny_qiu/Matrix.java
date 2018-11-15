import java.util.*;
import java.io.*;

public class Matrix {

    private ArrayList<int[]> matrix;
    int rows;
    int cols;

    /**
     * Method to create a new two-dimentional matrix to store points
     * @param _rows number of rows in the matrix
     * @param _cols number of columns in the matrix
     */
    private void newMatrix(int _rows, int _cols) {
        rows = _rows;
        cols = _cols;
        matrix = new ArrayList<int[]>();
        for (int i=0; i<rows; i++) {
            matrix.add(new int[cols]);
        }
    }

    public Matrix() {
        newMatrix(0, 4);
    }

    public Matrix(int rows, int cols) {
        newMatrix(rows, cols);
    }

    /**
     * Adds an edge to the matrix given x, y, z coordinates for the two points
     * that define the edge line
     * @param x0 x-coordinate of starting point 
     * @param y0 y-coordinate of starting point 
     * @param z0 z-coordinate of starting point 
     * @param x1 x-coordinate of ending point 
     * @param y1 y-coordinate of ending point 
     * @param z1 z-coordinate of ending point 
     */
    public void addEdge(int x0, int y0, int z0, int x1, int y1, int z1) {
        addPoint(x0, y0, z0);
        addPoint(x1, y1, z1);
    }

    /**
     * Adds a point to the matrix given x, y, z coordinates
     * @param x x-coordinate of point
     * @param y y-coordinate of point
     * @param z z-coordinate of point
     */
    public void addPoint(int x, int y, int z) {
        rows++;
        int[] p = {x, y, z, 1};
        matrix.add(p);
    }

    /**
     * Clears all points in the matrix
     */
    public void clear() {
        matrix.clear();
    }

    /**
     * Returns the matrix as an ArrayList of arrays
     * @return matrix as an ArrayList of arrays
     */
    public ArrayList<int[]> getMatrix() {
        return matrix;
    }

    /**
     * Converts the matrix into human-readable format
     * @return string containing the matrix printout
     */
    public String toString() {
        String output = "{\n";
        for (int i=0; i<rows; i++) {
            output += Arrays.toString(matrix.get(i)) + ",\n";
        }
        output += "}\n";
        return output;
    }

}
