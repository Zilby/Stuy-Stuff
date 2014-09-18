import java.io.*;
import java.util.*;

public class Luke {
    
    public int[] revFill (int n) {
	//will return an array of 
	//size n w/ the values
	// n, n-1, ... 1 
	int[] arr = new int[n];
	int x = 0;
	for (int  i = n ; i > 0 ; i--) {
	    arr[x] = i;
	    x++;
 
	}
        return arr;
    }

    public makeRandom (int n, int min, int max) {
	//return array of random ints between min and max
	// array length is random number s
    }

}