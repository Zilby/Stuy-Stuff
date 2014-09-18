import java.io.*;
import java.util.*;

public class Arrays {
    public int[] Revfill(int n){
	int[] result = new int[n];
	for (int i = 0; i < n; i++)
	    result[i] = n-i;
	return result;
    }

    public int[] makeRandom(int n, int min, int max) {
	int[] result = new int[n];
	Random r = new Random();

	for (int i = 0; i < n; i++) {
	    result[i] = r.nextInt(max-min) + min;
	}
	return result;
    }

    public int sum13(int[] a) {
	int result = 0;
	for (int i = 0; i < a.length; i++) {
	    if (a[i] != 13)
		result += a[i];
	}
	return result;
    }

    public boolean modThree(int[] a) {
	
    }
}