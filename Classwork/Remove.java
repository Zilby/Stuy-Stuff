import java.io.*;
import java.util.*;

public class Remove {
    data = new int[5];

    public void remove(int pos){
	tmparray = new int[data.length-1];
	for (int i=0;i<data.length;i++){
	    if (i != pos) {
		temparray[i] = data[i];