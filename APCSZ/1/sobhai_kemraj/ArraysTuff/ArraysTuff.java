import java.io.*;
import java.util.*;

public class ArraysTuff {

	public int[] Revfill(int n){
		int[] ans = new int[n];
		for (int i=n;i>0;i--){
			ans[n-i]=i;
		}
		return ans;
	}

	public int[] makeRandom(int size, int min, int max){
		int[] ans = new int[size];
		for (int i=0; i<size;i++){
			ans[i]=min+(int)(Math.random()*(max-min));
		}		
		return ans;
		
	}
	
	public int sum13(int[] nums) {
		int ans = 0;
		for (int i=0;i<nums.length;i++){
			if (nums[i] == 13)
				i++;
    		else
      			ans += nums[i];
  		}
  		return ans;
	}

	public boolean modThree(int[] nums) {
  		int odds=0;
  		int evens=0;
  		for (int i=0;i<nums.length;i++){
    			if ((nums[i] % 2)==1){
      				odds++;
      				evens=0;
    			}
    			else{
      				evens++;
      				odds=0;
    			}
    			if ((odds==3)||(evens==3))
      				return true;
  		}
  		return false;
	}

}
