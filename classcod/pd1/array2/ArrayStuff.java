import java.util.*;
import java.io.*;

public class ArrayStuff{
    private int[] a;
    private Random r = new Random();
    public ArrayStuff() {
	a=new int[20];
	 	for (int i=0;i<a.length;i++) {
     	    a[i]=r.nextInt(100);
     	}
     }
    
     public ArrayStuff(int s) {
     	a=new int[s];
     	for (int i=0;i<a.length;i++) {
     	    a[i]=r.nextInt(100);
     	}
     }
    public ArrayStuff(int s,int max) {
	a=new int[s];
	for (int i=0;i<a.length;i++) {
	    a[i]=r.nextInt(max);
	}
    }
    public String toString() {
	return Arrays.toString(a);
    }

    // return the index of the max element
    public int findMaxIndex() {
	if (a==null || a.length==0) 
	    return -1;

       	int maxi = 0;
	for (int i=0;i<a.length;i++) {
	    if (a[i] > a[maxi])
		maxi = i;
	}
	return maxi;
    }

    public int get(int n) {
	if (n>=0 && n < a.length) 
	    return a[n];
	else
	    return -1;
    }
    public int find(int n) {
	for (int i=0;i<a.length;i++) {
	    if (a[i]==n)
		return i;
	}
	return -1;
    }

    public int freq(int n) {
	int appearances = 0;
	for (int i=0;i<a.length;i++){
	    if (a[i]==n)
		appearances = appearances + 1;
	}
	return appearances;
    }


    public void mode2() {
	int maxval = a[findMaxIndex()];
	int[] buckets = new int[maxval+1];
	for (int i=0;i<a.length;i++) {
	    buckets[a[i]] = buckets[a[i]]+1;
	}

	int max=buckets[0];
	for (int i=0;i<buckets.length;i++) {
	    if (buckets[i]>max) {
		max = buckets[i];
	    }
	}

	System.out.print("Modes: ");
	for (int i=0;i<buckets.length;i++) {
	    if (buckets[i]==max) {
		System.out.print(i+",");
	    }
	}
	System.out.println();
    }



    public void mode() {
	int maxIndex = 0;
	int maxFreq=freq(a[0]);
	for (int i=0;i<a.length;i++){
	    int f = freq(a[i]);
	    if (f>maxFreq) {
		maxFreq=f;
		maxIndex = i;
	    }
	}
	System.out.println("Mode: "+a[maxIndex]+" Count: "+maxFreq);
    }
	
}


