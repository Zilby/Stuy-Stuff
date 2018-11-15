/*========== MDLReader.java ==========
  MDLReader objects minimally contain an ArrayList<opCode> containing
  the opCodes generated when an mdl file is run through the java created
  lexer/parser, as well as the associated SymTab (Symbol Table).

  The provided methods are a constructor, and methods to print out the
  entries in the symbol table and command ArrayList.

  Your job is to go through each entry in opCodes and perform
  the required action from the list below:

  frames: set numFrames for animation

  basename: set baseName for animation

  vary: manipluate knob values between two given frames
        over a specified interval

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
  	int numFrames;
  	String baseName;
  	boolean isAnimation;

  	public MDLReader(ArrayList<opCode> o, SymTab s) {

  		opcodes = o;
  		symbols = s;
  		symKeys = s.keySet();
  		numFrames = 0;
  		baseName = "frame";

  		tmp = new EdgeMatrix();
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

    /*======== public void firstPass()) ==========
      Inputs:   
      Returns: 

      Checks the op ArrayList for any animation commands
      (frames, basename, vary)
      
      Should set numFrames and basename if the frames 
      or basename commands are present
      
      If vary is found, but frames is not, the entire
      program should exit.
      
      If frames is found, but basename is not, set name
      to some default value, and print out a message
      with the name being used.

      05/17/12 09:54:22
      jdyrlandweaver
      ====================*/
      public void firstPass() {
      	Iterator i = opcodes.iterator();
      	opCode oc;
      	boolean foundFrames = false;
      	boolean foundBasename = false;

      	while(i.hasNext()) {
      		oc = (opCode)i.next();
      		if(oc instanceof opFrames) {
      			foundFrames = true;
      			numFrames = ((opFrames)oc).getNum();
      		} else if (oc instanceof opBasename) {
      			foundBasename = true;
      			baseName = ((opBasename)oc).getName();
      		} else if (oc instanceof opVary) {
      			if(!foundFrames) {
      				System.out.println("Frames command not found. Frames command must be before vary command. Exiting now.");
      				System.exit(1);
      			}
      		}
      	}

      	if(foundFrames && !foundBasename) {
      		System.out.println("Using default basename 'frame'");
      	}

      }




    /*======== public LinkedList<VaryNode>[] secondPass()) ==========
      Inputs:   
      Returns: An array of Linked Lists of VaryNodes

      In order to set the knobs for animation, we need to keep
      a seaprate value for each knob for each frame. We can do
      this by using an array of linked lists. Each array index
      will correspond to a frame (eg. knobs[0] would be the first
      frame, knobs[2] would be the 3rd frame and so on).
      
      Each index should contain a linked list of VaryNodes, each
      node contains a knob name and a value (see VaryNode.java)

      Go through the opcode ArrayList, and when you find vary, go 
      from knobs[0] to knobs[frames-1] and add (or modify) the
      vary_node corresponding to the given knob with the
      appropirate value. 

      05/17/12 09:55:29
      jdyrlandweaver
      ====================*/
      public LinkedList<VaryNode>[] secondPass() {
      	Iterator it = opcodes.iterator();
      	opCode oc;

      	LinkedList[] lists = new LinkedList[numFrames];
      	while(it.hasNext()) {
      		oc = (opCode)it.next();
      		if(oc instanceof opVary) {
      			opVary vary = (opVary)oc;
      			double inc = (vary.getEndval() - vary.getStartval())/(vary.getEndframe() - vary.getStartframe());
      			for(int i = vary.getStartframe(); i <= vary.getEndframe(); i++) {
      				int n = i - vary.getStartframe();
      				if(lists[i] == null) {
      					lists[i] = new LinkedList<VaryNode>();
      				}
      				lists[i].add(new VaryNode(n*inc + vary.getStartval(), vary.getKnob()));
      			}
      		}
      	}
      	return (LinkedList<VaryNode>[])lists;
      }

      public void printKnobs() {

      	Iterator i;
      	int c = 0;

      	i = symKeys.iterator();
      	System.out.println("Knob List:");
      	System.out.println( "ID\tNAME\tVALUE\n" );

      	while (i.hasNext()) {
      		String key = (String)i.next();
      		Object value=symbols.get(key);
      		System.out.printf( "%d\t%s\t%6.2f\n", c++, key, value );
      	}
      }

      private double getListVal(LinkedList<VaryNode> varyNodes, String knob) {
      	Iterator<VaryNode> i = varyNodes.iterator();
      	while(i.hasNext()) {
      		VaryNode p = i.next();
      		if(p.getName().equals(knob)) {
      			return p.getValue();
      		}
      	}
      	return 1;
      }
      public Frame processOps(LinkedList<VaryNode> varyNodes) {
      	Frame f = new Frame();
      	double knobVal, xval, yval, zval;

      	Iterator i = opcodes.iterator();
      	opCode oc;
      	origins = new Stack<Matrix>();
      	Matrix m = new Matrix();
      	m.ident();
      	origins.push(m);

      	while (i.hasNext()) {

      		oc = (opCode)i.next();
      		String command = oc.getClass().getName();

      		if ( oc instanceof opPush ) {

      			m = origins.peek().copy();
      			origins.push( m );
      		}

      		else if ( oc instanceof opPop ) {
      			origins.pop();
      		}

      		else if ( oc instanceof opSphere ) {

      			tmp.addSphere( ((opSphere)oc).getCenter()[0],
      				((opSphere)oc).getCenter()[1],
      				((opSphere)oc).getCenter()[2],
      				((opSphere)oc).getR());

      			tmp.matrixMult( origins.peek() );
      			f.drawPolygons( tmp, new Color( 0, 255, 255 ) );
      			tmp.clear();
      		}

      		else if ( oc instanceof opTorus ) {

      			tmp.addTorus( ((opTorus)oc).getCenter()[0],
      				((opTorus)oc).getCenter()[1],
      				((opTorus)oc).getCenter()[2],
      				((opTorus)oc).getr(), 
      				((opTorus)oc).getR());
      			tmp.matrixMult( origins.peek() );
      			f.drawPolygons( tmp, new Color( 0, 255, 255 ) );
      			tmp.clear();
      		}

      		else if ( oc instanceof opBox ) {

      			tmp.addBox( ((opBox)oc).getP1()[0],
      				((opBox)oc).getP1()[1],
      				((opBox)oc).getP1()[2],
      				((opBox)oc).getP2()[0],
      				((opBox)oc).getP2()[1],
      				((opBox)oc).getP2()[2] );

      			tmp.matrixMult( origins.peek() );
      			f.drawPolygons( tmp, new Color( 0, 255, 255 ) );
      			tmp.clear();
      		}

      		else if ( oc instanceof opMove ) {

      			Matrix t = new Matrix(4);

      			xval = ((opMove)oc).getValues()[0];
      			yval = ((opMove)oc).getValues()[1];
      			zval = ((opMove)oc).getValues()[2];
      			String knob = ((opMove)oc).getKnob();
      			double scale = 1;
      			if(knob != null && knob.length() > 0 && varyNodes != null ) {
      				scale = getListVal(varyNodes, knob);
      			}

      			t.makeTranslate( xval * scale, yval * scale, zval * scale);

      			t.matrixMult( origins.peek() );
      			origins.pop();
      			origins.push( t );
      		}	
      		else if ( oc instanceof opScale ) {

      			Matrix t = new Matrix(4);

      			xval = ((opScale)oc).getValues()[0];
      			yval = ((opScale)oc).getValues()[1];
      			zval = ((opScale)oc).getValues()[2];
      			String knob = ((opScale)oc).getKnob();
      			double scale = 1;
      			if(knob != null && knob.length() > 0 && varyNodes != null ) {
      				scale = getListVal(varyNodes, knob);
      			}
      			t.makeScale( xval * scale, yval * scale, zval * scale);

      			t.matrixMult( origins.peek() );
      			origins.pop();
      			origins.push( t );
      		}	

      		else if ( oc instanceof opRotate ) {

      			double angle = ((opRotate)oc).getDeg() * (Math.PI / 180);
      			char axis = ((opRotate)oc).getAxis();
      			Matrix t = new Matrix(4);
      			String knob = ((opRotate)oc).getKnob();
      			double scale = 1;

      			if(knob != null && knob.length() > 0 && varyNodes != null ) {
      				scale = getListVal(varyNodes, knob);
      			}
      			angle = angle * scale;
      			if ( axis == 'x' )
      				t.makeRotX( angle );
      			else if ( axis == 'y' )
      				t.makeRotY( angle );
      			else
      				t.makeRotZ( angle );


      			t.matrixMult( origins.peek() );
      			origins.pop();
      			origins.push( t );
      		}

      		else if ( oc instanceof opSave ) {
      			f.save( ((opSave)oc).getName() );
      		} 
      	}
      	return f;
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

      If frames is not present in the source (and therefore 
      numFrames is 1, then process_knobs should be called.
      
      If frames is present, the enitre op array must be
      applied frames time. At the end of each frame iteration
      save the current screen to a file named the
      provided basename plus a numeric string such that the
      files will be listed in order, then clear the screen and
      reset any other data structures that need it.
      
      Important note: you cannot just name your files in 
      regular sequence, like pic0, pic1, pic2, pic3... if that
      is done, then pic1, pic10, pic11... will come before pic2
      and so on. In order to keep things clear, add leading 0s
      to the numeric portion of the name. If you use String.format
      (look it up online), you can use "%0xd" for this purpose. 
      It will add at most x 0s in front of a number, if needed, 
      so if used correctly, and x = 4, you would get numbers 
      like 0001, 0002, 0011, 0487

      04/23/12 09:52:32
      jdyrlandweaver
      ====================*/
      public void process() {

      	double knobVal, xval, yval, zval;

      	opCode oc;
      	origins = new Stack<Matrix>();
      	Matrix m = new Matrix();
      	m.ident();
      	origins.push(m);

      	firstPass();
      	LinkedList<VaryNode>[] varyLists = secondPass();

      	if(numFrames == 1) {
      		processOps(null);
      		return;
      	}
      	int digits = String.valueOf(numFrames).length() + 1;
      	for(int i = 0; i < numFrames; i++) {
      		Frame f = processOps(varyLists[i]);
      		f.save(String.format(baseName + "%0" + digits + "d", i) + ".png");
      	}
      }
  }
