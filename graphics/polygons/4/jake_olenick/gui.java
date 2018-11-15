import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.image.*;
import javax.imageio.*;

import java.io.*;
import java.util.*;

public class gui implements ActionListener,MouseListener, MouseMotionListener {

    public static final Color IMAGE_BACKGROUND = Color.BLACK;
    public static final Color INTERFACE_BACKGROUND = Color.WHITE;
    public static final int WINDOW_HEIGHT = Canvas.YRES;
    
    //differnt drawing modes
    public static final int LINE_MODE = 0;
    public static final int CIRCLE_MODE = 1;
    public static final int HERMITE_MODE = 2;
    public static final int BEZIER_MODE = 3;
    public static final int SPHERE_MODE = 4;
    public static final int TORUS_MODE = 5;
    public static final int BOX_MODE = 6;

    JFrame frame;
    Canvas canvas;
    JPanel iface;
    JPanel sidebar;

    JButton quit;
    JButton clear;
    JButton save;
    JLabel fnamelabel;
    JLabel transformlabel;
    JTextField fnamefield;
    JComboBox transformation;
    JLabel drawlabel;
    JComboBox drawmode;
    JTextField xarg;
    JTextField yarg;
    JTextField zarg;
    JLabel xlab;
    JLabel ylab;
    JLabel zlab;
    JButton apply;

    int clickcount=0;
    int[] xes = new int[10];
    int[] ys = new int[10];

    public gui() {

	frame = new JFrame();
	canvas = new Canvas();
	canvas.addMouseListener(this);
	canvas.addMouseMotionListener(this);

	//set window defaults
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	frame.getContentPane().setLayout(new FlowLayout());

	frame.setBackground( IMAGE_BACKGROUND );

	//add canvas
	frame.getContentPane().add(canvas);

	//set up the interface area
	iface = new JPanel();
	iface.setLayout(new GridLayout(10,1));
	iface.setBackground( INTERFACE_BACKGROUND );
	

	//add each interface element
	drawmode = new JComboBox();
	/* not 3d shapes
	drawmode.addItem("line");
	drawmode.addItem("circle");
	drawmode.addItem("hermite curve");
	drawmode.addItem("bezier curve");
	*/
	drawmode.addItem("sphere");
	drawmode.addItem("torus");
	drawmode.addItem("box");

	drawlabel = new JLabel("Shape:");
	iface.add(drawlabel);
	iface.add(drawmode);

	transformation = new JComboBox();
	transformation.addItem("translate");
	transformation.addItem("scale");
	transformation.addItem("x rotation");
	transformation.addItem("y rotation");
	transformation.addItem("z rotation");

	transformlabel = new JLabel("Transformation:");
	iface.add( transformlabel );
	iface.add(transformation);

	xlab = new JLabel("X: ");
	ylab = new JLabel("Y: ");
	zlab = new JLabel("Z: ");
	xarg = new JTextField();
	yarg = new JTextField();
	zarg = new JTextField();
	
	iface.add(xlab);
	iface.add(xarg);
	iface.add(ylab);
	iface.add(yarg);
	iface.add(zlab);
	iface.add(zarg);

	fnamelabel = new JLabel("Filename");
	fnamefield = new JTextField(4);
	iface.add(fnamelabel);
	iface.add(fnamefield);

	apply = new JButton("Apply");
	quit = new JButton("Quit");
	clear = new JButton("Clear");
	save = new JButton("Save");

	apply.addActionListener(this);
	quit.addActionListener(this);
	clear.addActionListener(this);
	save.addActionListener(this);
	iface.add(apply);
	iface.add(clear);
	iface.add(save);
	iface.add(quit);
	
	sidebar = new JPanel();
	sidebar.setPreferredSize( new Dimension( 300, WINDOW_HEIGHT) );
	sidebar.setBackground( INTERFACE_BACKGROUND );
	sidebar.add( iface );

	//add interface
	frame.getContentPane().add(sidebar);

	frame.pack();
	frame.setVisible(true);
    }

    /*======== public void mousePressed() ==========
      
      mousePressed is triggered when the left mouse button 
      is initially pressed down. 

      No drawing occurs when the mouse is pressed, drawing 
      only happens on release or on dragging.

      The current x and y coordiantes of the mouse should
      be stored in the appropriate index of xes and ys, 
      respectively (the index should be the value of 
      clickcount.

      e.getX() and e.getY() will return the current x and
      y coordinates.
      ====================*/
    public void mousePressed(MouseEvent e) {
	int x,y;
	x = e.getX();
	y = e.getY();

	String mode = (String)drawmode.getSelectedItem();

	if ( clickcount == 0 || clickcount == 2 && !mode.equals("torus") ) {

	    xes[clickcount] = x;
	    ys[clickcount] = y;
	    clickcount++;
	}
    }

