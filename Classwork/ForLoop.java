import java.io.*;
import java.io.*;

public class ForLoop {
    public int fact(int n){
	int i=1;
	for (; n>=1; i=i*n) {
	    n--;
	}
	return i;
    }
    public int count(int n){
	int i=0;
	for (;i<10;i=i+1){
	    return i;
	}
	return i;
    }
}

