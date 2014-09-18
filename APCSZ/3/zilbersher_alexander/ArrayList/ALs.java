import java.util.*;
import java.io.*;

public class ALs {

    public long buildbasic(ArrayList a) {
	long start = System.currentTimeMillis();
	for (int i = 10000;i>0;i--) {
	    a.add("wow");
	}
	long end = System.currentTimeMillis();
	return end - start;
    }

    public long buildHard(ArrayList a) {
	long start = System.currentTimeMillis();
	for (int i = 10000;i>0;i--) {
	    a.add(0,"wow");
	}
	long end = System.currentTimeMillis();
	return end - start;
    }

}