import java.io.*;
import java.util.*;
import java.lang.Math.*;

public class test {
    public static void main(String[] args) {
	
	Parser p = new Parser();
	
       	try {
	    
	//InputStreamReader in = new InputStreamReader(System.in);
	   	 FileReader in = new FileReader("script_java_3");
	  	  BufferedReader bin = new BufferedReader( in );
	 	   p.parseFile(bin);
		} catch (IOException e) {
			System.out.println("File script_java_3 not found");
		}
    }
}
