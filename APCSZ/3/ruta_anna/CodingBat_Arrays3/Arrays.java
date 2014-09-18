import java.io.*;
import java.util.*;

public class Arrays {

/*Consider the leftmost and righmost appearances of some
value in an array. We'll say that the "span" is the number
of elements between the two inclusive. A single value has a
span of 1. Returns the largest span found in the given array.
(Efficiency is not a priority.)*/
public int maxSpan(int[] nums) {
  int largest = 0;
  int span;
  for(int i = 0; i < nums.length; i++) {
      span = 0;
      for(int j = i; j < nums.length; j++) {
         span++;
         if(nums[i] == nums[j]) {
            if(span > largest) {
               largest = span;
            }
         }
      }
   }
  return largest;
}

/*Given n>=0, create an array with the pattern
{1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n}
(spaces added to show the grouping). Note that the length
of the array will be 1 + 2 + 3 ... + n, which is known to
sum to exactly n*(n + 1)/2. */
public int[] seriesUp(int n) {
  int[] series = new int[n*(n + 1)/2];
  int index = 0;
  for (int i=0; i<n; i++){
    for(int j=1; j<=i+1; j++){
      series[index] = j;
      index = index + 1;
    }
  }
  return series;
}


/*Given a non-empty array, return true if there is a place to split
the array so that the sum of the numbers on one side is equal to
the sum of the numbers on the other side.*/
public boolean canBalance(int[] nums) {
   int sum = 0;
   int half;
   for(int i = 0; i < nums.length; i++) {
      sum = sum + nums[i];
   }
   if (sum % 2 == 0 ) {
      half = sum / 2;
      sum = 0;
      for(int j = 0; j < nums.length; j++) {
         sum = sum + nums[j];
         if (sum == half)
           return true;
      }
   }
  return false;
}

/*Return an array that contains exactly the same numbers as the given array,
but rearranged so that every 4 is immediately followed by a 5. Do not move
the 4's, but every other number may move. The array contains the same number
of 4's and 5's, and every 4 has a number after it that is not a 4.
In this version, 5's may appear anywhere in the original array. */
public int[] fix45(int[] nums) {
  int[] anArray = new int[nums.length];
  for(int i = 0; i < nums.length-1; i++) {
      if (nums[i] == 4) {
         anArray[i] = 4;
          if (nums[i+1] == 5) {
            anArray[i+1] = 5;
            nums[i+1] = 0;
         }
      }
   }
    for(int i = 0; i < nums.length-1; i++) {
      if (anArray[i] == 4 && anArray[i+1] != 5) {
         for(int j = 0; j < nums.length; j++) {
            if (nums[j] == 5) {
               anArray[i+1] = 5;
               nums[j] = nums[i+1];
               j =  nums.length;
            }
         }
      }
   }
  for(int i = 0; i < nums.length; i++) {
      if (anArray[i] != 4 && anArray[i] != 5) {
         anArray[i] = nums[i];
      }
   }
  return anArray;
}


}
