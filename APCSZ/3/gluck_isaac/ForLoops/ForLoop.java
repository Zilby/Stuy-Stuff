import java.util.*;
import java.io.*;

public class ForLoop {

    public boolean isPrime(int n) {
	int test = n-1;
	for (test = n-1;test > 1;test--) {
	    if (n%test==0)
		return false;
	}
	return true;
    }

    public String reverse(String s) {
	int length = s.length();
	String result = "";
	for(int i = length -1; i>=0; i--)
	    result = result + s.substring(i, i+1);
	return result;
    }

    /*public String table(int n, int m) {
	String r = "";
	for(int i=1; i<=n; i++) {
	    r = r+i+" ";
	}

	r = r+"\n";

	for (int k=1; k<=m; k++) {
	    r = r + k + " ";

	    for (int j=1;j<=n;j=j++) {
		r = r +(j*k)+" ";
	    }
	    r = r+"\n";
	}
	return r;
    }*/


    public String table(int n, int m) {
        String r="  ";
        
        //first row
        for (int j=1; j<=n; j++) {
            r=r+j+" ";
        }   
        r=r+"\n";
        
        //all the other rows
        for (int i=1; i<=m; i++) {
            r=r+i+" ";
            for (int j=1; j<=n; j++) {
                r=r+(i*j)+" ";
            }
            r=r+"\n";
        }

        return r;
    }
}
