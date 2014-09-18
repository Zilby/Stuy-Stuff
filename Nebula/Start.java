//Used for the intro

import java.awt.event.KeyEvent;
import java.util.*;

public class Start {

    private boolean go = false; //Used to tell the game if space was pressed
    private boolean skip1 = false;
    private boolean skip2 = false;
    private boolean skip3 = false;
    private boolean skip4 = false;
    private boolean skip5 = false;
    private boolean skip6 = false;
    private boolean skip7 = false;
    private boolean skip8 = false;
    private boolean skip9 = false;
    private boolean skip10 = false;
    private boolean restart = false;

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode(); //gets key code for any key pressed
	if (key == KeyEvent.VK_SPACE) { //if that key is space
            go = true; //go is activated
        }
	if (key == KeyEvent.VK_0) { //if that key is space
            skip10 = true; //skip is activated
        }
	if (key == KeyEvent.VK_1) { //if that key is space
            skip1 = true; //skip is activated
        }
	if (key == KeyEvent.VK_2) { //if that key is space
            skip2 = true; //skip is activated
        }
	if (key == KeyEvent.VK_3) { //if that key is space
            skip3 = true; //skip is activated
        }
	if (key == KeyEvent.VK_4) { //if that key is space
            skip4 = true; //skip is activated
        }
	if (key == KeyEvent.VK_5) { //if that key is space
            skip5 = true; //skip is activated
        }
	if (key == KeyEvent.VK_6) { //if that key is space
            skip6 = true; //skip is activated
        }
	if (key == KeyEvent.VK_7) { //if that key is space
            skip7 = true; //skip is activated
        }
	if (key == KeyEvent.VK_8) { //if that key is space
            skip8 = true; //skip is activated
        }
	if (key == KeyEvent.VK_9) { //if that key is space
            skip9 = true; //skip is activated
        }
	if (key == KeyEvent.VK_Z) { //if that key is space
            restart = true; //skip is activated
        }
    }
    
    public boolean getGo() {
	return go;
    }

    public void resetGo() {
	go = false;
    }

    public boolean getSkip10() {
	return skip10;
    }

    public boolean getSkip1() {
	return skip1;
    }

    public boolean getSkip2() {
	return skip2;
    }

    public boolean getSkip3() {
	return skip3;
    }

    public boolean getSkip4() {
	return skip4;
    }

    public boolean getSkip5() {
	return skip5;
    }

    public boolean getSkip6() {
	return skip6;
    }

    public boolean getSkip7() {
	return skip7;
    }

    public boolean getSkip8() {
	return skip8;
    }

    public boolean getSkip9() {
	return skip9;
    }


    public void resetSkip() {
	skip10 = false;
	skip1 = false;
	skip2 = false;
	skip3 = false;
	skip4 = false;
	skip5 = false;
	skip6 = false;
	skip7 = false;
	skip8 = false;
	skip9 = false;
    }

    public boolean getRestart() {
	return restart;
    }

    public void resetRestart() {
	restart = false;
    }
}