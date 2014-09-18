import java.io.*;
import java.util.*;

public class Arrays {

/*Given an array of ints, return true if 6 appears as either
the first or last element in the array.
The array will be length 1 or more. */
public boolean firstLast6(int[] nums) {
  if (nums[0]==6 || nums[nums.length-1]==6)
    return true;
   return false;
}

/*Given 2 arrays of ints, a and b, return true if they have
the same first element or they have the same last element.
Both arrays will be length 1 or more. */
public boolean commonEnd(int[] a, int[] b) {
  if (a[0]==b[0] || a[a.length-1]==b[b.length-1])
    return true;
  return false;
}


/*Given an array of ints length 3, return a new array with
the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.*/
public int[] reverse3(int[] nums) {
  int[] reverse = new int[3];
  for (int i=0; i<3; i++)
    reverse[i] = nums[2-i];
  return reverse;
}

/*Given 2 int arrays, a and b, each length 3, return a new
array length 2 containing their middle elements. */
public int[] middleWay(int[] a, int[] b) {
  int[] middle = new int[2];
  middle[0] = a[1];
  middle[1] = b[1];
  return middle;
}

/*Given an int array length 2, return true if it does not contain a 2 or 3.*/
public boolean no23(int[] nums) {
  for (int i=0;i<2;i++){
    if (nums[i]==2 || nums[i]==3)
      return false;
  }
  return true;
}

/* Given an array of ints, return a new array length 2 containing
the first and last elements from the orginal array. The original
array will be length 1 or more */
public int[] makeEnds(int[] nums) {
	int[] endPoints = new int[2];
	endPoints[0] = nums[0];
	endPoints[1] = nums[nums.length - 1];
	return endPoints;
}



}