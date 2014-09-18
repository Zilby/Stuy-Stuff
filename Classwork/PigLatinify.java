import java.io.*;
import java.util.*;

public class PigLatinify{
    public String makePiggy(String name){
	firstletter = name.substring(0,1);
	if (firstletter.equals("a") ||
	    firstletter.equals("e") ||
	    firstletter.equals("o") ||
	    firstletter.equals("i") ||
	    firstletter.equals("u") ||
	    firstletter.equals("y")) {

			   
	return name.substring(0,1).toUpperCase() 
	    + name.substring(1,name.indexOf(" ")) + " " 
	    + name.substring((name.indexOf(" ")+1),(name.indexOf(" ")+2)).toUpperCase() 
	    + name.substring((name.indexOf(" ")+2));
    }
