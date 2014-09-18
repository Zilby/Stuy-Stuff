import java.io.*;
import java.util.*;

public class diagonal {

    //diag - turn a number into a diagonal line

    public String diag(int n) {
	int i;
	//could also say i = 0 here, but not necessary as defied below
	String result = "";
	int spaces;
	
	for (i = 0; i != n; i++) { //can also say i = i + 1; i+=i;
	    //do this stuff, as long as i doesn't equal n.
	    // " " * i DOESNT WORK - you cant multiply Strings in Java
	    for (spaces = 0; spaces < i; spaces++) {
		result = result + " "; //adds appropriate number of spaces
		    }
	    result = result + "*"; //add the star at the end of the spaces
	    result += "\n";
	    }
	    return result;
	}

	
    public String diagWord(String w) {
		int i;
		String result = "";
		int space;
		int l = w.length();
		for (i = 0; i != l; i++) {
	 	   for (space = 0; space < i; space++) {
		 	   result = result + " ";
		 	   }
	    result = result + w.substring(i, i + 1) + "\n";
	    }
	return result;
    }   
    
}
