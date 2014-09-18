import java.io.*;
import java.util.*;

public class HW8pt2{
    private String word, firstLetter;
   
    public String latinify(String word){
	firstLetter = word.substring(0,1);
	String word1;
	word1 = new String();
	if (firstLetter.equals("a") || firstLetter.equals("e") ||firstLetter.equals("i") ||firstLetter.equals("o") || firstLetter.equals( "u")){
	    word1 = word + "yay";
	}
	else { 
	    word1 =  word.substring(1) + firstLetter + "ay";
	}
	return   word1
	    } 
     
}