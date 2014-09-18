public class Arrays2{

    public int[] Revfill(int n){
	int[] ans = new int[n];
	for (int i=n ; i>0; i--){
	    for (int j=0; j<n; j++){
		ans[j]= i;
	    }
	}
	return ans;


    }
}