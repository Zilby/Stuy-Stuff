import java.io.*;
import java.util.*;

public class Diagonal {
    public String diag(int n){
	String rs = "";
	for(int i = 0; i < n ; i ++) {
	    for(int j = 0; j <= i ; j++) {
		rs = rs + " ";
	    }
	    rs = rs + "* \n";
	}
	return rs;

    }



    public String diagword(String s) {
	String rs = "";
	int n = s.length();
	for(int i = 0; i < n ; i ++) {
	    for(int j = 0; j <= i ; j++) {
		rs = rs + " ";
	    }
	    rs = rs + s.substring(i, i+1) + " \n";
	}
	return rs;
    }



    public String fence(int n, int m) {
	String fence = "";
	if (n<2 || m<2) 
	    return "Cannot enclose";
	else {

	for(int i = 1; i <=n; i++){
	    for (int j = 1; j <= m; j++) {
		if (i == 1 || i == n){
		    if (j == 1||j==m) 
			fence = fence + "+";
		    else 
			fence = fence + "-";
		} else {
		    if (j==1||j==m)
			fence = fence + "|";
		    else fence = fence + " ";
		}
	    }
	    fence = fence + "\n";
	    
	}

	return fence;
	}
    }


    public static void main(String[] args) {
	Diagonal d = new Diagonal();
	System.out.println(d.diag(1));
	System.out.println(d.diag(5));
	System.out.println(d.diagword("Mim, Lichael Mim."));
	System.out.println(d.fence(1,2));
	System.out.println(d.fence(2,2));
	System.out.println(d.fence(7,5));
    }




}