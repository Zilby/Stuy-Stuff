import java.util.*;
import java.io.*;

public class ArrayStuff {

    public void demo1() {
	int[] intArray;
	String[] stringArray;

	// make and initialize an array of 4 ints
	int[] initIntArray={10,20,30,40};
	// make and initialize an array of 5 Strings
	String[] initStringArray={"one","two","three","four","five"};

	// make a contiguous block of memory large enough to hold 5 ints and
	//  return the address of the start of the block
	intArray = new int[5]; // make a block big enough to hold 5 ints

	// the same, but the block is big enough to hold 3 strings 
	stringArray = new String[3]; // make a block big enough to hold 3 Strings


	// We access individual elements with the []. Subscripts start with 0
	System.out.println(intArray[2]);
	System.out.println(stringArray[2]);
	intArray[1]=5;
	intArray[2]=intArray[1]+40;
	stringArray[1]="Hello World";

	// you get a built in public constant variable in the array pseudo-class
	// called length wich tells you the arrays size
	// it's constant so you can't set its value
	System.out.println(intArray.length);
	System.out.println(stringArray.length);

	for (int i =0; i<intArray.length;i++) {
	    System.out.print(intArray[i]+", ");
	}
	System.out.println();

	for (int i =0; i<stringArray.length;i++) {
	    System.out.print(stringArray[i]+", ");
	}
	System.out.println();

	// Once an Array is instantiated, you can't change its size (to make it either
	// larger or smaller.

	String[] tmpArray = new String[5];
	for (int i=0; i< stringArray.length;i++) {
	    tmpArray[i]=stringArray[i];
	}
	stringArray=tmpArray;

	for (int i =0; i<initStringArray.length;i++) {
	    System.out.print(initStringArray[i]+", ");
	}
	System.out.println();
	initStringArray[2]="changed the array";
	for (int i =0; i<initStringArray.length;i++) {
	    System.out.print(initStringArray[i]+", ");
	}
	System.out.println();

	
	// System.out.println(intArray);
	// System.out.println(stringArray);
    }


}