    /*======== public void mouseDragged() ==========

      mouseDragged is triggered when the left mouse button
      is being held down and the mouse is moving.
      
      When the mouse is being dragged, the temporary line in 
      canvas should be updated to draw the line from the (x, y)
      position when the mouse was initially clicked (stored in 
      xes and ys) and the current (x,y) position

      When drawmode is set to circle, update the canvas'
      temporary EdgeMatrix to draw the circle with center
      (xes[0], ys[0]) that goes to (x, y)
      

      When drawmode is set to one of the curves, clickcount 
      comes into play. If the clickcount == 1 (mouse has 
      been pressed down once), then you only have enough
      information to draw the first bounding line for the 
      curve. Store the current values of x and y in xes[1] 
      and ys[1] and have Canvas draw a single temporary line.
      If the clickcount == 3, then you have enough information
      to draw the two bounding lines and the curve, so all
      three should be added to the temporary line in canvas.

      When drawmode is set to sphere, updtae the canvas'
      temporary EdgeMatrix to draw the sphere points with
      center (xes[0], ys[0]) with (x, y) representing a 
      point on the sphere's surface.

      When drawmode is set to torus, we need clickcount.
      If clickcount == 1, draw a temporary line, this line
      will represent the inner radius of the torus. This
      is the only time mouseDragged is used for a torus.

      When drawmode is set to box, update the canvas'
      temporary EdgeMatrix to draw a box with upper 
      left corner (xes[0], ys[0]) and lower right corner
      (x, y). Because boxes need a depth as well,
      make the depth equal to one of the other 
      dimensions.

      You should use the setDrawing() method in canvas
      Make sure that you only draw one temporary line at
      a time.
      ====================*/
    public void mouseDragged(MouseEvent e) {
	int x,y;
	x = e.getX();
	y = e.getY();
	
	String mode = (String)drawmode.getSelectedItem();
	

	if ( mode.equals("line") )
	    canvas.setDrawing(xes[0], ys[0], x, y, 0, 0, 0, 0, LINE_MODE);
	   
	else if ( mode.equals("circle" ) ) {
	    double r = EdgeMatrix.distance( xes[0], ys[0], x, y );
	    canvas.setDrawing(xes[0], ys[0], (int)r, 0, 0, 0, 0, 0, CIRCLE_MODE);
	}

	else if ( mode.equals("sphere" ) ) {	    
	    double r = EdgeMatrix.distance( xes[0], ys[0], x, y );
	    canvas.setDrawing(xes[0], ys[0], (int)r, 0, 0, 0, 0, 0, SPHERE_MODE);	
	}

	else if ( mode.equals( "torus" ) ) {
	    
	    if ( clickcount == 1 ) 
		canvas.setDrawing(xes[0], ys[0], x, y, 0, 0, 0, 0, LINE_MODE);
	}

	else if ( mode.equals( "box" ) ) {
	    int width, height, depth;
	    
	    width = Math.abs( x - xes[0] );
	    height = Math.abs( y - ys[0] );
	    depth = height;
	    
	    canvas.setDrawing(xes[0], ys[0], 0, width, height, depth, 0, 0, BOX_MODE);
	}

	else if ( mode.equals("hermite curve") ||
		  mode.equals("bezier curve") ) {

	    if ( clickcount == 1 ) {
		canvas.setDrawing(xes[0], ys[0], x, y, 0, 0, 0, 0, LINE_MODE);
		
		xes[clickcount] = x;
		ys[clickcount] = y;
	    } //end initial curve line

	    else if (clickcount == 3 ) {

		if ( mode.equals( "hermite curve" ) )
		    canvas.setDrawing( xes[0], ys[0], xes[1], ys[1], xes[2], ys[2], x, y, HERMITE_MODE );
		else
		    canvas.setDrawing( xes[0], ys[0], xes[1], ys[1], xes[2], ys[2], x, y, BEZIER_MODE );
		
		xes[clickcount] = x;
		ys[clickcount] = y;
	    } //end second curve line

	} //end curve mode

	canvas.paintComponent(canvas.getGraphics());
	canvas.clearTmp();
    }

