/*========== MDLReader.java ==========
  MDLReader objects minimally contain an ArrayList<opCode> containing
  the opCodes generated when an mdl file is run through the java created
  lexer/parser, as well as the associated SymTab (Symbol Table).

  The provided methods are a constructor, and methods to print out the
  entries in the symbol table and command ArrayList.
  This is the only file you need to modify in order
  to get a working mdl project (for now).

  Your job is to go through each entry in opCodes and perform
  the required action from the list below:

  push: push a new origin matrix onto the origin stack
  pop: remove the top matrix on the origin stack

  move/scale/rotate: create a transformation matrix 
                     based on the provided values, then 
		     multiply the current top of the
		     origins stack by it.

  box/sphere/torus: create a solid object based on the
                    provided values. Store that in a 
		    temporary matrix, multiply it by the
		    current top of the origins stack, then
		    call draw_polygons.

  line: create a line based on the provided values. Store 
        that in a temporary matrix, multiply it by the
	current top of the origins stack, then call draw_lines.

  save: save the current screen with the provided filename

=========================*/

import java.util.*;
import java.io.*;
import java.awt.Color;

import parser.*;
import parseTables.*;

public class  MDLReader {

    ArrayList<opCode> opcodes;
    SymTab symbols;
    Set<String> symKeys;
    Stack<Matrix> origins;
    EdgeMatrix tmp;
    Frame f;

    public MDLReader(ArrayList<opCode> o, SymTab s) {

	opcodes = o;
	symbols = s;
	symKeys = s.keySet();
	
	tmp = new EdgeMatrix();
	f = new Frame();
	Matrix m = new Matrix(4);
	m.ident();
	origins = new Stack<Matrix>();
	origins.push(m);
    }

    public void printCommands() {
	
	Iterator i = opcodes.iterator();

	while (i.hasNext()) {
		System.out.println(i.next());
	    }
    }

    public void printSymbols() {

	Iterator i;

	i = symKeys.iterator();
	System.out.println("Symbol Table:");

	while (i.hasNext()) {
		String key = (String)i.next();
		Object value=symbols.get(key);
		System.out.println(""+key+"="+value);
	}
    }

    /*======== public void process()) ==========
      Inputs:   
      Returns: 
      
      Insert your interpreting code here

      you can use instanceof to check waht kind of op
      you are looking at:
          if ( oc instanceof opPush ) ...
	  
      you will need to typecast in order to get the
      operation specific data values

      04/23/12 09:52:32
      jdyrlandweaver
      ====================*/
    public void process() {
	
    	Iterator i = opcodes.iterator();
    	opCode oc;
    	
    	while (i.hasNext()) {
    	    
    	    oc = (opCode)i.next();
          if (oc instanceof opPop){
            origins.pop();
          } else if (oc instanceof opPush){
            Matrix copy = origins.peek().copy();
            origins.push(copy);

          } else if (oc instanceof opMove){
            double[] values = ((opMove)oc).getValues();
            tmp.makeTranslate(values[0],values[1],values[2]);

            Matrix top = origins.peek();
            top.matrixMult(tmp);

          } else if (oc instanceof opScale){
            double[] values = ((opScale)oc).getValues();
            tmp.makeScale(values[0],values[1],values[2]);

            Matrix top = origins.peek();
            top.matrixMult(tmp);
          } else if (oc instanceof opRotate){
            char axis = ((opRotate)oc).getAxis();
            double deg = ((opRotate)oc).getDeg();

            switch (axis){
              case 'x': tmp.makeRotX(deg);
                        break;
              case 'y': tmp.makeRotY(deg);
                        break;
              case 'z': tmp.makeRotZ(deg);
                        break;
            }
            Matrix top = origins.peek();
            top.matrixMult(tmp);
          } else if (oc instanceof opBox){
            double[] vertex = ((opBox)oc).getP1();
            double[] dims = ((opBox)oc).getP2();

            EdgeMatrix tmpbox = new EdgeMatrix();
            tmpbox.addPrism(vertex[0],vertex[1],vertex[2],
                          dims[0],dims[1],dims[2]);

            Matrix top = origins.peek();
            tmpbox.matrixMult(top);

            f.drawPolygons(tmpbox,Color.CYAN);
          } else if (oc instanceof opSphere){
            double[] center = ((opSphere)oc).getCenter();
            double radius = ((opSphere)oc).getR();

            EdgeMatrix tmpSphere = new EdgeMatrix();
            tmpSphere.addSphere(center[0],center[1],radius);

            Matrix top = origins.peek();
            tmpSphere.matrixMult(top);

            f.drawPolygons(tmpSphere,Color.CYAN);
          } else if (oc instanceof opTorus){
            double[] center = ((opTorus)oc).getCenter();
            double r = ((opTorus)oc).getr();
            double R = ((opTorus)oc).getR();

            EdgeMatrix tmpTorus = new EdgeMatrix();
            tmpTorus.addTorus(center[0],center[1],r,R);

            Matrix top = origins.peek();
            tmpTorus.matrixMult(top);

            f.drawPolygons(tmpTorus,Color.CYAN);
          } else if (oc instanceof opLine){
            double[] p1 = ((opLine)oc).getP1();
            double[] p2 = ((opLine)oc).getP2();

            f.drawLine((int)p1[0],(int)p1[1],
                      (int)p2[0],(int)p2[1],
                      Color.CYAN);
          } else if (oc instanceof opSave){
            String name = ((opSave)oc).getName();

            f.save(name);
          } else {
            System.out.println("opcode:"+ oc.toString() + " not recognized");
          }
    	}//end loop
    }
}
