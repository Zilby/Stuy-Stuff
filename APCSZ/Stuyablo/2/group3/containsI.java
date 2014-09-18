import java.io.*;
import java.util.*;

public class containsI {
    public boolean containsInt ( int[] a , int i ) {
	for ( int j = 0 ; j < a.length ; j++ ) {
	    if ( a [ j ] == i )
		return true;
	}
	return false;
    }

    public int findInt ( int[] a , int i ) {
	for ( int j = 0 ; j < a.length ; j++ ) {
	    if ( a [ j ] == i )
		return j;
	}
	return -1;
    }

    public int count ( int[] a , int i ) {
	int sum = 0;
	for ( int j = 0 ; j < a.length ; j++ ) {
	    if ( a [ j ] == i )
		sum = sum + 1;
	}
	return sum;
    }

    public int nextOccur ( int[] a , int i , int k ) {
	int index = findInt ( a , i ), sum = 0;
	int[] newArray = new int [ a.length - index - 1];
	while ( k > 0 ) {
	    int count = 0;
	    for ( int j = index + 1 ; j < a.length ; j++ ) {
		newArray [ count ] = a [ j ];
		count += 1;
	    }
	    sum = sum + a.length - index;
	    a = newArray;
	    k = k - 1;
	}
	// System.out.println ( Arrays.toString ( a ) );
	return findInt ( newArray , i ) + index + 1;
    }

    public String mapRow ( int[] x , int[] y , int i , int gridRange ) {
	int[] xcoors = new int [ count ( y , i ) ];
	String ans = new String();
	int c = 0;
	for ( int j = 0 ; j < y.length ; j++ ) {
	    if ( y [ j ] == i ) {
		xcoors [ c ] = x [ j ];
		c = c + 1;
	    }		    
	}
	//return Arrays.toString ( xcoors );
	for ( int j = -1 * gridRange ; j <= gridRange  ; j++ ) {
	    if ( containsInt ( xcoors , j ) )
		ans = ans + "E";
	    else ans = ans + "-";
	}
	return ans + "\n";
    }
}