    /*======== public void mouseReleased() ==========

      mouseReleased is triggered when the left mouse button
      is released. 
      
      If the drawmode is line, then releasing signals the
      end of drawing a line. The final line should be
      added to the canvas's permanent EdgeMatrix. Reset 
      clickcount as well.

      If the drawmode is circle, then releasing signals the
      end of drawing a circle. The final circle should be
      added to the canvas's permanent EdgeMatrix. Reset 
      clickcount as well.

      If drawmode is one of the curves, there are two 
      possibilities. 
           If the clickcount == 1, then only 
      the first bounding line has been set. This line 
      has already been added to the temporary matrix in
      the mouseDragged method. All that needs to be done 
      is update xes and ys to contain the current x and y
      coordinates (at clickcount) and increment clickcount.
           If the clickcount == 3, then add the correct curve
      to the canvas' permanent EdgeMatrix and reset clickcount

      If the drawmode is sphere, then releasing signals the
      end of drawing a sphere. The final sphere should be
      added to the canvas's permanent EdgeMatrix. Reset 
      clickcount as well.

      If the drawmode is torus, releasing signals the end
      of setting the inner radius. Add (x, y) to xes and 
      ys at clickout (which should be 1) and increment 
      clickcount. Do to not draw anything.
      
      If the drawmode is box, then releasing signals the
      end of drawing a box. The final box should be
      added to the canvas's permanent EdgeMatrix. Reset 
      clickcount as well.

      Clear the canvas' temporary line matrix and redraw
      the canvas for all modes other than torus.
      ====================*/
    public void mouseReleased(MouseEvent e) {
	int x,y;
	x = e.getX();
	y = e.getY();

	String mode = (String)drawmode.getSelectedItem();
	
	if ( mode.equals("line") ) {
	 
	    canvas.addLine( xes[0], ys[0], 0, x, y, 0 );
	    clickcount = 0;
	    canvas.stopDrawing();
	} //end line mode

	else if ( mode.equals("circle") ) {

	    double r = EdgeMatrix.distance( xes[0], ys[0], x, y );	 
	    canvas.addCircle( xes[0], ys[0], (int)r );
	    clickcount = 0;
	    canvas.stopDrawing();
	} //end circle mode

	else if ( mode.equals("sphere") ) {
	 
	    double r = EdgeMatrix.distance( xes[0], ys[0], x, y );
	    canvas.addSphere( xes[0], ys[0], (int)r );
	    clickcount = 0;
	    canvas.stopDrawing();
	} //end sphere mode

	else if ( mode.equals("torus") && clickcount == 1 ) {
	    
	    xes[clickcount] = x;
	    ys[clickcount] = y;
	    clickcount++;
	}
	
	else if ( mode.equals("box") ) {

	    int width, height, depth;
	    
	    width = Math.abs( x - xes[0] );
	    height = Math.abs( y - ys[0] );
	    depth = height;
	    
	    canvas.addBox( xes[0], ys[0], 0, width, height, depth );
	    clickcount = 0;
	    canvas.stopDrawing();
	}

	else if ( ( mode.equals("hermite curve") ||
		    mode.equals("bezier curve") ) &&
		  clickcount == 1 ) {

	    xes[clickcount] = x;
	    ys[clickcount] = y;
	    clickcount++;
	} //end mid-curve mode
	    
	else if ( ( mode.equals("hermite curve") ||
		    mode.equals("bezier curve") ) &&
		  clickcount == 3 ) {
		    
	    if ( mode.equals("hermite curve") )
		canvas.addCurve( xes[0], ys[0], xes[1], ys[1], xes[2], ys[2], x, y, HERMITE_MODE);
	    else
		canvas.addCurve( xes[0], ys[0], xes[1], ys[1], xes[2], ys[2], x, y, BEZIER_MODE);
	    
	    clickcount = 0;
	    canvas.stopDrawing();
	} //end curve mode


    }


    /*======== public void mouseMoved() ==========
      Inputs:  MouseEvent e 
      Returns: 
      
      Moving the mouse is a useful event only when drawing
      a torus.

      If drawmode is torus and clickount == 2, then moving the
      mouse (as opposed to dragging, which requires the button
      to be pushed) is used to deinfe the radius of the circles
      that make up the torus. When the mouse is moved, the 
      canvas' temporary EdgeMatrix should contain the torus with
      center (xes[0], ys[0]) whose inner radius is set by the 
      distance between (xes[0], ys[0]) and (xes[1], ys[1]), and 
      whose circle radius is set by the distance between 
      (x, y) and (xes[1], ys[1]). You should perform the distance
      calculations here.

      Remember to redraw the canvas and clear the temporary
      EdgeMatrix like in MouseDragged.


      04/01/12 17:02:05
      jonalf
      ====================*/
    public void mouseMoved(MouseEvent e) {
	
	String mode = (String)drawmode.getSelectedItem();
	int x,y;
	x = e.getX();
	y = e.getY();

	if ( mode.equals( "torus" ) && clickcount == 2 ) {
	    
	    double r2 = EdgeMatrix.distance( xes[0], ys[0], xes[1], ys[1] );
	    double r1 = EdgeMatrix.distance( xes[1], ys[1], x, y );		
	    
	    canvas.setDrawing( xes[0], ys[0], (int)r1, (int)r2, 
			       0, 0, 0, 0, TORUS_MODE);	

	    canvas.paintComponent(canvas.getGraphics());
	    canvas.clearTmp();
	}	
    }  

