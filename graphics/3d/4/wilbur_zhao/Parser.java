/*========== Parser.java ==========

Goes through a file and performs all of the actions listed.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         l: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 i: set the transform matrix to the identity matrix - 
	 s: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 t: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 x: create an x-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 y: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 z: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 a: apply the current transformation matrix to the 
	    edge matrix
	 g: draw the lines of the edge matrix to the Frame
	    save the Frame to a file -
	    takes 1 argument (file name)
	 q: end parsing

See the file script for an example of the file format


IMPORTANT MATH NOTE:
the trig functions in java.Math  use radian mesure, but us normal
humans use degrees, so the file will contain degrees for rotations,
be sure to conver those degrees to radians (Math.PI is the constant
for PI)


jdyrlandweaver
=========================*/

import java.io.*;
import java.util.*;
import java.awt.*;

public class Parser {

	public static final int HERMITE_MODE = 0;
	public static final int BEZIER_MODE = 1;

	public static Color DRAW_COLOR = Color.CYAN;
	
    /*===========================
      transform is the master transform Matrix
      em is the master EdgeMatrix
      f is the frame used for drawing and saving
      =========================*/
    private Matrix transform;
    private EdgeMatrix em;
    private Frame f;
	
    public Parser() {
	
	f = new Frame();
	transform = new Matrix();
	em = new EdgeMatrix();
	transform.ident();
    }


    /*========     public void parseFile() ==========
      Inputs:   BufferedReader in  
      Returns: 

      Goes through the input stream referred to by in,
      scans it for the commands listed above, and performs
      the required commands.
      
      03/08/12 19:20:55
      jdyrlandweaver
      ====================*/
    public void parseFile( BufferedReader in ) {
    	String line = "";
    	Matrix adjuster = new Matrix();
    	try {
	    	while (true){
	    		line = in.readLine();
	    		//System.out.println(line);
	    		if (line.equals("l")){//drawline
	    			line = in.readLine();
	    			String[] args = line.split(" ");

	    			double x0 = Double.parseDouble(args[0]);
	    			double y0 = Double.parseDouble(args[1]);
	    			double z0 = Double.parseDouble(args[2]);

	    			double x1 = Double.parseDouble(args[3]);
	    			double y1 = Double.parseDouble(args[4]);
	    			double z1 = Double.parseDouble(args[5]);

	    			em.addEdge(x0,y0,z0,x1,y1,z1);
	    		} else if (line.equals("i")){//identity matrix
	    			transform.ident();
	    		} else if (line.equals("s")){//scaling matrix
	    			line = in.readLine();
	    			String[] args = line.split(" ");

	    			double x = Double.parseDouble(args[0]);
	    			double y = Double.parseDouble(args[1]);
	    			double z = Double.parseDouble(args[2]);

	    			adjuster.makeScale(x,y,z);
	    			transform.matrixMult(adjuster);

	    		} else if (line.equals("t")){//translating matrix
	    			line = in.readLine();
	    			String[] args = line.split(" ");

	    			double x = Double.parseDouble(args[0]);
	    			double y = Double.parseDouble(args[1]);
	    			double z = Double.parseDouble(args[2]);

	    			adjuster.makeTranslate(x,y,z);
	    			transform.matrixMult(adjuster);
	    		} else if (line.equals("x")){//x rotation matrix
	    			line = in.readLine();

	    			double theta = Double.parseDouble(line);

	    			adjuster.makeRotX(theta);
	    			transform.matrixMult(adjuster);
	    		} else if (line.equals("y")){//y rotation matrix
	    			line = in.readLine();

	    			double theta = Double.parseDouble(line);

	    			adjuster.makeRotY(theta);
	    			transform.matrixMult(adjuster);
	    		} else if (line.equals("z")){//z rotation matrix
	    			line = in.readLine();

	    			double theta = Double.parseDouble(line);

	    			adjuster.makeRotZ(theta);
	    			transform.matrixMult(adjuster);
	    		} else if (line.equals("a")){//apply transformations and clears the transform
	    			em.matrixMult(transform);
	    			transform.ident();
	    		} else if (line.equals("c")){
					line = in.readLine();

					String[] args = line.split(" ");
					double cx = Double.parseDouble(args[0]);
					double cy = Double.parseDouble(args[1]);
					double r = Double.parseDouble(args[2]);
					
					em.addCircle(cx,cy,r);
				} else if (line.equals("h") || line.equals("b")){
					String type = line;
					line = in.readLine();

					String[] args = line.split(" ");
					double x0 = Double.parseDouble(args[0]);
					double y0 = Double.parseDouble(args[1]);
					double x1 = Double.parseDouble(args[2]);
					double y1 = Double.parseDouble(args[3]);
					double x2 = Double.parseDouble(args[4]);
					double y2 = Double.parseDouble(args[5]);
					double x3 = Double.parseDouble(args[6]);
					double y3 = Double.parseDouble(args[7]);
					if (type.equals("h")){
						em.addCurve(x0,y0,x1,y1,x2,y2,x3,y3,HERMITE_MODE);
					} else {
						em.addCurve(x0,y0,x1,y1,x2,y2,x3,y3,BEZIER_MODE);
					}
					
				} else if (line.equals("w")){//clears edge matrix
					em = new EdgeMatrix();
				} else if (line.equals("p")){//prism
					line = in.readLine();
					String[] args = line.split(" ");
					double x = Double.parseDouble(args[0]);
					double y = Double.parseDouble(args[1]);
					double z = Double.parseDouble(args[2]);
					double width = Double.parseDouble(args[3]);
					double height = Double.parseDouble(args[4]);
					double depth = Double.parseDouble(args[5]);

					em.addPrism(x,y,z,width,height,depth);
					
				} else if (line.equals("m")){//munchkin/sphere
					line = in.readLine();
					String[] args = line.split(" ");
					double x = Double.parseDouble(args[0]);
					double y = Double.parseDouble(args[1]);
					double r = Double.parseDouble(args[2]);

					em.addSphere(x,y,r);
				} else if (line.equals("d")){//torus/doughnut
					line = in.readLine();
					String[] args = line.split(" ");
					double x = Double.parseDouble(args[0]);
					double y = Double.parseDouble(args[1]);
					double r = Double.parseDouble(args[2]);
					double R = Double.parseDouble(args[3]);

					em.addTorus(x,y,r,R);
				} else if (line.equals("~")){//change color
					line = in.readLine();
					String[] args = line.split(" ");
					int r = Integer.parseInt(args[0]);
					int g = Integer.parseInt(args[1]);
					int b = Integer.parseInt(args[2]);

					DRAW_COLOR = new Color(r,g,b);
					
				} else if (line.equals("g")){//graph transformations, also clears the frame
	    			f.drawLines(em,DRAW_COLOR);
	    			line = in.readLine();
	    			f.save(line);
	    			f.clearScreen();

	    		} else if (line.equals("q")){//stop parsing
	    			System.out.println("q reached, ending parsing");
	    			break;
	    		}
	    	}
    	} catch (IOException E){
    		System.out.println("Incorrect formatting of script file.");
    	}

    }
}
