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

    public void mode() {
	int maxFreq=0;
	int maxNum=0;
	boolean flag = true;
	for(int i = 0; i < a.length; i++)
	{
		if(a[i] == 0) 
  			maxFreq++;
	}
	int i = 0;

	int currentCheck = 0;
	int currentFreq = 0;
	for(; i < a.length; i++)
	{
		if(a[i] != 0)
		{
			currentCheck = a[i];
			for(int j = i; j < a.length; j++)
			{
				if(a[j] == currentCheck)
				{
					a[j] = 0;
					currentFreq += 1;
				}
			}
			if(currentFreq > maxFreq)
			{
				maxFreq = currentFreq;
				maxNum = currentCheck;
			}
		}
	}
	System.out.println("Mode: "+ maxNum +" Count: "+maxFreq);
    }
    
}
