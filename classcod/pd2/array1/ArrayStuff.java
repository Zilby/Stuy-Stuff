import java.io.*;
import java.util.*;

public class ArrayStuff {

    public void demo1() {
	// We declare an array by adding [] to the type
	// so, intArray can refer to an arary if ints and stringArray to an
	// array of Strings
	int[] intArray;
	String[] stringArray;

	// an Arary is a contiguous block of data big enough to hold multiple
	// values of a single type. We'll say that arrays are pseudo-classes.
	// they mostly work like classes but there are a couple of differences
	
	// make a block big enough to hold 5 ints
	intArray = new int[5];

	// make a block big enough to hold 3 Strings
	stringArray = new String[3];

	// we access array elements using the [] notation (kindof like python lists
	// but less powerful. Indexing starts at 0.
	System.out.println(intArray[2]);
	System.out.println(stringArray[1]);
	intArray[1]=20;
	intArray[2]=intArray[1]+50;
        stringArray[1]="Hello World";
	System.out.println(intArray[2]);
	System.out.println(stringArray[1]);

	// all arrays have a public constant int variable named length
	// which has the number of cells in the array. It's constant so you
	// can't change it.
	for (int i=0;i<intArray.length;i++) {
	    System.out.print(intArray[i]+", ");
	}
	System.out.println();

	for (int i=0;i<stringArray.length;i++) {
	    System.out.print(stringArray[i]+", ");
	}
	System.out.println();

	// Once you instantiate an array, you can't change its size (make it 
	// bigger or smaller
	
	String[] tmpArray = new String[stringArray.length+5];
	for (int i=0;i<stringArray.length;i=i+1) {
	    tmpArray[i]=stringArray[i];
	}
	stringArray = tmpArray;

	for (int i=0;i<stringArray.length;i++) {
	    System.out.print(stringArray[i]+", ");
	}
	System.out.println();


    }

}
