import java.io.*;
import java.util.*;

public class Arrays {

/*Return the number of even ints in the given array.*/
public int countEvens(int[] nums) {
  int evens=0;
  for (int i=0; i<nums.length; i++){
    if (nums[i]%2==0)
      evens = evens + 1;
  }
  return evens;
}

/*Given a number n, create and return a new int array of
length n, containing the numbers 0, 1, 2, ... n-1.*/
public int[] fizzArray(int n) {
  int[] fizz = new int[n];
  for(int i=0; i<n; i++)
    fizz[i] = i;
  return fizz;
}

/*Given a number n, create and return a new string array of
length n, containing the strings "0", "1" "2" .. through n-1. */
public String[] fizzArray2(int n) {
  String[] fizz2 = new String[n];
  for(int i=0; i<n; i++)
    fizz2[i] = ("" + i + "");
  return fizz2;
}

/*Given start and end numbers, return a new array containing the sequence
of integers from start up to but not including end, so start=5 and end=10
yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the start number*/
public int[] fizzArray3(int start, int end) {
  int[] fizz3 = new int[end-start];
  for (int i=0; i<fizz3.length; i++)
    fizz3[i] = start + i;
  return fizz3;
}

/*This is slightly more difficult version of the famous FizzBuzz problem which is
sometimes given as a first problem for job interviews. Consider the series of numbers
beginning at start and running up to but not including end, so for example start=1
and end=5 gives the series 1, 2, 3, 4. Return a new String[] array containing the string
form of these numbers, except for multiples of 3, use "Fizz" instead of the number, for
multiples of 5 use "Buzz", and for multiples of both 3 and 5 use "FizzBuzz". */
public String[] fizzBuzz(int start, int end) {
  String[] fizzBuzz = new String[end-start];
  for (int i=0; i<fizzBuzz.length; i++){
    if ((start+i)%3==0 && (start+i)%5==0)
      fizzBuzz[i] = ("FizzBuzz");
    else if ((start+i)%3==0)
      fizzBuzz[i] = ("Fizz");
    else if ((start+i)%5==0)
      fizzBuzz[i] = ("Buzz");
    else
      fizzBuzz[i] = String.valueOf(start+i);
  }
  return fizzBuzz;
}

/*We'll say that a value is "everywhere" in an array if for every pair of adjacent
elements in the array, at least one of the pair is that value. Return true
if the given value is everywhere in the array. */
public boolean isEverywhere(int[] nums, int val) {
  for(int i=0; i<nums.length-1; i++){
    if (nums[i]!=val && nums[i+1]!=val)
      return false;
  }
  return true;
}

/*Return an array that is "left shifted" by one -- so {6, 2, 5, 3} returns {2, 5, 3, 6}.
You may modify and return the given array, or return a new array. */
public int[] shiftLeft(int[] nums) {
  int[] shifted = new int[nums.length];
  if (nums.length>0){
    shifted[shifted.length-1] = nums[0];
    for (int i=0; i<shifted.length-1; i++)
      shifted[i] = nums[i+1];
  }
  return shifted;
}

/*Return true if the array contains, somewhere, three increasing adjacent numbers
like .... 4, 5, 6, ... or 23, 24, 25.*/
public boolean tripleUp(int[] nums) {
  for(int i=1; i<nums.length-1; i++){
    if (nums[i-1] == nums[i]-1 && nums[i]+1 == nums[i+1])
      return true;
  }
  return false;
}

/*Given arrays nums1 and nums2 of the same length, for every element in nums1,
consider the corresponding element in nums2 (at the same index). Return the count of the
number of times that the two elements differ by 2 or less, but are not equal. */
public int matchUp(int[] nums1, int[] nums2) {
  int match=0;
  for(int i=0; i<nums1.length; i++){
    if(nums1[i]!=nums2[i]){
      if(nums1[i]>nums2[i] && nums1[i]-nums2[i]<=2)
        match = match + 1;
      if (nums2[i]>nums1[i] && nums2[i]-nums1[i]<=2)
        match = match + 1;
      }
   }
   return match;
}

/*Given an array of ints, return true if there is a 1 in the array
with a 2 somewhere later in the array.*/
public boolean has12(int[] nums) {
  for(int i=0; i<nums.length; i++){
    if (nums[i] == 1){
      for(int j=i+1; j<nums.length; j++){
         if (nums[j] == 2)
           return true;
      }
    }
  }
  return false;
}

/*Given a non-empty array of ints, return a new array containing the
elements from the original array that come after the last 4 in the
original array. The original array will contain at least one 4.
Note that it is valid in java to create an array of length 0. */
public int[] post4(int[] nums) {
  int index=0;
  for(int i=0; i<nums.length; i++){
    if(nums[i]==4){
      if(i>index)
        index=i;
    }
  }
  int[] post = new int[nums.length-1-index];
  for(int j=0; j<post.length; j++){
    post[j]=nums[index+1];
    index = index + 1;
  }
  return post;
}

/*Given an array of ints, return true if the sum of all the 2's in the array is exactly 8.*/
public boolean sum28(int[] nums) {
  int sum = 0;
  for(int i=0; i<nums.length; i++){
    if (nums[i]==2)
      sum = sum + 2;
  }
  if (sum == 8)
    return true;
  return false;
}


/*Return an array that contains the exact same numbers as the given array, but rearranged so
that all the zeros are grouped at the start of the array. The order of the non-zero numbers
does not matter. So {1, 0, 0, 1} becomes {0 ,0, 1, 1}. You may modify and return the given
array or make a new array.*/
public int[] zeroFront(int[] nums) {
  int[] front = new int[nums.length];
  int counter=0;
  for (int i=0; i<nums.length; i++){
    if (nums[i]==0){
      front[counter]=0;
      nums[i] = nums[counter];
      counter = counter + 1;
    }
  }
  for(int j= counter; j<nums.length; j++)
    front[j] = nums[j];
  return front;
}

/*Return the "centered" average of an array of ints, which we'll say is the mean average
of the values, except ignoring the largest and smallest values in the array. If there are
multiple copies of the smallest value, ignore just one copy, and likewise for the largest
value. You may assume that the array is length 3 or more. */
public int centeredAverage(int[] nums) {
  int maximum = nums[0];
  int minimum = nums[0];
  int sum = 0;
  int average;
  for (int i=0; i<nums.length; i++){
    if(nums[i] > maximum)
      maximum = nums[i];
    if(nums[i] < minimum)
      minimum = nums[i];
    sum = sum + nums[i];
  }
  sum = sum - (maximum + minimum);
  average = sum / (nums.length - 2);
  return average;
}

/*Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers
that come immediately after a 13 also do not count. */
public int sum13(int[] nums) {
  	int sum = 0;
 	for (int i= 0; i<nums.length; i++){
  		if (nums[i] == 13)
    	   i++;
    	 else
    	   sum = sum + nums[i];
  	}
  	return sum;
}

/*Given an array of ints, return true if the array contains
either 3 evenor 3 odd values all next to each other. */
public boolean modThree(int[] nums){
	 for (int i=0; i<=nums.length-3; i++){
	     if(nums[i]%2 == nums[i+1]%2 && nums[i+1]%2 == nums[i+2]%2)
	         return true;
	      }
	 return false;
}

/* Given an array of ints, return true if every element is a 1 or 4 */
public boolean only14(int[] nums) {
   int i= 0;
   while (i<nums.length){
     if (nums[i]==1 || nums[i]==4)
       i++;
     else
       return false;}
    return true;
 }

}
