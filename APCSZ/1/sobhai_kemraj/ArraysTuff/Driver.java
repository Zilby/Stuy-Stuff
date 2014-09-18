import java.io.*;
import java.util.*;

public class Driver{

	public static void main (String[] args){
		ArraysTuff A = new ArraysTuff();
		int[] B = A.Revfill(6);
		int[] C = A.makeRandom(5,3,9);
		for (int i=0;i<B.length;i+=1)
			System.out.println(B[i]);
		for (int i=0;i<C.length;i+=1)
			System.out.println(C[i]);
			
	}

}