    /*======== public void mouseClicked() ==========
      Inputs:  MouseEvent e 
      Returns: 
      
      A full mouse click (press and release in one action)
      is used to set the final infromation for a torus.

      When the drawmode is torus and clickcount == 2, The 
      canvas' permanent EdgeMatrix should contain the torus with
      center (xes[0], ys[0]) whose inner radius is set by the 
      distance between (xes[0], ys[0]) and (xes[1], ys[1]), and 
      whose circle radius is set by the distance between 
      (x, y) and (xes[1], ys[1]). You should perform the distance
      calculations here.

      Also remember to stop drawing and reset clickcount.

      04/01/12 17:09:16
      jonalf
      ====================*/
    public void mouseClicked(MouseEvent e) {
	


	String mode = (String)drawmode.getSelectedItem();
	int x,y;
	x = e.getX();
	y = e.getY();

	if ( mode.equals( "torus" ) && clickcount == 2) {
	    
	    double r2 = EdgeMatrix.distance( xes[0], ys[0], xes[1], ys[1] );
	    double r1 = EdgeMatrix.distance( xes[1], ys[1], x, y );		
	    
	    canvas.addTorus( xes[0], ys[0], (int)r1, (int)r2 );
	    canvas.stopDrawing();
	    clickcount = 0;
	}
    }

    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}


    /*======== public void actionPerformed() ==========
      Inputs:  ActionEvent e 
      Returns: 

      All of the interface buttons are attached to this
      method. If the "apply" button is clicked, you need
      to figure out which transformation is being applied
      and then apply it to the canvas

      03/09/12 09:24:44
      jdyrlandweaver
      ====================*/
    public void actionPerformed(ActionEvent e) {

	double xar, yar, zar;

	if (e.getSource()==quit) {
	    System.exit(0);
	}
	else if (e.getSource() == apply) {
	    
	    String mode=(String)transformation.getSelectedItem();
	    if ( mode.equals("translate") ) {
		
		if ( xarg.getText().equals("") )
		    xar = 0;
		else
		    xar = Double.parseDouble( xarg.getText() );
		if ( yarg.getText().equals("") )
		    yar = 0;
		else
		    yar = Double.parseDouble( yarg.getText() );
		if ( zarg.getText().equals("") )
		    zar = 0;
		else
		    zar = Double.parseDouble( zarg.getText() );

		canvas.translate( xar, yar, zar );
	    }
	    else if ( mode.equals("scale") ) {
		if ( xarg.getText().equals("") )
		    xar = 1;
		else
		    xar = Double.parseDouble( xarg.getText() );
		if ( yarg.getText().equals("") )
		    yar = 1;
		else
		    yar = Double.parseDouble( yarg.getText() );
		if ( zarg.getText().equals("") )
		    zar = 1;
		else
		    zar = Double.parseDouble( zarg.getText() );
		
		canvas.scale( xar, yar, zar );
	    }
	    else if ( mode.equals("x rotation") ) {
		if ( xarg.getText().equals("") )
		    xar = 0;
		else
		    xar = Double.parseDouble( xarg.getText() );
		canvas.rotX( xar );
	    }
	    else if ( mode.equals("y rotation") ) {
		if ( yarg.getText().equals("") )
		    yar = 0;
		else
		    yar = Double.parseDouble( yarg.getText() );		
		canvas.rotY( yar );
	    }
	    else if ( mode.equals("z rotation") ) {
		if ( zarg.getText().equals("") )
		    zar = 0;
		else
		    zar = Double.parseDouble( zarg.getText() );		
		canvas.rotZ( zar );
	    }
	}
				  
	else if (e.getSource()==save) {
	    // save
	    System.out.println("Saving: "+ fnamefield.getText() );
	    BufferedImage bi = canvas.getBufferedImage();
	    try {
		File fn = new File(fnamefield.getText());
		ImageIO.write(bi,"png",fn);
	    }
	    catch (IOException ex) { }
	}
	else if (e.getSource()==clear) {
	    canvas.clearPoints();
	}
    }

    public static void main(String[] args) {

	gui g = new gui();
    }
}

