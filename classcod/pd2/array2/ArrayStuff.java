import java.io.*;
import java.util.*;

public class ArrayStuff {
    private int[] a;
    private Random r;

    public ArrayStuff() {
	r = new Random();
	a = new int[20];
	for (int i=0;i<a.length;i++) 
	    a[i]=r.nextInt(100);
    }
    public ArrayStuff(int s) {
	r = new Random();
	a = new int[s];
	for (int i=0;i<a.length;i++) 
	    a[i]=r.nextInt(100);
    }
    public ArrayStuff(int s, int max) {
	r = new Random();
	a = new int[s];
	for (int i=0;i<a.length;i++) 
	    a[i]=r.nextInt(max);
    }

    public String toString() {
	return Arrays.toString(a);
    }

    public int get(int n) {
	return a[n];
    }

    public int findMaxIndex() {
	int maxi = 0;
	for (int i =0 ; i < a.length;i++) {
	    if (a[i]>a[maxi]) 
		maxi = i;
	}
	return maxi;
    }

    public int find(int n) {
	for (int i=0;i<a.length;i++) {
	    if (a[i]==n)
		return i;
	}
	return -1;
    }

    public int freq(int n) {
	int count=0;
	for (int i=0;i<a.length;i++) {
	    if (a[i]==n)
		count++;
	}
	return count;
    }

    public void mode2() {
	int maxval = a[ findMaxIndex() ];
	int[] buckets = new int[maxval+1];

	for (int i=0;i<a.length;i++) {
	    buckets[ a[i] ] = buckets[ a[i] ] + 1;
	}
	
	int mode = 0;
	for (int i=0;i<buckets.length;i++) {
	    if (buckets[i] > mode) {
		mode = buckets[i];
	    }
	}
	
	System.out.println("Mode: "+mode);
	System.out.print("Mode values: ");
	for (int i=0;i<buckets.length;i++) {
	    if (buckets[i]==mode) {
		System.out.print(i+", ");
	    }
	}
	System.out.println();
    }

    public void mode() {
	int maxFreq=0;
	int maxIndex=0;
	for (int i=0;i<a.length;i++){
	    int f = freq(a[i]);
	    if ( f>maxFreq){
		maxFreq= f;
		maxIndex=i;
	    }
	}
	System.out.println("Mode: "+a[maxIndex]+" Count: "+maxFreq);
    }
    
}
