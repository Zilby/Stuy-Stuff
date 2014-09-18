import java.io.*;
import java.util.*;

public class Arrays {

    public int [] revFill (int n) {

	int [] result = new int [n];
	for (int i = n; i > 0; i--) {

	    result [n-i] = i;
	    

	}

	return result;

    }

}