import java.io.*;
import java.util.*;


public class Driver {
    public static void main (String[] args) {
	diagonal d = new diagonal(); //Denotes to look at diagonal.java
	System.out.println(d.diag(14));
	System.out.println(d.diagWord("Supercalifragilisticexpalidocious"));
    }
}
			