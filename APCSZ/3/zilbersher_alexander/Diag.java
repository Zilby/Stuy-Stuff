import java.io.*;
import java.util.*;

public class Diag {

    public String diag(int i) {
	String output = "";
	String increment = "";
	for (;i>0;i--) {
	    output = output + "\n" + "*" + increment;
	    increment = increment + " ";
	}
	return output;
    }
    /*
    public String diagWord(String s) {
    }

    public String fence(int i, int j) {
    }

}
    */