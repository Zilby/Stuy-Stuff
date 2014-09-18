import java.io.*;
import java.util.*;

public class Buckets {
    private ArrayList[] buckets = new ArrayList[10];
    private int[] 4D = new int[10];
    private Random r = new Random();
    private int n = 0;

    private void makeBuckets() {
	for (int i=0;i<10;i++) {
	    buckets[i] = new ArrayList();
	}
    }
    
    public void fill(int max, int min) {
	for (int i=0;i<10;i++) {
	    4D[i] = min + (r.nextInt(max-min+1));
	}
    }

    
}