import java.io.*;
import java.util.*;
import javax.swing.JFrame; //imports tools to make arrange window

public class Learning extends JFrame {
    public Learning() {
	add(new Board()); //creates the board
        setTitle("Learning"); 
        setDefaultCloseOperation(EXIT_ON_CLOSE); //allows app to close when x'd out
        setSize(300, 280); //sets size of window
        setLocationRelativeTo(null); //centers the window
        setVisible(true); //shows window on screen
        setResizable(false); //prevents window from being resized
    }
    
    public static void main(String[] args) {
        new Learning();
    }

    //So far just creates the board
}