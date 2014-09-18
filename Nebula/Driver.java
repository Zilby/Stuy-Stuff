//basically just the Driver class

import java.io.*;     // Basic
import java.util.*;   // Imports
import javax.swing.JFrame; //Used for all the JFrame components such as the board itself

public class Driver extends JFrame { //extended so that it contains all that is in JFrame

    public Driver() {
        add(new Board()); //Creates Board itself
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Allows the Board window to be closed
        setSize(600, 600); //sets Board size
        setLocationRelativeTo(null);
        setTitle("Nebula Wars");
        setResizable(false); //prevents window from being resized screwing everything up
        setVisible(true); //sets default visible to true
    }

    public static void main(String[] args) {
        new Driver();
    }
}
