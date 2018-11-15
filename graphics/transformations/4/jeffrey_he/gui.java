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
    JTextField xarg;
    JTextField yarg;
    JTextField zarg;
    JLabel xlab;
    JLabel ylab;
    JLabel zlab;
    JButton apply;

    int clickcount = 0;
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
        sidebar.setPreferredSize( new Dimension( 250, WINDOW_HEIGHT) );
        sidebar.setBackground( INTERFACE_BACKGROUND );
        sidebar.add( iface );

        //add interface
        frame.getContentPane().add( sidebar );

        frame.pack();
        frame.setVisible(true);
    }

    /*======== public void mouseDragged() ==========

      mouseDragged is triggered when the left mouse button
      is being held down and the mouse is moving.
      
      When the mouse is being dragged, the temporary line in 
      canvas should be updated to draw the line from the (x, y)
      position when the mouse was initially clicked (stored in 
      xes and ys) and the current (x,y) position

      You should use the setDrawing() method in canvas
      Make sure that you only draw one temporary line at
      a time.
      ====================*/
    public void mouseDragged(MouseEvent e) {
        int x,y;
        x = e.getX();
        y = e.getY();

        canvas.setDrawing(xes[0], ys[0],x,y);
        canvas.paintComponent(canvas.getGraphics());
        canvas.clearTmp();
    }

    /*======== public void mousePressed() ==========
      
      mousePressed is triggered when the left mouse button 
      is initially pressed down. 

      The current x and y coordiantes of the mouse should
      be stored in the first index of xes and ys, respectively.
      
      No drawing occurs when the mouse is initially pressed.

      e.getX() and e.getY() will return the current x and
      y coordinates.
      ====================*/
    public void mousePressed(MouseEvent e) {
        int x,y;
        x = e.getX();
        y = e.getY();
        xes[clickcount] = x;
        ys[clickcount] = y;
    }

    /*======== public void mouseReleased() ==========

      mouseReleased is triggered when the left mouse button
      is released. This should signal the end of the temporary
      line drawing and add the line to the canvas' permanant
      edge matrix.

      You should use addLine and stopDrawing
      ====================*/
    public void mouseReleased(MouseEvent e) {
        int x,y;
        x = e.getX();
        y = e.getY();

        canvas.addLine(xes[0], ys[0], 0, x, y, 0);
        canvas.stopDrawing();
    }

    //needed to implement MouseListener and MouseMotionListener
    public void mouseMoved(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
    public void mouseClicked(MouseEvent e) {}


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
        if (e.getSource()==quit) {
            System.exit(0);
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
        } else if (e.getSource() == apply) {
            double x = Double.parseDouble(xarg.getText());
            double y = Double.parseDouble(yarg.getText());
            double z = Double.parseDouble(zarg.getText());
            if(transformation.getSelectedItem().equals("translate")) {
                canvas.translate(x,y,z);
            } else if(transformation.getSelectedItem().equals("scale")) {
                canvas.scale(x,y,z);
            } else if(transformation.getSelectedItem().equals("x rotation")) {
                canvas.rotX(x);
            } else if (transformation.getSelectedItem().equals("y rotation")) {
                canvas.rotY(y);
            } else if (transformation.getSelectedItem().equals("z rotation")) {
                canvas.rotZ(z);
            }

        }

    }

    public static void main(String[] args) {

        gui g = new gui();

    }
}

