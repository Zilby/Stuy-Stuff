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
		if(oc instanceof opPush) {
			Matrix top = origins.peek();
			origins.push(top.copy());
		} else if (oc instanceof opPop) {
			origins.pop();
		} else if (oc instanceof opMove) {
			Matrix trx = new Matrix();
			double[] vals = ((opMove)oc).getValues();
			trx.makeTranslate(vals[0], vals[1], vals[2]);
			origins.peek().matrixMult(trx);
		} else if (oc instanceof opRotate) {
			Matrix trx = new Matrix();
			char axis = ((opRotate)oc).getAxis();
			double angle = ((opRotate)oc).getDeg();
			switch(axis) {
				case 'x':
					trx.makeRotX(angle);
					break;
				case 'y':
					trx.makeRotY(angle);
					break;
				case 'z':
					trx.makeRotZ(angle);
					break;
			}
			origins.peek().matrixMult(trx);
		} else if (oc instanceof opScale) {
			Matrix trx = new Matrix();
			double[] vals = ((opScale)oc).getValues();
			trx.makeScale(vals[0], vals[1], vals[2]);
			origins.peek().matrixMult(trx);
		} else if (oc instanceof opBox) {
			double[] p1 = ((opBox)oc).getP1();
			double[] p2 = ((opBox)oc).getP2();
			 
			tmp.addBox(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2]);
			tmp.matrixMult(origins.peek());
			f.drawPolygons(tmp, new Color(128,128,128));
			tmp.clear();
		} else if (oc instanceof opSphere) {
			double[] c = ((opSphere)oc).getCenter();
			tmp.addSphere(c[0], c[1], c[2], ((opSphere)oc).getR());
			tmp.matrixMult(origins.peek());
			f.drawPolygons(tmp, new Color(128,128,128));
			tmp.clear();
		} else if (oc instanceof opTorus) {
			double[] c = ((opTorus)oc).getCenter();
			tmp.addTorus(c[0], c[1], c[2], ((opTorus)oc).getR(), ((opTorus)oc).getr());
			tmp.matrixMult(origins.peek());
			f.drawPolygons(tmp, new Color(128,128,128));
			tmp.clear();
		} else if (oc instanceof opLine) {
			double[] p1 = ((opLine)oc).getP1();
			double[] p2 = ((opLine)oc).getP2();
			tmp.addPolygon(p1[0],p1[1],p1[2],p2[0],p2[1],p2[2],p2[0],p2[1],p2[2]);
			tmp.matrixMult(origins.peek());
			f.drawPolygons(tmp, new Color(128,128,128));
			tmp.clear();
		} else if (oc instanceof opSave) {
			f.save(((opSave)oc).getName());
		}

	}//end loop
    }
}
