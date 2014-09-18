import java.io.*;
import java.util.*;

public class Loops2{
    public String diag(int n){
	String result = "";
	for (int i = 0; i < n; i = i + 1){
	    for (int j= i; j > 0; j = j -1){
		result = result + " ";
	    }
	    result = result + "*" + "\n";   

	}
	return result;
    }
    public String diagWord(String s){
	String result = "";
	for (int i = 0; i < s.length(); i = i + 1){
	    for (int j= i; j > 0; j = j -1){
		result = result + " ";
	    }
	    result = result + s.substring(i,i+1) + "\n";   

	}
	return result;
    }
}