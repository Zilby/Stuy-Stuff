public class Loops{
    public int gcd(int a, int b){
	if (a > b){
	    int c = b;
	    while ((a % c != 0) || (b % c != 0)){
		c = c-1;
	    }
	    return c;
		}
	else {
	    int c = a;
	    while ((b % c != 0) || (a % c != 0)){
		c = c-1;
	    }
	    return c;
	}
    }
    public int gcd2(int a, int b){
	while (a != 0 ||b != 0){
		int r = a % b;
		a = b;
		b = r;
	}
	if (a == 0){
	    return b;
	}
	else {
	    return a;
	}
    }
    
    public boolean isPrime (int  n){
	
        int other = (int)Math.round(Math.sqrt(n));
	while (other > 1){
	    if (gcd(n, other)>1){
		other = other - 1;
	    }
	    else{
		return true;
	    }
	}
	return false;
    }
    public boolean isPrimef (int n){
	for (int other= (int)Math.round(Math.sqrt(n)); other>1; other--){
	    if (gcd(n, other)>1){
		return false;
	    }
	}
	return true;
    }
    public String table(int n, int m){
	String final = ""
	for (int c= 0; c<(m+1) ; c++){
	    for (int j = 1; j<(nm +1); j+c){
		final = final + j + " "
	    }
	    return final
	}
	return "\n"
	    }

}